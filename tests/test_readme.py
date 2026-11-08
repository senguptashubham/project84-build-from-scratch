"""Checks on the real README.md and the files it links to (not on master.py's logic)."""
import re
import urllib.parse
from pathlib import Path

import master

ROOT = Path(__file__).resolve().parent.parent
PAGES = [ROOT / "README.md", ROOT / "archive" / "README.md", *sorted((ROOT / "derivation").glob("D??-*.md"))]


def github_slug(heading):
    h = re.sub(r"[^\w\- ]", "", heading.strip().lower().replace("`", "").replace("*", ""))
    return h.replace(" ", "-")


def headings(path):
    text = re.sub(r"```.*?```", "", path.read_text(encoding="utf-8"), flags=re.S)
    return {github_slug(l.lstrip("#")) for l in text.splitlines() if l.startswith("#")}


def test_every_relative_link_and_anchor_resolves():
    broken = []
    for page in PAGES:
        text = re.sub(r"```.*?```", "", page.read_text(encoding="utf-8"), flags=re.S)
        for m in re.finditer(r"(?<!!)\[[^\]]*\]\(([^)\s]+)\)", text):
            target = m.group(1)
            if re.match(r"(https?:|mailto:)", target):
                continue
            path, _, frag = target.partition("#")
            dest = page.parent / urllib.parse.unquote(path) if path else page
            if not dest.exists():
                broken.append(f"{page.relative_to(ROOT)}: {target}")
            elif frag and dest.suffix == ".md" and frag not in headings(dest):
                broken.append(f"{page.relative_to(ROOT)}: {target} (no such heading)")
    assert broken == []


def test_the_plan_is_valid_and_the_progress_section_is_current():
    text = (ROOT / "README.md").read_text(encoding="utf-8")
    items, weeks, problems = master.parse_readme(text)
    assert problems == []
    assert master.check_notes(items) == []
    assert sum(r["track"] == "S" for r in items.values()) == 103
    assert sum(r["track"] == "D" for r in items.values()) == 10
    assert master.splice(text, master.render_block(items, weeks)) == text


def test_a_derivation_is_placed_with_the_code_it_relates_to():
    """Each derivation sits in the same week as, or the week next to, a code item it names under Related code."""
    text = (ROOT / "README.md").read_text(encoding="utf-8")
    items, _, _ = master.parse_readme(text)
    for iid, r in items.items():
        if r["track"] != "D":
            continue
        related = re.search(r"\*\*Related code:\*\* (.*?)\*\*Done when", r["line"]).group(1)
        weeks = [items[c]["week"] for c in re.findall(r"S\d\.\d\d", related) if c in items]
        assert any(abs(w - r["week"]) <= 1 for w in weeks), f"{iid} is far from its related code"
