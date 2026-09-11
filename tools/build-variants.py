#!/usr/bin/env python3
"""Generate layout variants of index.html.

Each variant is the base page plus an appended override stylesheet, so the
markup, copy and JS have exactly one source of truth (index.html). Layout
differences are pure CSS. Run from the repo root:  python3 tools/build-variants.py
"""
import os
import re

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
BASE = os.path.join(ROOT, 'index.html')
OUT = os.path.join(ROOT, 'variants')

VARIANTS = [
    ('1-sidebar', 'Sidebar Console', 'Inputs pinned in a sticky left rail; results stream on the right. Reads like a tool.', '''
/* ---- 1. Sidebar Console ---- */
@media (min-width:960px){
  body>.wrap{display:grid; grid-template-columns:330px minmax(0,1fr); gap:0 34px; align-items:start;}
  /* child 2 is the impact card and child 3 the inputs panel: the number comes
     before the fields that drive it. The rail is child 3. */
  body>.wrap>*:nth-child(1){grid-column:1 / -1;}
  body>.wrap>*:nth-child(3){grid-column:1; grid-row:2 / span 7; position:sticky; top:24px; margin:0;}
  body>.wrap>*:nth-child(3) .field-grid{grid-template-columns:1fr; gap:16px;}
  body>.wrap>*:nth-child(3) .panel{padding:20px;}
  body>.wrap>*:nth-child(2),
  body>.wrap>*:nth-child(n+4){grid-column:2; margin-top:0; margin-bottom:22px;}
  body>.wrap>*:nth-child(2){margin-top:0;}
  .hero h1{max-width:26ch;}
  .hero .lede{max-width:70ch;}
  .callout{max-width:72ch;}
  .tiles{grid-template-columns:repeat(2,1fr);}
}
'''),
    ('2-hero-split', 'Hero Split', 'Headline and the daily-impact number side by side above the fold. Marketing-forward.', '''
/* ---- 2. Hero Split ---- */
@media (min-width:1000px){
  body>.wrap{display:grid; grid-template-columns:1fr 1fr; gap:0 40px; align-items:center;}
  body>.wrap>*:nth-child(1){grid-column:1; grid-row:1; padding-top:52px;}
  body>.wrap>*:nth-child(2){grid-column:2; grid-row:1; margin:52px 0 6px;}
  body>.wrap>*:nth-child(3){grid-column:1 / -1; grid-row:2;}
  body>.wrap>*:nth-child(n+4){grid-column:1 / -1;}
  .hero h1{max-width:18ch; font-size:clamp(1.9rem,3.4vw,2.7rem);}
  .impact-hero{padding:44px 28px;}
  .impact-hero .bignum{font-size:clamp(3rem,6vw,4.6rem);}
}
'''),
    ('3-stepped', 'Stepped Story', 'Numbered stages with a connector rail — built for walking a customer through it.', '''
/* ---- 3. Stepped Story ---- */
body>.wrap{counter-reset:step;}
@media (min-width:820px){
  body>.wrap>*:nth-child(n+2):nth-child(-n+6){
    counter-increment:step; position:relative; padding-left:76px; margin:0 0 34px;
  }
  body>.wrap>*:nth-child(n+2):nth-child(-n+6)::before{
    content:counter(step); position:absolute; left:0; top:0;
    width:44px; height:44px; border-radius:50%;
    background:var(--jlt); color:#fff;
    font-family:"Archivo",system-ui,sans-serif; font-weight:900; font-size:1.05rem;
    display:flex; align-items:center; justify-content:center; z-index:1;
  }
  body>.wrap>*:nth-child(n+2):nth-child(-n+5)::after{
    content:""; position:absolute; left:21px; top:44px; bottom:-34px;
    width:2px; background:var(--line-strong);
  }
  body>.wrap>*:nth-child(n+7){padding-left:76px;}
  .hero{padding-bottom:26px;}
}
'''),
    ('4-compact', 'Compact Console', 'Everything that matters on one screen. Dense, for a live screen-share.', '''
/* ---- 4. Compact Console ---- */
.hero{padding:22px 0 2px;}
.hero h1{font-size:clamp(1.35rem,2.4vw,1.85rem); max-width:34ch;}
.hero .lede{font-size:.9rem; margin-top:8px; max-width:76ch;}
.callout{margin-top:12px; padding:10px 14px; font-size:.82rem; max-width:76ch;}
.section{margin:16px 0;}
.panel{padding:16px 18px;}
.impact-hero{padding:20px 16px; margin:16px 0;}
.impact-hero .bignum{font-size:clamp(2rem,4.6vw,3rem); margin-top:2px;}
.impact-hero .eyebrow{margin-top:10px;}
.ticker-panel{padding:18px; margin:16px 0;}
.ticker-panel .tnum{font-size:clamp(1.6rem,4vw,2.3rem); margin-top:10px;}
.ticker-panel .tline{font-size:.88rem;}
.verdict{padding:18px 20px; margin:16px 0;}
.tile{padding:14px 13px;}
.tile .amt{font-size:clamp(1.05rem,2vw,1.3rem); margin-top:9px;}
.tile .spec{font-size:.71rem; min-height:0; margin-top:5px;}
.tile .delta{font-size:.72rem; min-height:0;}
@media (min-width:1060px){
  body>.wrap{max-width:1300px; display:grid; grid-template-columns:1fr 1fr; gap:16px 22px; align-items:start;}
  body>.wrap>*:nth-child(1){grid-column:1 / -1;}
  body>.wrap>*:nth-child(2){grid-column:1; margin:0;}
  body>.wrap>*:nth-child(3){grid-column:2; margin:0;}
  body>.wrap>*:nth-child(4){grid-column:1; margin:0;}
  body>.wrap>*:nth-child(5){grid-column:2; margin:0;}
  body>.wrap>*:nth-child(n+6){grid-column:1 / -1; margin:0;}
  .tiles{grid-template-columns:repeat(2,1fr);}
}
'''),
    ('5-cards', 'Card Deck', 'Every block an elevated card, two up. Airiest and friendliest of the five.', '''
/* ---- 5. Card Deck ---- */
:root{--radius:16px; --radius-sm:10px;}
.panel,.impact-hero,.ticker-panel,.verdict,details.assumptions,.tiles{
  box-shadow:0 2px 4px -2px rgba(15,23,42,.10), 0 12px 32px -14px rgba(15,23,42,.28);
}
.callout{border-radius:var(--radius-sm); border-left-width:4px;}
.tile{padding:22px 20px;}
.tile .amt{font-size:clamp(1.4rem,2.6vw,1.8rem);}
.impact-hero{padding:44px 24px;}
.section{margin:22px 0;}
.impact-hero,.ticker-panel,.verdict{margin:22px 0;}
@media (min-width:1000px){
  body>.wrap{max-width:1180px; display:grid; grid-template-columns:1fr 1fr; gap:22px; align-items:start;}
  body>.wrap>*:nth-child(1){grid-column:1 / -1;}
  body>.wrap>*:nth-child(2){grid-column:1 / -1; margin:0;}
  body>.wrap>*:nth-child(3){grid-column:1; margin:0;}
  body>.wrap>*:nth-child(4){grid-column:2; margin:0;}
  body>.wrap>*:nth-child(5){grid-column:1 / -1; margin:0;}
  body>.wrap>*:nth-child(6){grid-column:1 / -1; margin:0;}
  body>.wrap>*:nth-child(n+7){grid-column:auto; margin:0;}
  body>.wrap>*:nth-child(9){grid-column:1 / -1;}
  .tiles{grid-template-columns:repeat(4,1fr);}
}
'''),
]

SWITCHER_CSS = '''
/* ---- layout switcher (preview only, not part of any layout) ---- */
body{padding-bottom:64px;}
.vswitch{
  position:fixed; left:0; right:0; bottom:0; z-index:50;
  display:flex; flex-wrap:wrap; gap:6px; align-items:center; justify-content:center;
  padding:9px 12px; background:var(--banner-bg); border-top:1px solid var(--banner-border);
  font-family:"Public Sans",system-ui,sans-serif;
}
.vswitch b{
  color:var(--banner-accent); font-size:.66rem; font-weight:700;
  letter-spacing:.10em; text-transform:uppercase; margin-right:4px;
}
.vswitch a{
  color:var(--banner-fg); text-decoration:none; font-size:.76rem; font-weight:700;
  padding:5px 10px; border:1px solid rgba(238,241,246,.26); border-radius:6px;
}
.vswitch a:hover{border-color:var(--jlt); background:rgba(254,80,2,.20);}
.vswitch a[aria-current="page"]{background:var(--jlt); border-color:var(--jlt); color:#fff;}
'''


def switcher_html(active):
    links = ['<a href="../index.html"%s>Current</a>' %
             (' aria-current="page"' if active == 'current' else '')]
    for slug, name, _desc, _css in VARIANTS:
        cur = ' aria-current="page"' if slug == active else ''
        links.append('<a href="%s.html"%s>%s</a>' % (slug, cur, name))
    return '<nav class="vswitch"><b>Layout</b>%s</nav>\n' % ''.join(links)


def build():
    base = open(BASE).read()
    assert '</body>' in base and '</head>' in base
    os.makedirs(OUT, exist_ok=True)
    made = []
    for slug, name, desc, css in VARIANTS:
        page = base
        page = page.replace(
            '<title>Bottom-Line Impact Calculator</title>',
            '<title>%s - Bottom-Line Impact Calculator</title>' % name, 1)
        # relative asset paths are unaffected (no local assets), fonts are absolute
        page = page.replace('</head>',
                            '<style>%s%s</style>\n</head>' % (css, SWITCHER_CSS), 1)
        page = page.replace('</body>', switcher_html(slug) + '</body>', 1)
        path = os.path.join(OUT, slug + '.html')
        open(path, 'w').write(page)
        made.append((slug, name, desc))
        print('  wrote variants/%s.html  (%s)' % (slug, name))
    return made


def build_index(made):
    rows = '\n'.join(
        '    <li><a href="%s.html"><span class="n">%s</span>'
        '<span class="d">%s</span></a></li>' % (slug, name, desc)
        for slug, name, desc in made)
    html = '''<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>Layout Options - Bottom-Line Impact Calculator</title>
<style>
  :root{--paper:#f2f2f2;--surface:#fff;--ink:#0f172a;--ink-soft:#33333a;--muted:#6e6e6e;
        --line:rgba(15,23,42,.14);--jlt:#fe5002;--jlt-strong:#c43c00;color-scheme:light;}
  @media (prefers-color-scheme:dark){:root:not([data-theme="light"]){
        --paper:#0e131b;--surface:#161d28;--ink:#eef1f6;--ink-soft:#c3cad6;--muted:#949dab;
        --line:rgba(238,241,246,.14);--jlt-strong:#ff8a52;color-scheme:dark;}}
  *{box-sizing:border-box}
  body{margin:0;background:var(--paper);color:var(--ink);
       font:15px/1.5 "Public Sans",system-ui,-apple-system,sans-serif;}
  .w{max-width:760px;margin:0 auto;padding:48px clamp(16px,4vw,32px) 64px;}
  h1{font-family:"Archivo",system-ui,sans-serif;font-weight:900;font-size:1.7rem;margin:0;}
  p.lede{color:var(--ink-soft);margin:12px 0 0;}
  ul{list-style:none;padding:0;margin:28px 0 0;display:grid;gap:10px;}
  a{display:block;text-decoration:none;color:inherit;background:var(--surface);
    border:1px solid var(--line);border-radius:10px;padding:16px 18px;}
  a:hover{border-color:var(--jlt);}
  .n{display:block;font-family:"Archivo",system-ui,sans-serif;font-weight:800;
     font-size:1.02rem;color:var(--jlt-strong);}
  .d{display:block;font-size:.86rem;color:var(--ink-soft);margin-top:4px;}
  .back{margin-top:26px;font-size:.86rem;}
  .back a{display:inline;background:none;border:0;padding:0;color:var(--jlt-strong);
          font-weight:700;}
  footer{margin-top:34px;font-size:.78rem;color:var(--muted);}
</style>
</head>
<body>
<div class="w">
  <h1>Layout options</h1>
  <p class="lede">Five alternative layouts for the Bottom-Line Impact Calculator. Same
  copy, same maths, same brand colours &mdash; only the arrangement changes. Every one is
  fully interactive, and each has a switcher bar pinned to the bottom so you can flip
  between them without coming back here.</p>
  <ul>
%s
  </ul>
  <div class="back"><a href="../index.html">&larr; the current layout</a></div>
  <footer>Light and dark both follow your system setting. Pick one and it becomes the
  main page.</footer>
</div>
</body>
</html>
''' % rows
    open(os.path.join(OUT, 'index.html'), 'w').write(html)
    print('  wrote variants/index.html (picker)')


if __name__ == '__main__':
    build_index(build())
