"""Checks the interior-render-workflow repo before a push.

Usage, from the repo root:
    python3 validate.py            offline checks
    python3 validate.py --online   also checks that every raw link returns 200

No dependencies. Exit code 0 means every check passed.
"""
import json
import os
import re
import subprocess
import sys
import urllib.request

ROOT = os.path.dirname(os.path.abspath(__file__))
REPO = "kiianlow/interior-render-workflow"
RAW = "https://raw.githubusercontent.com/%s/main/" % REPO
MIRROR = "https://cdn.jsdelivr.net/gh/%s@main/" % REPO
UPPERCASE_OK = {"START-HERE.md", "README.md", "CHANGELOG.md", "STYLE-INDEX.md", "CLAUDE.md"}
REQUIRED = ["START-HERE.md", "README.md", "CHANGELOG.md", "CLAUDE.md", "STYLE-INDEX.md", "kickoff.md",
            "room-spec.md", "fov.py", "validate.py", "test-unit-hdb-4room.md", "test-unit-hdb-4room.json"]
FOLDERS_OK = {".git", ".github"}
MAX_START_HERE_WORDS = 3300
MAX_PROMPT_STYLE_WORDS = 130
MAX_PROMPT_WORDS = 470
STYLE_HEADINGS = ["Design Identity", "Colour Palette", "Materials", "Furniture Language", "Lighting",
                  "Curtains", "Wet Areas and Kitchen", "Decorative Styling", "Spatial Character", "Avoid",
                  "Photorealism Direction"]
WET_LINES = ["Bathroom floor and walls", "Bathroom fittings", "Kitchen"]
QC_ROWS = ["Doors and openings", "Door connections", "Windows", "Left and right mapping", "Near-to-far order",
           "Field of view", "Room ratio", "Fixed features", "Camera, furniture scale and walkways",
           "Style, light and view", "Artefacts"]
HYPE = re.compile(r"\b(stunning|amazing|breathtaking|incredible|revolutionary|world-class|jaw-dropping)\b", re.I)

errors = []


def fail(msg):
    errors.append(msg)


def read(name):
    with open(os.path.join(ROOT, name), encoding="utf-8") as fh:
        return fh.read()


def words(text):
    return [w for w in text.split() if re.search(r"[A-Za-z0-9]", w)]


def section(text, number):
    m = re.search(r"^## %d\. .*?\n(.*?)(?=^## |\Z)" % number, text, re.S | re.M)
    return m.group(1) if m else ""


def code_blocks(text, lang):
    return re.findall(r"^```%s\n(.*?)^```" % lang, text, re.S | re.M)


def repo_files():
    out = []
    for name in sorted(os.listdir(ROOT)):
        path = os.path.join(ROOT, name)
        if os.path.isdir(path):
            if name not in FOLDERS_OK:
                fail("Folder found: %s. Keep every file in the root." % name)
            continue
        if name.startswith("."):
            continue
        out.append(name)
    return out


def style_files(files):
    return sorted(f for f in files if re.fullmatch(r"\d\d-[a-z0-9-]+\.md", f))


def check_names(files):
    seen = {}
    for f in files:
        if f not in UPPERCASE_OK and not re.fullmatch(r"[a-z0-9-]+\.(md|py|json)", f):
            fail("Bad file name: %s. Use lowercase letters, digits and hyphens." % f)
        key = f.lower()
        if key in seen:
            fail("Duplicate name ignoring case: %s and %s" % (seen[key], f))
        seen[key] = f
    for f in REQUIRED:
        if f not in files:
            fail("Missing file: %s" % f)


def check_links(files):
    for f in files:
        if not f.endswith(".md"):
            continue
        for target in re.findall(re.escape(RAW) + r"([^\s|)`\"<]+)", read(f)):
            if "/" in target or target not in files:
                fail("%s links to a missing file or a folder: %s" % (f, target))
    sh = read("START-HERE.md")
    for url in re.findall(r"https?://[^\s|)`\"]+", sh):
        if not (url.startswith(RAW) or url.startswith(MIRROR)):
            fail("START-HERE has a link that is neither raw nor the mirror: %s" % url)
    for f in ("kickoff.md", "README.md"):
        t = read(f)
        for link in (RAW + "START-HERE.md", MIRROR + "START-HERE.md"):
            if link not in t:
                fail("%s does not contain %s" % (f, link))
        if "/blob/" in t:
            fail("%s uses a GitHub blob link. Use the raw link and the mirror." % f)


def check_kickoff():
    kick = code_blocks(read("kickoff.md"), "text")
    readme = code_blocks(read("README.md"), "text")
    if not kick or not readme:
        fail("kickoff.md or README.md has no kickoff text block.")
    elif kick[0] != readme[0]:
        fail("The kickoff in README.md differs from the first kickoff in kickoff.md.")


def check_styles(files):
    sh = read("START-HERE.md")
    s9 = section(sh, 9)
    list_sh = re.findall(r"^\| (\d\d) \| ([^|]+?) \| https", s9, re.M)
    list_idx = re.findall(r"^\| (\d\d) \| ([^|]+?) \|", read("STYLE-INDEX.md"), re.M)
    if not list_sh:
        fail("No style table found in START-HERE section 9.")
    if list_sh != list_idx:
        fail("Style list differs between START-HERE section 9 and STYLE-INDEX.md.")
    found = style_files(files)
    for num, name in list_sh:
        match = [f for f in found if f.startswith(num + "-")]
        if len(match) != 1:
            fail("Style %s needs exactly one file, found %d." % (num, len(match)))
            continue
        if RAW + match[0] not in s9:
            fail("Style %s file %s is not linked in START-HERE section 9." % (num, match[0]))
        t = read(match[0])
        title = t.splitlines()[0]
        if title != "# Style %s: %s" % (num, name):
            fail("%s title is '%s', expected '# Style %s: %s'." % (match[0], title, num, name))
        heads = re.findall(r"^## (.+)$", t, re.M)
        if heads != STYLE_HEADINGS:
            fail("%s headings are %s, expected %s." % (match[0], heads, STYLE_HEADINGS))
        wet = re.search(r"^## Wet Areas and Kitchen\n(.*?)(?=^## )", t, re.S | re.M)
        lines = re.findall(r"^- ([A-Za-z ]+): \S", wet.group(1), re.M) if wet else []
        if lines != WET_LINES:
            fail("%s Wet Areas and Kitchen lines are %s, expected %s." % (match[0], lines, WET_LINES))
        light = re.search(r"^## Lighting\n(.*?)(?=^## )", t, re.S | re.M)
        if light and re.search(r"recessed|cove|linear", light.group(1), re.I) and "false ceiling" not in light.group(1):
            fail("%s names recessed, cove or linear lights without the false ceiling note." % match[0])
    for f in found:
        if f[:2] not in [n for n, _ in list_sh]:
            fail("%s is not in the style list." % f)


def check_qc(files):
    sh = read("START-HERE.md")
    rows = re.findall(r"^\| (\d+)\. ([^|(]+?)(?: \(|\s*\|)", section(sh, 11), re.M)
    if [int(n) for n, _ in rows] != list(range(1, len(QC_ROWS) + 1)) or [r.strip() for _, r in rows] != QC_ROWS:
        fail("START-HERE section 11 QC rows are %s, expected %s." % ([r for _, r in rows], QC_ROWS))
    for f in files:
        if f.endswith(".md") and f not in ("START-HERE.md", "CHANGELOG.md") and re.search(r"^\| 1\. Doors and openings", read(f), re.M):
            fail("%s repeats the QC table. Keep it in START-HERE only." % f)


def check_heading_table():
    sh = read("START-HERE.md")
    rows = re.findall(r"^\| (plan-\w+) \| (plan-\w+) \| (plan-\w+) \| (plan-\w+) \|$", sh, re.M)
    sh_map = {r[0]: r[1:] for r in rows}
    src = read("fov.py")
    m = re.search(r"MAPPING = \{(.*?)\n\}", src, re.S)
    fov_map = {k: tuple(v) for k, *v in re.findall(r'"(plan-\w+)": \("(plan-\w+)", "(plan-\w+)", "(plan-\w+)"\)', m.group(1))} if m else {}
    if len(sh_map) != 4:
        fail("START-HERE heading table not found or incomplete.")
    if sh_map != fov_map:
        fail("Heading table in START-HERE differs from MAPPING in fov.py.")


def check_text(files):
    for f in files:
        t = read(f)
        if chr(0x2014) in t or chr(0x2013) in t:
            fail("%s contains an em or en dash." % f)
        if f != "validate.py" and HYPE.search(t):
            fail("%s contains a hype word: %s" % (f, HYPE.search(t).group(0)))
        if not f.endswith(".md"):
            continue
        in_code = False
        for i, line in enumerate(t.splitlines(), 1):
            if line.lstrip().startswith("```"):
                in_code = not in_code
                continue
            if ";" in line and not in_code:
                fail("%s line %d has a semicolon outside a code block." % (f, i))


def check_versions():
    sh = read("START-HERE.md")
    m = re.search(r"^Version (\d+\.\d+\.\d+)$", sh, re.M)
    if not m:
        fail("START-HERE has no 'Version X.Y.Z' line.")
        return None
    v = m.group(1)
    if "Engine %s loaded" % v not in sh:
        fail("START-HERE handshake line does not say 'Engine %s loaded'." % v)
    if "Engine: %s" % v not in sh:
        fail("START-HERE run summary does not say 'Engine: %s'." % v)
    top = re.search(r"^## (\S+)", read("CHANGELOG.md"), re.M)
    if not top or top.group(1) != v:
        fail("CHANGELOG top entry is %s, START-HERE is %s." % (top.group(1) if top else "missing", v))
    readme = read("README.md")
    if "Current engine: version %s." % v not in readme or "Engine %s loaded" % v not in readme:
        fail("README version lines do not match version %s." % v)
    if "at repo version %s." % v not in read("CLAUDE.md"):
        fail("CLAUDE.md 'Last updated' line does not match version %s." % v)
    if "START-HERE %s" % v not in read("test-unit-hdb-4room.md"):
        fail("test-unit-hdb-4room.md does not name START-HERE %s." % v)
    n = len(words(sh))
    if n > MAX_START_HERE_WORDS:
        fail("START-HERE has %d words. Keep it under %d." % (n, MAX_START_HERE_WORDS))
    nums = [int(x) for x in re.findall(r"^## (\d+)\. ", sh, re.M)]
    if nums != list(range(1, len(nums) + 1)):
        fail("START-HERE section numbers are not 1 to N in order: %s" % nums)
    return v, n


def check_test_unit():
    t = read("test-unit-hdb-4room.md")
    template = code_blocks(read("START-HERE.md"), "json")
    keys = list(json.loads(template[0]).keys()) if template else []
    blocks = code_blocks(t, "json")
    if not blocks:
        fail("test-unit-hdb-4room.md has no JSON prompts.")
    sizes = []
    for i, b in enumerate(blocks, 1):
        try:
            d = json.loads(b)
        except ValueError as e:
            fail("Test prompt %d is not valid JSON: %s" % (i, e))
            continue
        extra = [k for k in d if k not in keys]
        if extra:
            fail("Test prompt %d has fields not in the START-HERE template: %s" % (i, extra))
        body = json.dumps({k: v for k, v in d.items() if k != "plan_usage"})
        leak = re.search(r"(?i:plan-(up|down|left|right))|\b[DW]\d+\b", body)
        if leak:
            fail("Test prompt %d contains plan terms or IDs the image model cannot use: %s" % (i, leak.group(0)))
        if len(d.get("must_hold", [])) > 3:
            fail("Test prompt %d has more than 3 must_hold items." % i)
        style = sum(len(words(d.get(k, ""))) for k in ("style", "light_and_view", "quality"))
        total = len(words(" ".join(json.dumps(v) for v in d.values())))
        sizes.append(total)
        if style > MAX_PROMPT_STYLE_WORDS:
            fail("Test prompt %d style, light and quality text has %d words. Keep it under %d." % (i, style, MAX_PROMPT_STYLE_WORDS))
        if total > MAX_PROMPT_WORDS:
            fail("Test prompt %d has %d words. Keep it under %d." % (i, total, MAX_PROMPT_WORDS))
    run = subprocess.run([sys.executable, "-I", os.path.join(ROOT, "fov.py"), os.path.join(ROOT, "test-unit-hdb-4room.json")],
                         capture_output=True, text=True)
    if run.returncode != 0 or "### " not in run.stdout:
        fail("fov.py failed on test-unit-hdb-4room.json: %s" % run.stderr.strip()[-300:])
    return len(blocks), (min(sizes), max(sizes)) if sizes else (0, 0)


def check_online(files):
    for f in files:
        url = RAW + f
        try:
            with urllib.request.urlopen(urllib.request.Request(url, method="HEAD"), timeout=20) as r:
                code = r.status
        except Exception as e:  # report every failure, keep going
            code = getattr(e, "code", str(e))
        if code != 200:
            fail("Raw link did not return 200: %s (%s)" % (url, code))


def main():
    files = repo_files()
    check_names(files)
    check_links(files)
    check_kickoff()
    check_styles(files)
    check_qc(files)
    check_heading_table()
    check_text(files)
    info = check_versions()
    prompts, (lo, hi) = check_test_unit()
    if "--online" in sys.argv:
        check_online(files)
    print("Files: %d, all in root" % len(files))
    if info:
        print("START-HERE: version %s, %d words" % info)
    print("Test prompts: %d, %d to %d words" % (prompts, lo, hi))
    if errors:
        print("\nFAIL: %d problem(s)" % len(errors))
        for e in errors:
            print("- " + e)
        sys.exit(1)
    print("PASS: every check passed")


if __name__ == "__main__":
    main()
