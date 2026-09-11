# Interior Render Workflow

Source-of-truth workflow for photorealistic interior renders of Singapore homes from floorplans and reference photos, run in ChatGPT image generation.

Architecture is locked. Interior styling changes.

## How to run

1. Open a new ChatGPT chat.
2. Attach the floorplan or room photo.
3. Paste the kickoff from `prompts/kickoff.md` and fill the brackets.

ChatGPT reads `START-HERE.md`, opens one style file, then shows the Architecture Lock, generates, and shows a QC table.

## Structure

- `START-HERE.md`: the complete engine. The only file ChatGPT must read.
- `rules/`: architecture, perspective, materials, negative rules, Singapore context.
- `prompts/`: kickoff, floorplan analysis, generation prompt, QC, refinement commands.
- `styles/`: 10 style presets and the index.
- `projects/template/`: room spec, Style Lock, QC report.

## Editing rules

- START-HERE wins over every other file. When you change a rule, change it in START-HERE first.
- Upload whole folders, not loose files, so files keep their paths.
- Log changes in `CHANGELOG.md`.

## Posting renders

Caption marketing renders as virtually staged for illustration.
