"""Terminal theme: a shell window with whoami / git log / langs and a heatmap."""
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[2] / "scripts"))
from common import *

ROOT = Path(__file__).resolve().parent
G, DIM, BG, MONO = "#3fb950", "#8b949e", "#0d1117", "'JetBrains Mono','SF Mono',Consolas,monospace"
L = langs_top()
bars = "".join(f'<text x="40" y="{308 + i * 18}">{esc(n):<12}<tspan fill="{G}">{"█" * round(p / 4):<25}</tspan> {p:4.1f}%</text>' for i, (n, p) in enumerate(L))
prompt_y = 308 + 18 * max(len(L), 1) + 10
svg = f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 760 {prompt_y + 24}" width="760" height="{prompt_y + 24}" role="img" aria-label="Terminal card for {esc(USER)}: {total} contributions, {streak} day streak">
<rect width="760" height="{prompt_y + 24}" rx="10" fill="{BG}" stroke="#30363d"/><rect width="760" height="30" rx="10" fill="#161b22"/>
<circle cx="20" cy="15" r="6" fill="#ff5f56"/><circle cx="40" cy="15" r="6" fill="#ffbd2e"/><circle cx="60" cy="15" r="6" fill="{G}"/>
<text x="380" y="20" font-size="11" fill="{DIM}" text-anchor="middle" font-family="{MONO}">{esc(USER)}@github: ~</text>
<g font-family="{MONO}" font-size="13" xml:space="preserve" fill="#c9d1d9">
<text x="24" y="56"><tspan fill="{G}">$</tspan> whoami</text><text x="40" y="76">{esc(NAME)} · {esc(TAGLINE)}</text>
<text x="24" y="104"><tspan fill="{G}">$</tspan> git log --stat --since="1 year"</text>
<text x="40" y="124">contributions  <tspan fill="{G}">{total:,}</tspan>    active days  <tspan fill="{G}">{active}</tspan></text>
<text x="40" y="142">streak         <tspan fill="{G}">{streak}</tspan>    longest      <tspan fill="{G}">{longest}</tspan> ({long_range})</text>
<text x="40" y="160">repos          <tspan fill="{G}">{len(repos)}</tspan>    stars        <tspan fill="{G}">{stars}</tspan></text>
<text x="24" y="188"><tspan fill="{G}">$</tspan> heatmap --year</text></g>
{heat(40, 198, ["#161b22", "#0e4429", "#006d32", "#26a641", "#39d353"], size=9, gap=2)}
<g font-family="{MONO}" font-size="13" xml:space="preserve" fill="#c9d1d9"><text x="24" y="296"><tspan fill="{G}">$</tspan> langs</text>{bars}
<text x="24" y="{prompt_y}"><tspan fill="{G}">$</tspan> <tspan class="c">▮</tspan></text></g>
<style>.c{{animation:b 1s steps(1) infinite}}@keyframes b{{50%{{opacity:0}}}}</style></svg>'''
(ROOT / "assets").mkdir(exist_ok=True)
(ROOT / "assets" / "dashboard.svg").write_text(svg, encoding="utf-8")
snippet(ROOT, "terminal")
print("terminal ok")
