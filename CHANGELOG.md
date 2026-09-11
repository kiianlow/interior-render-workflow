# Changelog

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
