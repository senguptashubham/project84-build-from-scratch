import master

ITEMS = {
    "S1.01": dict(track="S", title="a", hours=1.5, opt=False, done=True),
    "S1.02": dict(track="S", title="b", hours=3.5, opt=False, done=True),
    "S1.03": dict(track="S", title="c", hours=1.5, opt=False, done=False),
}


def test_empty_minutes_is_unknown_not_zero():
    minutes, problems = master.parse_log("| Date | ID | Minutes |\n| --- | --- | --- |\n| | S1.01 | |\n", ITEMS)
    assert minutes == {} and problems == []


def test_sessions_for_one_item_add_up():
    text = "| Date | ID | Minutes |\n| --- | --- | --- |\n| | S1.02 | 60 |\n| | S1.02 | 30 |\n"
    minutes, problems = master.parse_log(text, ITEMS)
    assert minutes == {"S1.02": 90.0} and problems == []


def test_unknown_id_is_a_problem():
    minutes, problems = master.parse_log("| Date | ID | Minutes |\n| | S9.99 | 10 |\n", ITEMS)
    assert minutes == {} and len(problems) == 1 and "S9.99" in problems[0]


def test_non_numeric_minutes_is_a_problem():
    _, problems = master.parse_log("| Date | ID | Minutes |\n| | S1.01 | abc |\n", ITEMS)
    assert len(problems) == 1


def test_progress_ratio_uses_only_finished_rows_with_minutes():
    weeks = [dict(header="Week 1 · test", ids=list(ITEMS))]
    # S1.01: 1.5 h planned, 90 min logged -> ratio 1.00. S1.02 has no minutes, S1.03 is not done.
    out = master.render(ITEMS, weeks, "intro\n", "## License\n", {"S1.01": 90.0, "S1.03": 600.0})
    row = next(l for l in out.splitlines() if l.startswith("| Code |"))
    assert row.endswith("| 11.5 | 1.00 |")


def test_render_is_deterministic():
    weeks = [dict(header="Week 1 · test", ids=list(ITEMS))]
    a = master.render(ITEMS, weeks, "i\n", "## License\n", {"S1.01": 60.0})
    assert a == master.render(ITEMS, weeks, "i\n", "## License\n", {"S1.01": 60.0})


def test_next_up_mixes_tracks_in_plan_order():
    items = {
        "T0.1": dict(track="T", title="theory", hours=1, opt=False, done=False),
        "S1.01": dict(track="S", title="code", hours=1.5, opt=False, done=False),
        "D01": dict(track="D", title="derive", hours=1, opt=False, done=False),
        "T0.2": dict(track="T", title="skipped, optional", hours=1, opt=True, done=False),
        "S1.02": dict(track="S", title="later", hours=1.5, opt=False, done=False),
    }
    weeks = [dict(header="Week 1 · test", ids=["T0.1", "T0.2", "S1.01", "D01", "S1.02"])]
    out = master.render(items, weeks, "i\n", "## License\n")
    nxt = out.split("## Next up")[1].split("## Week")[0]
    assert [l.split("**")[1] for l in nxt.splitlines() if l[:2] == "1." or l[:2] in ("2.", "3.")] == ["T0.1", "S1.01", "D01"]


def test_check_notes_reports_missing_and_mismatched_links():
    items = {
        "T1.1": dict(track="T", title="a", hours=1, opt=False, done=False),
        "T1.2": dict(track="T", title="b", hours=1, opt=False, done=False),
        "T7.6": dict(track="T", title="optional reference pass", hours=1, opt=True, done=False),
        "T9.1": dict(track="T", title="consolidation", hours=1, opt=False, done=False),
    }
    notes = {"T1.1": "theory/notes/01-foundations/T1.1-a.md"}
    good = "- [ ] **T1.1 · a.** `1 h` text. Notes: [T1.1-a](notes/01-foundations/T1.1-a.md).\n"
    assert master.check_notes(items, notes, good) == [
        "T1.2 has no notes file (add theory/notes/<area>/T1.2-<title>.md with a 'row: T1.2' line)"
    ]
    stale = "- [ ] **T1.1 · a.** `1 h` text. Notes: [x](notes/01-foundations/old-name.md).\n"
    assert any("should link notes/01-foundations/T1.1-a.md" in p for p in master.check_notes(items, notes, stale))


def test_titles_link_to_notes_when_given():
    items = {"T1.1": dict(track="T", title="Estimation", hours=1, opt=False, done=False)}
    weeks = [dict(header="Week 1 · t", ids=["T1.1"])]
    out = master.render(items, weeks, "i\n", "## License\n", None, {"T1.1": "theory/notes/x/T1.1-estimation.md"})
    assert "| [Estimation](theory/notes/x/T1.1-estimation.md) |" in out


def test_slug_matches_github_anchors():
    assert master.slug("Sprint 1 · Days 1-14 · NumPy, data and statistics fluency") == "sprint-1--days-1-14--numpy-data-and-statistics-fluency"


def test_check_derivations_requires_a_note_file_and_a_matching_link():
    items = {
        "D01": dict(track="D", title="a", hours=1, opt=False, done=False),
        "D02": dict(track="D", title="b", hours=1, opt=False, done=False),
    }
    notes = {"D01": "derivation/D01-a.md"}
    text = "- [ ] **D01 \u00b7 a.** `1 h` text. Notes: [D01-a](D01-a.md).\n- [ ] **D02 \u00b7 b.** `1 h` text.\n"
    assert master.check_derivations(items, notes, text) == [
        "D02 has no note file (add derivation/D02-<title>.md with a 'row: D02' line)"
    ]
    wrong = "- [ ] **D01 \u00b7 a.** `1 h` text. Notes: [x](other.md).\n"
    assert any("should link D01-a.md" in p for p in master.check_derivations({"D01": items["D01"]}, notes, wrong))


def test_derivation_title_links_to_its_note_file_when_present(tmp_path):
    items = {"D01": dict(track="D", title="a", hours=1, opt=False, done=False)}
    links = master.build_links(items, {"D01": "derivation/D01-a.md"})
    assert links["D01"] == "derivation/D01-a.md"


def test_scratch_files_in_notes_are_ignored_but_a_note_without_row_is_reported(tmp_path):
    scratch = tmp_path / "Untitled.md"
    scratch.write_text("# scratch\n", encoding="utf-8")
    broken = tmp_path / "T1.2-bias.md"
    broken.write_text("# no frontmatter\n", encoding="utf-8")
    good = tmp_path / "T1.1-mle.md"
    good.write_text("---\nrow: T1.1\n---\n# T1.1\n", encoding="utf-8")
    # parse_notes reports paths relative to the repo, so point HERE at tmp_path for this test
    old = master.HERE
    master.HERE = tmp_path
    try:
        links, problems = master.parse_notes([scratch, broken, good])
    finally:
        master.HERE = old
    assert links == {"T1.1": "T1.1-mle.md"}
    assert problems == ["T1.2-bias.md has no 'row: ..' line"]
