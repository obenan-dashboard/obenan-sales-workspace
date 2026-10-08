# CLAUDE.md

Claude Code entry point for the Obenan Sales Workspace.

Read in this order before any work:

1. `START_HERE.md`
2. `AGENTS.md`
3. `STATUS.md`
4. One row of `knowledge/TASK_ROUTER.md`, retrieved with grep, not the whole table

Then follow the row.

## Standing rules

- You draft, a person sends. Never send, publish or reply on anyone's behalf.
- Read-only on customer accounts via the Obenan MCP.
- No price, no customer name and no claim without authorisation or a source.
- No em dashes, in any output, in any language.
- Keep the working set small. Retrieve `reference/` files on a trigger and cite them.

## Building a rendered document

HTML and CSS with print styles, rendered to A4 by system Chrome headless:

```bash
"/Applications/Google Chrome.app/Contents/MacOS/Google Chrome" \
  --headless --disable-gpu --no-pdf-header-footer \
  --print-to-pdf=out.pdf file://$PWD/deck.html
```

For Reporting and existing-client Upsell, read `knowledge/engagement/EXISTING_CLIENT_REVIEW.md`
and use `templates/deck/EXISTING_CLIENT_REVIEW.html`. Other sales decks start from
`templates/deck/DECK_SKELETON.html`. Open the rendered PDF and read every page
before handing it over. Confirm non-English glyphs render.

Every deliverable ships with an `EVIDENCE.md` mapping each figure to its source and date.

## Build safety

Keep customer builds and ledgers outside this public repo. Edit source through file/patch
tools. Shell interpolation can silently strip `$` from currencies in HTML. If an environment
requires a heredoc, quote its delimiter, never interpolate the customer source. `A&#36;`
is safe in the review template. Inspect the exported page, not only the source string.

Run `python3 scripts/validate_review.py /path/to/private/EVIDENCE.json` before handover.
Consistency checks do not replace source verification, review-policy checks or visual review.
Run `python3 -m unittest discover -s tests -v` and `bash scripts/validate_public_repo.sh`
before proposing changes to this repository. Work on a branch and review PR, not directly on main.
