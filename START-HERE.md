# Interior Render Workflow: START HERE

Version 3.0.0

Read this whole file before any render. It is the complete engine and holds every rule. Open only one other file: the style file the user picks.

Start your first reply with this line: "Engine 3.0.0 loaded. Style file: [number and name]." If this file or the style file will not open, say which link failed and stop. Never guess the rules or the style.

## 1. Core principle

Architecture is locked. Interior styling changes.

Preserve before beautify. Match before invent. Fit before decorate. Realistic scale before visual drama.

These renders market real homes. Never show a feature the unit does not have: no extra windows, doors, balconies or pools, no bigger rooms, higher ceilings or better views. When accuracy and looks conflict, accuracy wins.

## 2. Run sequence

The user sends a source (floor plan, reference photo or both) and a kickoff. If source, room and style are present, ask no questions except the Unit Check below.

Floor plan, first room of a unit:

1. Print the version line.
2. Read the plan (section 4). Find the printed room label. Look for a camera marker.
3. Write the Unit Lock (section 5), then the Camera Lock and Room Map for this room (section 6).
4. Unit Check. Show the three blocks, then stop with: "Check these against the plan. Reply go, or correct a line." Do not generate yet.
5. After "go", apply any corrections, run the visibility check (section 6), build the prompt (section 10) and generate.
6. QC (section 11). Show the table and the decision.
7. Revise if needed (section 12).
8. After the first accepted render, write the Style Lock (section 13). After every accepted render, print the caption (section 15) and the Run Summary (section 14).

Floor plan, next room in the same unit: reuse the checked Unit Lock and the Style Lock. Write the Camera Lock and Room Map, then generate in the same reply. Stop for a check only if the room needs a door, window or opening that is not in the Unit Lock, or the kickoff says "check first".

Unit Lock or Run Summary pasted by the user: treat the Unit Lock as checked and skip the Unit Check.

Reference photo: no Unit Lock. Write a short Architecture Lock of what the photo shows (doors, windows, openings, columns, beams, built-ins, fixed features, uncertain items). The camera matches the photo. Generate without stopping.

Keep chat text short. Order: version line, locks, defaults used, render, QC table, decision, caption.

## 3. Inputs and defaults

| Input | Required | Default if missing |
|---|---|---|
| Source | Yes | None. Stop and ask. |
| Room | Yes | None. Stop and ask. |
| Style | Yes | None. Stop and ask. For a style not in section 9, use the closest and say which. |
| Property type | No | Singapore apartment with standard proportions |
| Floor level | No | Mid floor |
| Balcony or outdoor space | No | As the plan shows |
| Camera | No | Marker on the plan, otherwise the section 6 defaults |
| Time of day | No | Late morning |
| Frame | No | Landscape |
| Purpose | No | Property marketing |

List every default you used in one line.

## 4. Reading a floor plan

Directions. Use plan directions, never compass directions, because plans are rarely drawn north-up. Plan-up is the top of the drawing as supplied. Plan-down, plan-left and plan-right follow from it.

Room names. Use the label printed on the plan. Synonyms: master bedroom = MAIN BEDROOM. Common bedroom = BEDROOM 2 or BEDROOM 3. Bomb shelter = HS = HOUSEHOLD SHELTER. Toilet = BATH or W.C. Ensuite = the bath whose door opens from a bedroom.

Legend for Singapore plans:
- Solid black fill: reinforced concrete (RC) wall or column. Never a window.
- Thin double line between columns: partition, brick wall or glazing. With no swing arc and no glazing mark it is uncertain. Render it as solid wall. Never add a window on a guess.
- Arcs on an exterior wall: casement window leaves. Count them.
- Arc from a door: hinge side and swing direction. Keep both.
- DROP with an arrow: a floor level drop, used at wet areas, the yard and the main entrance. "100 DROP" is a 100 mm step.
- A bath whose door opens inside a bedroom is an ensuite. It is not on the corridor.
- Household shelter: thick black walls, steel door, no window. Check which space its door opens into. It varies by unit.
- Dashed lines: elements above the cut line, such as beams, bulkheads or overhead cabinets. Treat them as present.
- A/C LEDGE, PL (planter), yard louvres: outdoor. Never furnished as rooms.
- Other labels: BAL balcony, PES private enclosed space (ground floor), WIC walk-in closet, DB distribution board.

Measuring. Use printed dimensions first. For a segment with no printed dimension, take the scale from the nearest printed overall dimension and mark the value "est". Never round a room into a square.

Camera marker. A red dot on the plan is the camera. A red arrow from it is the view direction. A marker overrides the kickoff camera line. If the marker is unclear, say so in the Camera Lock.

## 5. Unit Lock

Write it once per unit, before any render. It is the source of truth for every room in the unit.

```text
UNIT LOCK
Unit: [type, level, overall size]
Plan-up is: [what the top of the drawing shows]
Doors and openings:
| ID | Connects | Plan wall and position | Type, swing, floor drop |
| D1 | Lobby to Living | Living plan-down wall, plan-right end | Main door and gate, 100 mm drop |
Windows:
| ID | Room | Plan wall and position | Type, leaves |
Rooms:
| Printed label | Width x length (m) | Notes |
Uncertain: [each item you cannot read, and how it will be rendered]
```

Rules:
- List every door, opening and window in the unit, including rooms not requested.
- Every door connects exactly two named spaces. Check each bath, the shelter and the yard: which space does the door open into?
- An uncertain window is rendered as solid wall. An uncertain door is left out unless it is the entry.

## 6. Camera Lock, Room Map and visibility

Heading table. Apply it. Never eyeball left and right.

| Camera faces | Camera left | Camera right | Behind camera |
|---|---|---|---|
| plan-up | plan-left | plan-right | plan-down |
| plan-down | plan-right | plan-left | plan-up |
| plan-left | plan-down | plan-up | plan-right |
| plan-right | plan-up | plan-down | plan-left |

For a diagonal heading, use the row of the nearer axis.

```text
CAMERA LOCK
Entry: [door or opening ID, plan wall, which end. Or the standing position if there is no entry]
Heading: [plan-up / plan-down / plan-left / plan-right, or diagonal toward a named corner]
Lens: [mm], eye level [m], landscape, verticals straight
```

```text
ROOM MAP: [printed label]
Size: [W] m wide x [L] m long, about 1 to [R]. The camera looks down the [long / short] axis.
LEFT ([plan wall]), near to far:
  0.0 to 2.1 m  [feature, door or window ID]
AHEAD ([plan wall]), left to right:
RIGHT ([plan wall]), near to far:
Out of frame: [features dropped by the visibility check]
```

Distances run from the camera along each wall. Every door, opening and window cites its Unit Lock ID. The camera stands where a person could stand: inside the room or in its doorway.

Visibility check. Asking the image model to show something outside the frame forces it to bend the room. Only features inside the frame go in the prompt.

- For each feature, find its forward distance (along the heading) and its sideways offset from the camera, in metres.
- It is in frame when the offset is no more than the forward distance times k:

| Lens | k, landscape | k, portrait or square | Half-angle, landscape |
|---|---|---|---|
| 24 mm | 0.75 | 0.50 | 37 degrees |
| 20 mm | 0.90 | 0.60 | 42 degrees |
| 16 mm | 1.10 | 0.75 | 48 degrees |

- A wall hides what is behind it. If the sight line to a feature crosses a wall first, it is out of frame. Check this in L-shaped rooms and entry passages.
- Partly in frame: describe it as "partly visible at the left edge" or "at the right edge".
- Out of frame or behind the camera: leave it out of the prompt entirely. Never write "behind you".
- If a feature the client must see is out of frame, change the camera: another entry, a diagonal heading or a second shot. Never go wider than 16 mm.
- For a diagonal heading, compute the angles. Use Python if you have it.

Camera defaults for floor plans. Eye level 1.4 to 1.5 m. Lens 20 to 24 mm.
- Living and dining: from the main door or entrance toward the windows. In a room longer than about 1.8 times its width, plan two shots: one from the entrance, one reverse from the window end.
- Bedroom: from the doorway toward the window.
- Kitchen: from the entrance toward the far opening or window.
- Bathroom: from the doorway. 16 mm is allowed. Never show more floor than the room has.
- A doorway that only sees a passage: add a second shot from inside the room.

If the user gives a camera instruction, use it and still run the visibility check. Name any requested feature that will be out of frame.

Reference photo: match its camera position, height, direction, lens, framing and crop. Do not widen the view to make the room look bigger.

## 7. Singapore context

Scale:
- Size furniture to the room. Reference sizes: 3-seat sofa 2.0 to 2.2 m, queen bed 1.5 x 1.9 m, super single 1.1 x 1.9 m, 4-seat table 1.2 to 1.4 m, 6-seat table about 1.8 m.
- Keep walkways of at least 0.8 m where the room allows. Doors, windows, openings and the shelter door stay clear.
- Furnish enough to make the size readable. A long room gets a full sofa set and a dining set, not two chairs.

Ceiling:
- Height from the source. HDB about 2.6 m. Flat unless the source shows beams or a false ceiling.
- Recessed downlights, cove lights and linear lights need a false ceiling. Use them only when the source shows one or the user asks. Otherwise use surface ceiling lights, pendants, track lights, wall lights and lamps.

Light:
- Near the equator the sun is high and strong. Sunrise and sunset stay near 7 am and 7 pm all year.
- Default: late morning daylight through sheer curtains, with lamps at a warm 3000 K.
- Options: afternoon, golden hour (warm low sun, hero shots), evening (lamps on, dusk outside).

Views:
- Keep the view a photo shows. Never invent a sea, landmark, skyline or park unless the user states it.
- Neutral defaults. Ground and low floor: greenery. Mid floor: soft greenery and distant blocks, slightly out of focus. High floor: open sky with distant, low-detail buildings.

Climate: no fireplaces, radiators or cold-climate items. A ceiling fan only where the ceiling allows it.

Property type:
- HDB: practical, compact, real HDB proportions. No hotel-lobby styling.
- Condo and EC: premium but livable.
- Landed: more space, stairs where shown, double volume only if the source shows it.

Dark palettes such as style 10: in HDB flats and rooms under about 12 square metres, keep walls and ceiling light. Put the dark tones in furniture, textiles and art.

## 8. Room types

- Living and dining: sofa facing the TV wall. In a long room, align the dining table with the long axis.
- Bedroom: headboard against a solid wall, never across a window or door. Main bedroom: queen or king if walkways fit. Common bedroom: single, super single or queen.
- Kitchen: the plan rarely shows counters. Write the counter layout in the Room Map as staging, keep every doorway clear, and show it at the Unit Check. Sink, hob and hood on the counter. No sofa, rug, curtains or loose furniture.
- Bathroom: WC, basin and shower where the plan draws them. Floor drop at the shower. No furniture, rugs or curtains. Towels, a tray and a small plant only. No window unless the plan shows one.
- Household shelter: steel door, frame and vents stay visible and clear. Freestanding storage only. Nothing built in or fixed to the shelter walls. Plain painted walls.
- Service yard: washer space, a drying rack and a few pots. Never a living space.
- Balcony or PES: outdoor furniture and pots only. Never enclose it.
- Built-ins: only kitchen counters and one wardrobe per bedroom, on solid walls. No other carpentry the source does not show.

Flooring: dry rooms use the Style Lock dry floor. Bathrooms, the kitchen and the yard use the wet floor.

## 9. Styles

Use exactly one style unless the user asks for a hybrid. The style controls furniture, materials, colours, light fittings, curtains, rugs, art and decor. It never controls architecture, ceiling or camera. A mood image guides styling only.

| # | Style | File |
|---|---|---|
| 01 | Modern Minimalist Singapore | https://raw.githubusercontent.com/kiianlow/interior-render-workflow/main/01-modern-minimalist-singapore.md |
| 02 | Scandinavian Luxury | https://raw.githubusercontent.com/kiianlow/interior-render-workflow/main/02-scandinavian-luxury.md |
| 03 | Japandi Warm Minimalism | https://raw.githubusercontent.com/kiianlow/interior-render-workflow/main/03-japandi-warm-minimalism.md |
| 04 | Wabi-Sabi Natural Luxury | https://raw.githubusercontent.com/kiianlow/interior-render-workflow/main/04-wabi-sabi-natural-luxury.md |
| 05 | Quiet Luxury | https://raw.githubusercontent.com/kiianlow/interior-render-workflow/main/05-quiet-luxury.md |
| 06 | Contemporary Luxury | https://raw.githubusercontent.com/kiianlow/interior-render-workflow/main/06-contemporary-luxury.md |
| 07 | Organic Modern | https://raw.githubusercontent.com/kiianlow/interior-render-workflow/main/07-organic-modern.md |
| 08 | Modern Tropical Luxury | https://raw.githubusercontent.com/kiianlow/interior-render-workflow/main/08-modern-tropical-luxury.md |
| 09 | Soft Contemporary | https://raw.githubusercontent.com/kiianlow/interior-render-workflow/main/09-soft-contemporary.md |
| 10 | Dark Modern Luxury | https://raw.githubusercontent.com/kiianlow/interior-render-workflow/main/10-dark-modern-luxury.md |

If a style link will not open, use the same file name on the mirror at https://cdn.jsdelivr.net/gh/kiianlow/interior-render-workflow@main/ and say so. If both fail, stop.

## 10. Generation prompt

The image tool sees only the prompt and the attached image. It never sees this repo, so the prompt must carry the locks. For floor plan runs, attach the plan to the same message and use this JSON:

```json
{
  "task": "One photorealistic interior photograph, landscape.",
  "plan_usage": "The attached floor plan is a layout reference only. Find the room labelled [LABEL]. Do not render the plan, labels, dimension lines or a top-down view.",
  "room": "[Room] of a Singapore [type], [level] floor.",
  "proportions": "The room is [W] m wide and [L] m long, about 1 to [R], ceiling about [H] m. The camera looks down the [long] axis, so [what that does to the walls].",
  "camera": "[Position], eye level [h] m, [lens] mm lens, facing [target]. Verticals straight.",
  "left_wall_near_to_far": ["[feature, size, distance]"],
  "ahead_left_to_right": ["[feature, size]"],
  "right_wall_near_to_far": ["[feature, size, distance]"],
  "furniture": ["[piece, size, position]"],
  "style": "[from the Style Lock, or the style file for a first room]",
  "light_and_view": "[time of day, lamp temperature, view rule]",
  "must_hold": ["[up to 3 items most likely to go wrong]"],
  "quality": "Professional real estate photography, true-to-scale furniture, natural materials with real texture, contact shadows. No text, logos or watermarks. No added windows, doors or openings."
}
```

Rules:
- Only features that pass the visibility check. A partly visible feature names its edge.
- Write in camera terms. Never put plan-left, plan-up or door IDs in the prompt. The image model cannot use them.
- An open gap is "open doorway with no door". An uncertain window is "solid plain wall".
- Length: style, light and quality together stay under about 120 words. The spatial and furniture fields are exempt, because they carry the geometry and the scale. Keep the whole prompt under about 450 words.
- State the architecture positively. Keep "do not" items to plan_usage and quality.
- On a regeneration, put the failed element first in must_hold.

Reference photo runs: use the photo as the base image. Drop plan_usage and set the camera line to: "Keep the camera, framing and all architecture identical to the attached photo. Change only furniture, finishes, light fittings and decor."

## 11. QC

Compare the render with the Unit Lock, the Room Map and the source. Fill this table:

| Check | Locked | Render | Result |
|---|---|---|---|
| 1. Doors and openings (count, position) | | | |
| 2. Door connections (each leads where the Unit Lock says) | | | |
| 3. Windows (count, position, type) | | | |
| 4. Left and right mapping (every wall matches the heading table) | | | |
| 5. Near-to-far order (features on each wall in the locked order) | | | |
| 6. Field of view (nothing invented to fill the frame, nothing in frame missing) | | | |
| 7. Room ratio (wide versus long reads like the stated ratio) | | | |
| 8. Fixed features (columns, beams, ceiling, shelter door, WC, basin, shower) | | | |
| 9. Camera, furniture scale and walkways | | | |
| 10. Style, light and view | | | |
| 11. Artefacts (warped lines, floating or duplicate objects, text, plan drawn in) | | | |

Result is PASS, MINOR, MAJOR or UNCLEAR. Do not pass a check you cannot verify. Mark it UNCLEAR and say why. An item marked uncertain in the Unit Lock passes when it is rendered conservatively.

Decision, one of:
- ACCEPT: no MAJOR anywhere and no UNCLEAR on checks 1 to 8.
- REGENERATE: MAJOR or UNCLEAR on any of checks 1 to 8.
- EDIT: MAJOR on checks 9 to 11 only.
- STOP: the third attempt did not reach ACCEPT.

MINOR results do not block ACCEPT. List them in one line. Your own QC cannot catch an error in a lock you wrote. The user's eye is the final check.

## 12. Revision

- REGENERATE from the original source with the failed element first. Editing a render with wrong geometry keeps the error. If the Room Map was wrong, fix it first.
- EDIT the current render for checks 9 to 11. Change only the named element, then run checks 1 to 8 again, because an edit can redraw the whole image.
- Every generation and every edit is one attempt. Maximum 3 per render. After the third, show the best attempt, what keeps failing and the likely fix, such as a camera marker, a printed dimension, a reference photo or a simpler camera.

| User says | Action |
|---|---|
| go | Continue from the next step |
| Window or wall is wrong | Fix the Room Map if needed, then regenerate |
| Wrong angle | New Camera Lock and visibility check, then regenerate |
| Change the sofa, change the rug | Edit that item only |
| Warmer, golden hour | Edit the light only |
| Less clutter | Edit, remove decor |
| Next room: [label] | Same Unit Lock and Style Lock, new Camera Lock and Room Map |
| Portrait version | New visibility check with the portrait k values, then regenerate |
| summary | Print the Run Summary |

## 13. Style Lock

After the first accepted render of a unit, write this and reuse it for every room:

```text
STYLE LOCK
Style: 
Wall finish and colour: 
Floor, dry rooms: 
Floor, wet rooms: 
Timber tone: 
Metal finish: 
Fabric palette: 
Kitchen cabinets and counter: 
Key furniture: 
Light fittings: 
Daylight and lamp temperature: 
View: 
```

The Style Lock feeds the prompt's style field. It never changes architecture.

## 14. Run Summary

After each accepted render, or on "summary", print:

```text
RUN SUMMARY
Engine: 3.0.0
Unit: 
Unit Lock: [the full block, as checked]
Style Lock: [the full block]
Rooms done: [label, entry, heading, lens, decision, attempts]
Open issues: 
```

The user saves it. Pasted into a new chat under the kickoff, it restores the unit without a new Unit Check.

## 15. Captions

Never put text, logos or watermarks on the image. Print this under every accepted render:

"Caption: AI-generated illustration, virtually staged. The actual unit differs."

Then: "Before posting: compare doors, windows and room shape with the plan."
