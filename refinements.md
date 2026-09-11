# Refinement Commands

Short follow-up messages target one layer. Do not restart the project.

| User says | Layer | Action |
|---|---|---|
| The window is wrong | Architecture | Regenerate from source, name the window in the prompt |
| Wrong angle | Camera | Regenerate from source with the corrected Camera Lock |
| Make the sofa more premium | Furniture | Edit current render, sofa only |
| Change the rug | Styling | Edit current render, rug only |
| Warmer lighting | Lighting | Edit current render, light temperature only |
| Less clutter | Decor | Edit current render, remove decor items |
| Golden hour version | Light and view | Edit current render, keep everything else |
| Same design for the bedroom | Multi-room | Reuse the Style Lock, new Architecture Lock for the new room |
| Portrait version | Format | Regenerate at portrait with the same locks and Style Lock |

If an edit changes anything outside the named layer, treat it as a failed attempt and count it toward the 3-attempt limit.
