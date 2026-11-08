#!/usr/bin/env python3
"""Refresh the Progress section of README.md from the checkboxes in the same file.

README.md is the single source: every item (a code problem `S..` or a derivation `D..`)
is a checkbox row, listed in the order to do them, grouped under `### Week N` headings
inside `## Sprint N` sections. Everything between the progress markers is generated here
(progress, next up, plan by week); the rest is hand-written and left alone.

Usage (run from anywhere; paths are relative to this file):
    python master.py            refresh the Progress section in place
    python master.py --check    validate only; exit 1 on any problem, or if the section is stale
    python master.py --days     show which days you committed, from git history (read-only, nothing to log)

Notes:     derivation/D<nn>-<title>.md, one per derivation; its row links to it
"""
import re
import subprocess
import sys
from collections import Counter
from datetime import date, timedelta
from pathlib import Path

HERE = Path(__file__).resolve().parent
README = HERE / "README.md"
DERIV = HERE / "derivation"
START, END = "<!-- progress:start -->", "<!-- progress:end -->"
SIZE_H = {"S": 1.5, "M": 3.5, "L": 6.0}
TRACKS = [("S", "Code"), ("D", "Derivations")]
TRACK_NAME = dict(TRACKS)
NEXT_UP = 3

ITEM_RE = re.compile(r"^- \[( |x|X)\] \*\*([SD]\d[0-9.]*)( ★)? · (.*?)\*\* (?:`([SML])`|`([\d.]+) h`)", re.M)
SPRINT_RE = re.compile(r"^## Sprint (\d) · .*$")
WEEK_RE = re.compile(r"^### Week (\d+) · Days (\S+) · Part ([AB]): (.*)$")


def fmt(x):
    return f"{x:g}"


def parse_readme(text):
    """Return (items, weeks, problems). items: ID -> record; weeks: list of dict(n, days, sprint, part, focus, ids)."""
    items, weeks, problems = {}, [], []
    sprint, week = None, None
    for line in text.splitlines():
        m = SPRINT_RE.match(line)
        if m:
            sprint, week = m.group(1), None
            continue
        m = WEEK_RE.match(line)
        if m:
            if sprint is None:
                problems.append(f"{line.strip()!r} is not inside a Sprint section")
            week = dict(n=int(m.group(1)), days=m.group(2), sprint=sprint, part=m.group(3), focus=m.group(4).strip(), ids=[])
            weeks.append(week)
            continue
        m = ITEM_RE.match(line)
        if not m:
            if re.match(r"^- \[( |x|X)\] \*\*", line):
                problems.append(f"malformed item row (ID, size or hours tag): {line[:60]!r}")
            continue
        done, iid, star, title, size, hours = m.groups()
        track = iid[0]
        if week is None:
            problems.append(f"{iid} is not under a '### Week N' heading")
            continue
        if iid in items:
            problems.append(f"{iid} appears twice (Week {items[iid]['week']} and Week {week['n']})")
            continue
        if track == "S" and (not re.fullmatch(r"S\d\.\d\d", iid) or not size):
            problems.append(f"{iid} needs an ID like S1.01 and a size tag S, M or L")
        if track == "D" and (not re.fullmatch(r"D\d\d", iid) or not hours):
            problems.append(f"{iid} needs an ID like D01 and an hours tag such as `1.5 h`")
        if track == "S" and iid[1] != sprint:
            problems.append(f"{iid} is listed under Sprint {sprint}")
        title = title.rstrip(". ") + (" ★" if star else "")
        h = SIZE_H[size] if size else float(hours or 0)
        items[iid] = dict(track=track, title=title, hours=h, done=done in "xX", week=week["n"], line=line)
        week["ids"].append(iid)
    for a, b in zip(weeks, weeks[1:]):
        if b["n"] != a["n"] + 1:
            problems.append(f"Week {b['n']} follows Week {a['n']}")
    for w in weeks:
        if not w["ids"]:
            problems.append(f"Week {w['n']} has no items")
    return items, weeks, problems


def check_notes(items, deriv_dir=None):
    """Each derivation needs exactly one note file D<nn>-*.md, and its row must link to it."""
    deriv_dir = deriv_dir or DERIV
    problems = []
    for iid, r in items.items():
        if r["track"] != "D":
            continue
        found = sorted(deriv_dir.glob(f"{iid}-*.md"))
        if len(found) != 1:
            problems.append(f"{iid} needs exactly one note file {iid}-<title>.md in derivation/ (found {len(found)})")
        elif f"(derivation/{found[0].name})" not in r["line"]:
            problems.append(f"{iid} should link derivation/{found[0].name}")
    return problems


def render_block(items, weeks):
    """The generated Progress section: totals per track, next up, and the plan by week."""
    out = []
    A = out.append

    stats = {}
    for tr, name in TRACKS:
        ids = [i for i, r in items.items() if r["track"] == tr]
        done = [i for i in ids if items[i]["done"]]
        stats[tr] = dict(
            name=name, rows=len(ids), done=len(done),
            hours=sum(items[i]["hours"] for i in ids),
            hours_done=sum(items[i]["hours"] for i in done),
        )

    A("| Track | Rows done | Hours done | Hours in plan |")
    A("| --- | --- | --- | --- |")
    for tr, name in TRACKS:
        s = stats[tr]
        A(f"| {name} | {s['done']} / {s['rows']} | {fmt(s['hours_done'])} | {fmt(s['hours'])} |")
    tot = lambda k: sum(s[k] for s in stats.values())
    A(f"| **All** | **{tot('done')} / {tot('rows')}** | **{fmt(tot('hours_done'))}** | **{fmt(tot('hours'))}** |")
    A("")
    A("Hours come from the size tags and are planning numbers only; nothing is timed.")
    A("")

    A(f"**Next up** (the next {NEXT_UP} unticked rows in plan order, across both tracks):")
    A("")
    order = [i for w in weeks for i in w["ids"]]
    upcoming = [i for i in order if not items[i]["done"]][:NEXT_UP]
    for n, i in enumerate(upcoming, 1):
        A(f"{n}. **{i}** · {items[i]['title']} ({TRACK_NAME[items[i]['track']]}, Week {items[i]['week']})")
    if not upcoming:
        A("All rows are done.")
    A("")

    A("**Plan by week**")
    A("")
    A("| Week | Days | Sprint · Part | Focus | Rows | Hours | Done |")
    A("| --- | --- | --- | --- | --- | --- | --- |")
    for w in weeks:
        hours = sum(items[i]["hours"] for i in w["ids"])
        done = sum(items[i]["done"] for i in w["ids"])
        A(f"| {w['n']} | {w['days']} | {w['sprint']} · {w['part']} | {w['focus']} | {len(w['ids'])} | {fmt(hours)} | {done} / {len(w['ids'])} |")
    return "\n".join(out)


def commit_days(since_days=28):
    """Return {date: commit count} for the last `since_days` days, read from git history."""
    since = (date.today() - timedelta(days=since_days - 1)).isoformat()
    out = subprocess.run(["git", "log", f"--since={since}", "--format=%ad", "--date=short"],
                         cwd=HERE, capture_output=True, text=True, encoding="utf-8", check=True).stdout
    return Counter(date.fromisoformat(d) for d in out.split())


def show_days(since_days=28):
    """Print one line per day: commits made, newest first, plus the current streak."""
    counts = commit_days(since_days)
    today = date.today()
    streak = 0
    day = today if counts.get(today) else today - timedelta(days=1)
    while counts.get(day):
        streak += 1
        day -= timedelta(days=1)
    active = sum(1 for v in counts.values() if v)
    print(f"Last {since_days} days: {active} with a commit. Current streak: {streak}.")
    for k in range(since_days):
        d = today - timedelta(days=k)
        n = counts.get(d, 0)
        print(f"{d.isoformat()} {d.strftime('%a')}  {'#' * n if n else '.'}")


def splice(text, block):
    """Put `block` between the progress markers, or return None if the markers are missing or misplaced."""
    a, b = text.find(START), text.find(END)
    if a < 0 or b < a:
        return None
    return text[: a + len(START)] + "\n\n" + block + "\n\n" + text[b:]


def main():
    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(errors="replace")  # a non-ASCII log entry must not crash a cp1252 console
    if "--days" in sys.argv:
        show_days()
        return
    check = "--check" in sys.argv
    text = README.read_text(encoding="utf-8")
    items, weeks, problems = parse_readme(text)
    problems += check_notes(items)
    new = None
    if not problems:
        new = splice(text, render_block(items, weeks))
        if new is None:
            problems.append(f"README.md needs the markers {START} and {END} (in that order) under '## Progress'")
        elif check and new != text:
            problems.append("the Progress section of README.md is out of date (run: python master.py)")
    if problems:
        print("Problems found:")
        for p in problems:
            print(" -", p)
        if not check:
            print("README.md was not rewritten. Fix the problems above first.")
        sys.exit(1)
    if check:
        print("OK")
        return
    README.write_text(new, encoding="utf-8", newline="\n")
    print(f"README.md refreshed: {len(items)} rows, {len(weeks)} weeks.")


if __name__ == "__main__":
    main()
