"""Arcade theme: player stats, XP bar toward next rank, heat-block grid."""
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[2] / "scripts"))
from common import *

ROOT = Path(__file__).resolve().parent
MONO, PINK, CY, YL = "'Courier New',Consolas,monospace", "#ff2e97", "#00f0ff", "#ffe600"
lo, hi = RANKS[rank_i][0], (RANKS[rank_i + 1][0] if rank_i + 1 < len(RANKS) else max(total, 1))
xp = min(1, (total - lo) / max(hi - lo, 1))
svg = f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 760 400" width="760" height="400" role="img" aria-label="Arcade card for {esc(USER)}: level {rank_i + 1}, {total} XP">
<rect width="760" height="400" rx="6" fill="#1a0b2e" stroke="{PINK}" stroke-width="3"/><rect x="8" y="8" width="744" height="384" fill="none" stroke="{CY}" stroke-dasharray="6 4"/>
<g font-family="{MONO}" font-weight="700"><text x="32" y="52" font-size="12" fill="{CY}" letter-spacing="4">PLAYER ONE</text>
<text x="32" y="86" font-size="28" fill="{YL}">{esc(USER).upper()}</text><text x="32" y="108" font-size="12" fill="{PINK}">{esc(TAGLINE).upper()}</text>
<text x="728" y="52" font-size="12" fill="{CY}" text-anchor="end">LV {rank_i + 1} · {esc(rank_name).upper()}</text>
<text x="32" y="148" font-size="11" fill="#fff">XP {total:,} / {hi:,}</text><rect x="32" y="156" width="696" height="14" fill="none" stroke="{CY}"/><rect x="34" y="158" width="{692 * xp:.0f}" height="10" fill="{PINK}"/>
<text x="32" y="204" font-size="13" fill="#fff">COMBO <tspan fill="{YL}">{streak}</tspan>   BEST <tspan fill="{YL}">{longest}</tspan>   DAYS <tspan fill="{YL}">{active}</tspan>   REPOS <tspan fill="{YL}">{len(repos)}</tspan></text></g>
{heat(32, 222, ["#2a1647", "#5b2a86", "#9b3fd1", PINK, YL], rx=0)}
<text x="32" y="388" font-family="{MONO}" font-size="10" fill="{CY}">INSERT COIN TO CONTINUE · UPDATED {now:%b} {now.day}</text></svg>'''
(ROOT / "assets").mkdir(exist_ok=True)
(ROOT / "assets" / "dashboard.svg").write_text(svg, encoding="utf-8")
snippet(ROOT, "arcade")
print("arcade ok")
