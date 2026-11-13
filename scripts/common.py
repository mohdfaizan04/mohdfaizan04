"""Helpers shared by every theme: README heading, contribution heatmap, snippet writer."""
from html import escape as esc
from profile_data import *

NAME = CFG.get("name") or user.get("name") or USER
HEAD = f'<h1 align="center">{esc(NAME)}</h1>\n<p align="center"><b>{esc(CFG.get("headline") or TAGLINE)}</b></p>\n\n'


def heat(x, y, colors, size=10, gap=3, rx=2, stroke=None):
    """One <rect> per day, laid out like GitHub's calendar. colors = 5 fills for levels 0..4."""
    s = f' stroke="{stroke}" stroke-width="0.8"' if stroke else ""
    return "".join(f'<rect x="{x + c[1] * (size + gap)}" y="{y + c[0] * (size + gap)}" width="{size}" height="{size}" rx="{rx}" fill="{colors[c[3]]}"{s}><title>{c[2]}: {c[4]}</title></rect>' for c in days)


def snippet(root, theme):
    (root / "snippet.md").write_text(HEAD + f'''<p align="center">
  <a href="https://github.com/{esc(USER)}"><img src="./themes/{theme}/assets/dashboard.svg" alt="{esc(USER)} · {esc(TAGLINE)} · {total} contributions" width="100%" /></a>
</p>
''', encoding="utf-8")


def langs_top(n=4):
    return [(k, v / lang_total * 100) for k, v in lang_rows[:n]] if lang_total else []
