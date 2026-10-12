"""AC-URBAN: supplied aggregate proof, not live source-system verification."""

import hashlib
from pathlib import Path
import re
import unittest

ROOT = Path(__file__).resolve().parents[1]
CARD = "knowledge/proof/URBAN_FORK_GROUP.md"
SOURCE = "knowledge/proof/sources/urban-fork-google-performance-2026-10-12.png"
SOURCE_SHA256 = "7b7a653a32800db9f99f9cda9013c25b0998264bed07e412eaf62ca9f529a049"
EXPECTED = {
    "Total impressions": (719482, 1023677, 42),
    "Google Maps impressions": (524086, 756460, 44),
    "Google Search impressions": (195396, 267217, 37),
    "Total interactions": (49581, 57943, 17),
    "Bookings (source label)": (1189, 1600, 35),
    "Direction requests": (27006, 32566, 21),
    "Call clicks": (4940, 5904, 20),
    "Website clicks": (4353, 4797, 10),
    "Menu clicks": (12086, 13076, 8),
}


def rows(text):
    result = {}
    for line in text.splitlines():
        cells = [c.strip() for c in line.split("|")[1:-1]]
        if cells and cells[0] in EXPECTED:
            result[cells[0]] = (int(cells[1].replace(",", "")),
                                int(cells[2].replace(",", "")),
                                int(cells[3].removeprefix("+").removesuffix("%")))
    return result


class UrbanForkResultsTests(unittest.TestCase):
    def setUp(self):
        self.card = (ROOT / CARD).read_text()

    def test_AC_URBAN_1_exact_values_scope_and_same_months(self):
        self.assertEqual(rows(self.card), EXPECTED)
        for phrase in ("12 restaurants", "1 April to 30 September 2025",
                       "1 April to 30 September 2026"):
            self.assertIn(phrase, " ".join(self.card.split()))
        # Missing and corrupted metric rows cannot match the approved source values.
        table_line = "| Bookings (source label) | 1,189 | 1,600 | +35% |"
        self.assertNotEqual(rows(self.card.replace(table_line, "")), EXPECTED)
        self.assertNotEqual(rows(self.card.replace("1,600 | +35%", "1,601 | +35%")), EXPECTED)

    def test_AC_URBAN_2_arithmetic_preserves_and_discloses_gap(self):
        actual = rows(self.card)
        components = ("Bookings (source label)", "Direction requests", "Call clicks",
                      "Website clicks", "Menu clicks")
        for col in (0, 1):
            self.assertEqual(actual["Google Maps impressions"][col] +
                             actual["Google Search impressions"][col],
                             actual["Total impressions"][col])
        self.assertEqual(sum(actual[k][0] for k in components), 49574)
        self.assertEqual(actual["Total interactions"][0] -
                         sum(actual[k][0] for k in components), 7)
        self.assertEqual(sum(actual[k][1] for k in components), 57943)
        for before, after, growth in actual.values():
            self.assertEqual(round((after / before - 1) * 100), growth)
        for phrase in ("49,574", "49,581", "seven-action", "unresolved", "not silently correct",
                       "304,195 additional impressions", "8,362 additional profile actions",
                       "411 additional reported bookings", "5,560 additional direction requests"):
            self.assertIn(phrase, " ".join(self.card.split()))

    def test_AC_URBAN_3_pitch_definitions_and_negative_claims(self):
        pitch = self.card.split("## Ready-to-use pitch", 1)[1].strip().split("\n\n", 1)[0]
        pitch = " ".join(pitch.split())
        self.assertIn("reported bookings", pitch)
        self.assertIn("same months", pitch)
        first_sentence = pitch.split(". ", 1)[0]
        self.assertIn("reported bookings", first_sentence)
        self.assertIn("Maps impressions", first_sentence)
        for unsupported in ("completed calls", "confirmed visits", "fulfilled reservations",
                            "Obenan caused", "unique guests", "revenue", "Colombia",
                            "nonbrand", "better conversion"):
            self.assertNotIn(unsupported, pitch)
        for boundary in ("not completed calls", "not verified visits", "not fulfilled reservations",
                         "not causal attribution", "not unique people", "definition is unverified"):
            self.assertIn(boundary, self.card)

    def test_AC_URBAN_3_ratio_decline_is_not_hidden(self):
        actual = rows(self.card)
        ratios = [100 * actual["Total interactions"][c] / actual["Total impressions"][c]
                  for c in (0, 1)]
        self.assertAlmostEqual(ratios[0], 6.89, delta=.005)
        self.assertAlmostEqual(ratios[1], 5.66, delta=.005)
        self.assertAlmostEqual((ratios[1] / ratios[0] - 1) * 100, -17.9, delta=.05)
        for phrase in ("6.89", "5.66", "17.9% decline", "not a visitor-conversion rate",
                       "Do not claim improved conversion efficiency"):
            self.assertIn(phrase, self.card)

    def test_AC_URBAN_4_source_and_unverified_context(self):
        self.assertEqual(hashlib.sha256((ROOT / SOURCE).read_bytes()).hexdigest(), SOURCE_SHA256)
        self.assertIn(SOURCE_SHA256, self.card)
        for phrase in ("location count comes from the supplied summary", "Geography was not supplied",
                       "No independent source-system refresh", "Activation date", "same-store"):
            self.assertIn(phrase, self.card)

    def test_AC_URBAN_5_approval_and_retrieval(self):
        register = (ROOT / "knowledge/proof/PUBLIC_PROOF_REGISTER.md").read_text()
        urban = register.split("### Urban Fork Group", 1)[1].split("\n## ", 1)[0]
        for field in ("`APPROVED`", "URBAN_FORK_GROUP.md", "2026-10-12", "2027-01-12",
                      "seven-action", "`PENDING`", "Geography not supplied"):
            self.assertIn(field, urban)
        for path in ("START_HERE.md", "knowledge/proof/README.md", "STATUS.md"):
            self.assertIn("URBAN_FORK_GROUP.md", (ROOT / path).read_text())

    def test_AC_URBAN_6_no_contacts_or_internal_records(self):
        self.assertIsNone(re.search(r"[\w.+-]+@[\w.-]+\.[A-Za-z]{2,}", self.card))
        self.assertNotIn("/Users/", self.card)
        self.assertNotIn("obenan.slack.com", self.card)
        self.assertIsNone(re.search(r"\b(?:cus|sub|in)_[A-Za-z0-9]{8,}\b", self.card))


if __name__ == "__main__":
    unittest.main()
