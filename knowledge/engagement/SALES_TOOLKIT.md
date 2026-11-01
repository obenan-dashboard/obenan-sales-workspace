# Sales toolkit: interactive sections

Six reusable sections for pitch pages and their PDFs, in one shared stylesheet and script:
`templates/sections/toolkit.css` and `templates/sections/toolkit.js`. Three worked examples
show how the buyer's question changes which sections appear and in what order:
[coffee](../../templates/sections/coffee.html), [banking](../../templates/sections/banking.html)
and [fitness](../../templates/sections/fitness.html).

The examples use synthetic names and rows. They are teaching material, not customer pages.
Customer builds live in a private workspace, never in this repository.

## Start here

1. **Name the job.** Task, audience, vertical, language and the buyer's question in their words.
2. **Pick a recipe** below. It is a starting order, not a fixed page count. Drop any section
   that does not answer the question. Reviews never make up most of a page.
3. **Collect evidence privately.** Each figure needs a source and a date in your private
   `EVIDENCE.md`. Missing values stay `Unknown`, never zero.
4. **Build the closest example** into a private folder outside the repository with
   `node scripts/build_toolkit_example.cjs --example coffee --out DIR`. It copies `toolkit.css`,
   `toolkit.js` and every referenced asset. Replace synthetic rows with checked findings in the
   built copy. Keep every disclosure label.
5. **Render, check and hand over** with the commands at the end. A person reviews and sends.

## Copy-paste instruction for an agency agent

```text
Read https://github.com/obenan-dashboard/obenan-sales-workspace and follow START_HERE.md.
Task type: Interactive sections. Read knowledge/engagement/SALES_TOOLKIT.md and its router row.
Treat the shared workspace as read only. Build in a private folder outside the repository.

Buyer and audience: [company, who reads it, language]
Vertical: [coffee and restaurants | banking | fitness | other]
Buyer question: [in their words]
Evidence: [private paths to checked findings, with sources and dates]
Naming and proof rights: [approved proof cards, or NONE]
Commercial authority: [exact prices permitted, or NONE]
Output: [web page | PDF | both]
Reviewer and sender: [human who approves and sends]

Pick the sections that answer the buyer question, in that order. Start from the closest
example in templates/sections/ and the shared toolkit.css and toolkit.js. Keep every
disclosure label on screen and in print. Missing values read Unknown. Quote approved proof
exactly. Inputs in the business case start empty. Render the PDF with Chrome, view every page,
run the checks and record sources in a private EVIDENCE.md. Draft only. Send nothing.
```

## The six sections

Each section is a `<section class="tk" data-section="...">` with a `<p class="tk-label">`
disclosure as its first child. Without JavaScript every section is complete and readable;
the script only adds motion and controls. Print shows the static form.

| Section | `data-section` | Use it when | Print form | Adapt |
| --- | --- | --- | --- | --- |
| Product teaser | `teaser` | The buyer has not seen the product. One headline, one film. | Poster, plus link and QR only for an approved public address | Keep the label "Concept product film". Never quote a number from the film. |
| Observed and proposed | `compare` | One location shows a concrete gap. | Both states side by side | Observed comes from a dated check. Proposed is a proposal, never shown as achieved. |
| Review stream | `reviews` | Guest experience is part of the question. | Static grid of cards | Themes, not reviewer names. State "N unique"; the motion copies never count. |
| Portfolio explorer | `portfolio` | Many locations and the buyer asks where. | Full table | One row per location. Separate types (cafés and kiosks, branches and ATMs, clubs and studios). Unknown is not zero. |
| Assistant walkthrough | `assistant` | The buyer asks how an answer would look. | Full conversation | Question, response, conclusion. Label it a scripted demonstration, not a live connection. Use only facts already on the page. |
| Business case | `business-case` | The buyer asks what would have to be true, or who decides. | Blank inputs and owners | Buyer inputs only, empty by default. The result is a break-even threshold. Owners and next steps, no prices unless authorised. |

Two supporting blocks reuse approved material: the **directory network** (`network`) shows
the existing channel images and the roster counts, and **proof** (`proof`) quotes an approved
card from [the proof register](../proof/PUBLIC_PROOF_REGISTER.md) exactly as written.

## Recipes

| Recipe | Buyer question | Starting order |
| --- | --- | --- |
| Coffee and restaurants | Can guests find the right café, the current menu and the real hours, and is every café consistent? | teaser, compare, portfolio, reviews, assistant, network, proof, business case |
| Banking | Who owns the truth about each branch and each ATM? | portfolio, compare, assistant, network, business case (governance, no calculator) |
| Fitness | Do people nearby understand the offer well enough to book a trial, and do trials become memberships? | compare, teaser, assistant, portfolio, business case (trial to membership threshold) |

**Coffee and restaurants:** discovery, menus, consistency between locations and the guest
experience. Lead with a real gap at one café.

**Banking:** count branches and ATMs separately; an ATM inside a branch is its own row.
Accurate information and network governance come first: who approves hours, services,
closures and public wording. Read `knowledge/product/BUSINESS_UNITS.md` for the unit types.

**Fitness:** club discovery, an offer people understand and trial to membership measurement.
The calculator chains contribution per membership, trial conversion and booking rate.

## Evidence and claims

- Read current values from their source. Roster counts come from
  `reference/directories/directories.json`; a listed destination is not necessarily active.
- Quote proof cards verbatim. Never restate them in new words or add a number.
- Never state guaranteed results, savings, return figures, invented visibility scores,
  promised rating rises, review counts as search share or scale claims without a source.
- Never ask only happy guests for reviews, and never present a scripted answer as live.
- Keep private exports, account identifiers, reviewer identities and unapproved quotes out of
  this repository. Language rules: `knowledge/product/LANGUAGE_AND_CLAIM_BOUNDARIES.md`.
- In a Decision Pack, the narrow toolkit exception in
  [DECISION_PACK.md](DECISION_PACK.md) keeps these labels; every other rule there stands.

## Film

[The concept film](../../assets/product-film/README.md) is **held privately** until the
approvals listed there are recorded. It is not in this repository and has no public address.
The build leaves the teaser section out unless a person supplies the reviewed rendition:

```bash
node scripts/build_toolkit_example.cjs --example coffee --out DIR --film-dir PRIVATE_FILM_DIR
```

The build refuses a rendition or poster whose checksum differs from the README. The film page
then plays it with `preload="none"`, controls and no autoplay, and the PDF shows the poster with
"No public address is approved for this film yet." Add `--film-url URL` only once an approved,
working public address exists; the PDF then carries a clickable poster, link and QR.
[DESCRIPTION.md](../../assets/product-film/DESCRIPTION.md) is the scene by scene text.

## Build and check

Needs Node 18 or later, Python 3, ripgrep (`rg`) and Google Chrome or Chromium. The tests and
the validator fail on purpose when `rg` is missing. `pdftoppm` (poppler) is optional and adds
the PDF page fill check. From the repository root:

```bash
python3 -m unittest discover -s tests -v
bash scripts/validate_public_repo.sh
npm install --no-save --no-package-lock --prefix out/.tools \
  playwright-core@1.56.1 qrcode@1.5.4 jsqr@1.4.0 pngjs@7.0.0
node scripts/check_toolkit_browser.cjs
```

The npm step installs pinned tools into the ignored `out/.tools`; no package file is added.
The browser check builds every example into a temporary folder, serves it on a loopback port
and tests 390, 768, 1440 and 1920 px, keyboard tabs and filters, Unknown sorting, the business
case arithmetic, the chat replay, the review stream pause, reduced motion, no JavaScript, fast
scrolling and the A4 PDF. It writes captures, PDFs and `receipt.json` to `out/toolkit/` and
exits 1 on any failure. Set `CHROME=/path/to/chrome` if Chrome is not found. Film checks are
reported as skipped unless `TOOLKIT_FILM_DIR` points at the held rendition.

To preview one build, serve the build folder on loopback and open it:

```bash
node scripts/build_toolkit_example.cjs --example coffee --out /tmp/toolkit-coffee
python3 -m http.server 8765 --bind 127.0.0.1 --directory /tmp/toolkit-coffee
```

Then open `http://127.0.0.1:8765/`. Render the PDF from the build with Chrome headless
`--print-to-pdf` (see `CLAUDE.md`), or use `out/toolkit/coffee.pdf` from the check. Open the PDF
and read every page.

## Where the mechanics came from

Patterns were reused from earlier pitch sites; their data, logins, analytics and claims were not.

| Mechanic | Source repository and commit |
| --- | --- |
| Tabs, threshold calculator, decision wording | `trainmore` at `3b9f41443d16` |
| Review stream, sortable location table | `bluestonelane` at `20461fe00a66` |
| Scroll triggered reveal with reduced motion end state | `isbank` at `d8b55b890a3b` |
| Paginated review grid | `akbank` at `b725cbf51f6a` |
| Timed assistant reveal | `yapikredi` at `157e4c1a2b68` |
