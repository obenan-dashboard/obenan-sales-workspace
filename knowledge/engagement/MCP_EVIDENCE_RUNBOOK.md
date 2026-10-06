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

Never commit account identifiers, raw exports, contact details, private correspondence or
customer-specific metrics to this public repository.

## 5. Hard boundary

No writes: no posts, review replies, profile edits, bulk updates, connection flows or account
settings. If a tool would change what a customer's customers see, it is out of scope.

Billing or subscription anomalies go to an Obenan owner in a private internal note and never
onto a customer-facing page.
