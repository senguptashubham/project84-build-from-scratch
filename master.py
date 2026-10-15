#!/usr/bin/env python3
"""Refresh README.md (the master sequence) from the three tracker files.

README.md owns the sequence: the week blocks and the order of IDs inside them.
The text above the "## Progress" heading and the License section are hand-written
and kept as they are. Everything else (titles, hours, optional flags, ticks,
totals) is copied from the tracker files, so you never edit those by hand.

Usage (run from anywhere; paths are relative to this file):
    python master.py            refresh README.md in place
    python master.py --check    validate only; exit 1 on any problem

Trackers:  code/CODE_README.md (S..)  derivation/DERIVATION_README.md (D..)  theory/THEORY_README.md (T..)
"""
import re
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
MASTER = HERE / "README.md"
SIZE_H = {"S": 1.5, "M": 3.5, "L": 6.0}
TRACKS = [("S", "Code"), ("T", "Theory"), ("D", "Derivations")]
TRACK_NAME = dict(TRACKS)
ID_RE = r"[SDT]\d[0-9.SQ]*"


def fmt(x):
    return f"{x:g}"


def parse_trackers():
    items, problems = {}, []

    def add(i, rec, src):
        if i in items:
            problems.append(f"duplicate ID {i} in {src}")
        items[i] = rec

    # Code: README.md
    text = (HERE / "code" / "CODE_README.md").read_text(encoding="utf-8")
    pat = re.compile(r"^- \[( |x)\] \*\*(S\d\.\d\d)( ★)? · (.*?)\*\* `([SML])`", re.M)
    for m in pat.finditer(text):
        title = m.group(4).rstrip(". ")
        if m.group(3):
            title += " ★"
        add(m.group(2), dict(track="S", title=title, hours=SIZE_H[m.group(5)], opt=False, done=m.group(1) == "x"), "code/CODE_README.md")
    # Others
    pat2 = re.compile(r"^- \[( |x)\] \*\*(" + ID_RE + r") · (.*?)\*\* (`opt` )?`([\d.]+) h`", re.M)
    for fname, letter in (("derivation/DERIVATION_README.md", "D"), ("theory/THEORY_README.md", "T")):
        text = (HERE / fname).read_text(encoding="utf-8")
        for m in pat2.finditer(text):
            i = m.group(2)
            if i[0] != letter:
                problems.append(f"{i} in {fname} has the wrong prefix (expected {letter})")
            add(i, dict(track=i[0], title=m.group(3).rstrip(". "), hours=float(m.group(5)), opt=bool(m.group(4)), done=m.group(1) == "x"), fname)
    return items, problems


def parse_master():
    """Return list of weeks: dict(header=str, ids=[...])."""
    if not MASTER.exists():
        raise SystemExit("README.md not found")
    weeks, cur = [], None
    for line in MASTER.read_text(encoding="utf-8").splitlines():
        if line.startswith("## Week "):
            cur = dict(header=line[3:].strip(), ids=[])
            weeks.append(cur)
            continue
        if cur is None:
            continue
        m = re.match(r"^\|\s*(?:☑|☐)?\s*\|\s*(" + ID_RE + r")\s*\|", line)
        if m:
            cur["ids"].append(m.group(1))
    return weeks


def validate(items, weeks):
    problems = []
    seen = {}
    for wi, w in enumerate(weeks, 1):
        for i in w["ids"]:
            if i in seen:
                problems.append(f"{i} appears in Week {seen[i]} and Week {wi}")
            seen[i] = wi
            if i not in items:
                problems.append(f"{i} (Week {wi}) is not in any tracker file")
    for i in items:
        if i not in seen:
            problems.append(f"{i} is in a tracker but not in README.md")
    return problems


def render(items, weeks, intro, outro):
    out = []
    A = out.append
    A(intro.rstrip("\n"))
    A("")

    # progress
    stats = {}
    for tr, name in TRACKS:
        ids = [i for i, r in items.items() if r["track"] == tr]
        req = [i for i in ids if not items[i]["opt"]]
        done_req = [i for i in req if items[i]["done"]]
        done_all = [i for i in ids if items[i]["done"]]
        stats[tr] = dict(
            name=name, req=len(req), done_req=len(done_req),
            hours=sum(items[i]["hours"] for i in ids),
            hours_done=sum(items[i]["hours"] for i in done_all),
        )
    A("## Progress")
    A("")
    A("| Track | Required rows done | Hours done | Hours in plan |")
    A("| --- | --- | --- | --- |")
    for tr, name in TRACKS:
        s = stats[tr]
        A(f"| {name} | {s['done_req']} / {s['req']} | {fmt(s['hours_done'])} | {fmt(s['hours'])} |")
    tot_h = sum(s["hours"] for s in stats.values())
    tot_d = sum(s["hours_done"] for s in stats.values())
    A(f"| **All** | **{sum(s['done_req'] for s in stats.values())} / {sum(s['req'] for s in stats.values())}** | **{fmt(tot_d)}** | **{fmt(tot_h)}** |")
    A("")

    # next up
    A("## Next up")
    A("")
    week_of = {}
    order = []
    for wi, w in enumerate(weeks, 1):
        for i in w["ids"]:
            week_of[i] = wi
            order.append(i)
    for tr, name in TRACKS:
        nxt = next((i for i in order if i in items and items[i]["track"] == tr and not items[i]["done"] and not items[i]["opt"]), None)
        if nxt:
            A(f"- **{name}:** {nxt} · {items[nxt]['title']} (Week {week_of[nxt]})")
        else:
            A(f"- **{name}:** all required rows done")
    A("")

    # weeks
    for wi, w in enumerate(weeks, 1):
        A(f"## {w['header']}")
        A("")
        by = {tr: 0.0 for tr, _ in TRACKS}
        for i in w["ids"]:
            if i in items:
                by[items[i]["track"]] += items[i]["hours"]
        total = sum(by.values())
        parts = " · ".join(f"{name} {fmt(by[tr])}" for tr, name in TRACKS)
        A(f"**Hours:** {fmt(total)} ({parts})")
        A("")
        A("| Done | ID | Item | Hours |")
        A("| --- | --- | --- | --- |")
        for i in w["ids"]:
            r = items.get(i)
            if r is None:
                A(f"| ? | {i} | **missing from trackers** | |")
                continue
            mark = "☑" if r["done"] else "☐"
            title = r["title"] + (" *(optional)*" if r["opt"] else "")
            A(f"| {mark} | {i} | {title} | {fmt(r['hours'])} |")
        A("")
    A("---")
    A("")
    A("Generated by `master.py`. Edit the week blocks and the order of rows to change the sequence; everything below the Progress heading is overwritten on refresh.")
    A("")
    A(outro.strip("\n"))
    A("")
    return "\n".join(out)


def main():
    check = "--check" in sys.argv
    items, problems = parse_trackers()
    weeks = parse_master()
    problems += validate(items, weeks)
    if problems:
        print("Problems found:")
        for p in problems:
            print(" -", p)
    if check:
        print("OK" if not problems else "")
        sys.exit(1 if problems else 0)
    if problems:
        print("README.md was not rewritten. Fix the problems above first.")
        sys.exit(1)
    text = MASTER.read_text(encoding="utf-8")
    intro = text[: text.index("## Progress")]
    outro = text[text.index("\n## License"):]
    MASTER.write_text(render(items, weeks, intro, outro), encoding="utf-8", newline="\n")
    print(f"README.md refreshed: {len(items)} rows, {len(weeks)} weeks.")


if __name__ == "__main__":
    main()