# Floorplan Analysis Prompt

Analyse the source before any styling. This step describes. It does not redesign.

Identify:

1. Room label and boundaries
2. Proportions, and dimensions if printed
3. Doors: count, wall, swing direction
4. Windows: count, wall, type
5. Openings to other rooms
6. Columns, beams, bulkheads (dashed lines usually mark overhead elements)
7. Ceiling information
8. Built-ins and fixed cabinetry
9. Singapore fixed features: HS, DB, yard, AC ledge, planter, bay window
10. Stairs, pool, deck where applicable
11. Circulation paths
12. Possible camera positions
13. Uncertain elements

Output the Architecture Lock in this format:

```text
ARCHITECTURE LOCK
Room: 
Shape and size: 
Doors: 
Windows: 
Openings: 
Columns / beams / ceiling: 
Built-ins and fixed features: 
Outdoor elements: 
Uncertain: 
```

Do not invent missing architecture.
