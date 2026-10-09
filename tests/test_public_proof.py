"""Editorial source and retrieval checks, not a guarantee of agent output quality."""

from pathlib import Path
from html import unescape
import re
import unittest

ROOT = Path(__file__).resolve().parents[1]
CARD = "knowledge/proof/LE_PAIN_QUOTIDIEN.md"
LEAD = ("Obenan is way more advanced on the technology than any other competitor "
        "that I've met or seen out there.")


def normalize(text):
    return " ".join(text.split())


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
