# Customer references by country

Use [customer-countries.json](customer-countries.json) when a pitch needs customer names
from a particular market. Each row contains only `brand` and `country`. Filter by country,
then choose references relevant to the prospect's industry. Never copy every name into a deck.

Example request: "Build a Netherlands restaurant pitch. Follow START_HERE.md and use the
country index to select relevant local customer references."

## Source and meaning

Snapshot: **2026-10-13**. Source: the operator-supplied complete CSV from a read-only SQL
console query against the application replica, reconciled to its 556-row result. This is a
dated account-presence extract, not a live billing audit or a complete all-time customer list.

The query retained active, non-deleted, non-churned, non-merged accounts with active,
approved locations, excluding deleted, churned, deletion-requested and permanently closed
locations. Temporary closures and locations without an opening-status value can remain.
Database state is not evidence of current payment, current physical opening or endorsement.

`country` means an eligible location's country, not account headquarters or incorporation.
Country codes and explicit country spellings were reconciled; aliases were normalized and
duplicate brand-country pairs removed. Conflicts and unknown countries are held privately,
never inferred from a business name or another location.

`brand` preserves the account display name. Some names are legal entities, agencies or
portfolio labels, not a verified consumer-facing chain brand. Presence in several countries
means the account has locations in those markets. It is not whole-chain coverage, proof that
the named agency itself has an office there, or permission to name its underlying clients.
Unverified personal labels and Obenan's own account are excluded.

## What agents may use

Seven approved public **brand names and countries only** on 2026-10-13. Use them as dated
account references, not testimonials. Approval is recorded in
[PUBLIC_PROOF_REGISTER.md](PUBLIC_PROOF_REGISTER.md). Review by **2027-01-13**; refresh or
reconfirm before reuse after that date. Refresh sooner before making a current-status claim.

For metrics or quotes, retrieve the separately approved success-story card. This roster does
not change a historical story's geography, measurement cohort or location count. A present
location country cannot establish where a past comparison was measured.

For logos, use only the separately approved exact assets in
[the customer logo index](../../assets/customer-logos/README.md). Name approval does not grant
logo, photo, quote or metric approval. If a suitable approved logo is unavailable, use the name
as text; do not fetch or fabricate a mark under this approval.

Raw exports, identifiers, location counts, contact details, query text, billing and account
status records remain private. Only this two-field extract is public. No CRM records were
created or changed by this publication.
