"""Check a private review ledger. Passing checks does not independently verify sources."""
import argparse
from datetime import date
import json
import math
from pathlib import Path
import unicodedata


def normalize(text):
    return " ".join(unicodedata.normalize("NFKC", text).casefold().split())


def number(value, integer=False):
    return (type(value) in (int, float) and math.isfinite(value) and value >= 0
            and (not integer or type(value) is int))


def validate(data):
    errors = []
    if not isinstance(data, dict):
        return ["Evidence must be an object"]
    try:
        activation = date.fromisoformat(data["activation_date"])
        captured = date.fromisoformat(data["captured_at"])
        start, end = [date.fromisoformat(v) for v in data["window"]]
        prior_start, prior_end = [date.fromisoformat(v) for v in data["baseline"]]
        if start != activation:
            errors.append("Window must start on activation; explain a deliberate alternative privately")
        if not start <= end <= captured:
            errors.append("Window dates must be ordered and no later than capture")
        # Feb 29 maps to Feb 28; the ledger must disclose that calendar adjustment.
        def previous_year(value):
            try:
                return value.replace(year=value.year - 1)
            except ValueError:
                return value.replace(year=value.year - 1, day=28)
        if (prior_start, prior_end) != (previous_year(start), previous_year(end)):
            errors.append("baseline must cover the same calendar window in the prior year")
    except (KeyError, ValueError, TypeError):
        errors.append("Missing or invalid activation, capture, window or baseline date")
        captured = None

    terms = data.get("search_terms", [])
    aliases = data.get("brand_variants", [])
    if not isinstance(aliases, list) or not aliases or not all(isinstance(v, str) and v.strip() for v in aliases):
        errors.append("List brand variants, including known translated spellings")
        aliases = []
    total = nonbrand = unresolved = 0
    if not isinstance(terms, list):
        errors.append("search_terms must be an array")
        terms = []
    seen = set()
    for row in terms:
        if not isinstance(row, dict) or not isinstance(row.get("term"), str):
            errors.append("Invalid search term row")
            continue
        term = normalize(row["term"])
        count, category = row.get("count"), row.get("class")
        if not term or term in seen:
            errors.append("Empty or duplicate search term")
        seen.add(term)
        if not number(count, integer=True) or category not in ("brand", "nonbrand", "unresolved"):
            errors.append("Invalid search count or classification")
            continue
        if category == "nonbrand" and any(normalize(alias) in term for alias in aliases):
            errors.append("Known brand variant classified as nonbrand")
        total += count
        nonbrand += count if category == "nonbrand" else 0
        unresolved += count if category == "unresolved" else 0
    share = data.get("nonbrand_share")
    if share is not None:
        if not number(share) or share > 1 or not total or unresolved:
            errors.append("A nonbrand share needs reviewed, resolved terms and a nonzero denominator")
        elif not math.isclose(share, nonbrand / total, abs_tol=0.001):
            errors.append("nonbrand share does not match classified term counts")
    if not isinstance(data.get("search_scope"), str) or not data["search_scope"].strip():
        errors.append("search scope must say sample or population and coverage")

    score = data.get("score")
    if score is not None and not isinstance(score, dict):
        errors.append("score must be an object or null")
        score = None
    if score is not None:
        try:
            measured = date.fromisoformat(score["measured_at"])
            if captured is None or measured > captured or (score.get("current") and measured != captured):
                errors.append("Historical score cannot be labelled current without a fresh read")
        except (KeyError, ValueError, TypeError):
            errors.append("Invalid score measurement date")
    reviews = data.get("reviews", {})
    if not isinstance(reviews, dict):
        errors.append("reviews must be an object")
        reviews = {}
    growth = reviews.get("growth_percent")
    if growth is not None:
        current, prior = reviews.get("current"), reviews.get("prior")
        if (not number(current, True) or not number(prior, True) or prior == 0
                or type(growth) not in (int, float) or not math.isfinite(growth)):
            errors.append("review growth needs valid counts and a nonzero matched baseline")
        elif not math.isclose(growth, (current - prior) / prior * 100, abs_tol=0.01):
            errors.append("review growth does not match the prior-window counts")
    claims = data.get("claims", [])
    if not isinstance(claims, list) or not claims:
        errors.append("List every claim with source, state and capture date")
        claims = []
    for claim in claims:
        if not isinstance(claim, dict):
            errors.append("Invalid claim row")
            continue
        if not all(isinstance(claim.get(k), str) and claim[k].strip() for k in ("text", "source", "captured_at")):
            errors.append("Unsourced claim")
        try:
            read_at = date.fromisoformat(claim.get("captured_at", ""))
            if captured is not None and read_at > captured:
                errors.append("Claim capture is later than the ledger capture")
        except (ValueError, TypeError):
            errors.append("Invalid claim capture date")
        state = claim.get("state")
        if state not in ("measured", "supplied", "estimated", "inferred", "scheduled", "unknown"):
            errors.append("Invalid claim evidence state")
        if claim.get("presented_as_delivered") and state in ("scheduled", "unknown"):
            errors.append("Scheduled or unknown work cannot be presented as delivered")
    return errors


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("ledger", type=Path, help="Private EVIDENCE.json, never commit it here")
    args = parser.parse_args()
    try:
        errors = validate(json.loads(args.ledger.read_text()))
    except (OSError, ValueError, TypeError) as exc:
        errors = [str(exc)]
    for error in errors:
        print("FAIL:", error)
    if errors:
        raise SystemExit(1)
    print("Ledger consistency passed. Human source, copy and visual review still required.")
