# Worked Example: HDB 4-Room BTO, 10th Floor

A full run of START-HERE 3.0.0 on one unit, in wabi-sabi (style 04). Nine rooms, eleven shots. Use it as a model of what each block should look like.

Status:
- Built from the audit brief's reading of the plan (12 Nov 2026) and its printed dimensions.
- Not yet checked against the plan image itself. Treat every "est" value and every item under Uncertain as open.
- Geometry for every shot is in `test-unit-hdb-4room.json`. Run `python3 fov.py test-unit-hdb-4room.json` to reproduce the visibility results below.

To reuse the Unit Lock in ChatGPT, check it against the plan first, then paste it under the kickoff. ChatGPT then skips the Unit Check.

## Unit Lock

```text
UNIT LOCK
Unit: HDB 4-room BTO, 10th floor, 12.85 x 9.80 m overall
Plan-up is: the window facade of Bedroom 2, Bedroom 3 and Living/Dining

Doors and openings:
| ID  | Connects                     | Plan wall and position                                                                 | Type, swing, floor drop |
| D1  | Lobby to Living/Dining       | Living plan-down wall, plan-right end, beside an RC column                              | Main door and gate, 100 mm drop |
| D2  | Living/Dining to Kitchen     | Kitchen plan-up wall, plan-right end. In the Living it is the plan-down wall, plan-left end | Open gap, no door, about 1.0 m est |
| D3  | Living/Dining to Corridor    | Living plan-left wall, 2.1 to 3.1 m from the plan-down wall                             | Open gap, 1.0 m |
| D4  | Corridor to Household Shelter | Shelter plan-up wall                                                                   | Steel door, swings out into the corridor |
| D5  | Corridor to Bath/W.C.2       | Bath 2 plan-up wall, plan-right end                                                     | Door swings in, floor drop |
| D6  | Corridor to Bedroom 3        | Bedroom 3 plan-down wall, plan-left end, hinge at the party wall                         | Door swings in |
| D7  | Corridor to Bedroom 2        | Bedroom 2 plan-down wall, plan-right end, in a recess, hinge at the party wall           | Door swings in |
| D8  | Corridor to Main Bedroom     | Plan-right end wall of the Main Bedroom entry passage, at the plan-left end of the corridor | Door swings in toward plan-left |
| D9  | Main Bedroom to Bath/W.C.1   | Bath 1 plan-up wall, plan-right end, inside the entry passage                           | Door swings in, floor drop |
| D10 | Kitchen to Service Yard      | Kitchen plan-left wall, toward the plan-down end (est)                                  | Door or opening, floor drop |

Windows:
| ID   | Room         | Plan wall and position                               | Type, leaves |
| W1   | Living       | Plan-up wall, full width                             | Casement, 4 leaves |
| W2   | Living       | Plan-right wall, between two RC columns, about 4.6 m | UNCERTAIN, single heavy line. Render solid wall |
| W3   | Bedroom 3    | Plan-up wall, most of the width, RC column at the plan-right corner | Casement, 3 leaves |
| W4   | Bedroom 2    | Plan-up wall                                         | UNCERTAIN type, no swing arcs. Fixed or sliding |
| W5   | Bedroom 2    | Plan-left wall, narrow, faces the recess above the Main Bedroom | Narrow, type uncertain, position est |
| W6   | Main Bedroom | Plan-up wall of the main room, about 1.6 m est       | Casement, 2 leaves |
| W7   | Main Bedroom | Plan-down wall                                       | UNCERTAIN, thin line. Render solid wall |
| Yard | Service Yard | Plan-down side                                       | Louvres or open parapet |

Rooms:
| Printed label        | Width x length (m)                                   | Notes |
| LIVING/ DINING       | 3.25 x 7.15                                          | Long axis plan-up to plan-down. Ratio about 1 to 2.2 |
| MAIN BEDROOM         | Main room about 4.6 x 2.9, plus an entry passage 1.0 x 2.6 est | Ensuite takes the plan-right lower corner |
| BEDROOM 2            | about 3.4 x 3.85                                     | Door in a small recess |
| BEDROOM 3            | about 2.8 x 3.9                                      | |
| BATH/W.C.1           | about 2.4 x 1.6 est                                  | Ensuite. Door from the Main Bedroom passage |
| BATH/W.C.2           | about 1.6 x 2.3 est                                  | Door from the corridor |
| HOUSEHOLD SHELTER    | 2.3 x 2.1 outer, about 1.6 x 1.4 inside est         | Thick RC walls, no window |
| KITCHEN              | 3.2 x 2.3                                            | No cabinetry on the plan |
| SERVICE YARD         | about 2.4 x 1.4 est                                  | Louvres on the plan-down side |
| Corridor             | about 1.0 x 3.9 est                                  | Runs plan-left to plan-right |

Uncertain:
- W2, W4, W7: rendered as solid wall (W2, W7) or plain aluminium-framed panes (W4).
- W5 position along the wall. Out of frame in the Bedroom 2 shot, so it does not reach a prompt.
- D10 position and whether it has a door leaf. Rendered as an open doorway.
- Recess strip about 0.7 m between the kitchen opening and the main door. Rendered as plain wall with a shallow recess.
- A/C ledge below Bath 1, a small shaft beside Bath 1 and Bath 2, a small element at the yard's plan-down right corner. Outdoor or hidden. Not rendered.
- Shelter vent positions. Not marked in this reading. Add them if the plan shows them.
- Basin in Bath 2. Not in this reading. Check the plan.
```

## Style Lock

```text
STYLE LOCK
Style: 04 Wabi-Sabi Natural Luxury
Wall finish and colour: warm limewash-effect paint, soft greige, visible texture
Floor, dry rooms: natural white oak engineered timber, wide planks
Floor, wet rooms: honed grey microcement-look tiles (bathrooms, kitchen, yard)
Timber tone: natural white oak, visible grain
Metal finish: matte black or aged bronze
Fabric palette: linen and raw cotton in sand, clay and charcoal
Kitchen cabinets and counter: white oak flat-panel cabinets, honed travertine-look counter
Key furniture: low linen sofa, solid oak dining table, linen upholstered beds, travertine coffee table
Light fittings: clay or paper pendants, slim surface ceiling lights, linen floor and table lamps. Flat ceiling, no cove
Daylight and lamp temperature: soft late-morning daylight through sheer linen, lamps warm 3000 K
View: 10th floor, neighbouring HDB blocks, treetops and sky, slightly hazy
```

Changes from the field-test Style Lock: cove lighting removed, because cove needs a false ceiling the plan does not show. "Warm about 4000 K" changed, because 4000 K is neutral. Daylight stays daylight and lamps are warm 3000 K. Kitchen flooring and cabinets added.

Style text reused in the prompts:

- Dry rooms: "Wabi-sabi: warm greige limewash-effect walls with visible texture, natural white oak floor, solid white oak furniture, linen and raw cotton in sand, clay and charcoal, unglazed stoneware, rattan accents, dried branches in ceramic vases, matte black and aged bronze metal."
- Wet rooms: "Wabi-sabi: honed grey microcement-look tiles on floor and walls, white oak vanity, stoneware basin, aged bronze tapware, linen towels in sand and clay."
- Light: "Soft late-morning daylight through sheer linen curtains, lamps warm 3000 K. Flat ceiling with clay pendants and slim surface lights, no cove lighting."

## Living/Dining, shot A: hero from the main door

```text
CAMERA LOCK
Entry: D1, Living plan-down wall, plan-right end. Camera just inside, against the plan-right column
Heading: diagonal toward the far plan-left corner (window wall meets Bedroom 3 wall). Nearer axis plan-up
Lens: 20 mm, eye level 1.4 m, landscape, verticals straight

ROOM MAP: LIVING/ DINING
Size: 3.25 m wide x 7.15 m long, about 1 to 2.2. The camera looks down the long axis.
LEFT (plan-left), measured from the entrance wall:
  0.0 to 2.1 m  shelter wall, solid. Only 1.8 to 2.1 m in frame, at the left edge
  2.1 to 3.1 m  D3 open gap to the corridor
  3.1 to 7.15 m Bedroom 3 wall, solid, to the window corner
AHEAD (plan-up), left to right:
  W1 4-leaf casement, full width, from the centre to the right of the frame
RIGHT (plan-right), near to far:
  W2 long wall, render solid, foreshortened. In frame from about 1.6 m on
  RC column at the window end
Out of frame: D2 kitchen opening, the recess, D1 main door (behind the camera)
```

```json
{
  "task": "One photorealistic interior photograph, landscape.",
  "plan_usage": "The attached floor plan is a layout reference only. Find the room labelled LIVING/ DINING. Do not render the plan, labels, dimension lines or a top-down view.",
  "room": "Living and dining room of a Singapore HDB 4-room flat, 10th floor.",
  "proportions": "The room is 3.25 m wide and 7.15 m long, about 1 to 2.2, ceiling about 2.6 m. The camera looks down the long axis, so the side walls run long and the window wall at the far end reads narrow and distant.",
  "camera": "Standing just inside the main entrance in the near right corner, eye level 1.4 m, 20 mm lens, aimed diagonally at the far left corner where the window wall meets the left wall. Verticals straight.",
  "left_wall_near_to_far": [
    "Solid plain wall, only its far end visible at the left edge",
    "Open doorway with no door, 1.0 m wide, 2.1 to 3.1 m from the entrance end, leading to a bedroom corridor",
    "Solid plain wall, 3.9 m long, running to the window corner"
  ],
  "ahead_left_to_right": [
    "Full-width white aluminium casement windows with four leaves at the far end, from the centre to the right of the frame, sheer linen curtains"
  ],
  "right_wall_near_to_far": [
    "Solid plain wall running the full length, foreshortened along the right edge",
    "Square concrete column where it meets the window wall"
  ],
  "furniture": [
    "Near right: 6-seat solid oak dining table, 1.8 x 0.85 m, aligned with the room's length, a linen-cushioned oak bench against the right wall, three linen chairs on its left side, clay pendant above",
    "A clear walkway about 1.4 m wide along the left side, from the entrance to the open doorway",
    "Far half: 3-seat linen sofa, 2.1 m, against the left wall, facing a low oak TV console on the right wall",
    "Travertine coffee table, wool-linen rug about 2 x 3 m, linen lounge chair in the right corner by the window, floor lamp, ceramic vases with dried branches"
  ],
  "style": "Wabi-sabi: warm greige limewash-effect walls with visible texture, natural white oak floor, solid white oak furniture, linen and raw cotton in sand, clay and charcoal, unglazed stoneware, rattan accents, dried branches in ceramic vases, matte black and aged bronze metal.",
  "light_and_view": "Soft late-morning daylight through sheer linen curtains, lamps warm 3000 K. Flat ceiling with clay pendants and slim surface lights, no cove lighting. View from the 10th floor: neighbouring HDB blocks, treetops and sky, slightly hazy.",
  "must_hold": [
    "Long narrow room, about 1 to 2.2, not square",
    "One open doorway in the left wall, in the first half of the room. No other door on the left",
    "Windows only on the far wall"
  ],
  "quality": "Professional real estate photography, true-to-scale furniture, natural materials with real texture, contact shadows. No text, logos or watermarks. No added windows, doors or openings."
}
```

## Living/Dining, shot B: reverse from the window end

This is the shot that shows the shelter wall and the kitchen doorway in proportion. Shot A cannot.

```text
CAMERA LOCK
Entry: none. Camera stands 0.8 m in from the window wall, at the centre of the room width
Heading: plan-down
Lens: 20 mm, eye level 1.4 m, landscape, verticals straight

ROOM MAP: LIVING/ DINING
Size: 3.25 m wide x 7.15 m long, about 1 to 2.2. The camera looks down the long axis.
LEFT (plan-right), near to far:
  W2 long wall, render solid. In frame from about 1.8 m on, to the entrance end
AHEAD (plan-down), left to right:
  RC column, D1 main door and gate (slightly left of centre), plain wall with shallow recess, D2 kitchen opening (right of centre)
RIGHT (plan-left), near to far:
  1.8 to 3.25 m Bedroom 3 wall, solid, partly at the right edge
  3.25 to 4.25 m D3 open gap to the corridor
  4.25 to 6.35 m shelter wall, solid, 2.1 m, to the entrance corner
Out of frame: W1 (behind the camera), the near 1.8 m of both side walls
```

```json
{
  "task": "One photorealistic interior photograph, landscape.",
  "plan_usage": "The attached floor plan is a layout reference only. Find the room labelled LIVING/ DINING. Do not render the plan, labels, dimension lines or a top-down view.",
  "room": "Living and dining room of a Singapore HDB 4-room flat, 10th floor, seen from the window end looking back to the entrance.",
  "proportions": "The room is 3.25 m wide and 7.15 m long, about 1 to 2.2, ceiling about 2.6 m. The camera looks down the long axis toward the entrance, so the side walls run long and the entrance wall reads narrow and distant.",
  "camera": "Standing 0.8 m in front of the window wall at the centre of the room, eye level 1.4 m, 20 mm lens, facing the entrance wall at the far end. Verticals straight.",
  "left_wall_near_to_far": [
    "Solid plain wall running the full length to the entrance, partly visible at the left edge near the camera"
  ],
  "ahead_left_to_right": [
    "Square concrete column at the left corner",
    "Main entrance door with a metal gate, about 1 m wide, slightly left of centre",
    "Plain wall with a shallow recess",
    "Open kitchen doorway with no door, about 1 m wide, at the right end of the far wall, part of the kitchen visible through it"
  ],
  "right_wall_near_to_far": [
    "Solid plain wall, partly visible at the right edge",
    "Open doorway with no door, 1.0 m wide, 3.3 to 4.3 m from the camera, leading to a bedroom corridor",
    "Solid plain wall, 2.1 m long, running to the corner beside the kitchen doorway"
  ],
  "furniture": [
    "Foreground right: arm and side of a 3-seat linen sofa against the right wall, partly visible at the right edge",
    "Foreground centre: travertine coffee table on a wool-linen rug about 2 x 3 m",
    "Left edge: end of a low oak TV console against the left wall",
    "Mid-room left: 6-seat solid oak dining table, 1.8 m, aligned with the room, oak bench against the left wall, linen chairs on its right side, clay pendant above",
    "Open walkway on the right from the dining area to the corridor doorway and the kitchen doorway"
  ],
  "style": "Wabi-sabi: warm greige limewash-effect walls with visible texture, natural white oak floor, solid white oak furniture, linen and raw cotton in sand, clay and charcoal, unglazed stoneware, rattan accents, dried branches in ceramic vases, matte black and aged bronze metal.",
  "light_and_view": "Soft late-morning daylight from the windows behind the camera, lamps warm 3000 K. Flat ceiling with clay pendants and slim surface lights, no cove lighting.",
  "must_hold": [
    "Kitchen doorway in the far wall at its right end, beside the entrance. Not in the right wall",
    "The 2.1 m wall between the corridor doorway and the far corner has no door",
    "Long narrow room seen end to end"
  ],
  "quality": "Professional real estate photography, true-to-scale furniture, natural materials with real texture, contact shadows. No text, logos or watermarks. No added windows, doors or openings."
}
```

## Main Bedroom, shot A: from the door

```text
CAMERA LOCK
Entry: D8, plan-right end wall of the entry passage. Camera in the doorway
Heading: plan-left
Lens: 20 mm, eye level 1.4 m, landscape, verticals straight

ROOM MAP: MAIN BEDROOM
Size: entry passage 1.0 m wide x 2.6 m long, opening into a main room about 2.9 m deep x 4.6 m wide. The camera looks down the passage.
LEFT (plan-down), near to far:
  0.2 to 1.0 m  D9 door to Bath 1, partly at the left edge
  1.0 to 2.6 m  Bath 1 wall, solid
  beyond 2.6 m  the main room opens to the left, hidden by the bath wall
AHEAD (plan-left), left to right:
  far wall, solid RC, no window, about 5.4 m away. Only the slice seen through the passage end
RIGHT (plan-up), near to far:
  0.0 to 2.6 m  wall shared with Bedroom 2, solid, ending at the RC corner
Out of frame: W6 (hidden behind the Bedroom 2 wall), the main room's plan-down wall
```

```json
{
  "task": "One photorealistic interior photograph, landscape.",
  "plan_usage": "The attached floor plan is a layout reference only. Find the room labelled MAIN BEDROOM. Do not render the plan, labels, dimension lines or a top-down view.",
  "room": "Main bedroom of a Singapore HDB 4-room flat, 10th floor, seen from its door.",
  "proportions": "The door opens into a narrow entry passage 1.0 m wide and 2.6 m long. At its end the bedroom opens up, about 2.9 m deep and 4.6 m wide, mostly to the left and out of sight. Ceiling about 2.6 m. Only a slice of the bedroom shows through the end of the passage.",
  "camera": "Standing in the bedroom doorway, eye level 1.4 m, 20 mm lens, looking straight down the passage. Verticals straight.",
  "left_wall_near_to_far": [
    "Closed timber door to the ensuite bathroom, partly visible at the left edge, 0.2 to 1.0 m away",
    "Solid plain wall to 2.6 m, where the passage ends"
  ],
  "ahead_left_to_right": [
    "Through the end of the passage, about 5.4 m away: the solid far wall of the bedroom, no window",
    "Queen bed with its headboard against that wall, left of centre, partly hidden by the corner of the left wall"
  ],
  "right_wall_near_to_far": [
    "Solid plain wall from the camera to 2.6 m, ending at a square concrete corner"
  ],
  "furniture": [
    "Queen bed 1.5 x 1.9 m with linen bedding in sand and clay, headboard against the far wall",
    "Oak bedside table with a ceramic lamp beside the bed",
    "Narrow linen runner on the passage floor",
    "One small framed artwork on the right passage wall"
  ],
  "style": "Wabi-sabi: warm greige limewash-effect walls with visible texture, natural white oak floor, solid white oak furniture, linen and raw cotton in sand, clay and charcoal, unglazed stoneware, dried branches in ceramic vases, matte black and aged bronze metal.",
  "light_and_view": "Soft late-morning daylight falling into the bedroom from a window out of sight on the right, lamps warm 3000 K. Flat ceiling with a slim surface light, no cove lighting.",
  "must_hold": [
    "Narrow passage first, bedroom beyond. The room does not open up until 2.6 m",
    "Bathroom door on the left, right next to the camera",
    "No window in view. The far wall is solid"
  ],
  "quality": "Professional real estate photography, true-to-scale furniture, natural materials with real texture, contact shadows. No text, logos or watermarks. No added windows, doors or openings."
}
```

## Main Bedroom, shot B: from the end of the passage

Added because shot A cannot show the bed or the window. Use it as the room's hero shot.

```text
CAMERA LOCK
Entry: D8, then 2.2 m along the passage to where the main room opens
Heading: plan-left
Lens: 20 mm, eye level 1.4 m, landscape, verticals straight

ROOM MAP: MAIN BEDROOM
Size: main room about 4.6 m wide x 2.9 m deep. The camera looks across the short axis.
AHEAD (plan-left), left to right:
  far wall, solid RC, no window, 3.3 m away, running past the left edge
RIGHT (plan-up), near to far:
  1.5 to 2.7 m  W6 2-leaf casement, partly at the right edge
  2.7 to 3.6 m  solid wall to the far corner
Out of frame: Bath 1 door and wall, the passage walls (behind), the main room's plan-down wall (left edge)
```

```json
{
  "task": "One photorealistic interior photograph, landscape.",
  "plan_usage": "The attached floor plan is a layout reference only. Find the room labelled MAIN BEDROOM. Do not render the plan, labels, dimension lines or a top-down view.",
  "room": "Main bedroom of a Singapore HDB 4-room flat, 10th floor.",
  "proportions": "The bedroom is about 4.6 m wide and 2.9 m deep, ceiling about 2.6 m. The camera stands at the room's open side and looks across its depth to the far wall, so the room reads wide and shallow.",
  "camera": "Standing at the end of the entry passage where the room opens up, eye level 1.4 m, 20 mm lens, facing the far wall. Verticals straight.",
  "ahead_left_to_right": [
    "Solid plain far wall 3.3 m away, no window, continuing past the left edge",
    "Queen bed with its headboard against it, left of centre"
  ],
  "right_wall_near_to_far": [
    "White aluminium casement window with two leaves, partly visible at the right edge, 1.5 to 2.7 m away, sheer linen curtains",
    "Solid plain wall to the far corner"
  ],
  "furniture": [
    "Queen bed 1.5 x 1.9 m, linen upholstered headboard, linen bedding in sand, clay and charcoal",
    "Two oak bedside tables with ceramic lamps",
    "Wool-linen rug under the lower two-thirds of the bed",
    "Rattan accent chair near the window, ceramic vase with dried branches"
  ],
  "style": "Wabi-sabi: warm greige limewash-effect walls with visible texture, natural white oak floor, solid white oak furniture, linen and raw cotton in sand, clay and charcoal, unglazed stoneware, rattan accents, matte black and aged bronze metal.",
  "light_and_view": "Soft late-morning daylight through the window on the right, lamps warm 3000 K. Flat ceiling with a slim surface light, no cove lighting. View: neighbouring HDB blocks and treetops, slightly hazy.",
  "must_hold": [
    "Window only on the right wall, partly visible at the right edge. The far wall is solid",
    "Room wider than it is deep",
    "Bed against the far wall, not under the window"
  ],
  "quality": "Professional real estate photography, true-to-scale furniture, natural materials with real texture, contact shadows. No text, logos or watermarks. No added windows, doors or openings."
}
```

## Bedroom 2

```text
CAMERA LOCK
Entry: D7, Bedroom 2 plan-down wall, plan-right end, hinge at the party wall
Heading: plan-up
Lens: 20 mm, eye level 1.4 m, landscape, verticals straight

ROOM MAP: BEDROOM 2
Size: about 3.4 m wide x 3.85 m long, nearly square. The camera looks down the long axis.
LEFT (plan-left), near to far:
  plan-left wall about 2.9 m to the left. Only its far 0.5 m is in frame, at the left edge
AHEAD (plan-up):
  W4 window wall, type uncertain, plain aluminium-framed panes
RIGHT (plan-right), near to far:
  party wall with Bedroom 3, solid, at the camera's shoulder, to the far corner
Out of frame: W5 (too far left at 20 mm)
```

Option: a diagonal heading toward the far plan-left corner brings W5 into frame. Use it if the second window matters for the listing. Run `fov.py` with that heading first.

```json
{
  "task": "One photorealistic interior photograph, landscape.",
  "plan_usage": "The attached floor plan is a layout reference only. Find the room labelled BEDROOM 2. Do not render the plan, labels, dimension lines or a top-down view.",
  "room": "Common bedroom of a Singapore HDB 4-room flat, 10th floor.",
  "proportions": "The room is about 3.4 m wide and 3.85 m deep, nearly square, ceiling about 2.6 m. The camera stands in the doorway at the right end of the near wall, so the room opens out to the left.",
  "camera": "Standing in the doorway, tight against the right wall, eye level 1.4 m, 20 mm lens, facing the window wall straight ahead. Verticals straight.",
  "left_wall_near_to_far": [
    "Solid plain wall, only its far end visible at the left edge"
  ],
  "ahead_left_to_right": [
    "Window in the far wall, aluminium frame with plain fixed or sliding panes, sheer linen curtains"
  ],
  "right_wall_near_to_far": [
    "Solid plain wall right beside the camera, running straight to the far corner"
  ],
  "furniture": [
    "Queen bed 1.5 x 1.9 m with its headboard against the right wall, about 1.5 m in from the camera, seen from the foot end at an angle",
    "Oak bedside table and ceramic lamp on the window side of the bed",
    "Linen armchair and floor lamp in the far left corner",
    "Wool-linen rug beside the bed"
  ],
  "style": "Wabi-sabi: warm greige limewash-effect walls with visible texture, natural white oak floor, solid white oak furniture, linen and raw cotton in sand, clay and charcoal, unglazed stoneware, dried branches in ceramic vases, matte black and aged bronze metal.",
  "light_and_view": "Soft late-morning daylight through the far window, lamps warm 3000 K. Flat ceiling with a slim surface light, no cove lighting. View: neighbouring HDB blocks, treetops and sky, slightly hazy.",
  "must_hold": [
    "Tight on the right at the door. The room opens to the left",
    "One window, in the far wall",
    "Bed against the right wall, clear of the window"
  ],
  "quality": "Professional real estate photography, true-to-scale furniture, natural materials with real texture, contact shadows. No text, logos or watermarks. No added windows, doors or openings."
}
```

## Bedroom 3

```text
CAMERA LOCK
Entry: D6, Bedroom 3 plan-down wall, plan-left end, hinge at the party wall
Heading: plan-up
Lens: 20 mm, eye level 1.4 m, landscape, verticals straight

ROOM MAP: BEDROOM 3
Size: about 2.8 m wide x 3.9 m long, about 1 to 1.4. The camera looks down the long axis.
LEFT (plan-left), near to far:
  party wall with Bedroom 2, solid, at the camera's shoulder, to the far corner
AHEAD (plan-up), left to right:
  W3 3-leaf casement across most of the width, RC column in the right corner
RIGHT (plan-right), near to far:
  wall shared with Living/Dining, solid, about 2.4 m to the right. Only its far 1.1 m is in frame
Out of frame: the near part of the right wall
```

```json
{
  "task": "One photorealistic interior photograph, landscape.",
  "plan_usage": "The attached floor plan is a layout reference only. Find the room labelled BEDROOM 3. Do not render the plan, labels, dimension lines or a top-down view.",
  "room": "Common bedroom of a Singapore HDB 4-room flat, 10th floor.",
  "proportions": "The room is about 2.8 m wide and 3.9 m deep, about 1 to 1.4, ceiling about 2.6 m. The camera stands in the doorway at the left end of the near wall, so the room opens out to the right.",
  "camera": "Standing in the doorway, tight against the left wall, eye level 1.4 m, 20 mm lens, facing the window wall straight ahead. Verticals straight.",
  "left_wall_near_to_far": [
    "Solid plain wall right beside the camera, running straight to the far corner"
  ],
  "ahead_left_to_right": [
    "White aluminium casement window with three leaves across most of the far wall, sheer linen curtains",
    "Square concrete column in the far right corner"
  ],
  "right_wall_near_to_far": [
    "Solid plain wall, its far part visible at the right edge"
  ],
  "furniture": [
    "Super single bed 1.1 x 1.9 m with its headboard against the right wall, ahead and to the right",
    "Oak desk and linen chair under the left part of the window",
    "Small oak bedside table with a ceramic lamp",
    "Wool-linen rug beside the bed"
  ],
  "style": "Wabi-sabi: warm greige limewash-effect walls with visible texture, natural white oak floor, solid white oak furniture, linen and raw cotton in sand, clay and charcoal, unglazed stoneware, dried branches in ceramic vases, matte black and aged bronze metal.",
  "light_and_view": "Soft late-morning daylight through the window, lamps warm 3000 K. Flat ceiling with a slim surface light, no cove lighting. View: neighbouring HDB blocks, treetops and sky, slightly hazy.",
  "must_hold": [
    "Tight on the left at the door. The room opens to the right",
    "Three-leaf window across most of the far wall, column in the right corner",
    "Room deeper than it is wide"
  ],
  "quality": "Professional real estate photography, true-to-scale furniture, natural materials with real texture, contact shadows. No text, logos or watermarks. No added windows, doors or openings."
}
```

## Bath/W.C.1 (ensuite)

```text
CAMERA LOCK
Entry: D9 from the Main Bedroom passage, Bath 1 plan-up wall, plan-right end
Heading: plan-down
Lens: 16 mm, eye level 1.4 m, landscape, verticals straight

ROOM MAP: BATH/W.C.1
Size: about 2.4 m wide x 1.6 m deep est. The camera looks across the short axis.
LEFT (plan-right), near to far:
  wall toward Bath 2 and the shaft. Basin drawn near the door. Partly at the left edge
AHEAD (plan-down), left to right:
  WC on this wall, position as drawn. Shower drop zone at the right end, partly at the right edge
RIGHT (plan-left):
  wall shared with the Main Bedroom. Out of frame
Out of frame: the right wall, even at 16 mm
```

```json
{
  "task": "One photorealistic interior photograph, landscape.",
  "plan_usage": "The attached floor plan is a layout reference only. Find the room labelled BATH/W.C.1. Do not render the plan, labels, dimension lines or a top-down view.",
  "room": "Ensuite bathroom of the main bedroom in a Singapore HDB 4-room flat.",
  "proportions": "The room is about 2.4 m wide and 1.6 m deep. The camera stands in the doorway at the left end of the near wall, so the room extends to the right. Small room, show no more floor than this.",
  "camera": "Standing in the doorway, eye level 1.4 m, 16 mm lens, facing the far wall 1.5 m away. Verticals straight.",
  "left_wall_near_to_far": [
    "Tiled wall beside the camera with a wall-hung basin and mirror near the door, partly visible at the left edge"
  ],
  "ahead_left_to_right": [
    "Far wall 1.5 m away with the WC against it, where the plan draws it",
    "Shower area at the right end behind a clear glass screen, floor stepping down slightly, partly visible at the right edge"
  ],
  "furniture": [
    "Linen towels in sand and clay on a matte black rail",
    "Small stoneware tray and a small plant on the basin"
  ],
  "style": "Wabi-sabi: honed grey microcement-look tiles on floor and walls, white oak vanity, stoneware basin, aged bronze tapware, linen towels in sand and clay.",
  "light_and_view": "Soft warm light from a slim ceiling light at 3000 K. No daylight source in view.",
  "must_hold": [
    "No window",
    "Small room, about 2.4 by 1.6 m",
    "Shower at the right end, WC on the far wall"
  ],
  "quality": "Professional real estate photography, true-to-scale fittings, natural materials with real texture, contact shadows. No text, logos or watermarks. No added windows, doors or openings."
}
```

## Bath/W.C.2

```text
CAMERA LOCK
Entry: D5 from the corridor, Bath 2 plan-up wall, plan-right end
Heading: plan-down
Lens: 20 mm, eye level 1.4 m, landscape, verticals straight

ROOM MAP: BATH/W.C.2
Size: about 1.6 m wide x 2.3 m long est. The camera looks down the long axis.
LEFT (plan-right), near to far:
  wall shared with the Household Shelter, solid, at the camera's shoulder
AHEAD (plan-down), left to right:
  far wall 2.2 m away. WC toward the right end
RIGHT (plan-left), near to far:
  wall shared with Bath 1, solid. Only its far 0.9 m is in frame
Floor: shower drop zone in the middle of the room
Out of frame: the near part of the right wall
```

```json
{
  "task": "One photorealistic interior photograph, landscape.",
  "plan_usage": "The attached floor plan is a layout reference only. Find the room labelled BATH/W.C.2. Do not render the plan, labels, dimension lines or a top-down view.",
  "room": "Common bathroom of a Singapore HDB 4-room flat.",
  "proportions": "The room is about 1.6 m wide and 2.3 m deep. The camera stands in the doorway at the left end of the near wall and looks down the length of the room. Small room, show no more floor than this.",
  "camera": "Standing in the doorway, eye level 1.4 m, 20 mm lens, facing the far wall 2.2 m away. Verticals straight.",
  "left_wall_near_to_far": [
    "Tiled wall right beside the camera, running straight to the far corner"
  ],
  "ahead_left_to_right": [
    "Shower area in the middle of the room with a clear glass screen and a slight floor drop",
    "Far wall with the WC toward its right end"
  ],
  "right_wall_near_to_far": [
    "Tiled wall, its far part visible at the right edge"
  ],
  "furniture": [
    "Linen towels in sand and clay on a matte black rail",
    "Small stoneware tray and a small plant"
  ],
  "style": "Wabi-sabi: honed grey microcement-look tiles on floor and walls, white oak vanity, stoneware basin, aged bronze tapware, linen towels in sand and clay.",
  "light_and_view": "Soft warm light from a slim ceiling light at 3000 K. No daylight source in view.",
  "must_hold": [
    "No window",
    "Narrow room, 1.6 m wide",
    "WC on the far wall toward the right"
  ],
  "quality": "Professional real estate photography, true-to-scale fittings, natural materials with real texture, contact shadows. No text, logos or watermarks. No added windows, doors or openings."
}
```

## Household Shelter

```text
CAMERA LOCK
Entry: D4 from the corridor, Shelter plan-up wall. Camera in the open steel doorway
Heading: plan-down
Lens: 20 mm, eye level 1.4 m, landscape, verticals straight

ROOM MAP: HOUSEHOLD SHELTER
Size: about 1.6 m wide x 1.4 m deep inside est. Thick RC walls.
LEFT (plan-right): wall shared with Living/Dining, solid. Far part in frame
AHEAD (plan-down): wall backing onto the Kitchen, solid, 1.4 m away
RIGHT (plan-left): wall shared with Bath 2, solid. Far part in frame
Out of frame: the steel door leaf (opens outward, behind the camera)
```

```json
{
  "task": "One photorealistic interior photograph, landscape.",
  "plan_usage": "The attached floor plan is a layout reference only. Find the room labelled HOUSEHOLD SHELTER. Do not render the plan, labels, dimension lines or a top-down view.",
  "room": "Household shelter of a Singapore HDB 4-room flat: a small reinforced-concrete room used as a storeroom.",
  "proportions": "About 1.6 m wide and 1.4 m deep inside, ceiling about 2.6 m, thick concrete walls. Small room, show no more floor than this.",
  "camera": "Standing in the open steel doorway, eye level 1.4 m, 20 mm lens, facing the far wall. Verticals straight.",
  "left_wall_near_to_far": [
    "Solid plain wall, its far part visible at the left edge"
  ],
  "ahead_left_to_right": [
    "Solid plain far wall 1.4 m away"
  ],
  "right_wall_near_to_far": [
    "Solid plain wall, its far part visible at the right edge"
  ],
  "furniture": [
    "Freestanding oak and black metal open shelving unit standing against the far wall, not fixed to it",
    "Woven baskets and lidded linen boxes on the shelves",
    "A small oak step stool"
  ],
  "style": "Wabi-sabi: plain warm greige painted walls, natural white oak floor, oak and matte black metal, woven baskets, linen in sand and clay.",
  "light_and_view": "One slim surface ceiling light at 3000 K, and soft daylight from the corridor behind the camera.",
  "must_hold": [
    "No window",
    "Small room with thick plain walls",
    "Storage stands free. Nothing built in or fixed to the walls"
  ],
  "quality": "Professional real estate photography, true-to-scale furniture, natural materials with real texture, contact shadows. No text, logos or watermarks. No added windows, doors or openings."
}
```

## Kitchen

Counter layout is staging. The plan shows no cabinetry. Chosen layout: one straight run on the right (shelter back wall) and a short return on the left near the entrance. It keeps the yard doorway clear and the whole run in frame. The short return is behind the camera. To be confirmed by Kiian.

```text
CAMERA LOCK
Entry: D2 from the foyer, Kitchen plan-up wall, plan-right end. Camera 0.9 m inside the opening
Heading: plan-left, toward the yard
Lens: 20 mm, eye level 1.4 m, landscape, verticals straight

ROOM MAP: KITCHEN
Size: 3.2 m long x 2.3 m wide. The camera looks down the long axis.
LEFT (plan-down), near to far:
  exterior RC wall, no window. Far 1.3 m in frame, at the left edge. Tall fridge here (staging)
AHEAD (plan-left), left to right:
  solid wall, D10 doorway to the yard with a floor drop (slightly left of centre), solid wall
RIGHT (plan-up), near to far:
  shelter back wall, solid. Main counter run along it, 2.2 m (staging)
Out of frame: the short counter return near the entrance, the entrance itself
```

```json
{
  "task": "One photorealistic interior photograph, landscape.",
  "plan_usage": "The attached floor plan is a layout reference only. Find the room labelled KITCHEN. Do not render the plan, labels, dimension lines or a top-down view.",
  "room": "Enclosed kitchen of a Singapore HDB 4-room flat, 10th floor.",
  "proportions": "The kitchen is 3.2 m long and 2.3 m wide, ceiling about 2.6 m. The camera stands just inside the entrance at one end and looks down the length of the room to the service yard doorway.",
  "camera": "Standing just inside the kitchen entrance, eye level 1.4 m, 20 mm lens, facing the far wall. Verticals straight.",
  "left_wall_near_to_far": [
    "Solid plain wall, no window, its far part visible at the left edge, with a tall fridge against it near the far end"
  ],
  "ahead_left_to_right": [
    "Open doorway to the service yard, slightly left of centre, with a small step down and daylight beyond",
    "Solid plain wall to the right of the doorway"
  ],
  "right_wall_near_to_far": [
    "One straight kitchen counter along the right wall from the near end to the far wall, about 2.2 m: white oak base cabinets, travertine-look counter, sink, hob and slim cooker hood, oak wall cabinets above"
  ],
  "furniture": [
    "On the counter: stoneware jars, a wooden board and a small plant",
    "No table, chairs or rug"
  ],
  "style": "Wabi-sabi: honed grey microcement-look floor tiles, warm greige limewash-effect walls, white oak flat-panel cabinets, honed travertine-look counter, aged bronze tap and handles, unglazed stoneware.",
  "light_and_view": "Soft late-morning daylight through the yard doorway, slim surface ceiling light at 3000 K, under-cabinet light on the counter.",
  "must_hold": [
    "Service yard doorway straight ahead in the far wall, slightly left of centre",
    "One straight counter on the right. No L-shaped counter",
    "No window in view"
  ],
  "quality": "Professional real estate photography, true-to-scale cabinets and appliances, natural materials with real texture, contact shadows. No text, logos or watermarks. No added windows, doors or openings."
}
```

## Service Yard

```text
CAMERA LOCK
Entry: D10 from the Kitchen, yard plan-right side
Heading: plan-left
Lens: 20 mm, eye level 1.4 m, landscape, verticals straight

ROOM MAP: SERVICE YARD
Size: about 2.4 m long x 1.4 m wide est. The camera looks down the long axis.
LEFT (plan-down), near to far:
  louvres or open parapet to the outside. In frame from about 0.8 m on
AHEAD (plan-left):
  solid thick RC wall, 2.4 m away
RIGHT (plan-up), near to far:
  wall shared with Bath 2 and the shaft, solid. Far part in frame
Out of frame: the small element at the plan-down right corner (uncertain)
```

```json
{
  "task": "One photorealistic interior photograph, landscape.",
  "plan_usage": "The attached floor plan is a layout reference only. Find the room labelled SERVICE YARD. Do not render the plan, labels, dimension lines or a top-down view.",
  "room": "Service yard of a Singapore HDB 4-room flat, 10th floor.",
  "proportions": "The yard is about 2.4 m long and 1.4 m wide. The camera stands in the doorway from the kitchen and looks along its length. Small utility space.",
  "camera": "Standing in the kitchen doorway, eye level 1.4 m, 20 mm lens, facing the far wall. Verticals straight.",
  "left_wall_near_to_far": [
    "Open side to the outside along the whole length: a low parapet with aluminium louvres, partly visible at the left edge, daylight and treetops through the louvres"
  ],
  "ahead_left_to_right": [
    "Solid plain concrete wall 2.4 m away"
  ],
  "right_wall_near_to_far": [
    "Solid plain wall, its far part visible at the right edge"
  ],
  "furniture": [
    "Front-loading washer with a dryer stacked above, against the far wall in the right corner",
    "Folding drying rack with a few linen pieces",
    "Two potted plants"
  ],
  "style": "Wabi-sabi: honed grey microcement-look floor tiles, warm greige painted walls, matte black metal, linen in sand and clay.",
  "light_and_view": "Soft late-morning daylight through the louvres. View through the louvres: neighbouring HDB blocks and treetops, slightly hazy.",
  "must_hold": [
    "Louvred open side on the left, not ahead",
    "Far wall solid",
    "Small utility space, not a room"
  ],
  "quality": "Professional real estate photography, true-to-scale appliances, natural materials with real texture, contact shadows. No text, logos or watermarks. No added windows, doors or openings."
}
```

## Differences from the audit brief's answer key

Every wall mapping (left, right, ahead) matches the key for all nine rooms. Four readings differ. Each comes from the brief's own numbers, not from a new reading of the plan.

1. Kitchen doorway in Living shot B. The key lists it at the far end of the right wall. The door graph puts D2 in the Kitchen's plan-up wall, which is the Living's entrance wall, and the key's own angles (+5 to +13 degrees, facing the camera) agree. It is in the far wall, at its right end.
2. W6 in the Main Bedroom shot from the door. The key says partly visible. By the key's own angles (+18 to +26 degrees) and the 1 m passage width, the sight line crosses the Bedroom 2 wall first. The key's method checks angles only, not walls. W6 is left out of shot A, and shot B was added to show it.
3. W5 in Bedroom 2. On the correct wall, but 57 to 65 degrees left of the camera axis, outside a 20 mm frame. Left out of the prompt. A diagonal heading brings it in.
4. Corridor opening D3. The key says 2.2 to 3.3 m from the main door. The printed dimensions (2100 shelter wall, 1000 opening) give 2.1 to 3.1 m. Within tolerance. The printed values are used.
