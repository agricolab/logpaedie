"""Bildergeschichte: [Wort] im Text wird durch das Bild ersetzt."""
import re, os
from icons import ROOT, FONT_CSS, icon

STORIES = [('Ein Tag mit [Susi]', '''
Die [Sonne] lacht. [Susi] hüpft vom [Sofa].
Dann holt [Susi] eine [Socke] und den [Sombrero].

Mama ruft: „Heute fahren wir mit dem [Zug] an den [See]!“
Vorher kaufen Mama und [Susi] im [Supermarkt] noch einen [Saft],
eine [Zitrone] und [Salat] ein.

Am [See] baut Mama ein [Zelt] auf. Auf dem Wasser fährt ein [Segelboot].
Vorne am Boot hängt ein langes [Seil].

Da taucht ein [Seehund] auf! Er hat eine [Zahnbürste] im Maul.
[Susi] lacht und lacht.

Hinter dem [See] liegt ein [Sumpf]. Dort quaken Frösche: „Quak, quak!“
Wie viele Frösche? Eins, [Zwei], drei, vier, fünf, [Sechs], [Sieben]!

Daheim kocht Mama eine [Suppe]. [Susi] hilft mit dem [Sieb].
Am Abend wäscht [Susi] die Hände mit [Seife].
Dann kuschelt [Susi] im großen [Sessel].
Die [Sonne] geht unter. Gute Nacht, [Susi]!
''', 1.0),

('[Susi] im [Zirkus]', '''
Heute geht [Susi] mit Opa in den [Zirkus].
[Susi] trägt ihre rote [Mütze].

In der Manege tanzt ein [Zebra].
Dann kommt eine [Ziege] mit einer [Brezel] im Maul.

Jetzt kommt der [Zauberer]. Aus dem Hut hüpft ein [Hase]!
Und dann noch eine [Katze]. [Susi] klatscht laut.

In der Pause kauft Opa eine [Pizza].
Der Clown reitet auf einem [Esel]. Was für ein toller Tag!
''', 1.4),

('[Susi] auf der [Insel]', '''
[Susi] fährt mit Papa auf eine [Insel].
Die [Sonne] lacht. Auf der [Insel] wohnt ein [Esel].

Unter den Bäumen wachsen [Pilze] und eine [Rose].
[Susi] hat ihre blaue [Hose] an.
Da krabbelt eine [Ameise] auf die [Hose]. Huch!

Mittags gibt es [Käse] und [Salat].
Dann fährt [Susi] mit dem [Segelboot] heim.
Am Abend brennt eine [Kerze]. Gute Nacht, [Susi]!
''', 1.4),
]

def rebus(t):
    return re.sub(r'\[([^\]]+)\]', lambda m: f'<span class="pic" title="{m.group(1)}">{icon(m.group(1))}</span>', t)

def render(TITLE, STORY, zoom):
    # Jedes Wort mit s oder z am Anfang muss ein Bild sein.
    leftover = re.findall(r'\b[sSzZ]\w*', re.sub(r'\[[^\]]+\]', '', TITLE + STORY))
    assert not leftover, f'S/Z-Wörter ohne Bild: {leftover}'

    words = list(dict.fromkeys(re.findall(r'\[([^\]]+)\]', TITLE + STORY)))
    paras = [p.strip() for p in STORY.strip().split('\n\n')]
    body = ''.join('<p>' + rebus(p.replace('\n', ' ')) + '</p>\n' for p in paras)
    legend = ''.join(f'<div class="lg"><span class="pic">{icon(w)}</span><span>{w}</span></div>' for w in words)

    html = f'''<!DOCTYPE html>
<html lang="de"><head><meta charset="utf-8"><title>{TITLE.replace('[', '').replace(']', '')}</title>
<style>
{FONT_CSS}
@page{{size:A4 portrait;margin:0}}
*{{box-sizing:border-box;margin:0;padding:0}}
html,body{{background:#fff;font-family:'Baloo 2',sans-serif;color:#2b2b2b;-webkit-print-color-adjust:exact;print-color-adjust:exact}}
.page{{width:210mm;height:297mm;padding:13mm 15mm 7mm;display:flex;flex-direction:column;overflow:hidden;margin:0 auto;background:#fff}}
h1{{zoom:{zoom};font-size:40px;font-weight:700;text-align:center;margin-bottom:6mm}}
h1 .pic{{width:58px;height:58px;margin-left:8px}}
.story{{flex:1;zoom:{zoom}}}
p{{font-size:23px;font-weight:600;line-height:2.1;margin-bottom:3mm}}
.pic{{display:inline-flex;align-items:center;justify-content:center;width:50px;height:50px;vertical-align:middle;
  border-radius:50%;border:1.5px solid #bdbdbd;background:#fff;overflow:hidden;margin:-6px 2px 0}}
.pic img{{width:100%;height:100%}}
.pic svg{{width:92%;height:92%}}
.legend{{border-top:2px dashed #d6d1c4;padding-top:4mm;display:grid;grid-template-columns:repeat(12,1fr);gap:2mm 1mm}}
.lg{{display:flex;flex-direction:column;align-items:center;font-size:10.5px;white-space:nowrap;font-weight:700}}
.lg .pic{{width:38px;height:38px;margin:0}}
.foot{{font-size:7.5px;color:#9a968c;text-align:right;font-family:sans-serif;margin-top:3mm}}
@media screen{{body{{padding:16px 0}} .page{{box-shadow:0 1px 6px rgba(0,0,0,.15)}}}}
</style></head><body>
<div class="page">
<h1>{rebus(TITLE)}</h1>
<div class="story">
{body}</div>
<div class="legend">{legend}</div>
<div class="foot">Symbole: OpenMoji (openmoji.org, CC BY-SA 4.0), ergänzt um eigene Zeichnungen</div>
</div></body></html>'''
    plain = TITLE.replace('[', '').replace(']', '')
    open(os.path.join(ROOT, 'susi-stories', plain + '.html'), 'w').write(html)
    print(plain + ':', len(words), 'Bildwörter:', ', '.join(words))


for story in STORIES:
    render(*story)
