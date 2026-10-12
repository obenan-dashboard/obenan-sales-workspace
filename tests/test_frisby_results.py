"""AC-FRISBY: supplied aggregate proof consistency, not a live account audit."""

import hashlib
from pathlib import Path
import re
import unittest

ROOT = Path(__file__).resolve().parents[1]
CARD = "knowledge/proof/FRISBY_COLOMBIA.md"
SOURCE = "knowledge/proof/sources/frisby-google-performance-2026-10-12.png"
SOURCE_SHA256 = "d48fd9aa558e994e628110a5ba9d9a183800a0e6df40cc8a62f1679c892b753b"
EXPECTED = {
    "Total impressions": (6327278, 7261497, 15),
    "Google Search impressions": (3996638, 4539699, 14),
    "Google Maps impressions": (2330640, 2721798, 17),
    "Total interactions": (390017, 534616, 37),
    "Call clicks": (177960, 281163, 58),
    "Direction requests": (193916, 215511, 11),
    "Website clicks": (15880, 34266, 116),
    "Menu clicks": (2261, 3676, 63),
}


class FrisbyResultsTests(unittest.TestCase):
    def setUp(self):
        self.card = (ROOT / CARD).read_text()

    def rows(self):
        result = {}
        for line in self.card.splitlines():
            cells = [c.strip() for c in line.split("|")[1:-1]]
            if cells and cells[0] in EXPECTED:
                result[cells[0]] = (
                    int(cells[1].replace(",", "")),
                    int(cells[2].replace(",", "")),
                    int(cells[3].removeprefix("+").removesuffix("%")),
                )
        return result

    def test_AC_FRISBY_1_preserves_source_values_periods_and_scope(self):
        self.assertEqual(self.rows(), EXPECTED)
        for phrase in ("213 locations in Colombia", "1 October 2025 to 31 March 2026",
                       "1 April to 30 September 2026"):
            self.assertIn(phrase, self.card)

    def test_AC_FRISBY_2_components_growth_and_absolute_increases_reconcile(self):
        rows = self.rows()
        for column in (0, 1):
            self.assertEqual(sum(rows[k][column] for k in
                                 ("Google Search impressions", "Google Maps impressions")),
                             rows["Total impressions"][column])
            self.assertEqual(sum(rows[k][column] for k in
                                 ("Call clicks", "Direction requests", "Website clicks", "Menu clicks")),
                             rows["Total interactions"][column])
        for label, (before, after, growth) in rows.items():
            with self.subTest(metric=label):
                self.assertEqual(round((after / before - 1) * 100), growth)
        self.assertEqual(rows["Total interactions"][1] - rows["Total interactions"][0], 144599)
        self.assertEqual(rows["Call clicks"][1] - rows["Call clicks"][0], 103203)
        self.assertIn("144,599 additional profile actions", self.card)
        self.assertIn("103,203 additional call clicks", self.card)

    def test_AC_FRISBY_2_ratio_uses_unrounded_inputs(self):
        rows = self.rows()
        before = 100 * rows["Total interactions"][0] / rows["Total impressions"][0]
        after = 100 * rows["Total interactions"][1] / rows["Total impressions"][1]
        self.assertEqual((round(before, 1), round(after, 1)), (6.2, 7.4))
        self.assertAlmostEqual((after / before - 1) * 100, 19.4, delta=.05)
        stored = re.search(r"^\| Interactions per 100 impressions \| ([\d.]+) \| ([\d.]+) \| \+([\d.]+)% \|$",
                           self.card, re.M)
        self.assertIsNotNone(stored)
        self.assertEqual(tuple(float(value) for value in stored.groups()),
                         (round(before, 1), round(after, 1), round((after / before - 1) * 100)))
        self.assertIn("unrounded counts", self.card)

    def test_AC_FRISBY_3_pitch_uses_actions_not_completed_calls_or_visits(self):
        pitch = self.card.split("## Ready-to-use pitch", 1)[1].split("\n## ", 1)[0]
        self.assertIn("7.26 million", pitch)
        self.assertIn("call clicks", pitch)
        for unsupported in ("phone calls", "store visits", "unique customers", "revenue",
                            "Obenan caused", "nonbrand", "year-on-year"):
            with self.subTest(claim=unsupported):
                self.assertNotIn(unsupported, pitch)
        for boundary in ("not completed calls", "not verified visits", "not causal attribution",
                         "not unique people", "not a year-on-year comparison"):
            self.assertIn(boundary, self.card)

    def test_AC_FRISBY_4_source_image_is_unchanged_and_mobile_claim_is_separate(self):
        self.assertEqual(hashlib.sha256((ROOT / SOURCE).read_bytes()).hexdigest(), SOURCE_SHA256)
        self.assertIn(SOURCE_SHA256, self.card)
        mobile = " ".join(self.card.split("## Colleague-reported context", 1)[1]
                          .split("\n## ", 1)[0].split())
        for phrase in ("mobile Maps impressions +17%", "mobile Search impressions +15%",
                       "not present in the screenshot", "not independently verified"):
            self.assertIn(phrase, mobile)
        for limitation in ("Activation date", "same-store", "source-system refresh"):
            self.assertIn(limitation, self.card)

    def test_AC_FRISBY_5_approval_and_retrieval_are_scoped(self):
        register = (ROOT / "knowledge/proof/PUBLIC_PROOF_REGISTER.md").read_text()
        frisby = register.split("### Frisby", 1)[1].split("\n## ", 1)[0]
        for field in ("`APPROVED`", "FRISBY_COLOMBIA.md", "2026-10-12", "2027-01-12",
                      "Logo / testimonial quotes / other photos", "`PENDING`"):
            self.assertIn(field, frisby)
        for path in ("START_HERE.md", "knowledge/proof/README.md"):
            self.assertIn("FRISBY_COLOMBIA.md", (ROOT / path).read_text())

    def test_AC_FRISBY_6_no_contacts_or_internal_account_data_in_card(self):
        self.assertIsNone(re.search(r"[\w.+-]+@[\w.-]+\.[A-Za-z]{2,}", self.card))
        self.assertNotIn("/Users/", self.card)
        self.assertNotIn("obenan.slack.com", self.card)
        self.assertIsNone(re.search(r"\b(?:cus|sub|in)_[A-Za-z0-9]{8,}\b", self.card))


if __name__ == "__main__":
    unittest.main()
