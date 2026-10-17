"""Bildergeschichte: [Wort] im Text wird durch das Bild ersetzt."""
import re, os
from icons import ROOT, FONT_CSS, icon

TITLE = 'Susis Sonnentag'
STORY = '''
Die [Sonne] scheint hell. Susi springt vom [Sofa].
Schnell zieht sie eine [Socke] an. Dann setzt sie den [Sombrero] auf.

Mama sagt: „Wir gehen einkaufen!“ Zusammen laufen sie in den [Supermarkt].
Susi legt einen [Saft] in den Wagen. Mama nimmt einen [Sack] Kartoffeln.

Zu Hause kocht Mama eine leckere [Suppe].
Susi hilft und gießt die Nudeln durch das [Sieb].

Danach gehen sie zum [See]. Auf dem Wasser schaukelt ein [Segelboot].
Vorne am Boot hängt ein langes [Seil].

Hinter dem See ist ein [Sumpf]. Dort quakt es laut: „Quak, quak!“
Susi zählt die Frösche: eins, zwei, drei … [Sieben]!

Am Abend wäscht Susi ihre Hände mit [Seife].
Dann kuschelt sie sich in den großen [Sessel].
Die [Sonne] geht unter. Gute Nacht, Susi!
'''

words = list(dict.fromkeys(re.findall(r'\[([^\]]+)\]', STORY)))
paras = [p.strip() for p in STORY.strip().split('\n\n')]
body = ''.join('<p>' + re.sub(r'\[([^\]]+)\]', lambda m: f'<span class="pic" title="{m.group(1)}">{icon(m.group(1))}</span>',
                              p.replace('\n', ' ')) + '</p>\n' for p in paras)
legend = ''.join(f'<div class="lg"><span class="pic">{icon(w)}</span><span>{w}</span></div>' for w in words)

html = f'''<!DOCTYPE html>
<html lang="de"><head><meta charset="utf-8"><title>{TITLE}</title>
<style>
{FONT_CSS}
@page{{size:A4 portrait;margin:0}}
*{{box-sizing:border-box;margin:0;padding:0}}
html,body{{background:#fff;font-family:'Baloo 2',sans-serif;color:#2b2b2b;-webkit-print-color-adjust:exact;print-color-adjust:exact}}
.page{{width:210mm;height:297mm;padding:16mm 16mm 8mm;display:flex;flex-direction:column;overflow:hidden;margin:0 auto;background:#fff}}
h1{{font-size:40px;font-weight:700;text-align:center;margin-bottom:6mm}}
h1 .pic{{width:58px;height:58px;margin-left:8px}}
.story{{flex:1}}
p{{font-size:23px;font-weight:600;line-height:2.25;margin-bottom:4mm}}
.pic{{display:inline-flex;align-items:center;justify-content:center;width:50px;height:50px;vertical-align:middle;
  border-radius:50%;border:1.5px solid #bdbdbd;background:#fff;overflow:hidden;margin:-6px 2px 0}}
.pic img{{width:100%;height:100%}}
.pic svg{{width:92%;height:92%}}
.legend{{border-top:2px dashed #d6d1c4;padding-top:4mm;display:grid;grid-template-columns:repeat(8,1fr);gap:2mm 1mm}}
.lg{{display:flex;flex-direction:column;align-items:center;font-size:12px;font-weight:700}}
.lg .pic{{width:40px;height:40px;margin:0}}
.foot{{font-size:7.5px;color:#9a968c;text-align:right;font-family:sans-serif;margin-top:3mm}}
@media screen{{body{{padding:16px 0}} .page{{box-shadow:0 1px 6px rgba(0,0,0,.15)}}}}
</style></head><body>
<div class="page">
<h1>{TITLE} <span class="pic">{icon('Sonne')}</span></h1>
<div class="story">
{body}</div>
<div class="legend">{legend}</div>
<div class="foot">Symbole: OpenMoji (openmoji.org, CC BY-SA 4.0), ergänzt um eigene Zeichnungen</div>
</div></body></html>'''
open(os.path.join(ROOT, 'Susis Sonnentag.html'), 'w').write(html)
print(len(words), 'Bildwörter:', ', '.join(words))
