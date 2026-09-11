# Interior Render Workflow

Source-of-truth workflow for photorealistic interior renders of Singapore homes from floorplans and reference photos, run in ChatGPT image generation.

Architecture is locked. Interior styling changes.

## How to run

1. Open a new ChatGPT chat.
2. Attach the floorplan or room photo.
3. Paste the kickoff from `kickoff.md` and fill the brackets.

ChatGPT reads `START-HERE.md`, opens one style file, then shows the Architecture Lock, generates, and shows a QC table.

## Structure

All files sit in the repo root. No folders.

- `START-HERE.md`: the complete engine. The only file ChatGPT must read.
- Rules: `architecture.md`, `perspective.md`, `materials.md`, `negative-rules.md`, `singapore-context.md`
- Prompts: `kickoff.md`, `floorplan-analysis.md`, `generation-prompt.md`, `quality-control.md`, `refinements.md`
- Styles: `01` to `10` style files and `STYLE-INDEX.md`
- Templates: `room-spec.md`, `style-lock.md`, `qc-report.md`

## Editing rules

- START-HERE wins over every other file. When you change a rule, change it in START-HERE first.
- Keep every file in the root. Every file name must stay unique.
- To update a file, upload it with the same name. GitHub overwrites it.
- Log changes in `CHANGELOG.md`.

## Posting renders

Caption marketing renders as virtually staged for illustration.
