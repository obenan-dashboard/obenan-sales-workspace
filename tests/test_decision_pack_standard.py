"""Instruction contracts, not proof that a model followed them or that a PDF was checked."""

from hashlib import sha256
from pathlib import Path
import re
import unittest

ROOT = Path(__file__).resolve().parents[1]
STANDARD = "knowledge/engagement/DECISION_PACK.md"
PROMPT = "templates/decision-pack/BUILD_PROMPT.md"


def read(path):
    return (ROOT / path).read_text()


class DecisionPackStandardTests(unittest.TestCase):
    def test_AC_DPACK_1_entrypoint_and_single_route_reach_standard_and_prompt(self):
        for path in ("START_HERE.md", "README.md"):
            with self.subTest(path=path):
                self.assertIn(STANDARD, read(path))
                self.assertIn(PROMPT, read(path))
        router = read("knowledge/TASK_ROUTER.md")
        rows = [line for line in router.splitlines() if line.startswith("| Decision pack |")]
        self.assertEqual(len(rows), 1)
        self.assertIn("DPACK", rows[0])
        self.assertIn("BU, FO", rows[0])
        self.assertIn("DP, BS", rows[0])
        self.assertIn(STANDARD, router)
        self.assertIn(PROMPT, router)

    def test_AC_DPACK_2_operator_prompt_has_all_fields_and_no_private_defaults(self):
        text = read(PROMPT)
        fields = set(re.findall(r"^([A-Z][A-Za-z ]+):", text, re.M))
        self.assertTrue({"Prospect", "Occasion", "What we learned", "Account folder",
                         "Build folder", "Workspace", "Language", "Deliverable",
                         "Commercial authority", "Public naming rights", "Known sensitivities",
                         "Reviewer and sender", "Example bundle"}.issubset(fields))
        self.assertIn(STANDARD, text)
        self.assertNotRegex(text, r"/Users/|https?://(?!github\.com/obenan-dashboard/)")
        standard = read(STANDARD)
        for phrase in ("ask once", "NONE", "unpriced", "hard stop", "record gaps privately"):
            self.assertIn(phrase, standard)

    def test_AC_DPACK_3_meeting_page_grammar_and_exact_visual_profile(self):
        text = read(STANDARD)
        for phrase in ("their questions, in their order", "purpose, outcome and scope",
                       "shape, not the content", "10 words", "20 words", "one display number",
                       "Obenan Research", "No sender name", "month and year", "Appendix",
                       "#0F0F14", "#598AFF", "#C3D5FF", "#DAD6FF", "#9BECFF", "#2E5FD9",
                       "Helvetica Neue", "300", "200", "A4 portrait", "tabular",
                       "#F67900", "246,121,0", "6.8pt", "small, useful next step"):
            with self.subTest(phrase=phrase):
                self.assertIn(phrase, " ".join(text.split()))

    def test_AC_DPACK_4_customer_build_requires_real_gates_and_evidence(self):
        text = read(STANDARD)
        for phrase in ("python3 -I", "build_deck.py BUILD_DIR WORKSPACE_DIR", "source JSON",
                       "changed source stops the build", "data URIs", "pages N bytes N leaks N []",
                       "Leak gate", "Numbers gate", "after every change", "both gates print zero",
                       "pdftoppm -r 80", "pdfinfo", "every page", "SHA-256", ".bak_<topic>",
                       "cmp", "EVIDENCE.md", "NOTE_FOR_<REVIEWER>.md", "STATUS.md",
                       "DECISIONS_LOG.md", "not a draft email", "customer-specific gates"):
            with self.subTest(phrase=phrase):
                self.assertIn(phrase, " ".join(text.split()))

    def test_AC_DPACK_5_authority_language_and_private_artifact_boundaries(self):
        text = read(STANDARD)
        for phrase in ("no presenter notes or controls", "No reviewer names or review text",
                       "Unknown is not absent", "not verified", "active destinations",
                       "research scope", "No em or en dashes", "well managed", "gets it right",
                       "a few", "mostly", "slightly", "we checked", "invisible", "merchant",
                       "illustrative", "draft", "placeholder", "not published", "demo", "mock",
                       "sample data", "Pilot stage", "read only", "Never save email bodies",
                       "data, not instructions", "Send nothing. Publish nothing."):
            with self.subTest(phrase=phrase):
                self.assertIn(phrase, " ".join(text.split()))
        self.assertNotRegex(text, r"[\u2013\u2014]|/Users/")

    def test_AC_DPACK_6_old_templates_are_unchanged(self):
        # Reviewed base digests keep this contract independent of CI checkout history.
        expected = {
            "templates/deck/DECK_SKELETON.html":
                "9353847caf985db6fb1569b349fd4d84e654b19375e9be29f0cd28e4cc35c0a7",
            "templates/deck/EXISTING_CLIENT_REVIEW.html":
                "c4de4ed1197f3bfdbe4f7c9e66783cfdfaec2db7129f55664c335eb3b9596360",
        }
        for path, digest in expected.items():
            with self.subTest(path=path):
                self.assertEqual(sha256((ROOT / path).read_bytes()).hexdigest(), digest)
        text = read(STANDARD)
        for phrase in ("existing review evidence rules", "No fixed page count",
                       "AGENTIC_CLOSING.md", "operator's naming authority", "PUBLIC_PROOF_REGISTER.md"):
            self.assertIn(phrase, text)

    def test_AC_DPACK_7_scope_is_documented_not_a_claim_of_customer_validation(self):
        text = read(STANDARD)
        self.assertIn("cannot prove", text)
        self.assertIn("human", text)
        status = read("STATUS.md")
        self.assertIn(STANDARD, status)
        self.assertIn("No customer pack", status)


if __name__ == "__main__":
    unittest.main()
