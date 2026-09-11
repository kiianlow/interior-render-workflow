# Quality Control Prompt

Compare the render with the source. Fill the table. Do not pass a check you cannot verify. Mark it UNCLEAR and say why.

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
| Materials and light | | | |
| Artefacts (warped lines, floating or duplicate objects, text) | | | |

Result: PASS / MINOR / MAJOR / UNCLEAR

## Decision

- ACCEPT: no MAJOR, and no UNCLEAR on doors, windows, openings or proportions.
- REGENERATE: any MAJOR on architecture or camera. Start from the original source with a stronger architecture line naming the failed element.
- EDIT: MINOR or styling issues only. Change the named element on the current render.

Maximum 3 attempts per render. After the third, stop and report what keeps failing and the likely fix.
