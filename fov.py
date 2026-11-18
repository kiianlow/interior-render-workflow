"""Field-of-view check for a camera placed on a floor plan.

Answers one question per feature: can the camera see it?
A feature is visible when it is inside the lens angle, in front of the camera,
and not hidden behind a wall.

Usage, from the repo root:
    python3 fov.py test-unit-hdb-4room.json            every shot in the file
    python3 fov.py test-unit-hdb-4room.json living-a   one or more named shots

No dependencies. Output is a Markdown table per shot.

File format (JSON). Coordinates are metres on the plan as supplied:
x grows toward plan-right, y grows toward plan-up.

{
  "rooms": {
    "living": {
      "segments": [
        {"name": "Window W1", "wall": "plan-up", "from": [0, 7.15], "to": [3.25, 7.15]},
        {"name": "Corridor opening", "wall": "plan-left", "from": [0, 2.1], "to": [0, 3.1], "blocks": false},
        {"name": "Bath wall seen from behind", "from": [2.9, 1.1], "to": [2.9, 2.7], "show": false}
      ]
    }
  },
  "shots": [
    {"id": "living-a", "room": "living", "camera": [2.7, 0.45],
     "heading": {"toward": [0, 7.15]}, "lens": 20, "frame": "landscape"}
  ]
}

heading is "plan-up", "plan-down", "plan-left", "plan-right" or {"toward": [x, y]}.
blocks: false marks an open gap. show: false marks a wall used only to hide things.
"""
import json
import math
import sys

AXES = {"plan-up": (0.0, 1.0), "plan-down": (0.0, -1.0), "plan-left": (-1.0, 0.0), "plan-right": (1.0, 0.0)}

# Camera faces -> (camera left, camera right, behind). Same table as START-HERE.
MAPPING = {
    "plan-up": ("plan-left", "plan-right", "plan-down"),
    "plan-down": ("plan-right", "plan-left", "plan-up"),
    "plan-left": ("plan-down", "plan-up", "plan-right"),
    "plan-right": ("plan-up", "plan-down", "plan-left"),
}

# Full-frame sensor, 36 x 24 mm. Width of the frame for each orientation.
FRAME_WIDTH_MM = {"landscape": 36.0, "portrait": 24.0, "square": 24.0}
SAMPLES = 400
EPS = 1e-6


def half_angle(lens_mm, frame):
    return math.degrees(math.atan(FRAME_WIDTH_MM[frame] / 2.0 / lens_mm))


def heading_vector(heading, camera):
    if isinstance(heading, str):
        return AXES[heading]
    tx, ty = heading["toward"]
    dx, dy = tx - camera[0], ty - camera[1]
    n = math.hypot(dx, dy)
    return (dx / n, dy / n)


def nearest_axis(h):
    return max(AXES, key=lambda k: AXES[k][0] * h[0] + AXES[k][1] * h[1])


def cross(ax, ay, bx, by):
    return ax * by - ay * bx


def blocked(cam, pt, seg, own):
    """True when the sight line cam -> pt crosses seg before reaching pt."""
    if seg is own or not seg.get("blocks", True):
        return False
    px, py = cam
    rx, ry = pt[0] - px, pt[1] - py
    (ax, ay), (bx, by) = seg["from"], seg["to"]
    sx, sy = bx - ax, by - ay
    denom = cross(rx, ry, sx, sy)
    if abs(denom) < EPS:
        return False  # parallel: a wall seen edge-on does not hide anything
    t = cross(ax - px, ay - py, sx, sy) / denom
    u = cross(ax - px, ay - py, rx, ry) / denom
    return EPS < t < 1 - 1e-4 and -EPS <= u <= 1 + EPS


def side_name(wall, axis):
    if not wall:
        return ""
    left, right, behind = MAPPING[axis]
    if wall == left:
        return "left"
    if wall == right:
        return "right"
    if wall == behind:
        return "behind"
    return "ahead"


def check_shot(shot, room):
    cam = shot["camera"]
    h = heading_vector(shot["heading"], cam)
    r = (h[1], -h[0])  # unit vector toward camera-right
    frame = shot.get("frame", "landscape")
    half = half_angle(shot["lens"], frame)
    axis = nearest_axis(h)
    segs = room["segments"]
    rows = []
    for seg in segs:
        if not seg.get("show", True):
            continue
        (ax, ay), (bx, by) = seg["from"], seg["to"]
        length = math.hypot(bx - ax, by - ay)
        angles, dists, vis, why = [], [], [], set()
        for i in range(SAMPLES + 1):
            f = i / SAMPLES
            pt = (ax + (bx - ax) * f, ay + (by - ay) * f)
            dx, dy = pt[0] - cam[0], pt[1] - cam[1]
            fwd = dx * h[0] + dy * h[1]
            lat = dx * r[0] + dy * r[1]
            ang = math.degrees(math.atan2(lat, fwd))
            angles.append(ang)
            dists.append(math.hypot(dx, dy))
            if fwd <= 0.01:
                why.add("behind")
                continue
            if abs(ang) > half:
                why.add("left edge" if ang < 0 else "right edge")
                continue
            hider = next((s for s in segs if blocked(cam, pt, s, seg)), None)
            if hider is not None:
                why.add("hidden by " + hider["name"])
                continue
            vis.append(f * length)
        share = len(vis) / float(SAMPLES + 1)
        if share >= 0.97:
            status = "IN"
        elif not vis:
            status = "OUT"
        else:
            status = "PART %.1f to %.1f m" % (min(vis), max(vis))
        note = ", ".join(sorted(why)) if status != "IN" else ""
        rows.append((seg["name"], seg.get("wall", ""), side_name(seg.get("wall"), axis),
                     "%+.0f to %+.0f" % (angles[0], angles[-1]),
                     "%.1f to %.1f" % (dists[0], dists[-1]), status, note))
    return axis, half, frame, rows


def main(argv):
    if len(argv) < 2:
        print(__doc__)
        return 2
    with open(argv[1], encoding="utf-8") as fh:
        data = json.load(fh)
    wanted = set(argv[2:])
    for shot in data["shots"]:
        if wanted and shot["id"] not in wanted:
            continue
        axis, half, frame, rows = check_shot(shot, data["rooms"][shot["room"]])
        left, right, behind = MAPPING[axis]
        print("### %s" % shot["id"])
        print("")
        print("Camera %s, heading %s, %s mm %s, half-angle %.1f degrees. "
              "Camera faces %s: left = %s, right = %s, behind = %s."
              % (shot["camera"], json.dumps(shot["heading"]), shot["lens"], frame, half,
                 axis, left, right, behind))
        print("")
        print("| Feature | Plan wall | Camera side | Angle (deg, minus is left) | Distance (m) | In frame | Why not |")
        print("|---|---|---|---|---|---|---|")
        for row in rows:
            print("| %s | %s | %s | %s | %s | %s | %s |" % row)
        print("")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
