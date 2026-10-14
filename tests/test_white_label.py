"""Masked white-label screens: exact bytes, no metadata, gated approval and stated limits."""

from hashlib import sha256
from pathlib import Path
import re
import struct
import unittest

ROOT = Path(__file__).resolve().parents[1]
ASSETS = ROOT / "assets/white-label"
INDEX = ASSETS / "README.md"
UI = ROOT / "reference/product-ui/PRODUCT_UI_OVERVIEW.md"
REGISTER = ROOT / "knowledge/proof/PUBLIC_PROOF_REGISTER.md"
SCREENS = {"findri-01-login.png", "findri-02-get-started.png", "findri-03-insights.png",
           "findri-04-indexability.png", "findri-05-discoverability.png",
           "findri-06-reputation.png"}


def records():
    return re.findall(r"^\| \[([^]]+\.png)\]\(([^)]+\.png)\) \| [^|]+ \| `([a-f0-9]{64})` \|",
                      INDEX.read_text(), re.M)


def chunks(data):
    pos = 8
    while pos < len(data):
        length, kind = struct.unpack(">I4s", data[pos:pos + 8])
        yield kind.decode("latin-1")
        pos += 12 + length


def section(text, heading):
    match = re.search(rf"^## {heading}\n(.*?)(?=^## |\Z)", text, re.M | re.S)
    return match.group(1) if match else ""


class WhiteLabelScreenTests(unittest.TestCase):
    def test_six_masked_screens_match_recorded_bytes(self):
        rows = records()
        self.assertEqual({row[1] for row in rows}, SCREENS)
        self.assertEqual({p.name for p in ASSETS.glob("*.png")}, SCREENS)
        for label, file, digest in rows:
            with self.subTest(file=file):
                self.assertEqual(label, file)
                self.assertEqual(sha256((ASSETS / file).read_bytes()).hexdigest(), digest)

    def test_screens_carry_no_capture_metadata(self):
        for file in SCREENS:
            with self.subTest(file=file):
                data = (ASSETS / file).read_bytes()
                self.assertEqual(data[:8], b"\x89PNG\r\n\x1a\n")
                kinds = set(chunks(data))
                self.assertFalse(kinds & {"tEXt", "iTXt", "zTXt", "eXIf"}, kinds)

    def test_index_masks_the_underlying_customer_and_never_names_it(self):
        text = INDEX.read_text()
        for phrase in ("masked", "Do not unmask", "PUBLIC_PROOF_REGISTER.md"):
            self.assertIn(phrase.lower(), text.lower())
        for document in (INDEX, UI, REGISTER):
            with self.subTest(document=document.name):
                self.assertNotRegex(document.read_text(), r"(?i)factory\s*girl|friedrichstra")

    def test_findri_publication_is_gated_in_the_register(self):
        entry = re.search(r"^### Findri white-label screens\n(.*?)(?=^#{2,3} |\Z)",
                          REGISTER.read_text(), re.M | re.S)
        self.assertIsNotNone(entry)
        body = entry.group(1)
        status = re.search(r"\| Status \| `(PENDING|APPROVED)` \|", body)
        self.assertIsNotNone(status)
        self.assertIn("assets/white-label/README.md", body)
        self.assertRegex(body, r"(?i)metrics[^|]*\|[^|]*not")
        index_status = re.search(r"^\*\*Status: (pending|approved)\.\*\*", INDEX.read_text(), re.M)
        self.assertIsNotNone(index_status)
        self.assertEqual(index_status.group(1).upper(), status.group(1))
        if status.group(1) == "APPROVED":
            self.assertRegex(body, r"\| Review date \| 20\d\d-\d\d-\d\d \|")

    def test_product_overview_names_where_obenan_stays_visible(self):
        text = section(UI.read_text(), "White-label")
        self.assertTrue(text, "missing White-label section")
        for phrase in ("Google", "Terms", "Privacy Policy", "email", "assets/white-label/README.md"):
            self.assertIn(phrase, text)
        self.assertNotRegex(text, r"(?i)vercel|cname\.|dns record value")
        promise = re.compile(r"(?i)(customers|they) (will )?never (know|see)")
        for line in text.splitlines():
            if promise.search(line):
                self.assertRegex(line, r"(?i)\bnever tell\b|\bdo not\b")

    def test_entry_points_link_the_screen_index(self):
        for doc in ("START_HERE.md", "reference/design/BRAND_ASSET_LIBRARY.md"):
            with self.subTest(doc=doc):
                self.assertIn("assets/white-label/", (ROOT / doc).read_text())


if __name__ == "__main__":
    unittest.main()
