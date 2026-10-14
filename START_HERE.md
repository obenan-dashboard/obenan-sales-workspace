# Start here

You are producing a sales deliverable for Obenan. These files are your source of truth.
When they disagree with general sales instinct, the files win.

Before routing any task, read these files in order:

1. `START_HERE.md`
2. `AGENTS.md`
3. `STATUS.md`
4. `CLAUDE.md` only when using Claude Code

Then retrieve the legend and exactly one task row from `knowledge/TASK_ROUTER.md`.

Obenan keeps multi-location businesses found, trusted and chosen everywhere customers look:
Google, Apple Maps, the directories people use, and AI assistants. It runs autonomously on
the business's behalf.

## Step 1. Name the task type

Pick exactly one. They do not blend.

| Task type | You are doing this when |
|---|---|
| `Win-back` | the customer left, lapsed, or went quiet and we want them back |
| `Upsell` | an existing customer uses part of what they own and could use more |
| `Reporting` | a monthly, quarterly or annual account review |
| `New pitch` | a prospect who has never bought |
| `Proposal` | post-meeting, inputs are locked, a priced document is wanted |
| `Meeting recap` | a transcript exists and needs structuring |
| `Outreach` | a single message, email, LinkedIn or WhatsApp |

Infer the task type when the request is clear. A results review is Reporting. Ask only if the
intent is genuinely ambiguous, not merely because the operator did not supply the label.

## Step 2. Retrieve one router row

```bash
grep -n "^| Upsell" knowledge/TASK_ROUTER.md
```

Read the legend at the top of that file plus your row. Do not preload the table.

## Step 3. Get the evidence before writing

For an existing customer, pull their real numbers first.
`knowledge/engagement/MCP_EVIDENCE_RUNBOOK.md` carries the account switch and the exact call
sequence. A deliverable built on adjectives instead of the customer's own data is the weakest
thing we produce.

## Step 4. Build, then hand over

Every deliverable ships with its evidence: each figure, its source, and the date it was
captured. You draft. A person sends.

For Reporting and existing-client Upsell, read
`knowledge/engagement/EXISTING_CLIENT_REVIEW.md`. Rendered results reviews start from
`templates/deck/EXISTING_CLIENT_REVIEW.html`, not the generic sales deck. No connector or
supplied evidence means a labelled template and missing-input list, not invented results.

When using a success story, read `knowledge/proof/PUBLIC_PROOF_REGISTER.md` and its linked
card. Approved stories are named, not anonymized by default. For prospect PDFs with a proof
page, read `knowledge/proof/LE_PAIN_QUOTIDIEN.md` and lead with Joost's exact technology quote,
attribution and video preview: the approved still with its play icon and QR, linked to 2:24,
never a text-only panel. The same card supplies approved three-year LPQ
results: choose discovery/actions before review automation, keep dates and scope, and do not
present ad equivalents or assumed effort as financial outcomes. Do not replace a customer's
own results with LPQ proof.

For multi-location restaurant proof in Colombia, retrieve
[Frisby's six-month Google results](knowledge/proof/FRISBY_COLOMBIA.md). Keep Google scope,
the consecutive-period comparison and action definitions; do not describe clicks as completed
calls or visits, or infer nonbrand discovery, AI visibility or causal revenue.

For a 12-restaurant year-on-year comparison, retrieve
[Urban Fork Group's Google results](knowledge/proof/URBAN_FORK_GROUP.md). Lead with reported
bookings and Maps visibility; preserve the metric definitions and unresolved baseline gap.
Do not claim improved conversion efficiency or infer a country.

For customer logo proof, retrieve `assets/customer-logos/README.md`. Its nine website marks
are approved for reuse, with source provenance and static PDF guidance. Information Seven
explicitly stores for public sharing is usable proof within its recorded scope.

For country-specific pitches, retrieve [the country account guide](knowledge/proof/CUSTOMER_COUNTRIES.md)
and filter its canonical JSON by the requested country. Select relevant account references,
not the entire roster. Country is a location market, not headquarters or whole-chain coverage.
Names do not authorize new logos, metrics or quotes; use separately approved assets and cards.

For agency or reseller pitches about white-label, retrieve the White-label section of
`reference/product-ui/PRODUCT_UI_OVERVIEW.md` and
[the white-label screen index](assets/white-label/README.md). State where Obenan stays visible.
Use the screens only when their register entry is approved.

## Map

| Path | Holds | Load |
|---|---|---|
| `knowledge/product/` | business units, value proposition, features, language and claim boundaries | boundaries always, the rest per row |
| `knowledge/proof/` | separately approved names, aggregate metrics and success stories | whenever reusable customer proof is used |
| `knowledge/sales/` | objections, psychology, conversation engine, patterns, diagnostic framework | per row |
| `knowledge/voice/` | house voice, plus per-market voice modules | one voice per deliverable, never blended |
| `knowledge/engagement/` | the four modes, the analysis doctrine, the MCP evidence runbook | per row |
| `reference/design/` | design principles, brand system, design core, applied guide, token contract, asset library | only when something gets rendered |
| `reference/messaging/` | messaging core and applied messaging guide | when positioning copy is being written |
| `reference/product-ui/` | sales-safe overview of product surfaces and boundaries | only when the task is about the product's screens |
| `assets/logos/` | canonical Obenan logos, SVG; legacy marks under `legacy/` | whenever a document carries the logo |
| `assets/guidelines/` | brand guideline PDFs | when checking logo or wave usage |
| `reference/directories/` | the 104-destination directory roster, A to Z with logos and live links, plus JSON | when directory coverage is named or shown |
| `assets/directory-logos/` | one mark per roster destination, with provenance and checksums | when a document shows directory or platform marks |
| `assets/components/` | rendered components: the homepage channel map and the What comes next card | when a deck shows channels or closes |
| `assets/white-label/` | masked screens of a live agency white-label instance, with approval status | when pitching white-label to an agency or reseller |
| `templates/` | A4 sales deck, eleven-page results review, evidence methods and proposal procedure | per row |
| `examples/` | one anonymized finished brief, as the standard to hit | when calibrating quality |
