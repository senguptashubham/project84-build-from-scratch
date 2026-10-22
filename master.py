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
Time log:  log.md, one row per work session: | Date | ID | Minutes |  (empty Minutes = unknown)
Notes:     theory/notes/<area>/T<row>-<title>.md and derivation/D<nn>-<title>.md, one per row, each with a "row: .." line;
           item titles on the README link to them
"""
import re
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
MASTER = HERE / "README.md"
LOG = HERE / "log.md"
NOTES = HERE / "theory" / "notes"
NO_NOTES = {"T7.6"}  # topic rows that deliberately have no notes chapter
SIZE_H = {"S": 1.5, "M": 3.5, "L": 6.0}
TRACKS = [("S", "Code"), ("T", "Theory"), ("D", "Derivations")]
TRACK_NAME = dict(TRACKS)
NEXT_UP = 3
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


def parse_log(text, items):
    """Return (minutes, problems). minutes maps ID -> total logged minutes.

    A row with an empty Minutes cell is unknown, not zero, so it adds nothing.
    """
    minutes, problems = {}, []
    for n, line in enumerate(text.splitlines(), 1):
        if not line.startswith("|"):
            continue
        cells = [c.strip() for c in line.strip().strip("|").split("|")]
        if len(cells) < 3 or cells[1] == "ID" or set(cells[1]) <= set("-: "):
            continue
        i, mins = cells[1], cells[2]
        if i not in items:
            problems.append(f"log.md line {n}: {i!r} is not in any tracker file")
            continue
        if mins == "":
            continue
        try:
            minutes[i] = minutes.get(i, 0.0) + float(mins)
        except ValueError:
            problems.append(f"log.md line {n}: Minutes {mins!r} is not a number")
    return minutes, problems


def slug(heading):
    """GitHub-style anchor for a Markdown heading."""
    h = re.sub(r"[^\w\- ]", "", heading.strip().lower().replace("`", "").replace("*", ""))
    return h.replace(" ", "-")


def parse_notes(files=None, row_pat=r"T\d\.\d"):
    """Return ({row: notes path relative to the repo root}, problems), from each note file's row: line."""
    links, problems = {}, []
    for f in sorted(NOTES.glob("*/*.md")) if files is None else files:
        rel = f.relative_to(HERE).as_posix()
        m = re.search(rf"^row: ({row_pat})\s*$", f.read_text(encoding="utf-8"), re.M)
        if not m:
            # a file that is not named like a note (a scratch page, say) is ignored; a note missing its row: line is not
            if re.match(rf"({row_pat})-", f.name):
                problems.append(f"{rel} has no 'row: ..' line")
            continue
        row = m.group(1)
        if not f.name.startswith(row + "-"):
            problems.append(f"{rel} should start with its row ID {row}-")
        if row in links:
            problems.append(f"{row} is claimed by two note files")
        links[row] = rel
    return links, problems


def check_links(items, notes, tracker_text, tracker_file):
    """Each note file must belong to a tracker row, and that row must link to it."""
    problems = []
    base = tracker_file.rsplit("/", 1)[0] + "/"
    for row, rel in notes.items():
        if row not in items:
            problems.append(f"{rel} lists {row}, which is not a row in {tracker_file}")
            continue
        line = next((l for l in tracker_text.splitlines() if l.startswith("- [") and f"**{row} \u00b7 " in l), "")
        want = "(" + rel.split(base, 1)[1] + ")"
        if want not in line:
            problems.append(f"{tracker_file} row {row} should link {want[1:-1]}")
    return problems


def check_derivations(items, notes, text):
    problems = check_links(items, notes, text, "derivation/DERIVATION_README.md")
    for row in items:
        if re.fullmatch(r"D\d\d", row) and row not in notes:
            problems.append(f"{row} has no note file (add derivation/{row}-<title>.md with a 'row: {row}' line)")
    return problems


def check_notes(items, notes, theory_text):
    problems = check_links(items, notes, theory_text, "theory/THEORY_README.md")
    for row in items:
        if re.fullmatch(r"T\d\.\d", row) and row not in NO_NOTES and not row.startswith("T9") and row not in notes:
            problems.append(f"{row} has no notes file (add theory/notes/<area>/{row}-<title>.md with a 'row: {row}' line)")
    return problems


def build_links(items, notes):
    """Where each plan row's title should point, as paths relative to the repo root."""
    code = (HERE / "code" / "CODE_README.md").read_text(encoding="utf-8")
    deriv = (HERE / "derivation" / "DERIVATION_README.md").read_text(encoding="utf-8")
    theory = (HERE / "theory" / "THEORY_README.md").read_text(encoding="utf-8")
    sprint = {m.group(1): slug(m.group(0)[3:]) for m in re.finditer(r"^## Sprint (\d) \u00b7 .*$", code, re.M)}
    derive = {m.group(1): slug(m.group(0)[3:]) for m in re.finditer(r"^## (D\d\d) \u00b7 .*$", deriv, re.M)}
    module = {m.group(1): slug(m.group(0)[3:]) for m in re.finditer(r"^## M(\d)\. .*$", theory, re.M)}
    links = {}
    for i, r in items.items():
        if r["track"] == "S" and i[1] in sprint:
            links[i] = f"code/CODE_README.md#{sprint[i[1]]}"
        elif r["track"] == "D" and (i in notes or i in derive):
            links[i] = notes.get(i) or f"derivation/DERIVATION_README.md#{derive[i]}"
        elif r["track"] == "T":
            if i in notes:
                links[i] = notes[i]
            elif i[1] in module:
                links[i] = f"theory/THEORY_README.md#{module[i[1]]}"
    return links


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


def render(items, weeks, intro, outro, minutes=None, links=None):
    minutes = minutes or {}
    links = links or {}
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
        timed = [i for i in done_all if i in minutes]
        planned_timed = sum(items[i]["hours"] for i in timed)
        stats[tr] = dict(
            name=name, req=len(req), done_req=len(done_req),
            hours=sum(items[i]["hours"] for i in ids),
            hours_done=sum(items[i]["hours"] for i in done_all),
            actual=sum(minutes.get(i, 0.0) for i in ids) / 60,
            actual_timed=sum(minutes[i] for i in timed) / 60,
            planned_timed=planned_timed,
        )
    A("## Progress")
    A("")
    A("| Track | Required rows done | Hours done | Hours in plan | Actual hours logged | Actual / planned |")
    A("| --- | --- | --- | --- | --- | --- |")

    def ratio(actual, planned):
        return f"{actual / planned:.2f}" if planned else "-"

    for tr, name in TRACKS:
        s = stats[tr]
        A(f"| {name} | {s['done_req']} / {s['req']} | {fmt(s['hours_done'])} | {fmt(s['hours'])} | {fmt(round(s['actual'], 1))} | {ratio(s['actual_timed'], s['planned_timed'])} |")
    tot_h = sum(s["hours"] for s in stats.values())
    tot_d = sum(s["hours_done"] for s in stats.values())
    tot_a = sum(s["actual"] for s in stats.values())
    tot_at = sum(s["actual_timed"] for s in stats.values())
    tot_pt = sum(s["planned_timed"] for s in stats.values())
    A(f"| **All** | **{sum(s['done_req'] for s in stats.values())} / {sum(s['req'] for s in stats.values())}** | **{fmt(tot_d)}** | **{fmt(tot_h)}** | **{fmt(round(tot_a, 1))}** | **{ratio(tot_at, tot_pt)}** |")
    A("")
    A("*Actual / planned* compares logged time with the size tags, for finished rows that have minutes in `log.md`.")
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
    A(f"The next {NEXT_UP} unticked rows in plan order, across all three tracks. Optional rows are skipped.")
    A("")
    upcoming = [i for i in order if i in items and not items[i]["done"] and not items[i]["opt"]][:NEXT_UP]
    for n, i in enumerate(upcoming, 1):
        A(f"{n}. **{i}** · {items[i]['title']} ({TRACK_NAME[items[i]['track']]}, Week {week_of[i]})")
    if not upcoming:
        A("All required rows are done.")
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
            title = f"[{r['title']}]({links[i]})" if i in links else r["title"]
            title += " *(optional)*" if r["opt"] else ""
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
    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(errors="replace")  # a non-ASCII log entry must not crash a cp1252 console
    check = "--check" in sys.argv
    items, problems = parse_trackers()
    weeks = parse_master()
    problems += validate(items, weeks)
    notes, note_problems = parse_notes()
    problems += note_problems + check_notes(items, notes, (HERE / "theory" / "THEORY_README.md").read_text(encoding="utf-8"))
    dnotes, dnote_problems = parse_notes(sorted((HERE / "derivation").glob("D??-*.md")), r"D\d\d")
    problems += dnote_problems + check_derivations(items, dnotes, (HERE / "derivation" / "DERIVATION_README.md").read_text(encoding="utf-8"))
    notes = {**notes, **dnotes}
    minutes, log_problems = parse_log(LOG.read_text(encoding="utf-8") if LOG.exists() else "", items)
    problems += log_problems
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
    MASTER.write_text(render(items, weeks, intro, outro, minutes, build_links(items, notes)), encoding="utf-8", newline="\n")
    print(f"README.md refreshed: {len(items)} rows, {len(weeks)} weeks.")


if __name__ == "__main__":
    main()
