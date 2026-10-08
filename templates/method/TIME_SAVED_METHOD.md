# Estimated manual effort avoided

Use delivered counts, not recurrence schedules. This is an estimate against an assumed manual
workflow, never measured staff time, a guaranteed saving or a conservative floor.

Formula: `sum(delivered_count × (manual_minutes - remaining_minutes)) / 60`.

Keep a private input ledger with one row per non-overlapping work type:

```json
[
  {"label": "Delivered posts", "count": 10, "state": "delivered",
   "manual_minutes": 15, "remaining_minutes": 2},
  {"label": "Scheduled posts", "count": 20, "state": "scheduled"}
]
```

These are synthetic inputs, not approved default assumptions. The example produces 2.17
estimated hours and excludes 20 scheduled posts.

Run `python3 templates/method/time_saved.py /path/to/private/work.json`.

Record each count's period, source, status and capture date in the private evidence file.
Document who supplied each minute assumption; include a lower and upper estimate if useful.
Account for approval, editing and manual handling in `remaining_minutes`. Keep automatic and
assisted replies in separate rows. Do not double count one reply under both categories.
Automation rules show intended routing, not proof that each reply ran automatically.

Posts scheduled, queued, failed or unknown are excluded. If only schedules are available,
report the schedule as planned work and omit the saving headline. Blank minutes are unknown,
not zero. Do not monetize the estimate without an approved labor-cost assumption.

If expressing working days, state the assumed hours per day. Do not hard-code a country's
working-day length for every customer. The published total is rounded once, after summing.
