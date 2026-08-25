"""Render one og:image per page, plus the favicons, from the site's own palette.

Images land in site-src/static/ and are copied into site/ by build.py, so CI
never needs to render anything — only this script does, and only when titles
or the source mix change.

    python3 make_og.py

Uses SVG + macOS Quick Look (qlmanage) to rasterise, so it has no third-party
dependencies. Quick Look scales an SVG to a square, so each card is drawn on a
1200x1200 canvas with the real 1200x630 artboard centred, then cropped back.
"""
import base64
import os
import shutil
import subprocess
import sys
import tempfile
from xml.sax.saxutils import escape

from content import PAGES, HEROES

HERE = os.path.dirname(os.path.abspath(__file__))
STATIC = os.path.join(HERE, "static")   # mirrors the layout of site/
OG = os.path.join(STATIC, "og")
ASSETS = os.path.join(STATIC, "assets")

# straight from :root in build.py
INK, BONE, SLATE, VERDIGRIS = "#0F1417", "#E9EDE7", "#7C8A8D", "#6FA894"
SERIF = "Iowan Old Style, Palatino, Georgia, serif"
SANS = "Helvetica Neue, Arial, sans-serif"

W, H, PAD = 1200, 630, 72
TIERS = [("t1", "Official"), ("t2", "Tested"), ("t3", "Unconfirmed"), ("ugc", "Players")]


def og_name(slug):
    return slug.replace("/", "-") + ".jpg"


def backdrop(slug):
    """Pages with a hero screenshot get it behind the type, dimmed so the
    text stays legible. Pages without one keep the flat ink ground."""
    if slug not in HEROES:
        return ""
    src = os.path.join(HERE, "static", "shots", HEROES[slug][0] + ".jpg")
    if not os.path.exists(src):
        return ""
    with open(src, "rb") as f:
        b64 = base64.b64encode(f.read()).decode()
    return (
        f'<image xlink:href="data:image/jpeg;base64,{b64}" x="0" y="0" '
        f'width="{W}" height="{H}" preserveAspectRatio="xMidYMid slice"/>'
        f'<rect width="{W}" height="{H}" fill="{INK}" opacity="0.72"/>'
    )


def wrap(text, size, width):
    """Greedy wrap. Serif caps average ~0.5em per glyph at these sizes."""
    limit = max(8, int(width / (size * 0.5)))
    words, lines, line = text.split(), [], ""
    for w in words:
        cand = f"{line} {w}".strip()
        if len(cand) <= limit:
            line = cand
        else:
            if line:
                lines.append(line)
            line = w
    if line:
        lines.append(line)
    return lines


def source_mix(p):
    """The page's source breakdown — the one thing this site exists to show."""
    counts = {}
    for tier, _, _ in p.get("sources", []):
        counts[tier] = counts.get(tier, 0) + 1
    parts = [f"{counts[k]} {label.upper()}" for k, label in TIERS if counts.get(k)]
    return "  ·  ".join(parts) or "EVERY CLAIM MARKED WITH ITS SOURCE"


def card_svg(p):
    eyebrow = p.get("eyebrow") or ("Guide index" if p.get("kind") == "hub" else "Field notes")
    title = p["h1"]
    size = 56 if len(title) > 46 else 68
    lines = wrap(title, size, W - PAD * 2 - 34)
    lead = size * 1.16
    # keep the block optically centred however many lines it runs to
    top = 300 - (len(lines) - 1) * lead / 2

    rows = "".join(
        f'<text x="{PAD + 34}" y="{top + i * lead:.0f}" fill="{BONE}" '
        f'font-family="{SERIF}" font-size="{size}">{escape(ln)}</text>'
        for i, ln in enumerate(lines)
    )
    rule_top = top - size * 0.78
    rule_h = (len(lines) - 1) * lead + size * 0.98

    return f"""<svg xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink"
     width="{W}" height="{W}" viewBox="0 0 {W} {W}">
<rect width="{W}" height="{W}" fill="{INK}"/>
<g transform="translate(0,{(W - H) // 2})">
  {backdrop(p['slug'])}
  <text x="{PAD}" y="86" fill="{BONE}" font-family="{SANS}" font-size="19"
        font-weight="600" letter-spacing="4.5">MARROW·NOTES</text>
  <text x="{PAD}" y="124" fill="{VERDIGRIS}" font-family="{SANS}" font-size="16"
        font-weight="600" letter-spacing="3.2">{escape(eyebrow.upper())}</text>
  <rect x="{PAD}" y="{rule_top:.0f}" width="4" height="{rule_h:.0f}" fill="{VERDIGRIS}"/>
  {rows}
  <text x="{PAD}" y="556" fill="{SLATE}" font-family="{SANS}" font-size="15"
        font-weight="600" letter-spacing="2.1">{escape(source_mix(p))}</text>
  <text x="{W - PAD}" y="556" fill="#3F4B50" font-family="{SANS}" font-size="15"
        font-weight="600" letter-spacing="2.1" text-anchor="end">MORTAL SHELL II</text>
</g>
</svg>"""


def favicon_svg(px=None):
    """The brand mark: the M of Marrow, with the dot from Marrow·Notes."""
    size = f' width="{px}" height="{px}"' if px else ""
    return f"""<svg xmlns="http://www.w3.org/2000/svg"{size} viewBox="0 0 64 64">
<rect width="64" height="64" rx="13" fill="{INK}"/>
<text x="30" y="46" fill="{BONE}" font-family="{SERIF}" font-size="42"
      text-anchor="middle">M</text>
<circle cx="51" cy="18" r="5.5" fill="{VERDIGRIS}"/>
</svg>"""


def rasterise(svg, dst, crop=None, size=1200, scale_to=None):
    """SVG -> PNG via Quick Look, cropped back to the artboard and/or scaled down.

    Quick Look only fills its canvas at large sizes, so small icons are drawn
    big and resampled afterwards.
    """
    with tempfile.TemporaryDirectory() as tmp:
        src = os.path.join(tmp, "card.svg")
        with open(src, "w") as f:
            f.write(svg)
        subprocess.run(["qlmanage", "-t", "-s", str(size), "-o", tmp, src],
                       check=True, capture_output=True)
        raw = os.path.join(tmp, "card.svg.png")
        if not os.path.exists(raw):
            sys.exit(f"Quick Look produced no thumbnail for {dst}")
        if crop:
            subprocess.run(["sips", "-c", str(crop[1]), str(crop[0]),
                            "-s", "format", "jpeg", "-s", "formatOptions", "78",
                            raw, "--out", dst],
                           check=True, capture_output=True)
        elif scale_to:
            subprocess.run(["sips", "--resampleWidth", str(scale_to), raw, "--out", dst],
                           check=True, capture_output=True)
        else:
            shutil.copy(raw, dst)


def main():
    if sys.platform != "darwin":
        sys.exit("Needs macOS Quick Look (qlmanage) to rasterise. Commit the PNGs instead.")
    if os.path.isdir(OG):
        shutil.rmtree(OG)          # shots/ is hand-curated — never wipe it
    os.makedirs(OG, exist_ok=True)
    os.makedirs(ASSETS, exist_ok=True)

    for p in PAGES:
        dst = os.path.join(OG, og_name(p["slug"]))
        rasterise(card_svg(p), dst, crop=(W, H))
        print("og", og_name(p["slug"]))

    with open(os.path.join(ASSETS, "favicon.svg"), "w") as f:
        f.write(favicon_svg())
    rasterise(favicon_svg(1200), os.path.join(ASSETS, "apple-touch-icon.png"),
              size=1200, scale_to=180)
    print("assets/favicon.svg, assets/apple-touch-icon.png")

    print(f"\n{len(PAGES)} cards + 2 icons -> {STATIC}")


if __name__ == "__main__":
    main()
