# Interior Render Workflow: START HERE

Version 2.0.1

Read this whole file before any render. It is the complete engine. The other files in this repo add detail. If any file conflicts with this one, this file wins.

## 1. Core principle

Architecture is locked. Interior styling changes.

Preserve before beautify. Match before invent. Fit before decorate. Realistic scale before visual drama.

## 2. Run sequence

The user sends a source image plus a short kickoff (room, style, property context). If source, room and style are present, do not ask clarifying questions. Use the defaults in section 3 for anything missing and list which defaults you used.

1. Read the source image(s).
2. Open the selected style file (links in section 8).
3. Write the Architecture Lock (section 4) and show it in the chat.
4. Write the Camera Lock (section 5).
5. Apply Singapore property context (section 6).
6. Define the room design and furniture staging.
7. Build the generation prompt (section 9) and generate.
8. Run evidence-based QC (section 10) and show the QC table.
9. Revise using section 11.
10. After the first accepted render of a unit, write a Style Lock (section 12) and reuse it for every other room in that unit.

Chat output order: Architecture Lock, Camera Lock, Defaults used, render, QC table, decision. Keep text short.

## 3. Inputs and defaults

| Input | Required | Default if missing |
|---|---|---|
| Source image | Yes | None. Stop and ask for it. |
| Room | Yes | None. Stop and ask for it. |
| Style | Yes | None. Stop and ask for it. |
| Property type | No | Singapore apartment with standard proportions |
| Floor level | No | Mid floor |
| View | No | Neutral view for the level (section 6) |
| Camera | No | Generated camera (section 5) |
| Time of day | No | Late morning daylight |
| Format | No | Landscape |
| Purpose | No | Property marketing (section 7) |

## 4. Architecture Lock

Before generating, list what the source shows. Use counts and wall positions, not general statements.

- Room shape and proportions. Dimensions if printed.
- Doors: count, which wall, swing direction.
- Windows: count, which wall, type (full-height, bay, casement, sliding).
- Openings to other rooms.
- Columns, beams, bulkheads, ceiling level changes.
- Built-ins: kitchen runs, wardrobes, household shelter door, DB box, fixed cabinetry.
- Outdoor elements: balcony, yard, planter, AC ledge, PES.
- Stairs, railings, pool, deck where they exist.
- Uncertain items: list them and render them conservatively.

Do not move, resize, add, remove, mirror, straighten or redesign any locked element unless the user asks. If the style conflicts with the architecture, change the styling.

Floorplan reading notes:
- Common Singapore plan labels: HS (household shelter, steel door, must stay), BAL (balcony), PES (private enclosed space, ground floor), A/C LEDGE and PL (planter) are outdoor and not furnished as rooms, WIC (walk-in closet), DB (distribution board).
- Door swings show door position and opening direction. Keep both.
- Dashed lines usually mark elements above the cut line, such as beams, bulkheads or overhead cabinets. Treat them as present.

## 5. Camera Lock

Reference photo supplied: use it as the base image. Match camera position, height, direction, lens, framing and crop. Do not widen the view to make the room look bigger.

Floorplan only: the camera is generated. State it in one line, for example: "Camera: from the main door looking toward the balcony, eye level 1.4 m, 24 mm equivalent, verticals straight." Defaults:

- Eye level about 1.4 to 1.5 m.
- Lens 20 to 24 mm full-frame equivalent. Never wider than 16 mm.
- Vertical lines stay vertical.
- Living and dining: from the entrance or a corner, looking toward the windows or balcony.
- Bedroom: from the doorway toward the window, bed seen at an angle.
- Kitchen: from the kitchen entrance along the main counter run.
- Bathroom: from the doorway. Do not show more floor area than the room has.

If the user gives a camera instruction, use it.

## 6. Singapore property context

Scale:
- Singapore homes are compact. Size furniture to the room, not to the style.
- Reference sizes: 3-seater sofa about 2.0 to 2.2 m, queen bed about 1.5 x 1.9 m, 4-seater dining table about 1.2 to 1.4 m.
- Keep walkways of at least 0.8 m where the room allows.
- Ceiling height: use the source. Never add high ceilings, double volume or bulkheads that the source does not show.

Fixed features to keep when present: household shelter steel door and vent, DB box, service yard, AC ledge, planter, bay window ledge, window grilles shown in the photo.

Light:
- Singapore sits near the equator. The sun is high and strong, and sunrise and sunset stay near 7 am and 7 pm all year.
- Default: late morning daylight softened by sheer curtains.
- Options: late morning, afternoon, golden hour (warm low sun for hero shots), evening (interior lights on, dusk outside).

Views:
- Never invent a specific view such as sea, a landmark, a skyline or a park unless the user states it.
- If a photo shows the view, keep that view.
- Neutral defaults: ground and low floor, greenery and landscaping. Mid floor, soft greenery and distant neighbouring blocks, slightly out of focus. High floor, open sky with distant, low-detail buildings.

Climate:
- No fireplaces, radiators or cold-climate items.
- Ceiling fans suit Singapore homes. Add one only if the style suits it and the ceiling allows.

Property type:
- HDB: practical, compact, real HDB proportions. No hotel-lobby styling.
- Condo and EC: premium but livable.
- Landed: more space, stairs where shown, double volume only if the source shows it.

## 7. Purpose and accuracy

Default purpose is property marketing. For marketing renders, never show a feature the unit does not have: no extra windows, larger rooms, higher ceilings, better views, balconies or pools that are not in the source.

Do not put text, captions, logos or watermarks on the image. After an accepted marketing render, remind the user to caption it as virtually staged for illustration.

## 8. Styles

Use exactly one style unless the user asks for a hybrid. Open the style file before writing the room design. The style controls furniture, materials, colours, lighting fixtures, curtains, rugs, art and decor. It never controls architecture or camera.

If the user attaches a mood reference image, it guides styling only.

| # | Style | File |
|---|---|---|
| 01 | Modern Minimalist Singapore Condo | https://raw.githubusercontent.com/kiianlow/interior-render-workflow/main/01-modern-minimalist-singapore.md |
| 02 | Scandinavian Luxury | https://raw.githubusercontent.com/kiianlow/interior-render-workflow/main/02-scandinavian-luxury.md |
| 03 | Japandi Warm Minimalism | https://raw.githubusercontent.com/kiianlow/interior-render-workflow/main/03-japandi-warm-minimalism.md |
| 04 | Wabi-Sabi Natural Luxury | https://raw.githubusercontent.com/kiianlow/interior-render-workflow/main/04-wabi-sabi-natural-luxury.md |
| 05 | Quiet Luxury | https://raw.githubusercontent.com/kiianlow/interior-render-workflow/main/05-quiet-luxury.md |
| 06 | Contemporary Luxury | https://raw.githubusercontent.com/kiianlow/interior-render-workflow/main/06-contemporary-luxury.md |
| 07 | Organic Modern | https://raw.githubusercontent.com/kiianlow/interior-render-workflow/main/07-organic-modern.md |
| 08 | Modern Tropical Luxury | https://raw.githubusercontent.com/kiianlow/interior-render-workflow/main/08-modern-tropical-luxury.md |
| 09 | Soft Contemporary | https://raw.githubusercontent.com/kiianlow/interior-render-workflow/main/09-soft-contemporary.md |
| 10 | Dark Modern Luxury | https://raw.githubusercontent.com/kiianlow/interior-render-workflow/main/10-dark-modern-luxury.md |

If a link will not open, use the matching file at https://github.com/kiianlow/interior-render-workflow and say which one you used.

## 9. Generation prompt

The image tool only sees the prompt and the image. It does not see this repo. The prompt must carry the locks.

Build it in this order and keep it under about 200 words:

1. Subject: "Photorealistic interior photograph of the [room] of a Singapore [type], [level] floor."
2. Architecture: state what exists, with counts and positions. Example: "One full-height window on the left wall, sliding door to the balcony on the far wall, kitchen opening on the right, beam across the ceiling near the window."
3. Camera: the one-line Camera Lock.
4. Style: two or three lines taken from the style file (palette, key materials, key furniture).
5. Light and view: time of day and the view rule from section 6.
6. Quality: "Professional real estate interior photography, true-to-scale furniture, natural materials, contact shadows, straight verticals."
7. Exclusions, kept short: "No text, logos or watermarks. No added windows, doors or openings."

State the architecture positively. Long lists of "do not" items dilute the prompt.

Full template: `generation-prompt.md`.

## 10. QC with evidence

Compare the render with the source and fill this table in the chat:

| Check | Source | Render | Result |
|---|---|---|---|
| Doors (count, position) | | | |
| Windows (count, position, type) | | | |
| Openings | | | |
| Columns, beams, ceiling | | | |
| Built-ins and fixed features | | | |
| Room proportions | | | |
| Camera and verticals | | | |
| Furniture scale and walkways | | | |
| View and daylight | | | |
| Style match | | | |
| Artefacts (warped lines, floating or duplicate objects, text) | | | |

Result is PASS, MINOR or MAJOR. Do not pass a check you cannot verify. Mark it UNCLEAR and say why.

Decision: ACCEPT only when there is no MAJOR and no UNCLEAR on doors, windows, openings or proportions.

## 11. Revision

- MAJOR on architecture or camera: regenerate from the original source with a stronger architecture line that names the failed element. Editing a render with wrong geometry keeps the error.
- MINOR or styling issues: edit the current render and change only the named element.
- Maximum 3 attempts per render. After the third, stop. Report what keeps failing and the likely fix, such as supplying a reference photo, stating dimensions, or choosing a simpler camera.

Short user commands and how to handle them: `refinements.md`.

## 12. Style Lock for multi-room units

After the first accepted render of a unit, write this in the chat and reuse it for every other room in the same unit:

- Style number
- Wall colour
- Flooring (continuous across rooms unless the source shows a change)
- Timber tone
- Metal finish
- Fabric palette
- Key furniture pieces
- Lighting temperature and time of day

Template: `style-lock.md`.
