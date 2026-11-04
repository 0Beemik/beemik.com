"""Generate the Beemik logo SVGs: regular octagon with a capital B, plus wordmarks and app icons."""
import math
import sys
from pathlib import Path

from fontTools.pens.boundsPen import BoundsPen
from fontTools.pens.svgPathPen import SVGPathPen
from fontTools.pens.transformPen import TransformPen
from fontTools.ttLib import TTFont

FONTS = Path(sys.argv[1])
OUT = Path(sys.argv[2])

INK, WHITE, HONEY, GRAY = '#1d1d1f', '#ffffff', '#f5a524', '#6e6e73'


def outline(font_path, text, height, x0=0.0, baseline=0.0, tracking=0.0):
    """Text as SVG path data, scaled so cap height == height, starting at x0 on baseline."""
    font = TTFont(font_path)
    gs = font.getGlyphSet()
    cmap = font.getBestCmap()
    cap = font['OS/2'].sCapHeight
    s = height / cap
    x = x0
    d = []
    for ch in text:
        g = cmap[ord(ch)]
        pen = SVGPathPen(gs)
        gs[g].draw(TransformPen(pen, (s, 0, 0, -s, x, baseline)))
        d.append(pen.getCommands())
        x += gs[g].width * s + tracking
    return ' '.join(d), x - tracking


def glyph_bounds(font_path, ch):
    font = TTFont(font_path)
    gs = font.getGlyphSet()
    bp = BoundsPen(gs)
    gs[font.getBestCmap()[ord(ch)]].draw(bp)
    return bp.bounds, font['OS/2'].sCapHeight


# Regular octagon, flat top, centered in a 100x100 box. Apothem 46 + 2 of rounded stroke = 48.
APOTHEM = 46
R = APOTHEM / math.cos(math.radians(22.5))
pts = [(50 + R * math.cos(math.radians(22.5 + 45 * i)), 50 + R * math.sin(math.radians(22.5 + 45 * i))) for i in range(8)]
OCT = 'M' + ' L'.join(f'{x:.3f} {y:.3f}' for x, y in pts) + ' Z'

# Capital B, cap height 44, optically centered.
XB = FONTS / 'InterTight-ExtraBold.ttf'
(bx0, by0, bx1, by1), cap = glyph_bounds(XB, 'B')
B_H = 44
sc = B_H / cap
b_w = (bx1 - bx0) * sc
B_X = 50 - b_w / 2 - bx0 * sc + 1.0  # +1: the bowls make B look left-heavy
B_BASE = 50 + B_H / 2
B_PATH, _ = outline(XB, 'B', B_H, B_X, B_BASE)


def mark_svg(shape, letter, size=None, knockout=False):
    w = f' width="{size}" height="{size}"' if size else ''
    if knockout:
        return f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 100 100"{w}>
  <mask id="k"><rect width="100" height="100" fill="#fff"/><path d="{B_PATH}" fill="#000"/></mask>
  <path d="{OCT}" fill="{shape}" stroke="{shape}" stroke-width="4" stroke-linejoin="round" mask="url(#k)"/>
</svg>
'''
    return f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 100 100"{w}>
  <path d="{OCT}" fill="{shape}" stroke="{shape}" stroke-width="4" stroke-linejoin="round"/>
  <path d="{B_PATH}" fill="{letter}"/>
</svg>
'''


def mark_group(shape, letter, tx, ty, scale):
    return (f'<g transform="translate({tx:.2f} {ty:.2f}) scale({scale})">'
            f'<path d="{OCT}" fill="{shape}" stroke="{shape}" stroke-width="4" stroke-linejoin="round"/>'
            f'<path d="{B_PATH}" fill="{letter}"/></g>')


def wordmark_svg(shape, letter, text_color):
    # Horizontal: mark (height 100) + "beemik", x-height balanced against the mark.
    bold = FONTS / 'InterTight-Bold.ttf'
    text_cap = 58
    d, end = outline(bold, 'beemik', text_cap, 128, 50 + text_cap * 0.5, tracking=-2.2)
    width = math.ceil(end + 4)
    return f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {width} 100">
  {mark_group(shape, letter, 0, 0, 1)}
  <path d="{d}" fill="{text_color}"/>
</svg>
'''


def wordmark_stacked_svg(shape, letter, text_color):
    bold = FONTS / 'InterTight-Bold.ttf'
    text_cap = 40
    d, end = outline(bold, 'beemik', text_cap, 0, 0, tracking=-1.5)
    tx = (240 - end) / 2
    d, _ = outline(bold, 'beemik', text_cap, tx, 176, tracking=-1.5)
    return f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 240 190">
  {mark_group(shape, letter, 70, 0, 1)}
  <path d="{d}" fill="{text_color}"/>
</svg>
'''


def app_icon_svg(bg, shape, letter, scale=0.62):
    """Full-bleed square for app stores (no transparency); the mark sits in the middle."""
    off = 50 * (1 - scale) * 10.24
    return f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1024 1024">
  <rect width="1024" height="1024" fill="{bg}"/>
  {mark_group(shape, letter, off, off, 10.24 * scale)}
</svg>
'''


svg = OUT / 'svg'
svg.mkdir(parents=True, exist_ok=True)
files = {
    'beemik-mark-black.svg': mark_svg(INK, WHITE),
    'beemik-mark-white.svg': mark_svg(WHITE, INK),
    'beemik-mark-honey.svg': mark_svg(HONEY, INK),
    'beemik-mark-mono-black.svg': mark_svg(INK, None, knockout=True),
    'beemik-mark-mono-white.svg': mark_svg(WHITE, None, knockout=True),
    'beemik-wordmark-black.svg': wordmark_svg(INK, WHITE, INK),
    'beemik-wordmark-white.svg': wordmark_svg(WHITE, INK, WHITE),
    'beemik-wordmark-stacked-black.svg': wordmark_stacked_svg(INK, WHITE, INK),
    'beemik-wordmark-stacked-white.svg': wordmark_stacked_svg(WHITE, INK, WHITE),
    'beemik-appicon-light.svg': app_icon_svg(WHITE, INK, WHITE),
    'beemik-appicon-dark.svg': app_icon_svg(INK, WHITE, INK),
    'beemik-appicon-honey.svg': app_icon_svg(HONEY, INK, WHITE),
}
for name, body in files.items():
    (svg / name).write_text(body)
# Raw paths for reuse (site component, 3D render)
(OUT / 'paths.txt').write_text(f'OCT={OCT}\nB={B_PATH}\n')
print('\n'.join(files))
