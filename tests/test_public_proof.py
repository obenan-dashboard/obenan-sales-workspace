"""Editorial source and retrieval checks, not a guarantee of agent output quality."""

from pathlib import Path
from html import unescape
from html.parser import HTMLParser
import hashlib
import re
import unittest

ROOT = Path(__file__).resolve().parents[1]
CARD = "knowledge/proof/LE_PAIN_QUOTIDIEN.md"
LEAD = ("Obenan is way more advanced on the technology than any other competitor "
        "that I've met or seen out there.")
CLIP = "https://www.youtube.com/watch?v=vxrYXjTXJp4&t=144s"
PREVIEW = "assets/video-previews/lpq-joost-interview.jpg"
QR = "assets/video-previews/lpq-joost-interview-qr.svg"


def normalize(text):
    return " ".join(text.split())


class LinkedImages(HTMLParser):
    def __init__(self):
        super().__init__()
        self.href, self.images = None, []

    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        if tag == "a":
            self.href = attrs.get("href")
        if tag == "img":
            self.images.append((attrs.get("src", ""), self.href))

    def handle_endtag(self, tag):
        if tag == "a":
            self.href = None


class PublicProofTests(unittest.TestCase):
    def test_lpq_quote_excerpts_preserve_the_transcript(self):
        card = (ROOT / CARD).read_text()
        source = normalize(card.split("## Supplied transcript", 1)[1])
        excerpts = re.findall(r"^\| [^|]+ \| “([^”]+)” \|", card, re.M)
        self.assertGreaterEqual(len(excerpts), 4)
        for quote in excerpts:
            with self.subTest(quote=quote):
                self.assertIn(normalize(quote), source)
        self.assertEqual(excerpts[0], LEAD)

    def test_lpq_has_attribution_timestamp_and_limits(self):
        card = (ROOT / CARD).read_text()
        self.assertIn("Joost Vastenavondt", card)
        self.assertIn("CMO, Le Pain Quotidien (at the time of recording)", card)
        self.assertIn("vxrYXjTXJp4&t=144s", card)
        self.assertIn("Recording date: not supplied", card)
        self.assertIn("not a completed rollout", card)
        self.assertIn("not measured headcount savings", card)

    def test_entrypoint_and_generic_deck_route_to_named_proof(self):
        entry = (ROOT / "START_HERE.md").read_text()
        self.assertIn(CARD, entry)
        template = unescape((ROOT / "templates/deck/DECK_SKELETON.html").read_text())
        self.assertIn(LEAD, template)
        self.assertIn("vxrYXjTXJp4&t=144s", template)
        self.assertIn("Joost Vastenavondt", template)

    def test_lpq_video_renders_as_a_linked_preview_with_qr(self):
        templates = [p for p in (ROOT / "templates").rglob("*.html") if "vxrYXjTXJp4" in p.read_text()]
        self.assertTrue(templates)
        for path in templates:
            parser = LinkedImages()
            parser.feed(path.read_text())
            lpq = [(src, href) for src, href in parser.images if "video-previews/lpq-" in src]
            with self.subTest(template=path.name):
                sources = {(path.parent / src).resolve() for src, _ in lpq}
                self.assertEqual(sources, {ROOT / PREVIEW, ROOT / QR})
                self.assertEqual({href for _, href in lpq}, {CLIP})

    def test_preview_files_match_their_recorded_checksums(self):
        index = (ROOT / "assets/video-previews/README.md").read_text()
        self.assertIn(CLIP, index)
        for path in (PREVIEW, QR):
            with self.subTest(file=path):
                data = (ROOT / path).read_bytes()
                self.assertIn(hashlib.sha256(data).hexdigest(), index)
        self.assertTrue((ROOT / PREVIEW).read_bytes().startswith(b"\xff\xd8\xff"))
        self.assertIn(b"<svg", (ROOT / QR).read_bytes()[:400])

    def test_card_and_register_bind_the_preview_rule(self):
        card = (ROOT / CARD).read_text()
        rule = card.split("## Video preview", 1)[1].split("\n## ", 1)[0]
        for needle in (PREVIEW, QR, "play icon", "Never replace the preview"):
            with self.subTest(needle=needle):
                self.assertIn(needle, rule)
        register = (ROOT / "knowledge/proof/PUBLIC_PROOF_REGISTER.md").read_text()
        lpq = register.split("### Le Pain Quotidien", 1)[1].split("### ", 1)[0]
        self.assertIn("assets/video-previews/", lpq)
        self.assertIn("Interview still: `APPROVED`", lpq)

    def test_named_approval_does_not_expand_to_all_assets(self):
        register = (ROOT / "knowledge/proof/PUBLIC_PROOF_REGISTER.md").read_text()
        coffee = register.split("### Campos Coffee", 1)[1].split("## Partner proof", 1)[0]
        self.assertIn("`APPROVED`", coffee)
        self.assertIn("`PENDING`", coffee)
        card = (ROOT / "knowledge/proof/SPECIALTY_COFFEE_TWO_CAFES.md").read_text()
        self.assertIn("Approved named pitch use", card)
        self.assertNotIn("Approved anonymous pitch use only", card)


if __name__ == "__main__":
    unittest.main()
