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

If the request names no task type, ask which one before working.

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

## Map

| Path | Holds | Load |
|---|---|---|
| `knowledge/product/` | business units, value proposition, features, language and claim boundaries | boundaries always, the rest per row |
| `knowledge/proof/` | customer names, claims and success stories approved for public use | whenever another customer is named |
| `knowledge/sales/` | objections, psychology, conversation engine, patterns, diagnostic framework | per row |
| `knowledge/voice/` | house voice, plus per-market voice modules | one voice per deliverable, never blended |
| `knowledge/engagement/` | the four modes, the analysis doctrine, the MCP evidence runbook | per row |
| `reference/design/` | design principles, brand system, design core, applied guide, token contract, asset library | only when something gets rendered |
| `reference/messaging/` | messaging core and applied messaging guide | when positioning copy is being written |
| `reference/product-ui/` | sales-safe overview of product surfaces and boundaries | only when the task is about the product's screens |
| `assets/logos/` | canonical Obenan logos, SVG; legacy marks under `legacy/` | whenever a document carries the logo |
| `assets/guidelines/` | brand guideline PDFs | when checking logo or wave usage |
| `templates/` | A4 deck skeleton, proposal generator and procedure | per row |
| `examples/` | one anonymized finished brief, as the standard to hit | when calibrating quality |
