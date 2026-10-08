"""Estimate manual effort avoided from delivered work, not schedules or observed staff time."""
import argparse
import json
import math
from pathlib import Path


def minutes(value):
    if type(value) not in (int, float) or not math.isfinite(value) or value < 0:
        raise ValueError("Minutes must be finite, nonnegative numbers")
    return value


def calculate(rows):
    if not isinstance(rows, list):
        raise ValueError("Input must be an array of work rows")
    total, excluded, delivered = 0, 0, 0
    for row in rows:
        if not isinstance(row, dict):
            raise ValueError("Work row must be an object")
        count = row.get("count")
        if type(count) is not int or count < 0:
            raise ValueError("Count must be a nonnegative integer")
        state = row.get("state")
        if state not in ("delivered", "scheduled", "unknown"):
            raise ValueError("State must be delivered, scheduled or unknown")
        if state != "delivered":
            excluded += count
            continue
        manual = minutes(row.get("manual_minutes"))
        remaining = minutes(row.get("remaining_minutes"))
        if remaining > manual:
            raise ValueError("Remaining effort exceeds baseline; report added effort separately")
        total += count * (manual - remaining)
        delivered += count
    return {"label": "Estimated manual effort avoided, not measured time saved",
            "estimated_hours": total / 60, "delivered_count": delivered,
            "excluded_count": excluded}


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("ledger", type=Path, help="Private array of work rows")
    args = parser.parse_args()
    try:
        print(json.dumps(calculate(json.loads(args.ledger.read_text())), indent=2))
    except (OSError, ValueError, TypeError) as exc:
        parser.exit(1, f"Invalid ledger: {exc}\n")
