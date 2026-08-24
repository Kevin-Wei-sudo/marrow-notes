#!/usr/bin/env python3
"""Check the built site for the things AITDK's overview panel reports on."""
import os
import re
import sys
from html.parser import HTMLParser

SITE = os.path.normpath(os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "site"))


class Grab(HTMLParser):
    def __init__(self):
        super().__init__()
        self.title = ""
        self.desc = None
        self.canonical = None
        self.viewport = None
        self.og = 0
        self.jsonld = 0
        self.heads = []
        self.links = []
        self._t = None
        self._h = None

    def handle_starttag(self, tag, attrs):
        a = dict(attrs)
        if tag == "title":
            self._t = True
        elif tag == "meta":
            if a.get("name") == "description":
                self.desc = a.get("content", "")
            elif a.get("name") == "viewport":
                self.viewport = a.get("content", "")
            elif a.get("property", "").startswith("og:"):
                self.og += 1
        elif tag == "link" and a.get("rel") == "canonical":
            self.canonical = a.get("href")
        elif tag == "script" and a.get("type") == "application/ld+json":
            self.jsonld += 1
        elif tag in ("h1", "h2", "h3", "h4"):
            self._h = [tag, ""]
        elif tag == "a" and a.get("href"):
            self.links.append(a["href"])

    def handle_endtag(self, tag):
        if tag == "title":
            self._t = None
        elif tag in ("h1", "h2", "h3", "h4") and self._h:
            self.heads.append((self._h[0], re.sub(r"\s+", " ", self._h[1]).strip()))
            self._h = None

    def handle_data(self, d):
        if self._t:
            self.title += d
        if self._h:
            self._h[1] += d


def check(path, rel):
    g = Grab()
    raw = open(path, encoding="utf-8").read()
    g.feed(raw)
    errs, warns = [], []

    t = g.title.strip()
    if not t:
        errs.append("no <title>")
    elif len(t) > 60:
        warns.append(f"title {len(t)} chars (>60, may truncate)")
    elif len(t) < 25:
        warns.append(f"title only {len(t)} chars")

    if g.desc is None:
        errs.append("no meta description")
    elif not 110 <= len(g.desc) <= 165:
        warns.append(f"description {len(g.desc)} chars (aim 110-165)")

    h1s = [h for h in g.heads if h[0] == "h1"]
    if len(h1s) != 1:
        errs.append(f"{len(h1s)} H1 tags (need exactly 1)")

    seq = [int(t_[1]) for t_, _ in [(h[0], h[1]) for h in g.heads]]
    prev = 0
    for lvl, txt in [(int(h[0][1]), h[1]) for h in g.heads]:
        if prev and lvl > prev + 1:
            errs.append(f"heading jumps H{prev} -> H{lvl} at '{txt[:34]}'")
        prev = lvl

    if not g.canonical:
        warns.append("no canonical")
    if not g.viewport:
        errs.append("no viewport meta (mobile will break)")
    if g.og < 4:
        warns.append(f"only {g.og} og: tags")
    if not g.jsonld:
        warns.append("no JSON-LD")

    base = os.path.dirname(path)
    internal = [l for l in g.links if not l.startswith(("http", "#", "mailto"))]
    for l in internal:
        target = os.path.normpath(os.path.join(base, l.split("#")[0]))
        if not os.path.exists(target):
            errs.append(f"broken link -> {l}")

    return t, g.desc or "", len(h1s), len([h for h in g.heads if h[0] == "h2"]), len(internal), errs, warns


def main():
    pages = sorted(
        os.path.join(dp, f)
        for dp, _, fs in os.walk(SITE)
        for f in fs
        if f.endswith(".html")
    )
    if not pages:
        print("no pages found — run build.py first")
        return 1

    ne = nw = 0
    titles, descs = {}, {}
    print(f"{'page':38} {'title':>5} {'desc':>5} {'h1':>3} {'h2':>3} {'links':>5}  status")
    print("-" * 84)
    for p in pages:
        rel = os.path.relpath(p, SITE)
        t, d, h1, h2, li, errs, warns = check(p, rel)
        titles.setdefault(t, []).append(rel)
        descs.setdefault(d, []).append(rel)
        ne += len(errs)
        nw += len(warns)
        status = "OK" if not errs and not warns else ("FAIL" if errs else "warn")
        print(f"{rel:38} {len(t):>5} {len(d):>5} {h1:>3} {h2:>3} {li:>5}  {status}")
        for e in errs:
            print(f"{'':38} ! {e}")
        for w in warns:
            print(f"{'':38} - {w}")

    for label, m in (("title", titles), ("description", descs)):
        dupes = {k: v for k, v in m.items() if len(v) > 1}
        for k, v in dupes.items():
            ne += 1
            print(f"\n! duplicate {label} across {len(v)} pages: {', '.join(v)}")

    print("-" * 84)
    print(f"{len(pages)} pages | {ne} errors | {nw} warnings")
    return 1 if ne else 0


if __name__ == "__main__":
    sys.exit(main())
