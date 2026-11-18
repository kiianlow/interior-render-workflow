# Interior Render Workflow

Photorealistic interior renders of Singapore homes from floor plans and reference photos, run in ChatGPT image generation.

Architecture is locked. Interior styling changes.

Current engine: version 3.0.0.

## How to run

1. Optional: mark the camera on the plan. A red dot where the camera stands and a red arrow for the view direction. Phone or Preview markup is enough.
2. Open a new ChatGPT chat. Attach the floor plan or photo.
3. Paste the kickoff below and fill the brackets.
4. Check the first line of the reply. It must say "Engine 3.0.0 loaded". Anything else means the rules did not load (see Problems).
5. Unit Check. ChatGPT shows the Unit Lock (every door, opening and window), the Camera Lock and the Room Map, then stops. Compare them with the plan. Reply "go", or correct a line, for example "D4 opens into the corridor, not the living room".
6. ChatGPT renders and shows the QC table and caption. Reply with short commands, such as "change the sofa" or "wrong angle".
7. Next room: use the short kickoff. No new check is needed.
8. Save the RUN SUMMARY after each accepted room. It restarts the unit in a new chat.

The Unit Check takes about two minutes per unit. It catches the errors that QC cannot, because QC compares the render with the locks ChatGPT wrote itself.

## Kickoff

```text
Use this GitHub repo as the source of truth: https://github.com/kiianlow/interior-render-workflow
Read this file fully and follow it: https://raw.githubusercontent.com/kiianlow/interior-render-workflow/main/START-HERE.md
If that link fails, use https://cdn.jsdelivr.net/gh/kiianlow/interior-render-workflow@main/START-HERE.md
Start your reply with its version line. If neither link opens, say so and stop.

Style: [01 to 10, or style name]
Room: [room label exactly as printed on the plan]
Source: attached [floorplan / reference photo / both]
Property context: [HDB / condo / EC / landed], [floor level], [approx size], [area], [balcony / none]
Camera: [marker on plan] or [match reference photo] or [enter through: door or opening] [facing: wall, window or corner]
Keep the architecture exactly as shown.
```

Next room in the same chat: see `kickoff.md`.

## Problems

| Symptom | Fix |
|---|---|
| No version line, or an older version | ChatGPT did not read the file. Start a new chat. After a push, the mirror can lag for some minutes |
| Left and right swapped in the Room Map | Correct it at the Unit Check. Add a camera marker next time |
| A window or door appears that the plan does not have | Reply "window is wrong". It regenerates with that item first |
| Room looks square or too big | Check the Room Map ratio line, then "wrong angle" |
| Three attempts fail | Mark the camera on the plan, or try a simpler camera such as a straight view |

## Posting

Use the caption ChatGPT prints: "AI-generated illustration, virtually staged. The actual unit differs." CEA expects agents to highlight images that are AI-generated or enhanced. Confirm the exact wording with your agency.

## Files

All files sit in the repo root, so every raw link stays short and stable.

- `START-HERE.md`: the engine. The only rules file ChatGPT reads.
- `kickoff.md`: the kickoff texts.
- `01` to `10`: style files. `STYLE-INDEX.md` lists them with their marketing fit.
- `room-spec.md`: optional planning sheet for a unit.
- `test-unit-hdb-4room.md`: worked example. A 4-room BTO with every lock and prompt. `test-unit-hdb-4room.json` holds its geometry.
- `fov.py`: checks what a camera can see on a plan, including walls that block the view.
- `validate.py`: checks the repo before each push.
- `CLAUDE.md`: notes for Claude when editing this repo.

## Editing

- Change rules in START-HERE only. No other file repeats them.
- Edit with git, not the GitHub web uploader. The uploader flattens folders and cannot delete files.
- Run `python3 validate.py` before every push. GitHub runs it again on every push.
- Bump the version in START-HERE, README, CLAUDE.md and CHANGELOG together.
