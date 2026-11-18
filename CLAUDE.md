# CLAUDE.md

Notes for Claude when editing this repo. ChatGPT never reads this file.

Last updated 18 Nov 2026, at repo version 3.0.0.

## What this repo is

The instruction set ChatGPT reads before rendering Singapore interiors from floor plans or photos. Kiian (SG Launch Homes) runs it in ChatGPT image generation. The runtime is ChatGPT, so START-HERE plus one style file must be enough to run.

Sister repo: kiianlow/interior-reimagine-workflow (restyles real room photos). Shared rules (Singapore context, captions, room types, shelter) are copied, not linked. When you change one, list it in the handback so Kiian can decide whether to port it.

## Rules for edits

- START-HERE holds every rule. No other file repeats a rule. Templates and examples may show a rule in use.
- Keep the layout flat. Raw links in START-HERE and in Kiian's saved kickoff depend on it.
- Never touch the core principle: architecture is locked, styling changes. Marketing accuracy wins over looks.
- Keep the 3-attempt cap and the regenerate versus edit split.
- Free tools only.
- House style for every file: short active sentences, no em dashes, no semicolons, no hype or filler, UK spelling (colour, centre). validate.py enforces the punctuation.
- When a plan reading changes in the worked example, update the JSON geometry too and rerun fov.py.

## Deploy

1. `python3 validate.py`. It must print PASS.
2. Bump the version in START-HERE (Version line, handshake, Run Summary), README, this file, the worked example and a new CHANGELOG entry.
3. Commit and push to main with git. Never use the GitHub web uploader. It flattens folders and cannot delete files.
4. `python3 validate.py --online` after the push. Raw GitHub can serve a cached copy for a few minutes.
5. Purge the mirror: open https://purge.jsdelivr.net/gh/kiianlow/interior-render-workflow@main/START-HERE.md and check that https://cdn.jsdelivr.net/gh/kiianlow/interior-render-workflow@main/START-HERE.md shows the new version line.

## Open items

- The worked example has not been checked against the plan image. See its Differences section.
- No field test of 3.0.0 in ChatGPT yet. Unknown: whether ChatGPT applies the heading table and the k values reliably, and whether it reads a camera marker.
- Camera marker HTML tool (brief item P2-1) not built. Phone or Preview markup does the job.
