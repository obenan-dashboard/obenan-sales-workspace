"""Exact approved assets and their print-template integration, not client-status inference."""

from hashlib import sha256
from html.parser import HTMLParser
from pathlib import Path
import re
import unittest
import xml.etree.ElementTree as ET

ROOT = Path(__file__).resolve().parents[1]
ASSETS = ROOT / "assets/customer-logos"
BRANDS = {"Nusr-Et", "Warna Baru", "Banco de Boquerones", "Rotana", "Adina Hotels",
          "Casa Ràfols", "Poke Perfect", "Wagamama", "SLA"}


def records():
    return re.findall(r"^\| \[([^]]+)\]\(([^)]+\.svg)\) \| `([a-f0-9]{64})` \|",
                      (ASSETS / "README.md").read_text(), re.M)


class Images(HTMLParser):
    def __init__(self):
        super().__init__()
        self.images = []

    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        if tag == "img" and "customer-logos/" in attrs.get("src", ""):
            self.images.append(attrs)


class CustomerLogoTests(unittest.TestCase):
    def test_exact_nine_approved_assets_match_recorded_source_bytes(self):
        rows = records()
        self.assertEqual(len(rows), 9)
        self.assertEqual({row[0] for row in rows}, BRANDS)
        self.assertEqual(len({row[1] for row in rows}), 9)
        self.assertEqual({p.name for p in ASSETS.glob("*.svg")}, {row[1] for row in rows})
        for name, file, digest in rows:
            with self.subTest(brand=name):
                self.assertEqual(sha256((ASSETS / file).read_bytes()).hexdigest(), digest)

    def test_logos_are_self_contained_without_active_content(self):
        for name, file, _ in records():
            with self.subTest(brand=name):
                text = (ASSETS / file).read_text()
                svg = ET.fromstring(text)
                self.assertEqual(svg.tag.rsplit("}", 1)[-1], "svg")
                self.assertNotRegex(text, r"(?i)@import|url\(\s*['\"]?https?://")
                for node in svg.iter():
                    self.assertNotIn(node.tag.rsplit("}", 1)[-1], ("script", "foreignObject"))
                    for key, value in node.attrib.items():
                        attr = key.rsplit("}", 1)[-1]
                        self.assertFalse(attr.lower().startswith("on"))
                        if attr in ("href", "src"):
                            self.assertTrue(value.startswith(("#", "data:image/")), value[:80])

    def test_prospect_template_has_local_logos_and_accessible_names(self):
        parser = Images()
        template = ROOT / "templates/deck/DECK_SKELETON.html"
        parser.feed(template.read_text())
        self.assertEqual(len(parser.images), 9)
        self.assertEqual({img.get("alt") for img in parser.images}, BRANDS)
        expected = {file for _, file, _ in records()}
        self.assertEqual({Path(img["src"]).name for img in parser.images}, expected)
        for img in parser.images:
            self.assertTrue((template.parent / img["src"]).resolve().is_file())


if __name__ == "__main__":
    unittest.main()
