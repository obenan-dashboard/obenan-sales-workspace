---
feature: sales-toolkit-sections
status: in-review
---

# Sales toolkit sections

## Overview

Turn the strongest mechanics from Obenan's past pitch sites into reusable, public-safe
HTML/CSS/print sections with three worked examples (coffee, banking, fitness). A zero-context
agency agent starts at the repository, picks a recipe by the buyer's question, supplies
evidence privately and produces web and PDF output that discloses every demonstration.
Mechanics are reused; pitch datasets, backends, analytics, login and claims are not.

## Criteria

```gherkin
@AC-TOOLKIT-1
Scenario: A zero-context agent reaches one toolkit document from the existing entry points
  Given an agent that starts at START_HERE.md
  When it looks for interactive pitch sections
  Then START_HERE.md, README.md, the task router and BUILD_PROMPT.md point to knowledge/engagement/SALES_TOOLKIT.md
  And the toolkit document names the six sections, three recipes, a copy-paste agency instruction and the check commands
  And no second master prompt, proof ledger or asset catalogue is introduced

@AC-TOOLKIT-2
Scenario: Six sections share one implementation
  Given templates/sections/toolkit.css and templates/sections/toolkit.js
  When an example page is built
  Then it links those shared files, plus at most one stylesheet ported from its named source design, and carries no inline style or script block
  And the teaser and the assistant walkthrough are separate sections

@AC-TOOLKIT-3
Scenario: Recipes vary by the buyer's question, not by duplicated code
  Given the coffee, banking and fitness examples
  Then their section order and section count differ
  And coffee covers discovery, menus, consistency and guest experience
  And banking counts branches and ATMs separately and is about network governance
  And fitness covers club discovery, understandable offers and trial-to-membership measurement
  And reviews are not the majority of any example

@AC-TOOLKIT-4
Scenario: Every demonstration is disclosed on screen and in print
  Given a section that shows a film, scripted chat, synthetic rows or a proposed state
  Then a visible disclosure label sits inside that section and survives print
  And the Decision Pack keeps its customer-page wording rules except for this narrow, named exception

@AC-TOOLKIT-5
Scenario: Content stays inside the evidence and claim boundaries
  Then no example states guaranteed savings, ROI, a visibility score, a promised rating rise, a live MCP connection or other banned claims
  And named proof is quoted verbatim from its approved card and directory counts match directories.json
  And missing values read Unknown, never zero
  And the stated unique review count equals the unique cards, excluding the repeated motion copies

@AC-TOOLKIT-6
Scenario: The concept film stays private until its release is approved
  Given the concept film shows a real restaurant name, a real hotel and a person's photo
  Then no film rendition, poster or QR is stored in the public repository
  And assets/product-film records the scene description, the approvals still needed and the checksums of the held rendition and both masters, without absolute paths
  And the build refuses a supplied film whose checksum differs from the recorded rendition
  And a built page loads a supplied film with preload="none", visible controls, a poster and no autoplay
  And a build without a supplied film leaves the teaser section out instead of showing an empty slot
  And the build refuses an output folder that is not empty before writing anything, so earlier film files never survive a film-free build

@AC-TOOLKIT-7
Scenario: The business case uses only buyer inputs
  Given a business-case section
  Then every input starts empty and the result shows a threshold, not a forecast, until inputs are valid
  And arithmetic on money and rates is exact

@AC-TOOLKIT-8
Scenario: Motion really runs and never blanks content
  When the examples run in a browser at 390, 768, 1440 and 1920 px
  Then a supplied film plays and its time advances, the chat and review stream transition, and there is no horizontal overflow
  And fast scrolling, re-entry, reduced motion and no JavaScript leave every section readable

@AC-TOOLKIT-9
Scenario: The coffee example renders as a static PDF
  When coffee.html is printed to A4 by Chrome
  Then both observed and proposed states, the static review cards, the full conversation and the blank business case appear
  And a supplied film prints as its poster, and a supplied film address prints as a clickable poster, a clickable link and a QR that decodes to that address
  And no motion control or duplicated review card is printed
  And the business case label, every input and the result print on one page, both blank and filled
  And every link in the PDF opens outside the machine that printed it, never a local server address

@AC-TOOLKIT-10
Scenario: Existing material stays compatible
  Then the pinned deck templates are byte-identical, the existing tests pass and the public repository validator passes
  And the validator ignores only the root .git entry, still rejects absolute paths, private details and unapproved names elsewhere, and fails when ripgrep is missing

@AC-TOOLKIT-11
Scenario: An agent outside Obenan builds a self-contained example
  Given a clean copy of the repository and only its public instructions
  When the agent builds an example into a folder outside the repository
  Then every local link and asset in the folder resolves inside that folder
  And every link to a repository document opens its public source pinned to a commit that holds the same text
  And nothing in it points to the repository checkout, a home directory or a private file

@AC-TOOLKIT-12
Scenario: The coffee example is a port of the Bluestone Lane pitch, not a new design
  Given the Bluestone Lane pitch site as the coffee source design
  When coffee.html is built
  Then it links coffee.css after toolkit.css, and coffee.css carries the source colour tokens and fonts scoped to the coffee page
  And the fonts are vendored with their OFL licences, so the page makes no request outside its own folder
  And Joost's interview appears as the approved linked still, the QR labelled Scan to watch and the caption with its printed address, beside his verbatim lead quote
  And the banking and fitness examples do not link the coffee stylesheet
  And the toolkit document maps each coffee section to its source section and names every intentional difference

@AC-TOOLKIT-13
Scenario: The banking example is a port of the bank pitch sites, not a new design
  Given the Yapı Kredi pitch site as the banking layout, with the İşbank and Akbank pitch sites as its references
  When banking.html is built
  Then it links banking.css after toolkit.css and no other vertical stylesheet, and banking.css carries the source colour tokens and Inter, scoped to the banking page
  And no bank's name, logo, photograph or figure appears in the example
  And the toolkit document names the source commits and maps each banking section to its source section with every intentional difference

@AC-TOOLKIT-14
Scenario: The fitness example is a port of the TrainMore pitch site, not a new design
  Given the TrainMore pitch site as the fitness source design
  When fitness.html is built
  Then it links fitness.css after toolkit.css and no other vertical stylesheet, and fitness.css carries the source colour tokens and Inter, scoped to the fitness page
  And no club's name, logo, photograph or figure appears in the example
  And the toolkit document names the source commit and maps each fitness section to its source section with every intentional difference

@AC-TOOLKIT-15
Scenario: An agency agent finds what each vertical may reuse, and the claims stay within the proof
  Given a zero-context agent reading START_HERE.md and the toolkit document
  Then for each vertical it finds the source reference and commit, the reusable sections, the logo files, the media it may use, the usage restrictions and the exact build command
  And the LPQ interview is described as usable and the concept film as held, with each approval the film still needs
  And the coffee example promises no delivery to every directory and no closed door that the proof does not show
```

## Scope

In: shared CSS/JS, six sections, three examples, one recipe document, a build script that
exports a self-contained example, the product film's provenance and release conditions, a narrow Decision Pack exception, routing updates, contract tests
and a local browser check. Out: customer builds, pitch datasets, backends, analytics, login,
hosting or deployment, invented design tokens (source tokens ported per vertical are in), and changes to existing deck templates.
