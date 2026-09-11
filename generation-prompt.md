# Generation Prompt Template

The image tool only sees this prompt and the source image. Fill every bracket. Keep the result under about 200 words. Architecture comes before style.

```text
Photorealistic interior photograph of the [ROOM] of a Singapore [PROPERTY TYPE], [LEVEL] floor.

Architecture, keep exactly: [COUNTS AND POSITIONS FROM THE ARCHITECTURE LOCK].

Camera: [ONE-LINE CAMERA LOCK].

Style [NUMBER + NAME]: [PALETTE]. [KEY MATERIALS]. [KEY FURNITURE, SIZED TO THE ROOM].

Light and view: [TIME OF DAY], [VIEW RULE].

Professional real estate interior photography, true-to-scale furniture, natural materials, contact shadows, straight verticals.

No text, logos or watermarks. No added windows, doors or openings.
```

## Reference photo supplied

Use the photo as the base image and add: "Keep the camera, framing and all architecture identical to the attached photo. Change only furniture, finishes, lighting fixtures and decor."

## Tips

- State what exists rather than listing what not to do.
- Name the failed element directly when regenerating, for example: "The window on the left wall is full-height and must stay full-height."
