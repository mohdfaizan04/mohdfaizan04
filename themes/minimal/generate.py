"""Minimal light theme: white card, stats row, heatmap, language bar."""
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[2] / "scripts"))
from common import *

ROOT = Path(__file__).resolve().parent
SANS, INK, DIM = "'Segoe UI',Inter,system-ui,sans-serif", "#1f2328", "#656d76"
stats = [("Contributions", f"{total:,}"), ("Active days", active), ("Current streak", streak), ("Longest streak", longest), ("Repos", len(repos))]
tiles = "".join(f'<text x="{32 + i * 140}" y="112" font-size="26" font-weight="700" fill="{INK}">{v}</text><text x="{32 + i * 140}" y="132" font-size="11" fill="{DIM}">{k}</text>' for i, (k, v) in enumerate(stats))
cols, x, seg = ["#2da44e", "#4ac26b", "#7ee2a8", "#6e7781", "#8c959f"], 32, ""
for i, (n, p) in enumerate(langs_top(5)):
    w = 696 * p / 100
    seg += f'<rect x="{x:.1f}" y="352" width="{w:.1f}" height="8" fill="{cols[i]}"/><text x="{x:.1f}" y="378" font-size="11" fill="{DIM}">{esc(n)} {p:.0f}%</text>'
    x += w
seg = seg or f'<text x="32" y="368" font-size="12" fill="{DIM}">no public code yet</text>'
svg = f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 760 400" width="760" height="400" role="img" aria-label="Minimal card for {esc(USER)}: {total} contributions">
<rect x=".5" y=".5" width="759" height="399" rx="12" fill="#fff" stroke="#d0d7de"/>
<g font-family="{SANS}"><text x="32" y="48" font-size="20" font-weight="700" fill="{INK}">{esc(NAME)}</text><text x="32" y="68" font-size="13" fill="{DIM}">@{esc(USER)} · {esc(TAGLINE)}</text>
<text x="728" y="48" font-size="11" fill="{DIM}" text-anchor="end">updated {now:%b} {now.day}, {now.year}</text>{tiles}
<text x="32" y="168" font-size="11" fill="{DIM}">LAST 12 MONTHS</text>{heat(32, 178, ["#ebedf0", "#9be9a8", "#40c463", "#30a14e", "#216e39"])}
<text x="32" y="340" font-size="11" fill="{DIM}">LANGUAGES</text>{seg}</g></svg>'''
(ROOT / "assets").mkdir(exist_ok=True)
(ROOT / "assets" / "dashboard.svg").write_text(svg, encoding="utf-8")
snippet(ROOT, "minimal")
print("minimal ok")
