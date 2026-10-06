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

Start from `templates/deck/DECK_SKELETON.html`. Open the rendered PDF and read every page
before handing it over. Confirm non-English glyphs render.

Every deliverable ships with an `EVIDENCE.md` mapping each figure to its source and date.
