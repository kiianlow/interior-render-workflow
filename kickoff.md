# Kickoff

Paste one of these into ChatGPT with the floor plan or photo attached. This is the only kickoff. README quotes the same text.

## New unit

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

ChatGPT replies with the Unit Lock, Camera Lock and Room Map, then stops. Check them against the plan. Reply "go" or correct a line.

## Next room in the same unit

Same chat, floor plan attached again:

```text
Same unit. Room: [room label exactly as printed on the plan]
Camera: [marker on plan] or [enter through: door or opening] [facing: wall, window or corner]
```

Add "check first" to see the Room Map before it renders.

## Same unit in a new chat

Paste the New unit kickoff, then the last RUN SUMMARY below it. The Unit Lock in the summary counts as checked.
