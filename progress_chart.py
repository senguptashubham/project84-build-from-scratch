"""Draw the progress picture (assets/progress.svg) that README.md shows.

GitHub runs no JavaScript in a README but displays SVG images as drawn, so the picture is
a plain SVG file written by master.py. It has its own dark background and reads the same
in GitHub's light and dark themes. Output is deterministic: same ticks, same bytes.
"""
import math

SPRINT_COLORS = ["#ff6b6b", "#ff9f43", "#feca57", "#1dd1a1", "#48dbfb", "#54a0ff", "#a55eea", "#f368e0", "#ff7aa2"]
W, H = 840, 410
FONT = "Segoe UI, Helvetica, Arial, sans-serif"


def _f(x):
    return f"{x:.1f}"


def _bar(x, y, width, frac, gradient, label, value):
    """A rounded progress bar with a label above it and the value at the right end."""
    fill = max(frac * width, 18) if frac > 0 else 0
    out = [
        f'<text x="{x}" y="{y - 10}" fill="#e6edf3" font-size="15" font-weight="600">{label}</text>',
        f'<text x="{x + width}" y="{y - 10}" fill="#8b949e" font-size="14" text-anchor="end">{value}</text>',
        f'<rect x="{x}" y="{y}" width="{width}" height="20" rx="10" fill="#21262d"/>',
    ]
    if fill:
        out.append(f'<rect x="{x}" y="{y}" width="{_f(fill)}" height="20" rx="10" fill="url(#{gradient})"/>')
    return out


def render_svg(items, weeks):
    rows = len(items)
    done = sum(r["done"] for r in items.values())
    hours = sum(r["hours"] for r in items.values())
    hours_done = sum(r["hours"] for r in items.values() if r["done"])
    code = [r for r in items.values() if r["track"] == "S"]
    der = [r for r in items.values() if r["track"] == "D"]
    frac = done / rows if rows else 0
    pct = round(100 * frac)
    summary = f"Project 84 progress: {done} of {rows} rows done, {pct} percent"

    cx, cy, r = 130, 175, 64
    circ = 2 * math.pi * r
    g = [
        f'<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}" role="img" aria-label="{summary}">',
        f"<title>{summary}</title>",
        "<defs>",
        '<linearGradient id="bg" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="#161b22"/><stop offset="1" stop-color="#0d1117"/></linearGradient>',
        '<linearGradient id="ring" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="#f368e0"/><stop offset="0.5" stop-color="#54a0ff"/><stop offset="1" stop-color="#1dd1a1"/></linearGradient>',
        '<linearGradient id="code" x1="0" y1="0" x2="1" y2="0"><stop offset="0" stop-color="#54a0ff"/><stop offset="1" stop-color="#1dd1a1"/></linearGradient>',
        '<linearGradient id="der" x1="0" y1="0" x2="1" y2="0"><stop offset="0" stop-color="#f368e0"/><stop offset="1" stop-color="#ff9f43"/></linearGradient>',
        '<linearGradient id="hrs" x1="0" y1="0" x2="1" y2="0"><stop offset="0" stop-color="#feca57"/><stop offset="1" stop-color="#ff6b6b"/></linearGradient>',
        "</defs>",
        f'<rect width="{W}" height="{H}" rx="18" fill="url(#bg)"/>',
        f'<g font-family="{FONT}">',
        '<text x="32" y="46" fill="#e6edf3" font-size="24" font-weight="700">Project 84 · progress</text>',
        f'<text x="32" y="70" fill="#8b949e" font-size="14">{done} of {rows} rows done · {hours_done:g} of {hours:g} planned hours</text>',
        f'<circle cx="{cx}" cy="{cy}" r="{r}" fill="none" stroke="#21262d" stroke-width="24"/>',
    ]
    if frac > 0:
        arc = max(frac * circ, 1)
        g.append(
            f'<circle cx="{cx}" cy="{cy}" r="{r}" fill="none" stroke="url(#ring)" stroke-width="24" stroke-linecap="round" '
            f'stroke-dasharray="{_f(arc)} {_f(circ)}" transform="rotate(-90 {cx} {cy})"/>'
        )
    g += [
        f'<text x="{cx}" y="{cy + 8}" fill="#e6edf3" font-size="26" font-weight="700" text-anchor="middle">{pct}%</text>',
        f'<text x="{cx}" y="{cy + 28}" fill="#8b949e" font-size="12" text-anchor="middle">rows done</text>',
    ]
    bx, bw = 270, 530
    g += _bar(bx, 120, bw, sum(r["done"] for r in code) / len(code) if code else 0, "code", "Code problems",
              f"{sum(r['done'] for r in code)} / {len(code)}")
    g += _bar(bx, 175, bw, sum(r["done"] for r in der) / len(der) if der else 0, "der", "Derivations",
              f"{sum(r['done'] for r in der)} / {len(der)}")
    g += _bar(bx, 230, bw, hours_done / hours if hours else 0, "hrs", "Planned hours covered", f"{hours_done:g} / {hours:g} h")

    g.append('<text x="32" y="283" fill="#8b949e" font-size="13">Plan by week · column height is planned hours, bright part is done, colour is the sprint</text>')
    base, top = 372, 296
    slot = (W - 64) / max(len(weeks), 1)
    bar_w = min(30, slot - 8)
    tallest = max((sum(items[i]["hours"] for i in w["ids"]) for w in weeks), default=1) or 1
    for k, w in enumerate(weeks):
        total = sum(items[i]["hours"] for i in w["ids"])
        got = sum(items[i]["hours"] for i in w["ids"] if items[i]["done"])
        h = (base - top) * total / tallest
        x = 32 + k * slot + (slot - bar_w) / 2
        color = SPRINT_COLORS[(int(w["sprint"]) - 1) % len(SPRINT_COLORS)]
        g.append(f'<rect x="{_f(x)}" y="{_f(base - h)}" width="{_f(bar_w)}" height="{_f(h)}" rx="5" fill="{color}" fill-opacity="0.25"/>')
        if got:
            hh = max(h * got / total, 5)
            g.append(f'<rect x="{_f(x)}" y="{_f(base - hh)}" width="{_f(bar_w)}" height="{_f(hh)}" rx="5" fill="{color}"/>')
        g.append(f'<text x="{_f(x + bar_w / 2)}" y="{base + 18}" fill="#8b949e" font-size="11" text-anchor="middle">{w["n"]}</text>')
    g += ["</g>", "</svg>"]
    return "\n".join(g) + "\n"
