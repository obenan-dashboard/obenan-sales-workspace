"""Dated public extract regression checks, not a live database audit."""

import hashlib
import json
from pathlib import Path
import re
import unittest

ROOT = Path(__file__).resolve().parents[1]
INDEX = "knowledge/proof/customer-countries.json"
APPROVED_SNAPSHOT_SHA256 = "27c733d6c4f6603d2b5fbff865b55aadba799b6008b7446d10c76702ef4f71bf"
COUNTRIES = {
    "Argentina", "Australia", "Austria", "Azerbaijan", "Bahrain", "Belgium", "Brazil",
    "Canada", "Colombia", "Croatia", "Curaçao", "Democratic Republic of the Congo",
    "Dominican Republic", "Fiji", "France", "Germany", "Greece", "Hungary", "Iceland",
    "India", "Indonesia", "Iraq", "Italy", "Japan", "Jordan", "Kazakhstan", "Luxembourg",
    "Malta", "Mexico", "Morocco", "Netherlands", "Oman", "Pakistan", "Panama", "Peru",
    "Poland", "Portugal", "Qatar", "Saudi Arabia", "South Africa", "Spain", "Sweden",
    "Switzerland", "Tanzania", "Turkey", "United Arab Emirates", "United Kingdom",
    "United States", "Uruguay", "Vanuatu", "Venezuela",
}


def snapshot_digest(rows):
    serialized = json.dumps(rows, ensure_ascii=False, sort_keys=True, separators=(",", ":"))
    return hashlib.sha256(serialized.encode()).hexdigest()


class CountryAccountsTests(unittest.TestCase):
    def setUp(self):
        self.rows = json.loads((ROOT / INDEX).read_text())
        self.pairs = {(r["brand"], r["country"]) for r in self.rows}

    def test_AC_COUNTRY_1_only_public_fields_and_business_names(self):
        self.assertIsInstance(self.rows, list)
        self.assertGreater(len(self.rows), 400)
        for row in self.rows:
            self.assertEqual(set(row), {"brand", "country"})
            for value in row.values():
                self.assertIsInstance(value, str)
                self.assertEqual(value, value.strip())
                self.assertTrue(value)
                self.assertIsNone(re.search(r"[\w.+-]+@[\w.-]+\.[A-Za-z]{2,}|https?://|/Users/", value))

    def test_AC_COUNTRY_2_sorted_unique_canonical_and_accents(self):
        ordered = [(r["brand"], r["country"]) for r in self.rows]
        self.assertEqual(len(ordered), len(self.pairs))
        self.assertEqual(ordered, sorted(ordered, key=lambda p: (p[1].casefold(), p[0].casefold())))
        countries = {r["country"] for r in self.rows}
        self.assertEqual(countries, COUNTRIES)
        self.assertTrue(countries.isdisjoint({"Nederland", "NL", "Deutschland", "España", "México", "US", "BR", "CO", "", "Unknown"}))
        self.assertIn(("Poké Perfect", "Netherlands"), self.pairs)
        self.assertIn(("Bakhuys Amsterdam", "Netherlands"), self.pairs)
        self.assertIn(("Frisby", "Colombia"), self.pairs)

    def test_AC_COUNTRY_3_multiple_markets_and_held_labels(self):
        lpq = {country for brand, country in self.pairs if brand == "Le Pain Quotidien"}
        self.assertEqual(lpq, {"Argentina", "Azerbaijan", "Belgium", "Brazil", "Democratic Republic of the Congo", "France", "Greece", "Hungary", "India", "Japan", "Kazakhstan", "Luxembourg", "Mexico", "Morocco", "Netherlands", "Turkey", "United Arab Emirates", "United Kingdom", "United States", "Uruguay"})
        self.assertIn(("Urban Fork Group", "Mexico"), self.pairs)
        self.assertNotIn("obenan", {brand.casefold() for brand, _ in self.pairs})
        self.assertFalse({country for _, country in self.pairs} & {"Unknown", "NULL", ""})

    def test_AC_COUNTRY_1_2_3_exact_approved_extract_and_negative_changes(self):
        # Pinned to the independently reconciled, approved extract. Holds stay private;
        # any new row requires source reconciliation and an intentional snapshot update.
        self.assertEqual(snapshot_digest(self.rows), APPROVED_SNAPSHOT_SHA256)
        mutations = [
            self.rows + [{"brand": "Sample business", "country": "Atlantis"}],
            self.rows + [{"brand": "Unapproved personal label", "country": "Netherlands"}],
            [{**self.rows[0], "private_field": "not authorized"}] + self.rows[1:],
            self.rows + [self.rows[0]],
            self.rows[1:],
            [{**self.rows[0], "country": "Netherlands"}] + self.rows[1:],
        ]
        for changed in mutations:
            with self.subTest(change=changed[0]):
                self.assertNotEqual(snapshot_digest(changed), APPROVED_SNAPSHOT_SHA256)

    def test_AC_COUNTRY_4_scope_approval_and_retrieval(self):
        guide = (ROOT / "knowledge/proof/CUSTOMER_COUNTRIES.md").read_text()
        for phrase in ("2026-10-13", "2027-01-13", "headquarters", "whole-chain", "billing", "portfolio", "unknown", "customer-countries.json"):
            self.assertIn(phrase, guide)
        register = (ROOT / "knowledge/proof/PUBLIC_PROOF_REGISTER.md").read_text()
        self.assertIn("Country account index", register)
        for path in ("START_HERE.md", "README.md", "knowledge/proof/README.md"):
            self.assertIn("CUSTOMER_COUNTRIES.md", (ROOT / path).read_text())


if __name__ == "__main__":
    unittest.main()
