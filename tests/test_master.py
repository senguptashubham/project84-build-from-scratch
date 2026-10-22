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


def test_tracker_descriptions_strip_the_notes_link_and_hours():
    text = ("- [ ] **T1.2 \u00b7 Bias.** `2.5 h` Bias, variance; splits. Notes: [T1.2-bias](notes/x/T1.2-bias.md).\n"
            "- [ ] **T8.10 \u00b7 APIs.** `1 h` Retries and backoff.\n"
            "- [ ] **T6.5 \u00b7 Video.** `opt` `2 h` Optional depth.\n")
    assert master.tracker_descriptions(text) == {
        "T1.2": "Bias, variance; splits.",
        "T8.10": "Retries and backoff.",
        "T6.5": "Optional depth.",
    }


def test_yaml_scalar_quotes_only_when_needed():
    assert master.yaml_scalar("Plain text; with *stars* and commas, fine.") == "Plain text; with *stars* and commas, fine."
    assert master.yaml_scalar("Transfer learning: freeze") == '"Transfer learning: freeze"'
    assert master.yaml_scalar("A note # with hash") == '"A note # with hash"'


def test_sync_descriptions_rewrites_only_the_description_line(tmp_path):
    note = tmp_path / "T1.2-bias.md"
    note.write_text("---\ntags:\n  - foundations\nrow: T1.2\ndescription: old text\n---\n# T1.2\n\nmy own notes\n", encoding="utf-8")
    old_here, master.HERE = master.HERE, tmp_path
    try:
        tracker = "- [ ] **T1.2 \u00b7 Bias.** `2 h` New text: with colon. Notes: [x](y.md).\n"
        want = master.tracker_descriptions(tracker)
        assert master.check_descriptions({"T1.2": "T1.2-bias.md"}, want)  # drift is reported
        assert master.sync_descriptions({"T1.2": "T1.2-bias.md"}, want) == ["T1.2-bias.md"]
        assert master.check_descriptions({"T1.2": "T1.2-bias.md"}, want) == []
        assert master.sync_descriptions({"T1.2": "T1.2-bias.md"}, want) == []  # idempotent
    finally:
        master.HERE = old_here
    body = note.read_text(encoding="utf-8")
    assert 'description: "New text: with colon."' in body and body.endswith("my own notes\n")


def test_derivation_descriptions_come_from_the_derive_line():
    text = (
        "## D01 · First\n\n- [ ] **D01 · First.** `1 h` x\n\n**Related code:** S3.02.\n\n"
        "**Derive:** Show that `a = b`.\n\n**Intuition:** ...\n\n---\n\n"
        "## D02 · Second\n\n**Derive:** Obtain the normal equations.\n"
    )
    assert master.derivation_descriptions(text) == {"D01": "Show that `a = b`.", "D02": "Obtain the normal equations."}


def test_note_description_reads_the_shapes_an_editor_may_resave():
    def note(desc_block):
        return "---\ntags:\n  - x\nrow: T1.1\n" + desc_block + "\n---\n# body\n"

    assert master.note_description(note("description: plain text")) == "plain text"
    assert master.note_description(note('description: "quoted: yes"')) == "quoted: yes"
    assert master.note_description(note("description: 'it''s single quoted'")) == "it's single quoted"
    assert master.note_description(note("description: first part\n  second part")) == "first part second part"
    assert master.note_description(note("description: >-\n  folded\n  text")) == "folded text"
    assert master.note_description(note("tags: []")) is None


def test_sync_replaces_a_wrapped_description_completely(tmp_path):
    note = tmp_path / "T1.1-x.md"
    note.write_text("---\ntags:\n  - x\nrow: T1.1\ndescription: old first line\n  old second line\n---\n# body\n", encoding="utf-8")
    old_here, master.HERE = master.HERE, tmp_path
    try:
        assert master.sync_descriptions({"T1.1": "T1.1-x.md"}, {"T1.1": "new text"}) == ["T1.1-x.md"]
    finally:
        master.HERE = old_here
    assert note.read_text(encoding="utf-8") == "---\ntags:\n  - x\nrow: T1.1\ndescription: new text\n---\n# body\n"


def test_log_rejects_nan_inf_and_negative_minutes():
    items = {"S1.01": dict(track="S", title="a", hours=1.5, opt=False, done=True)}
    text = "| Date | ID | Minutes |\n| | S1.01 | nan |\n| | S1.01 | inf |\n| | S1.01 | -5 |\n| | S1.01 | 30 |\n"
    minutes, problems = master.parse_log(text, items)
    assert minutes == {"S1.01": 30.0} and len(problems) == 3
