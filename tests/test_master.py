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
