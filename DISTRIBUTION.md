# Distribution

This public repository is the agent-ready Obenan sales workspace. It carries public-safe
doctrine, templates, references and approved customer proof. It carries no private customer
data.

Public visibility is for frictionless read access by authorized Obenan employees, agencies and
resellers. It is not an open-source software license and does not authorize redistribution of
customer data or Obenan materials outside approved sales work.

## Two distributions, one source

| Surface | For | How it is produced |
|---|---|---|
| This repository | Employees, agencies and resellers whose agent can read a public URL | Point the agent at the URL and name the task type. No GitHub account is required for read access. |
| The shared Claude project | Colleagues who do not use git | Assembled from this repository. When this repository changes, the project is re-uploaded from it. |

The repository is the source. The Claude project is a build of it. Never edit the project
knowledge directly, or the two drift and nobody can tell which is current.

## What stays out, permanently

- prospect and customer folders, account exports, scraped estates
- billing records, invoices, pricing history, commercial negotiation state
- investor material and internal performance reporting
- private contact lists, personal emails or phone numbers
- security research, authentication findings and internal implementation detail

Those live in the operator's private workspace. Live customer numbers reach a deliverable
through the Obenan MCP at build time.

## Customer success stories

Only customer names and claims marked `APPROVED` in
`knowledge/proof/PUBLIC_PROOF_REGISTER.md` may enter reusable sales material. Public naming
permission does not authorize internal metrics, account structure or private correspondence.

## Keeping it honest

When a document here is superseded, update it here first, then rebuild the Claude project.
Record anything contested in `STATUS.md` rather than quietly editing doctrine.
