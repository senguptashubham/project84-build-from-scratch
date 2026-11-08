import master

PAGE = """\
# Title

## Progress

<!-- progress:start -->
<!-- progress:end -->

## Sprint 1 · Days 1-14 · Theme

### Week 1 · Days 1-7 · Part A: First

- [x] **S1.01 · Pairwise distances.** `S` text
- [ ] **S1.02 ★ · Activations.** `M` text
- [ ] **D01 · Softmax gradient.** `1.5 h` **Derive:** text. Notes: [D01-x](derivation/D01-x.md).
  - [ ] Blind re-derive, 7 days later, 15 minutes, no notes.

### Week 2 · Days 8-14 · Part B: Second

- [ ] **S1.03 · Splits.** `L` text
"""


def test_parse_readme_reads_items_weeks_ticks_and_hours():
    items, weeks, problems = master.parse_readme(PAGE)
    assert problems == []
    assert list(items) == ["S1.01", "S1.02", "D01", "S1.03"]
    assert items["S1.01"]["done"] and not items["S1.02"]["done"]
    assert items["S1.02"]["title"] == "Activations ★" and items["S1.02"]["hours"] == 3.5
    assert items["D01"]["hours"] == 1.5 and items["D01"]["track"] == "D"
    assert [w["ids"] for w in weeks] == [["S1.01", "S1.02", "D01"], ["S1.03"]]
    assert weeks[1]["part"] == "B" and weeks[1]["sprint"] == "1" and weeks[1]["days"] == "8-14"


def test_parse_readme_reports_structural_mistakes():
    def problems_for(page):
        return master.parse_readme(page)[2]

    assert any("appears twice" in p for p in problems_for(PAGE.replace("**S1.03 · Splits.**", "**S1.01 · Splits.**")))
    assert any("listed under Sprint 1" in p for p in problems_for(PAGE.replace("**S1.03 · Splits.**", "**S2.03 · Splits.**")))
    assert any("size tag" in p for p in problems_for(PAGE.replace("`L` text", "`2 h` text")))
    assert any("hours tag" in p for p in problems_for(PAGE.replace("`1.5 h`", "`S`")))
    assert any("malformed" in p for p in problems_for(PAGE.replace("`L` text", "text")))
    assert any("Week 3 follows Week 1" in p for p in problems_for(PAGE.replace("### Week 2", "### Week 3")))
    assert any("not under a '### Week N'" in p for p in problems_for("## Sprint 1 · x\n\n- [ ] **S1.01 · a.** `S` t\n"))


def test_a_malformed_item_row_is_reported_not_skipped():
    problems = master.parse_readme(PAGE.replace("**S1.03 · Splits.**", "**X1.03 · Splits.**"))[2]
    assert any("X1.03" in p and "malformed" in p for p in problems)


def test_progress_block_embeds_the_picture_with_counts_in_its_alt_text():
    items, weeks, _ = master.parse_readme(PAGE)
    out = master.render_block(items, weeks)
    assert "![Progress: 1 of 4 rows done](assets/progress.svg)" in out
    assert "Actual" not in out


def test_the_svg_is_valid_xml_shows_the_counts_and_is_deterministic():
    import xml.etree.ElementTree as ET

    items, weeks, _ = master.parse_readme(PAGE)
    svg = master.progress_chart.render_svg(items, weeks)
    root = ET.fromstring(svg)
    assert root.tag.endswith("svg")
    assert "1 of 4 rows done" in svg and "25%" in svg
    assert svg == master.progress_chart.render_svg(items, weeks)
    assert "<script" not in svg and "foreignObject" not in svg  # GitHub would drop them


def test_the_svg_handles_nothing_done_and_everything_done():
    import xml.etree.ElementTree as ET

    items, weeks, _ = master.parse_readme(PAGE)
    for flag in (False, True):
        for r in items.values():
            r["done"] = flag
        ET.fromstring(master.progress_chart.render_svg(items, weeks))


def test_render_is_deterministic_and_lists_next_up_in_plan_order():
    items, weeks, _ = master.parse_readme(PAGE)
    a = master.render_block(items, weeks)
    assert a == master.render_block(items, weeks)
    nxt = a.split("**Next up**")[1].split("**Plan by week**")[0]
    assert [l.split("**")[1] for l in nxt.splitlines() if l[:2] in ("1.", "2.", "3.")] == ["S1.02", "D01", "S1.03"]


def test_plan_by_week_sums_hours_and_ticks():
    items, weeks, _ = master.parse_readme(PAGE)
    out = master.render_block(items, weeks)
    assert "| 1 | 1-7 | 1 · A | First | 3 | 6.5 | 1 / 3 |" in out
    assert "| 2 | 8-14 | 1 · B | Second | 1 | 6 | 0 / 1 |" in out


def test_splice_replaces_only_between_the_markers_and_is_idempotent():
    once = master.splice(PAGE, "BLOCK")
    assert once.startswith("# Title") and "BLOCK" in once and "## Sprint 1" in once
    assert master.splice(once, "BLOCK") == once
    assert master.splice(once, "OTHER").count("BLOCK") == 0
    assert master.splice("no markers here", "BLOCK") is None


def test_check_notes_requires_one_note_file_and_a_matching_link(tmp_path):
    items, _, _ = master.parse_readme(PAGE)
    assert master.check_notes(items, tmp_path) == ["D01 needs exactly one note file D01-<title>.md in derivation/ (found 0)"]
    (tmp_path / "D01-x.md").write_text("# D01\n", encoding="utf-8")
    assert master.check_notes(items, tmp_path) == []
    (tmp_path / "D01-y.md").write_text("# D01\n", encoding="utf-8")
    assert "found 2" in master.check_notes(items, tmp_path)[0]
    (tmp_path / "D01-y.md").unlink()
    (tmp_path / "D01-x.md").rename(tmp_path / "D01-renamed.md")
    assert master.check_notes(items, tmp_path) == ["D01 should link derivation/D01-renamed.md"]


def test_commit_days_counts_commits_per_day(monkeypatch):
    class R:
        stdout = " ".join(["2026-11-08", "2026-11-08", "2026-11-06"])

    monkeypatch.setattr(master.subprocess, "run", lambda *a, **k: R())
    counts = master.commit_days(28)
    assert counts[master.date(2026, 11, 8)] == 2 and counts[master.date(2026, 11, 6)] == 1
