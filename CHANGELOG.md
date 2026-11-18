# Changelog

## 3.0.0

Major version because the run sequence changed: the first room of a unit now stops for a Unit Check before rendering.

Why: a field test on an HDB 4-room BTO (wabi-sabi, 9 rooms, floor plan only) shipped a spatial error in every room. Left and right were mirrored in three rooms. Doors were centred that sit in corners. The ensuite was placed on the corridor. The kitchen and shelter were described where the camera could not see them. QC could not catch any of it, because it compared each render with locks ChatGPT had written itself.

Run sequence and checks:
- Version handshake. The first reply starts "Engine 3.0.0 loaded" and stops if the rules did not load.
- Unit Lock: every door, opening and window in the unit, with the two spaces each connects. Written once per unit.
- Unit Check: ChatGPT stops after the Unit Lock, Camera Lock and Room Map. The user checks them against the plan and replies "go". Later rooms in the unit do not stop.
- A pasted Unit Lock or Run Summary counts as checked.
- Run Summary after each accepted render. It restarts a unit in a new chat.

Plan reading:
- Plan directions (plan-up, plan-down, plan-left, plan-right), never compass directions.
- Heading table that maps plan walls to camera left, right and behind.
- Camera Lock records the entry point and the heading.
- Room Map lists each wall's features near to far, in metres, from printed dimensions or marked "est".
- Visibility check: lens k values for landscape and portrait, walls that hide features, partial features named by edge, out-of-frame features left out of the prompt.
- Proportion line in every prompt: width, length, ratio and which axis the camera looks down.
- Floor plan legend for Singapore plans, room name synonyms, camera marker convention (red dot and arrow).
- Camera defaults: kitchen from the entrance toward the far opening or window. Long living rooms get two shots. A doorway that only sees a passage gets a second shot from inside.

Prompt and QC:
- JSON prompt template with a plan-usage line, so the image model does not render the plan.
- Length rule: style, light and quality under about 120 words. Spatial and furniture fields exempt. Whole prompt under about 450 words.
- QC is one 11-row table, in START-HERE only. Rows added: door connections, left and right mapping, near-to-far order, field of view, room ratio. Fixed decisions: ACCEPT, REGENERATE, EDIT, STOP. Edits count as attempts and get the hard checks again.

Rooms and context:
- New Room types section: wet rooms, kitchen counters as declared staging, shelter, yard, balcony, built-ins.
- Household shelter: freestanding storage only, steel door and vents clear. SCDF permits only drilling up to 50 mm for inserts and removable screws, and bars fixtures that are not easily removable. Showing nothing fixed is the safe choice for a marketing image. Sources: SCDF Technical Requirements for Household Shelters, clause 7.2 (https://www.scdf.gov.sg/civil-defence-shelter/acts-and-requirements/table-of-content/chapter-7---permitted-and-not-permitted-works-in-hs-tower/clause-7.2-permitted-and-not-permitted-works/) and BCA permitted works guide (https://www1.bca.gov.sg/regulatory-info/building-control/household-and-storey-shelters/permitted-and-not-permitted-works).
- Ceiling rule: recessed, cove and linear lights only where a false ceiling exists. This resolves a conflict between styles 01, 06 and 10 and the no-bulkhead rule.
- Daylight and lamp temperature split. Lamps warm 3000 K.
- Dark palette rule for small rooms and HDB flats.
- Style Lock adds wet-room floor, kitchen cabinets, light fittings and view.
- Caption now names AI: "AI-generated illustration, virtually staged. The actual unit differs." CEA has said agents must highlight AI-generated or enhanced images (MTI written reply, Feb 2026: https://www.mti.gov.sg/newsroom/written-reply-to-pqs-on-regulations-for-advertisements-that-make-false-claims-by-using-ai-generated-images).

Kickoff:
- One kickoff, in kickoff.md and README, in the user's field order. Raw link with a jsDelivr mirror fallback. The GitHub blob link is gone.
- Short kickoff for the next room. A new-chat route using the Run Summary.

Styles:
- Titles use a colon, not an em dash.
- Every style gains a Wet Areas and Kitchen section.
- Styles that name recessed, cove or linear lights carry the false ceiling note.
- Style 01 renamed Modern Minimalist Singapore and no longer says condominium, since the index offers it for HDB.
- Style 04 absorbs white oak and matte black or aged bronze metal from the field-test Style Lock.
- Style 06 cabinetry is freestanding. Style 08 no longer suggests ventilation openings.

Files:
- Added: CLAUDE.md, fov.py, validate.py, test-unit-hdb-4room.md, test-unit-hdb-4room.json, .github/workflows/validate.yml.
- Deleted, because START-HERE now holds every rule: architecture.md, perspective.md, materials.md, negative-rules.md, singapore-context.md, floorplan-analysis.md, generation-prompt.md, quality-control.md, qc-report.md, refinements.md, style-lock.md.
- Layout stays flat. Folders would change every raw link in START-HERE and in saved kickoffs, for no gain to ChatGPT. The .github folder holds only the check that runs on push.

## 2.0.1

- Switched to a flat structure. All files live in the root because the GitHub web uploader flattens folders.
- Updated style links and file references in START-HERE and README.

## 2.0

- Fixed a flattened upload that placed 29 duplicate files in the repo root. START-HERE pointed to the older folder copies, so newer edits were never read.
- Removed 3 legacy short style files that conflicted with the numbered styles.
- Kept the detailed style files (about 2 to 3 KB each) over the short root versions.
- Made START-HERE the single complete engine file so ChatGPT only needs one fetch, plus one style file.
- Added raw file links, which return clean text instead of GitHub page markup.
- Added Singapore context: scale, fixed features, floorplan labels, equatorial light, view rules, climate.
- Added floorplan-only camera defaults.
- Changed QC to an evidence table with counts and an UNCLEAR result.
- Split revision into regenerate (architecture or camera) and edit (styling), with a 3-attempt cap.
- Added Style Lock for multi-room consistency.
- Added marketing accuracy rules and a kickoff prompt file.
- Merged ENGINE.md, SYSTEM.md, PROPERTY-CONTEXT.md and workflow/ into START-HERE and rules/ to remove conflicting priority lists.
- Merged three overlapping prompt files into one generation prompt template.
