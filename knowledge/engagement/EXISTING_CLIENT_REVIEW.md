# Existing-client results review

Mandatory for Reporting and existing-client Upsell. A results review is not a new-business
pitch. Lead with how people discover the customer, show what changed, then propose a few
specific improvements. Read the evidence runbook before writing.

## Inputs and stop conditions

Confirm audience, account, locations, activation date, reporting cutoff and output language.
Audience includes anyone likely to receive a forwarded PDF. Infer Reporting from a clear
results-review request; do not make the operator restate an obvious task type.

Read authorized live evidence or supplied exports. A public repo URL is not account access.
With neither, return PARTIAL: a template and the exact missing inputs. Never insert another
customer's proof as this customer's performance. Keep raw evidence in a private workspace.

## Eight non-negotiable rules

1. **Discovery leads.** Reviews and posting counts are supporting evidence, not the cover hook.
2. **Reclassify search terms.** Google's Discovery label is not audited non-brand demand.
   Review spelling variants, product-plus-brand queries, addresses and other scripts. Class
   each term as brand, nonbrand or unresolved. Preserve the count-weighted denominator and
   sample coverage. Do not apply a top-terms sample to all searches as a measured fact.
3. **Scores are dated.** Read a fresh score before calling it current. If only a historical
   score exists, date it plainly or omit it. Never silently carry a prior audit score forward.
4. **Use the right window.** Start the first review on verified activation, not a later
   onboarding meeting or arbitrary date. Compare the same calendar dates last year, same
   locations and metric definitions. For subsequent reviews, state the deliberate period.
   If the connector cannot filter partial months, label the full-month data separately.
5. **Reviews need a baseline.** Count the matched prior-year window before claiming growth
   or a better reply rate. Automation can be the win even if the customer already answered
   everything. Request opens are not requests sent, available credits or reviews generated.
6. **No unsupported generalisations.** No invented competitor, sector or audience behavior.
   Name declines and alternative explanations. Attributes suggest a fix, not a proven cause.
7. **Keep the PDF forwardable.** No internal account history, private correspondence, partner
   names, pricing, network expansion pitch or undelivered commitments. If pricing is asked
   for, make a separate authorized commercial proposal. Future capability is explicitly
   pilot-stage, not current delivery or a promised date.
8. **The customer is the hero.** A permissioned customer photo leads. Small Obenan mark,
   generous white space, concise finding-led headlines. No stock AI cover or review dashboard.

## Eleven-page standard

Use [the review template](../../templates/deck/EXISTING_CLIENT_REVIEW.html), not the generic
sales deck. It preserves the reference's photo-led cover, A4 grid, large numbers, quiet source
notes, location comparisons and dark closing page. Replace placeholders; never invent data
to fill a layout. Eleven pages is the default for two locations; expand location pages for a
larger estate or mark evidence unavailable rather than manufacture a positive location.

| Page | Job | Evidence and boundary |
|---|---|---|
| 1. Customer cover | A real discovery finding, customer photo and period | Counted nonbrand searches with sample qualifier where needed; authorized photo credit. |
| 2. Discovery | How people found the locations | Monthly trend, brand reclassification and language split, each with its own denominator. Seasonal growth is not all ours. |
| 3. Ad-equivalent | Explain the potential value of that reach | Optional estimated scenario, never ROI or spend saved. If CPC evidence is missing, use measured actions instead. |
| 4. Location comparison | What improved at one location | Absolute values, same-window baseline, dates and attribution caveat. |
| 5. Location diagnosis | Show a decline or material gap | Same-window decline; independently verify the missing attribute or link. Do not claim it explains the whole gap. |
| 6. Reviews | Work automated and room to improve | Current and prior volume, ratings, reply coverage, observed automation vs rule-based inference, request opens. |
| 7. Time back | What manual work was avoided | Delivered counts plus transparent minute assumptions. No scheduled counts dressed as published work or false brand-voice claim. |
| 8. Simple switches | A few practical improvements | Current state, proposed action, owner and dependency. Credentials, approval or integration needs are stated, not hidden behind “one switch”. |
| 9. Background | Explain verified operational value | Active destinations, supported fields and configured cadence. Google and AI readiness, not a promise to appear in AI answers. |
| 10. What comes next | One agreed next step | Shared illustrative card, pilot-stage boundary, booking/order/payment in the customer's systems. No rollout date. |
| 11. See it | The public agentic-commerce film and who does what | Locked copy and placement in [the closing-pair note](AGENTIC_CLOSING.md). Only the closing line may change, and only for a verified agentic build. |

## Ad-equivalent method

Keep measured actions separate from an **inferred** nonbrand action share. If actions are not
attributed to search terms, `all_actions × audited_search_share` is only a scenario. Profile
actions are not equivalent to paid clicks, unique guests, sales or incremental acquisition.

Show the formula, action window, search sample/window, local CPC source/date, keyword coverage,
currency and dated FX source or explicit FX assumption. A ceiling CPC is an assumption, not
the customer's observed cost. The range is an estimated ad-cost equivalent, not money saved.
Do not turn a sampled CPC for one language into a measured cost for every query or geography.

## What runs in the background

The platform can resynchronize supported information on connected destinations every 48
hours. The supported-destination roster is not a count of this account's active connections;
field availability varies by destination. Quote field and destination counts only from current
product evidence. A zero-row directory response means coverage unknown until verified.

Show actual published posts and review replies, configured cadence and approved voice.
`default_prompt: true` is default wording, not a bespoke customer voice. Do not claim every
review, every field or every destination is always updated. Third-party suggested edits can
be corrected through synchronization; do not promise nobody can ever override a listing.

## Review-request safety

Invite genuine customers neutrally, regardless of their experience. No incentives, filtering
by rating, suppression of negative reviews or route that sends only happy customers to public
reviews. Private feedback can coexist with the same public-review opportunity for everyone.
Never promise review volume or ranking gains. Check the current platform policy before
recommending a request workflow; a wording change alone does not fix a gated flow.
Source checked 8 October 2026: [Google Maps contribution policy](https://support.google.com/contributionpolicy/answer/7400114).

## Build and evidence contract

Use a private `EVIDENCE.md` for sources, coverage, arithmetic, assumptions and missing data.
Also create private `EVIDENCE.json` when using the automatic consistency check:

```json
{
  "activation_date": "2026-06-04", "captured_at": "2026-10-08",
  "window": ["2026-06-04", "2026-10-04"],
  "baseline": ["2025-06-04", "2025-10-04"],
  "brand_variants": ["Example Coffee", "예시 커피"],
  "search_terms": [{"term": "example coffee", "count": 40, "class": "brand"},
                   {"term": "coffee near me", "count": 60, "class": "nonbrand"}],
  "search_scope": "Reviewed top terms, not the full population", "nonbrand_share": 0.6,
  "reviews": {"current": 83, "prior": 80, "growth_percent": 3.75},
  "claims": [{"text": "Observed actions", "source": "authorized export",
              "captured_at": "2026-10-08", "state": "measured"}]
}
```

The example is synthetic. An unknown share is `null`, not zero. Include known address/product
aliases and translated brand spellings. List all material claims; their states are measured,
supplied, estimated, inferred, scheduled or unknown. Optional `score` has `value`, `measured_at`
and `current`. Optional `presented_as_delivered` rejects scheduled/unknown claims. The checker
does not authenticate sources, evaluate prose, or prove completeness.

Run `python3 scripts/validate_review.py /path/to/private/EVIDENCE.json`.
The first-review date check intentionally rejects a later start. For subsequent reporting
periods, do not change the true activation date to pass: document the exception and use human
review instead. Feb 29 maps to Feb 28 in the prior year; disclose that adjustment.

For time estimates use [the method](../../templates/method/TIME_SAVED_METHOD.md).
Render A4, inspect every page, and confirm dollars survive the HTML-to-PDF path. Review
approval checks the actual deck against the ledger; a passing script alone is not PASS.

## Final human preflight

- Discovery leads; customer photo is authorized; no `{{` placeholder and no `template-note`
  element remains in a final deck.
- Every figure has scope, source, date and state; trends and baselines use the correct window.
- Search classification, score freshness and prior review coverage have been checked.
- Declines are visible; no unsupported causality, generalisation or falsely delivered work.
- No private history, partner name, pricing or unsolicited expansion pitch in the PDF.
- Time and ad value are estimates; requests are not gated; active destinations are verified.
- All rendered pages are legible and unclipped; one concrete next step closes the document.

Hand over the PDF, source HTML, private evidence, PASS/PARTIAL status and any pending inputs.
This standard governs narrative and layout; it cannot guarantee model behavior by itself.
