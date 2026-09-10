#!/usr/bin/env python3
"""Generate every layout x colour combination, plus a chooser page.

Reuses the layout CSS from build-variants.py and the scheme tokens from
build-colors.py, so there is still exactly one definition of each layout and
each scheme. Produces:

  variants/combo/<layout><scheme>.html   e.g. 2e.html  (25 pages)
  choose.html                            the page you send to a reviewer

Run from the repo root:  python3 tools/build-combos.py
"""
import importlib.util
import os

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
TOOLS = os.path.join(ROOT, 'tools')
BASE = os.path.join(ROOT, 'index.html')
OUT = os.path.join(ROOT, 'variants', 'combo')


def load(name, filename):
    spec = importlib.util.spec_from_file_location(name, os.path.join(TOOLS, filename))
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


layouts_mod = load('bv', 'build-variants.py')
colors_mod = load('bc', 'build-colors.py')

# (digit, name, css) -- the numbering the reviewer sees
LAYOUTS = [(str(i + 1), name, css)
           for i, (_slug, name, _desc, css) in enumerate(layouts_mod.VARIANTS)]

# (letter, name, tokens, extra) -- schemes are already ordered a..e
SCHEMES = [(slug[0], name, tokens, extra)
           for slug, name, _desc, tokens, extra in colors_mod.SCHEMES]


def build_combos():
    base = open(BASE).read()
    os.makedirs(OUT, exist_ok=True)
    n = 0
    for digit, lname, lcss in LAYOUTS:
        for letter, sname, tokens, extra in SCHEMES:
            page = base.replace(
                '<title>Bottom-Line Impact Calculator</title>',
                '<title>%s%s - %s / %s</title>' % (
                    digit, letter.upper(), lname, sname), 1)
            page = page.replace('</head>', '<style>%s%s%s</style>\n</head>' % (
                lcss, colors_mod.token_css(tokens), extra), 1)
            open(os.path.join(OUT, '%s%s.html' % (digit, letter)), 'w').write(page)
            n += 1
    print('  wrote %d combination pages to variants/combo/' % n)
    return n


CHOOSER = '''<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>Choose a Layout and Colour - Bottom-Line Impact Calculator</title>
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Archivo:wght@700;800;900&family=Public+Sans:wght@400;600;700&display=swap">
<style>
  :root{
    --paper:#f2f2f2; --surface:#ffffff; --ink:#0f172a; --ink-soft:#33333a;
    --muted:#6e6e6e; --line:rgba(15,23,42,.14); --line-strong:rgba(15,23,42,.26);
    --jlt:#fe5002; --jlt-strong:#c43c00; --radius:10px; color-scheme:light;
  }
  @media (prefers-color-scheme:dark){ :root:not([data-theme="light"]){
    --paper:#0e131b; --surface:#161d28; --ink:#eef1f6; --ink-soft:#c3cad6;
    --muted:#949dab; --line:rgba(238,241,246,.14); --line-strong:rgba(238,241,246,.26);
    --jlt-strong:#ff8a52; color-scheme:dark;
  }}
  *{box-sizing:border-box}
  body{margin:0; background:var(--paper); color:var(--ink);
       font:15px/1.5 "Public Sans",system-ui,-apple-system,sans-serif;}
  header{background:var(--surface); border-bottom:1px solid var(--line);
         padding:20px clamp(16px,4vw,32px);}
  .hw{max-width:1320px; margin:0 auto;}
  h1{font-family:"Archivo",system-ui,sans-serif; font-weight:900;
     font-size:clamp(1.2rem,2.4vw,1.55rem); margin:0;}
  .sub{color:var(--ink-soft); font-size:.92rem; margin-top:6px; max-width:70ch;}
  main{max-width:1320px; margin:0 auto; padding:20px clamp(16px,4vw,32px) 48px;}
  .pick{background:var(--surface); border:1px solid var(--line);
        border-radius:var(--radius); padding:16px 18px; margin-bottom:14px;}
  .row{display:flex; flex-wrap:wrap; gap:8px; align-items:center;}
  .row + .row{margin-top:14px; padding-top:14px; border-top:1px solid var(--line);}
  .lbl{font-size:.68rem; font-weight:700; letter-spacing:.11em; text-transform:uppercase;
       color:var(--muted); min-width:66px;}
  button{font:inherit; color:inherit; cursor:pointer;
         border:1px solid var(--line-strong); border-radius:6px;
         background:transparent; padding:7px 13px; font-weight:700; font-size:.84rem;}
  button:hover{border-color:var(--jlt); color:var(--jlt-strong);}
  button[aria-pressed="true"]{background:var(--jlt); border-color:var(--jlt); color:#fff;}
  button .k{font-family:"Archivo",system-ui,sans-serif; font-weight:900; margin-right:6px;
            opacity:.75;}
  button[aria-pressed="true"] .k{opacity:1;}
  .now{display:flex; flex-wrap:wrap; gap:12px; align-items:baseline;
       margin:0 0 12px; padding:14px 18px; background:var(--surface);
       border:1px solid var(--line); border-left:3px solid var(--jlt);
       border-radius:0 var(--radius) var(--radius) 0;}
  .code{font-family:"Archivo",system-ui,sans-serif; font-weight:900;
        font-size:1.5rem; color:var(--jlt-strong); line-height:1;}
  .desc{color:var(--ink-soft); font-size:.92rem;}
  .open{margin-left:auto; font-size:.84rem; font-weight:700; color:var(--jlt-strong);}
  .frame{background:var(--surface); border:1px solid var(--line);
         border-radius:var(--radius); overflow:hidden;}
  iframe{display:block; width:100%; height:min(78vh,900px); border:0;}
  footer{color:var(--muted); font-size:.82rem; margin-top:18px; max-width:78ch;}
  footer b{color:var(--ink);}
  @media (max-width:640px){
    .lbl{min-width:0; width:100%;}
    iframe{height:70vh;}
    .open{margin-left:0; width:100%;}
  }
</style>
</head>
<body>
<header><div class="hw">
  <h1>Pick a layout, then a colour</h1>
  <p class="sub">Two choices. The preview below updates as you click, and every
  combination is the real working calculator &mdash; the sliders and the live ticker
  all function. When you land on one you like, note its code (like <b>2E</b>) and
  send that back.</p>
</div></header>

<main>
  <div class="pick">
    <div class="row" id="rowL"><span class="lbl">Layout</span></div>
    <div class="row" id="rowC"><span class="lbl">Colour</span></div>
  </div>

  <div class="now">
    <span class="code" id="code">--</span>
    <span class="desc" id="desc"></span>
    <a class="open" id="open" href="#" target="_blank" rel="noopener">
      Open full screen &nearr;</a>
  </div>

  <div class="frame"><iframe id="pv" title="Calculator preview"
       src="about:blank" loading="eager"></iframe></div>

  <footer>Colour schemes are fixed, so what you see here is what everyone sees &mdash;
  it will not change with your computer's light or dark setting. On a phone, use
  <b>Open full screen</b>; the preview window is too narrow to show the wider layouts
  properly.</footer>
</main>

<script>
(function(){
  "use strict";
  var LAYOUTS = __LAYOUTS__;
  var SCHEMES = __SCHEMES__;
  var sel = { l: LAYOUTS[0][0], c: SCHEMES[0][0] };

  function $(id){ return document.getElementById(id); }

  function mkButtons(row, items, key){
    items.forEach(function(it){
      var b = document.createElement('button');
      b.type = 'button';
      b.innerHTML = '<span class="k">' + (key === 'l' ? it[0] : it[0].toUpperCase())
                  + '</span>' + it[1];
      b.setAttribute('aria-pressed', 'false');
      b.addEventListener('click', function(){ sel[key] = it[0]; render(); });
      b.dataset.val = it[0];
      b.dataset.key = key;
      row.appendChild(b);
    });
  }

  function nameOf(items, val){
    for (var i = 0; i < items.length; i++) if (items[i][0] === val) return items[i][1];
    return val;
  }

  function render(){
    var code = sel.l + sel.c.toUpperCase();
    var href = 'variants/combo/' + sel.l + sel.c + '.html';
    $('code').textContent = code;
    $('desc').textContent = nameOf(LAYOUTS, sel.l) + '  \\u00b7  ' + nameOf(SCHEMES, sel.c);
    $('open').href = href;
    if ($('pv').getAttribute('src') !== href) $('pv').setAttribute('src', href);
    document.querySelectorAll('button[data-key]').forEach(function(b){
      b.setAttribute('aria-pressed', String(sel[b.dataset.key] === b.dataset.val));
    });
    try { localStorage.setItem('blic-choice', sel.l + sel.c); } catch(e){}
    if (location.hash.slice(1).toLowerCase() !== (sel.l + sel.c))
      history.replaceState(null, '', '#' + sel.l + sel.c);
  }

  mkButtons($('rowL'), LAYOUTS, 'l');
  mkButtons($('rowC'), SCHEMES, 'c');

  // a shared link like choose.html#4d wins, then whatever was last viewed here
  var want = (location.hash.slice(1) || '');
  try { want = want || localStorage.getItem('blic-choice') || ''; } catch(e){}
  var m = /^([1-9])([a-z])$/.exec(want.toLowerCase());
  if (m && LAYOUTS.some(function(x){ return x[0] === m[1]; })
        && SCHEMES.some(function(x){ return x[0] === m[2]; })) {
    sel.l = m[1]; sel.c = m[2];
  }
  render();
})();
</script>
</body>
</html>
'''


def build_chooser():
    import json
    ls = json.dumps([[d, n] for d, n, _ in LAYOUTS])
    ss = json.dumps([[l, n] for l, n, _t, _x in SCHEMES])
    html = CHOOSER.replace('__LAYOUTS__', ls).replace('__SCHEMES__', ss)
    open(os.path.join(ROOT, 'choose.html'), 'w').write(html)
    print('  wrote choose.html  (%d layouts x %d schemes)' % (len(LAYOUTS), len(SCHEMES)))


if __name__ == '__main__':
    build_combos()
    build_chooser()
