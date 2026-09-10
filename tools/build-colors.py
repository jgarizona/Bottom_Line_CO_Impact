#!/usr/bin/env python3
"""Generate colour-scheme options for the Hero Split layout.

Each scheme is index.html + the Hero Split layout CSS + a fixed token block,
so copy, markup and JS keep a single source of truth. Schemes are *fixed*
rather than following the viewer's OS theme: a colour choice should look the
same for everyone comparing it, and the same for whoever it gets shown to.

Every value below was contrast-checked against WCAG AA before being committed;
see the commit message for the measured ratios.

Run from the repo root:  python3 tools/build-colors.py
"""
import os

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
BASE = os.path.join(ROOT, 'index.html')
OUT = os.path.join(ROOT, 'variants', 'colors')

# The Hero Split layout, same as variants/2-hero-split.html
LAYOUT = '''
/* ---- Hero Split layout ---- */
@media (min-width:1000px){
  body>.wrap{display:grid; grid-template-columns:1fr 1fr; gap:0 40px; align-items:center;}
  body>.wrap>*:nth-child(1){grid-column:1; grid-row:1; padding-top:52px;}
  body>.wrap>*:nth-child(3){grid-column:2; grid-row:1; margin:52px 0 6px;}
  body>.wrap>*:nth-child(2){grid-column:1 / -1; grid-row:2;}
  body>.wrap>*:nth-child(n+4){grid-column:1 / -1;}
  .hero h1{max-width:18ch; font-size:clamp(1.9rem,3.4vw,2.7rem);}
  .impact-hero{padding:44px 28px;}
  .impact-hero .bignum{font-size:clamp(3rem,6vw,4.6rem);}
}
'''

# name, one-line description, token dict, extra CSS
SCHEMES = [
 ('a-jlt-light', 'JLT Cool - Light',
  'The current palette, pinned to light. JLT neutrals, navy panels.', dict(
   paper='#f2f2f2', surface='#ffffff', surface_2='#e7e8ea',
   ink='#0f172a', ink_soft='#33333a', muted='#6e6e6e',
   line='rgba(15,23,42,0.14)', line_strong='rgba(15,23,42,0.26)',
   jlt='#fe5002', jlt_strong='#c43c00', jlt_wash='rgba(254,80,2,0.10)',
   banner_bg='#0f172a', banner_fg='#eef1f6', banner_border='rgba(254,80,2,0.30)',
   banner_accent='#f39200', banner_fg_soft='rgba(238,241,246,0.80)',
   banner_fg_faint='rgba(238,241,246,0.64)', banner_hairline='rgba(238,241,246,0.28)',
   banner_fill='rgba(238,241,246,0.10)',
   shadow='0 1px 0 rgba(15,23,42,0.04), 0 8px 24px -16px rgba(15,23,42,0.30)',
   scheme='light'), ''),

 ('b-jlt-dark', 'JLT Cool - Dark',
  'The current palette, pinned to dark. Cool slates derived from the navy.', dict(
   paper='#0e131b', surface='#161d28', surface_2='#1e2735',
   ink='#eef1f6', ink_soft='#c3cad6', muted='#949dab',
   line='rgba(238,241,246,0.13)', line_strong='rgba(238,241,246,0.26)',
   jlt='#fe5002', jlt_strong='#ff8a52', jlt_wash='rgba(254,80,2,0.16)',
   banner_bg='#0f172a', banner_fg='#eef1f6', banner_border='rgba(254,80,2,0.30)',
   banner_accent='#f39200', banner_fg_soft='rgba(238,241,246,0.80)',
   banner_fg_faint='rgba(238,241,246,0.64)', banner_hairline='rgba(238,241,246,0.28)',
   banner_fill='rgba(238,241,246,0.10)',
   shadow='0 1px 0 rgba(0,0,0,0.4), 0 8px 24px -16px rgba(0,0,0,0.6)',
   scheme='dark'), ''),

 ('c-signal', 'Signal',
  'The brand CTA gradient promoted to the panels. Loudest and most salesy.', dict(
   paper='#ffffff', surface='#ffffff', surface_2='#fff5f0',
   ink='#0f172a', ink_soft='#33333a', muted='#6e6e6e',
   line='rgba(15,23,42,0.13)', line_strong='rgba(254,80,2,0.40)',
   jlt='#fe5002', jlt_strong='#c43c00', jlt_wash='rgba(243,146,0,0.16)',
   banner_bg='#fe5002', banner_fg='#0b1220', banner_border='rgba(15,23,42,0.22)',
   banner_accent='#2e0c00', banner_fg_soft='rgba(11,18,32,0.94)',
   banner_fg_faint='rgba(11,18,32,0.86)', banner_hairline='rgba(11,18,32,0.32)',
   banner_fill='rgba(255,255,255,0.26)',
   shadow='0 1px 0 rgba(15,23,42,0.04), 0 10px 28px -16px rgba(254,80,2,0.45)',
   scheme='light'), '''
/* the brand CTA gradient, on the panels themselves */
.ticker-panel,.verdict{background-image:linear-gradient(48deg,#fe5000 0%,#f39200 85%);}
.verdict h2{color:#0b1220;}
.ticker-panel .tnum{color:#0b1220;}
.tbtn:hover{border-color:#0b1220; background:rgba(255,255,255,.42); color:#0b1220;}
.tbtn.active{background:#0b1220; border-color:#0b1220; color:#fff;}
.ticker-check input,.ticker-panel input[type=checkbox]{accent-color:#0b1220;}
'''),

 ('d-steel', 'Steel Blue',
  "Their link blue as structure, orange kept for the money. Most technical.", dict(
   paper='#eef3f8', surface='#ffffff', surface_2='#e3ecf4',
   ink='#0a2540', ink_soft='#33333a', muted='#5f7183',
   line='rgba(10,37,64,0.14)', line_strong='rgba(10,37,64,0.26)',
   jlt='#fe5002', jlt_strong='#c43c00', jlt_wash='rgba(254,80,2,0.10)',
   banner_bg='#0a3255', banner_fg='#e9f2fa', banner_border='rgba(43,123,185,0.50)',
   banner_accent='#f39200', banner_fg_soft='rgba(233,242,250,0.82)',
   banner_fg_faint='rgba(233,242,250,0.66)', banner_hairline='rgba(233,242,250,0.30)',
   banner_fill='rgba(233,242,250,0.12)',
   shadow='0 1px 0 rgba(10,37,64,0.04), 0 8px 24px -16px rgba(10,37,64,0.34)',
   scheme='light'), '''
/* #2b7bb9 finally earns a job: estimate data reads blue, JLT's validated data orange */
.badge{color:#2b7bb9; border-color:rgba(43,123,185,0.55);}
.badge.validated{color:var(--jlt-strong); border-color:var(--jlt-strong);}
.tile:not(.win){border-top-color:#2b7bb9;}
'''),

 ('e-jltbanner', 'JLT Banner',
  "Built from the /rugged-computers hero banner: its cream-to-mint wash, its "
  "warm off-white, its navy, and its CTA gradient on the buttons.", dict(
   paper='#f7f5ee', surface='#ffffff', surface_2='#e2ecdc',
   ink='#0f172a', ink_soft='#33333a', muted='#585858',
   line='rgba(15,23,42,0.12)', line_strong='rgba(15,23,42,0.22)',
   jlt='#fe5002', jlt_strong='#c43c00', jlt_wash='rgba(254,80,2,0.09)',
   banner_bg='#0f172a', banner_fg='#eef1f6', banner_border='rgba(254,80,2,0.28)',
   banner_accent='#f39200', banner_fg_soft='rgba(238,241,246,0.80)',
   banner_fg_faint='rgba(238,241,246,0.64)', banner_hairline='rgba(238,241,246,0.28)',
   banner_fill='rgba(238,241,246,0.10)',
   shadow='0 1px 0 rgba(15,23,42,0.04), 0 10px 30px -18px rgba(15,23,42,0.30)',
   scheme='light'), '''
/* The hero banner itself, full-bleed. Stops read off the /rugged-computers
   header: warm cream on the left through a pale neutral into soft mint. */
body{
  background:
    linear-gradient(105deg,#f6efcf 0%,#eff0d4 28%,#e2ecdc 58%,#c9e4d7 100%)
      no-repeat 0 0 / 100% 720px,
    var(--paper);
}
@media (max-width:999px){
  body{background:
    linear-gradient(165deg,#f6efcf 0%,#eff0d4 30%,#e2ecdc 62%,#c9e4d7 100%)
      no-repeat 0 0 / 100% 600px,
    var(--paper);}
}
.hero .callout{background:rgba(255,255,255,.78); border-color:rgba(15,23,42,.10);}
.tool-tag{background:rgba(255,255,255,.72);}

/* JLT's CTA gradient, exact stops, on the selected controls. Text is navy, not
   white: white measures 2.35:1 on the #f39200 end, which fails WCAG even at
   large sizes, while navy clears 5.67:1 at the orange end and 7.96:1 at the
   amber. The gradient itself is unchanged. */
.chip.active,.tbtn.active{
  background:linear-gradient(48deg,#fe5000 0%,#f39200 85%);
  border-color:#fe5002; color:#0b1220;
}
.tbtn.active:hover{color:#0b1220;}
'''),
]

TOKEN_ORDER = [
 ('paper', '--paper'), ('surface', '--surface'), ('surface_2', '--surface-2'),
 ('ink', '--ink'), ('ink_soft', '--ink-soft'), ('muted', '--muted'),
 ('line', '--line'), ('line_strong', '--line-strong'),
 ('jlt', '--jlt'), ('jlt_strong', '--jlt-strong'), ('jlt_wash', '--jlt-wash'),
 ('banner_bg', '--banner-bg'), ('banner_fg', '--banner-fg'),
 ('banner_border', '--banner-border'), ('banner_accent', '--banner-accent'),
 ('banner_fg_soft', '--banner-fg-soft'), ('banner_fg_faint', '--banner-fg-faint'),
 ('banner_hairline', '--banner-hairline'), ('banner_fill', '--banner-fill'),
 ('shadow', '--shadow'),
]


def token_css(t):
    """Emit a fixed token block that outranks the base sheet's theme blocks.

    The base defines dark tokens under `:root:not([data-theme="light"])` inside a
    prefers-color-scheme query. Matching that specificity and coming later in
    source order is what pins the scheme regardless of the viewer's OS setting.
    """
    decls = '\n'.join('  %s:%s;' % (css, t[key]) for key, css in TOKEN_ORDER if key in t)
    return (':root,\n:root:not([data-theme="light"]),\n:root[data-theme="dark"]{\n'
            '%s\n  color-scheme:%s;\n}\n' % (decls, t['scheme']))


SWITCHER_CSS = '''
/* ---- colour switcher (preview only, not part of any scheme) ---- */
body{padding-bottom:64px;}
.cswitch{
  position:fixed; left:0; right:0; bottom:0; z-index:50;
  display:flex; flex-wrap:wrap; gap:6px; align-items:center; justify-content:center;
  padding:9px 12px; background:#0f172a; border-top:1px solid rgba(254,80,2,.34);
  font-family:"Public Sans",system-ui,sans-serif;
}
.cswitch b{
  color:#f39200; font-size:.66rem; font-weight:700;
  letter-spacing:.10em; text-transform:uppercase; margin-right:4px;
}
.cswitch a{
  color:#eef1f6; text-decoration:none; font-size:.76rem; font-weight:700;
  padding:5px 10px; border:1px solid rgba(238,241,246,.26); border-radius:6px;
}
.cswitch a:hover{border-color:#fe5002; background:rgba(254,80,2,.22);}
.cswitch a[aria-current="page"]{background:#fe5002; border-color:#fe5002; color:#fff;}
'''


def switcher_html(active):
    links = []
    for slug, name, _desc, _t, _x in SCHEMES:
        cur = ' aria-current="page"' if slug == active else ''
        links.append('<a href="%s.html"%s>%s</a>' % (slug, cur, name))
    links.append('<a href="../../index.html">Back to main</a>')
    return '<nav class="cswitch"><b>Colour</b>%s</nav>\n' % ''.join(links)


def build():
    base = open(BASE).read()
    os.makedirs(OUT, exist_ok=True)
    made = []
    for slug, name, desc, tokens, extra in SCHEMES:
        page = base.replace(
            '<title>Bottom-Line Impact Calculator</title>',
            '<title>%s - Bottom-Line Impact Calculator</title>' % name, 1)
        # ../../ because these live two levels down from the repo root
        page = page.replace('</head>', '<style>%s%s%s%s</style>\n</head>' % (
            LAYOUT, token_css(tokens), extra, SWITCHER_CSS), 1)
        page = page.replace('</body>', switcher_html(slug) + '</body>', 1)
        open(os.path.join(OUT, slug + '.html'), 'w').write(page)
        made.append((slug, name, desc, tokens))
        print('  wrote variants/colors/%s.html  (%s)' % (slug, name))
    return made


def build_index(made):
    cards = []
    for slug, name, desc, t in made:
        cards.append('''    <li><a href="%s.html">
      <span class="sw"><i style="background:%s"></i><i style="background:%s"></i>
      <i style="background:%s"></i><i style="background:%s"></i></span>
      <span class="n">%s</span><span class="d">%s</span></a></li>''' % (
            slug, t['paper'], t['surface'], t['banner_bg'], t['jlt'], name, desc))
    html = '''<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>Colour Options - Bottom-Line Impact Calculator</title>
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
  .sw{display:flex;gap:4px;margin-bottom:10px;}
  .sw i{width:26px;height:14px;border-radius:3px;border:1px solid var(--line);}
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
  <h1>Colour options</h1>
  <p class="lede">Five colour schemes on the <strong>Hero Split</strong> layout. The first
  two are the palette already in use, split into its light and dark forms; the other three
  are new. Every scheme is pinned &mdash; it looks the same on your screen as on the
  screen you show it on, rather than following each viewer's system theme.</p>
  <ul>
%s
  </ul>
  <div class="back"><a href="../index.html">&larr; layout options</a> &nbsp;&middot;&nbsp;
  <a href="../../index.html">the live page</a></div>
  <footer>Every value here clears WCAG AA for the text that uses it. Pick one and it
  becomes the main page.</footer>
</div>
</body>
</html>
''' % '\n'.join(cards)
    open(os.path.join(OUT, 'index.html'), 'w').write(html)
    print('  wrote variants/colors/index.html (picker)')


if __name__ == '__main__':
    build_index(build())
