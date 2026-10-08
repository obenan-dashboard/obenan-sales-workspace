# Authorized evidence runbook

Use customer evidence only when the operator has authorized access to that customer's account.
This runbook is read-only and deliberately does not describe private connector architecture.

## 1. Establish access and identity

Before reading data:

1. Confirm the customer name and the requested deliverable.
2. Confirm that the available connector is authorized for that customer.
3. Read the active account and verify the customer-recognizable name.
4. If the connector is unavailable, the account cannot be verified, or the scope is broader
   than the operator's authority, stop. Treat the evidence as unknown, not zero.

External agencies and resellers must use per-account or otherwise least-privileged access. A
public repository never grants account access.

## 2. Collect only what the story needs

Typical evidence categories:

| Evidence | Question it answers |
|---|---|
| Visibility and customer actions | What changed against a comparable period? |
| Branded and non-branded discovery | How much demand came from people not searching for the brand? |
| Publishing cadence and status | Is approved local activity running as intended? |
| Review volume, rating and reply coverage | Where is reputation work complete or missing? |
| Listing completeness | Which approved business facts need attention? |
| Directory presence | Where is the location represented or absent? |
| Sentiment and topics | What themes recur in customer feedback? |

Use the minimum queries required. Do not export unrelated customer data.

## 3. Make the comparison valid

- State the measurement window and comparison window.
- Compare like with like, including portfolio and geography.
- Note partial onboarding or location changes.
- Label current-page samples as samples.
- Page through before stating a population rate.
- Use absolute values when a small base makes percentages misleading.
- Never claim causality from correlation.

## 4. Record evidence outside this repository

For the private customer deliverable, record each figure with:

- customer-recognizable label
- metric and unit
- period and geography
- source and capture date
- measured, supplied, estimated or inferred state
- any limitation

Never commit account identifiers, raw exports, contact details or private correspondence.
Customer-specific metrics stay private unless the operator explicitly approves a curated
aggregate card in the public proof register. Metrics approval does not grant naming permission.

## 5. Hard boundary

No writes: no posts, review replies, profile edits, bulk updates, connection flows or account
settings. If a tool would change what a customer's customers see, it is out of scope.

Billing or subscription anomalies go to an Obenan owner in a private internal note and never
onto a customer-facing page.

## 6. Existing-client review sequence

Follow [EXISTING_CLIENT_REVIEW.md](EXISTING_CLIENT_REVIEW.md). Discover available tools and
read their current schemas; names below describe the needed reads, not invented API contracts.

1. Read account identity and location inventory. Confirm selected locations and activation
   from authorized connection records or supplied history. Keep account selectors private.
2. Read profile performance for activation to reporting cutoff and the same dates last year,
   per location and total. Preserve timezone, boundary semantics, metric definitions and gaps.
3. Read monthly search terms, counts and raw labels. Page through where possible. Reclassify
   brand variants, addresses, product-plus-brand terms and translated spellings. If the tool
   returns only top terms or censored counts, record that coverage and denominator.
4. Read the latest AI audit/score with its measurement date. No fresh read means historical
   or unknown, never current. Do not substitute the date the agent fetched an old score.
5. Read current and prior-window reviews, ratings and replies. Separate observed replies,
   per-reply automation logs and rule-based inference. Read auto-reply settings to verify
   voice and routing. Default prompts do not establish a bespoke brand voice.
6. Read review-request metrics with event definitions. Opens, sends and completed reviews
   are different measures. Do not attribute reviews to requests without linked evidence.
7. Read post programs and delivered location posts separately. A recurrence schedule is
   planned volume. Sample a live window as a cross-check, not proof of the whole period.
8. Read live profile attributes/services, pre-order links and directory presence. Empty
   records are unknown until coverage is verified; do not equate them with every connection
   being off. Check the customer's actual offerings before proposing attribute changes.
9. If useful, obtain permitted customer photos through a read such as `get_location_posts`.
   Confirm permission, location, resolution and credit. Photos remain in the private build.
10. Only for the optional ad-equivalent scenario, read local CPC evidence with units, date,
    keyword coverage and FX provenance. Missing CPC means omit the scenario, not invent it.

Every read stays read-only. Stop before a tool that creates posts, replies, links, request
campaigns or connection changes. Preserve pagination/truncation gaps in the private ledger.
