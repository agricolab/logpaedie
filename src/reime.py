"""s/z-Reimpaare: {..} markiert den s-Laut (blau), [..] den z-Laut (rot)."""
import re, os, base64
from icons import ROOT, FONT_CSS, icon

TITLE = 's oder z? Reimpaare'
S_COL, Z_COL = '#1e88e5', '#d84315'
SECTIONS = [
    ('s und z am Wortanfang', [
        ('{s}auberer [Z]auberer', '1F9FC', '1F9D9'),
        ('{S}ocken [z]ocken', '1F9E6', '1F3AE'),
        ('{s}elten [z]elten', '1F48E', '26FA'),
        ('[Z]iegen {s}iegen', '1F410', '1F3C6'),
        ('[Z]ehen {s}ehen', '1F9B6', '1F440'),
        ('[z]ehn {S}een', '1F51F', '1F3DE'),
        ('{S}itz-[Z]itze', '1F4BA', '1F404'),
        ('{S}ack – [z]ack!', 'Sack', '26A1'),
    ]),
    ('s und z in der Wortmitte oder am Ende', [
        ('kra{ss}e Ka[tz]e', '1F60E', '1F431'),
        ('na{ss}e Ta[tz]e', '1F4A7', '1F43E'),
        ('bla{ss}e Gla[tz]e', '1F636', '1F468-200D-1F9B2'),
        ('Pup{s}-Pu[tz]', '1F4A8', '1F9FD'),
        ('Ro[tz]-Ro{ss}', '1F927', '1F40E'),
        ('Pil[z]-Pil{s}', '1F344', '1F37A'),
        ('gan[z]e Gan{s}', '1F4AF', '1FABF'),
        ('Schwei{ß}-Schwei[z]', '1F4A6', '1F1E8-1F1ED'),
    ]),
]

def om(code):
    if not os.path.exists(f'openmoji/{code}.svg'):
        return icon(code)
    b = base64.b64encode(open(f'openmoji/{code}.svg', 'rb').read()).decode()
    return f'<img src="data:image/svg+xml;base64,{b}">'

def label(t):
    t = re.sub(r'\{([^}]+)\}', r'<b class="s">\1</b>', t)
    return re.sub(r'\[([^\]]+)\]', r'<b class="z">\1</b>', t)

KEY = f'<div class="key"><b class="s">s</b> wie Sonne &nbsp;·&nbsp; <b class="z">z</b> wie Zahn</div>'
FOOT = '<div class="foot">Symbole: OpenMoji (openmoji.org, CC BY-SA 4.0)</div>'
body = ''
for head, pairs in SECTIONS:
    body += f'<div class="page">\n<h1>{TITLE}</h1>\n{KEY}\n<h2>{head}</h2>\n<div class="grid">\n'
    body += ''.join(f'<div class="card"><div class="circ">{om(a)}</div><div class="circ">{om(b)}</div>'
                    f'<div class="lbl">{label(t)}</div></div>\n' for t, a, b in pairs)
    body += f'</div>\n{FOOT}\n</div>\n'

html = f'''<!DOCTYPE html>
<html lang="de"><head><meta charset="utf-8"><title>{TITLE}</title>
<style>
{FONT_CSS}
@page{{size:A4 portrait;margin:0}}
*{{box-sizing:border-box;margin:0;padding:0}}
html,body{{background:#fff;font-family:'Baloo 2',sans-serif;color:#2b2b2b;-webkit-print-color-adjust:exact;print-color-adjust:exact}}
.page{{width:210mm;height:297mm;padding:12mm 12mm 6mm;display:flex;flex-direction:column;overflow:hidden;margin:0 auto;background:#fff;break-after:page}}
h1{{font-size:40px;font-weight:700;text-align:center;line-height:1.1}}
.key{{text-align:center;font-size:20px;font-weight:700;margin:1mm 0 2mm}}
h2{{font-size:24px;font-weight:700;border-bottom:2px dashed #d6d1c4;margin:4mm 0 4mm}}
.grid{{flex:1;display:grid;grid-template-columns:1fr 1fr;align-content:space-evenly;gap:3mm 6mm}}
.card{{display:grid;grid-template-columns:auto auto;justify-content:center;gap:1mm 3mm}}
.circ{{flex:none;width:34mm;height:34mm;border-radius:50%;border:1.5px solid #bdbdbd;background:#fff;overflow:hidden}}
.circ img{{width:100%;height:100%}}
.circ svg{{width:92%;height:92%}}
.lbl{{grid-column:1 / 3;text-align:center;font-size:24px;font-weight:700;line-height:1.15}}
b.s{{color:{S_COL}}} b.z{{color:{Z_COL}}}
.foot{{font-size:7.5px;color:#9a968c;text-align:right;font-family:sans-serif}}
@media screen{{body{{padding:16px 0}} .page{{margin-bottom:16px;box-shadow:0 1px 6px rgba(0,0,0,.15)}}}}
</style></head><body>
{body}</body></html>'''
open(os.path.join(ROOT, 'sz-Reimpaare.html'), 'w').write(html)
print(sum(len(p) for _, p in SECTIONS), 'Paare')
