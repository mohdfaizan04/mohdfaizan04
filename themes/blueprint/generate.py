"""Blueprint theme: blue technical drawing with annotated stats."""
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[2] / "scripts"))
from common import *

ROOT = Path(__file__).resolve().parent
MONO, LN = "'Courier New',Consolas,monospace", "#9fd0ff"
ann = [("TOTAL", f"{total:,}"), ("ACTIVE DAYS", active), ("STREAK", streak), ("LONGEST", longest), ("REPOS", len(repos)), ("STARS", stars)]
tiles = "".join(f'<g transform="translate({32 + i * 118} 100)"><rect width="106" height="54" fill="none" stroke="{LN}"/><text x="8" y="20" font-size="9" fill="{LN}">{k}</text><text x="8" y="44" font-size="22" fill="#fff">{v}</text></g>' for i, (k, v) in enumerate(ann))
lang_txt = esc(", ".join(f"{n} {p:.0f}%" for n, p in langs_top(5)) or "N/A")
svg = f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 760 400" width="760" height="400" role="img" aria-label="Blueprint card for {esc(USER)}: {total} contributions">
<defs><pattern id="g" width="20" height="20" patternUnits="userSpaceOnUse"><path d="M20 0H0V20" fill="none" stroke="#2f6fb5" stroke-width=".5"/></pattern></defs>
<rect width="760" height="400" fill="#0b3a75"/><rect width="760" height="400" fill="url(#g)"/><rect x="10" y="10" width="740" height="380" fill="none" stroke="{LN}" stroke-width="1.5"/>
<g font-family="{MONO}" fill="#fff"><text x="32" y="48" font-size="22" font-weight="700">{esc(NAME).upper()}</text><text x="32" y="70" font-size="11" fill="{LN}">DWG NO. {esc(USER).upper()} · {esc(TAGLINE).upper()}</text>
<text x="728" y="48" font-size="10" fill="{LN}" text-anchor="end">REV {now:%Y-%m-%d} · SCALE 1:1</text>{tiles}
<text x="32" y="188" font-size="10" fill="{LN}">FIG.1 — CONTRIBUTION MAP (52 WK)</text></g>
{heat(32, 196, ["none", "#2f6fb5", "#5fa2e8", LN, "#ffffff"], rx=0, stroke=LN)}
<text x="32" y="372" font-family="{MONO}" font-size="10" fill="{LN}">LANGUAGES: {lang_txt}</text></svg>'''
(ROOT / "assets").mkdir(exist_ok=True)
(ROOT / "assets" / "dashboard.svg").write_text(svg, encoding="utf-8")
snippet(ROOT, "blueprint")
print("blueprint ok")
