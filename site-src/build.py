#!/usr/bin/env python3
"""Build the Marrow Notes static site from content.py."""
import html
import os
import re
import shutil
from content import SITE, PAGES, HEROES, IMAGE_CREDIT

OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "site")
OUT = os.path.normpath(OUT)

TIERS = {
    "t1": ("Official", "Stated by Cold Symmetry, Playstack, or a platform store listing"),
    "t2": ("Tested", "Reported by a guide site working from the retail build"),
    "t3": ("Unconfirmed", "Single source, or a claim we could not cross-check"),
    "ugc": ("Players", "Community reports — treated as leads, not facts"),
}

CSS = """
:root{
  --ink:#0F1417; --stone:#171E22; --raise:#1D262B; --line:#2A3439;
  --ash:#B4BDBA; --bone:#E9EDE7; --slate:#7C8A8D;
  --verdigris:#6FA894; --ochre:#C99A4B; --steel:#84A3B8;
  --sans:"Helvetica Neue",Inter,Arial,system-ui,sans-serif;
  --serif:"Iowan Old Style","Palatino Linotype",Palatino,Georgia,serif;
  --wrap:1120px;
}
*{box-sizing:border-box}
html{-webkit-text-size-adjust:100%}
body{
  margin:0;background:var(--ink);color:var(--ash);
  font-family:var(--serif);font-size:17px;line-height:1.75;
  overflow-wrap:break-word;
}
a{color:var(--verdigris);text-decoration:none;border-bottom:1px solid rgba(111,168,148,.35)}
a:hover{border-bottom-color:var(--verdigris)}
a:focus-visible{outline:2px solid var(--verdigris);outline-offset:3px;border-radius:2px}
img{max-width:100%}

.skip{position:absolute;left:-9999px}
.skip:focus{left:12px;top:12px;background:var(--raise);color:var(--bone);padding:8px 14px;z-index:20;border-radius:4px}

.bar{border-bottom:1px solid var(--line);background:var(--ink);position:sticky;top:0;z-index:10}
.bar-in{max-width:var(--wrap);margin:0 auto;padding:14px 22px;display:flex;flex-wrap:wrap;gap:14px 26px;align-items:baseline}
.brand{font-family:var(--sans);font-weight:600;letter-spacing:.16em;text-transform:uppercase;font-size:13px;color:var(--bone);border:0}
.brand span{color:var(--verdigris)}
.nav{display:flex;gap:20px;font-family:var(--sans);font-size:13px;letter-spacing:.06em}
.nav a{color:var(--slate);border:0}
.nav a:hover,.nav a[aria-current]{color:var(--bone)}

.wrap{max-width:var(--wrap);margin:0 auto;padding:0 22px}
.cols{display:grid;grid-template-columns:1fr;gap:36px;padding:34px 0 72px}
@media(min-width:960px){.cols{grid-template-columns:minmax(0,1fr) 230px;gap:56px}}

main{min-width:0;max-width:70ch}
.crumb{font-family:var(--sans);font-size:12px;letter-spacing:.08em;color:var(--slate);margin:0 0 20px}
.crumb a{color:var(--slate);border:0}
.crumb a:hover{color:var(--ash)}
.eyebrow{font-family:var(--sans);font-size:11px;font-weight:600;letter-spacing:.22em;text-transform:uppercase;color:var(--verdigris);margin:0 0 12px}
h1{font-family:var(--sans);font-weight:600;font-size:2.05rem;line-height:1.15;letter-spacing:-.02em;color:var(--bone);margin:0 0 18px}
.lede{font-size:1.14rem;line-height:1.7;color:#CBD3D0;margin:0 0 8px;border-left:2px solid var(--verdigris);padding-left:18px}
.hero{margin:26px 0 30px}
.hero img{display:block;width:100%;height:auto;border:1px solid var(--line);background:var(--stone)}
.hero figcaption{font-family:var(--sans);font-size:12.5px;line-height:1.6;color:var(--slate);margin-top:9px}
.hero .credit{display:block;font-size:11px;letter-spacing:.1em;text-transform:uppercase;color:#5A666A;margin-top:3px}
h2{font-family:var(--sans);font-weight:600;font-size:1.28rem;letter-spacing:-.01em;color:var(--bone);margin:46px 0 14px;padding-top:14px;border-top:1px solid var(--line)}
h3{font-family:var(--sans);font-weight:600;font-size:1.02rem;color:var(--bone);margin:28px 0 8px}
p{margin:0 0 18px}
ul,ol{margin:0 0 18px;padding-left:22px}
li{margin:0 0 9px}
strong{color:var(--bone);font-weight:600}
code{font-family:ui-monospace,SFMono-Regular,Menlo,monospace;font-size:.88em;background:var(--raise);padding:2px 6px;border-radius:3px;color:#D6DEDA}

.tw{overflow-x:auto;margin:0 0 22px;border:1px solid var(--line);border-radius:6px}
table{border-collapse:collapse;width:100%;font-family:var(--sans);font-size:14px;line-height:1.55}
th,td{text-align:left;padding:11px 14px;border-bottom:1px solid var(--line);vertical-align:top}
th{color:var(--bone);font-weight:600;letter-spacing:.03em;background:var(--stone);white-space:nowrap}
tr:last-child td{border-bottom:0}

.mk{font-family:var(--sans);font-size:10px;font-weight:600;letter-spacing:.1em;text-transform:uppercase;
  padding:2px 6px;border-radius:3px;margin-left:5px;white-space:nowrap;vertical-align:2px;border:1px solid}
.mk-t1{color:#8FCBB4;border-color:rgba(143,203,180,.4);background:rgba(143,203,180,.09)}
.mk-t2{color:#9CBBD0;border-color:rgba(156,187,208,.4);background:rgba(156,187,208,.09)}
.mk-t3{color:#98A6A9;border-color:rgba(152,166,169,.4);background:rgba(152,166,169,.09)}
.mk-ugc{color:#B6A9C9;border-color:rgba(182,169,201,.4);background:rgba(182,169,201,.09)}

.call{border-left:3px solid var(--ochre);background:var(--stone);padding:16px 20px;margin:0 0 22px;border-radius:0 6px 6px 0}
.call .lab{display:block;font-family:var(--sans);font-size:11px;font-weight:600;letter-spacing:.18em;text-transform:uppercase;color:var(--ochre);margin-bottom:7px}
.call p{margin:0;font-size:.97rem}
.call-unconfirmed{border-left-color:var(--slate)}
.call-unconfirmed .lab{color:var(--slate)}

.src{margin:56px 0 0;border-top:1px solid var(--line);padding-top:24px}
.src h2{border:0;margin:0 0 6px;padding:0;font-size:1.1rem}
.src .hint{font-family:var(--sans);font-size:13px;color:var(--slate);margin:0 0 18px}
.src ol{list-style:none;padding:0;margin:0}
.src li{border-left:2px solid var(--line);padding:0 0 0 16px;margin:0 0 16px}
.src li.s-t1{border-left-color:#8FCBB4}
.src li.s-t2{border-left-color:#9CBBD0}
.src li.s-t3{border-left-color:#98A6A9}
.src li.s-ugc{border-left-color:#B6A9C9}
.src .nm{display:block;font-family:var(--sans);font-size:14px;font-weight:600;color:var(--bone)}
.src .wh{display:block;font-size:.95rem;color:var(--slate);line-height:1.6}

.toc{font-family:var(--sans);font-size:13px;line-height:1.5}
@media(min-width:960px){.toc{position:sticky;top:78px;align-self:start}}
.toc-t{font-size:11px;font-weight:600;letter-spacing:.18em;text-transform:uppercase;color:var(--slate);border:0;margin:0 0 12px;padding:0}
.toc ul{list-style:none;margin:0;padding:0}
.toc li{margin:0 0 10px}
.toc a{color:var(--slate);border:0;display:block}
.toc a:hover{color:var(--bone)}

.cards{list-style:none;padding:0;margin:0 0 22px}
.cards li{margin:0 0 12px}
.cards a{display:block;background:var(--stone);border:1px solid var(--line);border-left:3px solid var(--verdigris);
  border-radius:0 6px 6px 0;padding:15px 18px;color:var(--bone);font-family:var(--sans);font-size:15px;font-weight:600}
.cards a:hover{background:var(--raise)}
.cards .sub{display:block;font-family:var(--serif);font-weight:400;font-size:15px;color:var(--slate);margin-top:4px;line-height:1.6}

footer{border-top:1px solid var(--line);margin-top:0}
.foot{max-width:var(--wrap);margin:0 auto;padding:28px 22px 56px;font-family:var(--sans);font-size:13px;color:var(--slate);
  display:flex;flex-wrap:wrap;gap:10px 28px;justify-content:space-between}
.foot a{color:var(--slate)}

@media(max-width:600px){
  body{font-size:16px}
  h1{font-size:1.62rem}
  .lede{font-size:1.05rem;padding-left:14px}
  h2{font-size:1.16rem;margin-top:38px}
  .bar-in{padding:12px 18px;gap:10px 18px}
  .nav{gap:14px;font-size:12px;flex-wrap:wrap}
  .wrap{padding:0 18px}
  .cols{padding:26px 0 48px}
  .mk{margin-left:4px}
}
@media(prefers-reduced-motion:reduce){*{animation:none!important;transition:none!important}}
"""

# ---------------------------------------------------------------- mini markdown
def inline(t):
    t = html.escape(t)
    t = re.sub(r"\[\[(.+?)\|(.+?)\]\]", r'<a href="\2">\1</a>', t)
    t = re.sub(r"\*\*(.+?)\*\*", r"<strong>\1</strong>", t)
    t = re.sub(r"`(.+?)`", r"<code>\1</code>", t)
    def mark(m):
        k = m.group(1)
        lab, why = TIERS[k]
        return f'<span class="mk mk-{k}" title="{html.escape(why)}">{lab}</span>'
    return re.sub(r"\{\{(t1|t2|t3|ugc)\}\}", mark, t)


def slugify(s):
    s = re.sub(r"<[^>]+>", "", s)
    return re.sub(r"[^a-z0-9]+", "-", s.lower()).strip("-")


def render(md):
    out, toc = [], []
    lines = md.strip("\n").split("\n")
    i, para, ul, tbl = 0, [], [], []

    def flush_para():
        if para:
            out.append("<p>" + inline(" ".join(para)) + "</p>")
            para.clear()

    def flush_ul():
        if ul:
            out.append("<ul>" + "".join(f"<li>{inline(x)}</li>" for x in ul) + "</ul>")
            ul.clear()

    def flush_tbl():
        if tbl:
            head, *rest = tbl
            th = "".join(f"<th>{inline(c)}</th>" for c in head)
            body = "".join("<tr>" + "".join(f"<td>{inline(c)}</td>" for c in r) + "</tr>" for r in rest)
            out.append(f'<div class="tw"><table><thead><tr>{th}</tr></thead><tbody>{body}</tbody></table></div>')
            tbl.clear()

    def flush_all():
        flush_para(); flush_ul(); flush_tbl()

    while i < len(lines):
        ln = lines[i].rstrip()
        if not ln.strip():
            flush_all()
        elif ln.startswith("## "):
            flush_all()
            txt = ln[3:].strip()
            sid = slugify(txt)
            toc.append((sid, txt))
            out.append(f'<h2 id="{sid}">{inline(txt)}</h2>')
        elif ln.startswith("### "):
            flush_all()
            out.append(f"<h3>{inline(ln[4:].strip())}</h3>")
        elif ln.startswith("!!"):
            flush_all()
            lab, _, txt = ln[2:].partition("|")
            cls = "call-unconfirmed" if lab.strip().lower() == "unconfirmed" else ""
            out.append(f'<aside class="call {cls}"><span class="lab">{html.escape(lab.strip())}</span>'
                       f"<p>{inline(txt.strip())}</p></aside>")
        elif ln.startswith("- "):
            flush_para(); flush_tbl()
            ul.append(ln[2:].strip())
        elif ln.startswith("|"):
            flush_para(); flush_ul()
            tbl.append([c.strip() for c in ln.strip("|").split("|")])
        else:
            flush_ul(); flush_tbl()
            para.append(ln.strip())
        i += 1
    flush_all()
    return "\n".join(out), toc


# ---------------------------------------------------------------- page shell
NAV = [("/bosses/index.html", "Bosses"), ("/shells/index.html", "Shells"), ("/systems/index.html", "Systems")]


def url_for(slug):
    return "/" + slug + ".html"


def depth_prefix(slug):
    return "../" * slug.count("/")


def og_url(slug):
    """Absolute — social scrapers do not resolve relative image paths.

    Cards live in static/og/ and are made by make_og.py, not by this build.
    """
    return SITE["base"] + "/og/" + slug.replace("/", "-") + ".jpg"


def localize(h, slug):
    """Rewrite root-absolute links to relative so file:// browsing works."""
    pre = depth_prefix(slug)
    return re.sub(r'(href|src)="/([^"]*)"', lambda m: f'{m.group(1)}="{pre}{m.group(2)}"', h)


def hero_block(slug):
    """Publisher screenshot under the lede. Caption carries the credit, the
    same way every factual claim on this site carries its source."""
    if slug not in HEROES:
        return ""
    name, caption = HEROES[slug]
    return (
        f'<figure class="hero">'
        f'<img src="/shots/{name}.jpg" width="1400" height="788" '
        f'alt="{html.escape(caption)}" loading="lazy" decoding="async">'
        f'<figcaption>{html.escape(caption)} '
        f'<span class="credit">{html.escape(IMAGE_CREDIT)}</span></figcaption>'
        f"</figure>"
    )


def sources_block(srcs):
    if not srcs:
        return ""
    items = "".join(
        f'<li class="s-{t}"><span class="nm">{html.escape(n)} '
        f'<span class="mk mk-{t}" title="{html.escape(TIERS[t][1])}">{TIERS[t][0]}</span></span>'
        f'<span class="wh">{html.escape(w)}</span></li>'
        for t, n, w in srcs
    )
    return ('<section class="src"><h2 id="where-this-comes-from">Where this comes from</h2>'
            '<p class="hint">Every claim above carries a marker. These are the sources behind them, '
            'graded by how directly they touch the retail build.</p>'
            f"<ol>{items}</ol></section>")


def build_page(p):
    slug = p["slug"]
    body, toc = render(p["body"])
    canonical = SITE["base"] + ("/" if slug == "index" else url_for(slug))

    crumb = ""
    if slug != "index":
        parts = ['<a href="/index.html">Home</a>']
        if "/" in slug:
            sec = slug.split("/")[0]
            label = dict((u.strip("/").split("/")[0], n) for u, n in NAV).get(sec, sec.title())
            if not slug.endswith("/index"):
                parts.append(f'<a href="/{sec}/index.html">{label}</a>')
            else:
                parts.append(label)
        if not slug.endswith("index"):
            parts.append(html.escape(p["h1"]))
        crumb = '<nav class="crumb" aria-label="Breadcrumb">' + " &rsaquo; ".join(parts) + "</nav>"

    toc_html = ""
    if toc and p["kind"] != "home":
        li = "".join(f'<li><a href="#{i}">{html.escape(t)}</a></li>' for i, t in toc)
        if p.get("sources"):
            li += '<li><a href="#where-this-comes-from">Where this comes from</a></li>'
        toc_html = f'<nav class="toc" aria-label="On this page"><p class="toc-t">On this page</p><ul>{li}</ul></nav>'

    nav = "".join(
        f'<a href="{u}"{" aria-current=\"page\"" if slug.startswith(u.strip("/").split("/")[0]) else ""}>{n}</a>'
        for u, n in NAV
    )

    ld = ('{"@context":"https://schema.org","@type":"%s","headline":%s,"description":%s,'
          '"inLanguage":"en","dateModified":"2026-08-24","publisher":{"@type":"Organization","name":"Marrow Notes"}}'
          % ("WebSite" if slug == "index" else "Article",
             '"' + p["h1"].replace('"', "") + '"', '"' + p["desc"].replace('"', "") + '"'))

    doc = f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{html.escape(p['title'])}</title>
<meta name="description" content="{html.escape(p['desc'])}">
<link rel="canonical" href="{canonical}">
<meta name="robots" content="index, follow">
<meta property="og:type" content="{'website' if slug == 'index' else 'article'}">
<meta property="og:title" content="{html.escape(p['title'])}">
<meta property="og:description" content="{html.escape(p['desc'])}">
<meta property="og:url" content="{canonical}">
<meta property="og:site_name" content="{SITE['name']}">
<meta property="og:image" content="{og_url(slug)}">
<meta property="og:image:type" content="image/jpeg">
<meta property="og:image:width" content="1200">
<meta property="og:image:height" content="630">
<meta property="og:image:alt" content="{html.escape(p['h1'])} — {SITE['name']}">
<meta name="twitter:card" content="summary_large_image">
<meta name="twitter:title" content="{html.escape(p['title'])}">
<meta name="twitter:description" content="{html.escape(p['desc'])}">
<meta name="twitter:image" content="{og_url(slug)}">
<script type="application/ld+json">{ld}</script>
<link rel="stylesheet" href="/assets/site.css">
<link rel="icon" href="/assets/favicon.svg" type="image/svg+xml">
<link rel="apple-touch-icon" href="/assets/apple-touch-icon.png">
</head>
<body>
<a class="skip" href="#main">Skip to content</a>
<header class="bar"><div class="bar-in">
  <a class="brand" href="/index.html">Marrow<span>&#183;</span>Notes</a>
  <nav class="nav" aria-label="Main">{nav}</nav>
</div></header>

<div class="wrap"><div class="cols">
<main id="main">
{crumb}
<p class="eyebrow">{html.escape(p['eyebrow'])}</p>
<h1>{html.escape(p['h1'])}</h1>
<p class="lede">{html.escape(p['lede'])}</p>
{hero_block(slug)}
{body}
{sources_block(p.get('sources'))}
</main>
{toc_html}
</div></div>

<footer><div class="foot">
  <span>{SITE['name']} &mdash; {SITE['tagline']}</span>
  <span>Checked {SITE['updated']}. Unofficial fan guide, not affiliated with Cold Symmetry or Playstack.</span>
</div></footer>
</body>
</html>
"""
    return localize(doc, slug)


def main():
    if os.path.isdir(OUT):
        shutil.rmtree(OUT)
    os.makedirs(os.path.join(OUT, "assets"), exist_ok=True)
    with open(os.path.join(OUT, "assets", "site.css"), "w") as f:
        f.write(CSS.strip() + "\n")

    # og cards and icons, pre-rendered by make_og.py — copied, never regenerated
    # here, so CI does not need a renderer.
    static = os.path.join(os.path.dirname(os.path.abspath(__file__)), "static")
    if os.path.isdir(static):
        shutil.copytree(static, OUT, dirs_exist_ok=True)
        n = sum(len(fs) for _, _, fs in os.walk(static))
        print(f"copied {n} static files")
    else:
        print("WARNING: site-src/static/ missing — run make_og.py (og images, favicon)")

    for p in PAGES:
        path = os.path.join(OUT, p["slug"] + ".html")
        os.makedirs(os.path.dirname(path), exist_ok=True)
        with open(path, "w") as f:
            f.write(build_page(p))
        print("built", p["slug"] + ".html")

    urls = "".join(
        f"<url><loc>{SITE['base']}{'/' if p['slug'] == 'index' else url_for(p['slug'])}</loc>"
        f"<lastmod>2026-08-24</lastmod></url>\n"
        for p in PAGES
    )
    with open(os.path.join(OUT, "sitemap.xml"), "w") as f:
        f.write('<?xml version="1.0" encoding="UTF-8"?>\n'
                '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n' + urls + "</urlset>\n")
    with open(os.path.join(OUT, "robots.txt"), "w") as f:
        f.write(f"User-agent: *\nAllow: /\nSitemap: {SITE['base']}/sitemap.xml\n")
    print(f"\n{len(PAGES)} pages -> {OUT}")


if __name__ == "__main__":
    main()
