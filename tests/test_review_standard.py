import copy
import importlib.util
from pathlib import Path
import unittest

ROOT = Path(__file__).resolve().parents[1]


def module(path):
    spec = importlib.util.spec_from_file_location(Path(path).stem, ROOT / path)
    result = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(result)
    return result


class ReviewEvidenceTests(unittest.TestCase):
    def setUp(self):
        self.check = module("scripts/validate_review.py").validate
        self.evidence = {
            "activation_date": "2026-06-04",
            "captured_at": "2026-10-08",
            "window": ["2026-06-04", "2026-10-04"],
            "baseline": ["2025-06-04", "2025-10-04"],
            "brand_variants": ["Example Coffee", "예시 커피"],
            "search_terms": [
                {"term": "example coffee beans", "count": 30, "class": "brand"},
                {"term": "예시 커피", "count": 10, "class": "brand"},
                {"term": "coffee near me", "count": 60, "class": "nonbrand"},
            ],
            "search_scope": "Reviewed top terms, not all searches",
            "nonbrand_share": 0.6,
            "reviews": {"current": 83, "prior": 80, "growth_percent": 3.75},
            "claims": [{"text": "Observed profile actions", "source": "authorized export",
                        "captured_at": "2026-10-08", "state": "measured"}],
        }

    def test_valid_evidence(self):
        self.assertEqual(self.check(self.evidence), [])

    def test_raw_discovery_brand_variants_rejected(self):
        for index in (0, 1):
            with self.subTest(index=index):
                data = copy.deepcopy(self.evidence)
                data["search_terms"][index]["class"] = "nonbrand"
                self.assertTrue(any("brand" in e for e in self.check(data)))

    def test_wrong_share_and_missing_scope_rejected(self):
        self.evidence["nonbrand_share"] = 0.75
        self.evidence["search_scope"] = ""
        errors = self.check(self.evidence)
        self.assertTrue(any("share" in e for e in errors))
        self.assertTrue(any("scope" in e for e in errors))

    def test_zero_or_unresolved_terms_cannot_support_share(self):
        self.evidence["search_terms"] = []
        self.assertTrue(self.check(self.evidence))
        self.evidence["search_terms"] = [{"term": "unknown", "count": 5, "class": "unresolved"}]
        self.assertTrue(self.check(self.evidence))

    def test_wrong_start_and_prior_window_rejected(self):
        self.evidence["window"][0] = "2026-06-10"
        self.assertTrue(any("activation" in e for e in self.check(self.evidence)))
        self.evidence["window"][0] = "2026-06-04"
        self.evidence["baseline"][0] = "2025-06-10"
        self.assertTrue(any("baseline" in e for e in self.check(self.evidence)))

    def test_score_is_not_current_when_historical(self):
        self.evidence["score"] = {"value": 40, "measured_at": "2026-07-31", "current": True}
        self.assertTrue(any("score" in e for e in self.check(self.evidence)))
        self.evidence["score"]["current"] = False
        self.assertEqual(self.check(self.evidence), [])

    def test_review_growth_needs_correct_baseline(self):
        self.evidence["reviews"]["growth_percent"] = 40
        self.assertTrue(any("review" in e for e in self.check(self.evidence)))
        self.evidence["reviews"]["prior"] = None
        self.assertTrue(self.check(self.evidence))

    def test_unsourced_or_scheduled_claim_rejected(self):
        self.evidence["claims"][0]["source"] = ""
        self.assertTrue(self.check(self.evidence))
        self.evidence["claims"][0]["source"] = "schedule"
        self.evidence["claims"][0]["state"] = "scheduled"
        self.evidence["claims"][0]["presented_as_delivered"] = True
        self.assertTrue(self.check(self.evidence))

    def test_decline_is_valid_not_suppressed(self):
        self.evidence["reviews"] = {"current": 60, "prior": 80, "growth_percent": -25}
        self.assertEqual(self.check(self.evidence), [])

    def test_bad_date_and_nonfinite_or_boolean_count_rejected(self):
        self.evidence["captured_at"] = "not a date"
        self.assertTrue(self.check(self.evidence))
        self.evidence["captured_at"] = "2026-10-08"
        for value in (-1, True, float("nan")):
            self.evidence["search_terms"][0]["count"] = value
            self.assertTrue(self.check(self.evidence))

    def test_malformed_shapes_report_errors_not_tracebacks(self):
        for key, value in (("score", []), ("score", "old"), ("reviews", []),
                           ("brand_variants", "Example"), ("search_terms", {}),
                           ("claims", None), ("window", [1, 2])):
            with self.subTest(key=key):
                data = copy.deepcopy(self.evidence)
                data[key] = value
                self.assertTrue(self.check(data))

    def test_future_dates_rejected(self):
        self.evidence["window"][1] = "2026-10-09"
        self.evidence["claims"][0]["captured_at"] = "2026-10-09"
        self.assertTrue(self.check(self.evidence))

    def test_leap_day_calendar_adjustment(self):
        self.evidence.update(activation_date="2024-02-29", captured_at="2024-04-01",
                             window=["2024-02-29", "2024-03-31"],
                             baseline=["2023-02-28", "2023-03-31"])
        self.evidence["claims"][0]["captured_at"] = "2024-04-01"
        self.assertEqual(self.check(self.evidence), [])

    def test_unknown_search_share_can_remain_unknown(self):
        self.evidence["search_terms"] = []
        self.evidence["nonbrand_share"] = None
        self.evidence["search_scope"] = "Unavailable, not zero"
        self.assertEqual(self.check(self.evidence), [])


class TimeEstimateTests(unittest.TestCase):
    def setUp(self):
        self.calculate = module("templates/method/time_saved.py").calculate
        self.rows = [{"label": "Posts", "count": 10, "state": "delivered",
                      "manual_minutes": 15, "remaining_minutes": 2}]

    def test_delivered_work_minus_remaining_effort(self):
        result = self.calculate(self.rows)
        self.assertAlmostEqual(result["estimated_hours"], 130 / 60)
        self.assertEqual(result["excluded_count"], 0)

    def test_scheduled_work_excluded(self):
        self.rows.append({"label": "Posts", "count": 300, "state": "scheduled"})
        result = self.calculate(self.rows)
        self.assertAlmostEqual(result["estimated_hours"], 130 / 60)
        self.assertEqual(result["excluded_count"], 300)

    def test_empty_is_zero_not_claim_of_observed_saving(self):
        result = self.calculate([])
        self.assertEqual(result["estimated_hours"], 0)
        self.assertIn("estimate", result["label"].lower())

    def test_invalid_counts_and_minutes(self):
        for key, value in (("count", -1), ("count", True), ("count", 1.5),
                           ("manual_minutes", float("inf")), ("remaining_minutes", 16),
                           ("remaining_minutes", -1), ("state", "unknown-state")):
            with self.subTest(key=key, value=value):
                row = dict(self.rows[0], **{key: value})
                with self.assertRaises(ValueError):
                    self.calculate([row])


class RoutingTests(unittest.TestCase):
    def test_existing_client_routes_are_mandatory(self):
        router = (ROOT / "knowledge/TASK_ROUTER.md").read_text()
        for task in ("Reporting", "Upsell"):
            row = next(line for line in router.splitlines() if line.startswith(f"| {task} |"))
            self.assertIn("ECR", row.split("|")[2])

    def test_template_has_ten_ordered_pages(self):
        from html.parser import HTMLParser

        class Pages(HTMLParser):
            def __init__(self):
                super().__init__()
                self.pages = []

            def handle_starttag(self, tag, attrs):
                attrs = dict(attrs)
                if tag == "section" and "page" in attrs.get("class", "").split():
                    self.pages.append(attrs.get("data-page"))

        template = (ROOT / "templates/deck/EXISTING_CLIENT_REVIEW.html").read_text()
        parser = Pages()
        parser.feed(template)
        self.assertEqual(parser.pages, ["cover", "discovery", "ad-equivalent", "location-positive",
                                       "location-gap", "reviews", "time-back", "switches",
                                       "background", "next"])
        self.assertIn("A&#36;", template)
        self.assertIn("whats-next-card.png", template)


if __name__ == "__main__":
    unittest.main()
