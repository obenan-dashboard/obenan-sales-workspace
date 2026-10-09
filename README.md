# Obenan Sales Workspace

Point your agent at this repository and ask for the deliverable. It guides outreach, a
meeting recap, a proposal, a performance review, or a full presentation, in Obenan's voice,
inside Obenan's claim boundaries, in Obenan's design. Customer-specific outputs require
authorized evidence; this URL does not provide customer-account access.

```
Read https://github.com/obenan-dashboard/obenan-sales-workspace
Follow START_HERE.md. Build an upsell presentation for <account>.
```

This is the sales counterpart to `obenan-design-workspace`. Same discipline, same shape:
a small mandatory bundle, a task router, and deep references that are retrieved only when a
task needs them.

## Layer 1, the mandatory bundle

Every agent reads these four, and nothing else, before routing:

1. `START_HERE.md`
2. `AGENTS.md`
3. `STATUS.md`
4. `CLAUDE.md` if the agent is Claude Code

Then one row from `knowledge/TASK_ROUTER.md`. Not the whole table.

## What is in here

Product truth and claim boundaries, sales craft, voice, the four engagement modes, the MCP
evidence runbook, the public document design system, a sales-safe product UI overview, the canonical logos and
brand guidelines, an A4 deck skeleton and the proposal engine. Everything a sales agent needs
to produce a finished, on-brand deliverable.

## What is not here

No private customer data. No prospect folders, account exports, internal account identifiers,
billing records, pricing history, CRM extracts or security research. Those stay in restricted
Obenan workspaces. This repository carries public-safe doctrine, templates, references and
customer success stories whose names and claims have been approved for public use.

Live customer numbers reach a deliverable through authorized connectors or supplied exports
at build time. Only explicitly approved, dated aggregate proof cards are stored here.
See `knowledge/engagement/MCP_EVIDENCE_RUNBOOK.md`.

Approved public customer proof is governed separately in
`knowledge/proof/PUBLIC_PROOF_REGISTER.md`. A customer name being approved does not approve
internal metrics, account structure or private correspondence.

## Existing-customer results review

Ask your agent:

```text
Read this repository and follow START_HERE.md. Prepare a Reporting results review for
<customer>, using authorized data from <activation date> to <cutoff>, compared with the same
dates last year. Follow EXISTING_CLIENT_REVIEW.md and its eleven-page HTML template. Lead with
discovery, show declines, distinguish delivered work from estimates, and inspect every PDF
page. Keep customer evidence private. If evidence is unavailable, return a labelled template
and the missing inputs. Draft only; do not send.
```

The [review playbook](knowledge/engagement/EXISTING_CLIENT_REVIEW.md) defines the narrative,
evidence and final checks. [Reusable proof](knowledge/proof/README.md) has separate name and
metric permissions. Local checks: `python3 -m unittest discover -s tests -v` and
`bash scripts/validate_public_repo.sh`.
