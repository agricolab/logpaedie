from icons import ROOT, OM, FONT_CSS, icon
import os
cols=[('Sa','#d97757','#fff',['Sack','Saft','Salz','Sattel','Sandale']),
      ('Se','#1e88e5','#fff',['Seife','See','Segelboot','Sessel','Seil']),
      ('Si','#43a047','#fff',['Sieb','Sirup','Sichel','Sieben','Silo']),
      ('So','#fbc02d','#2b2b2b',['Sonne','Sofa','Socke','Soldat','Sombrero']),
      ('Su','#8e24aa','#fff',['Suppe','Supermarkt','Sushi','Sultan','Sumpf'])]
used_draft=[]
head=''.join(f'<div class="hd" style="background:{c};color:{t}">{s}</div>' for s,c,t,_ in cols)
cells=''
for r in range(5):
    for s,c,t,ws in cols:
        w=ws[r]
        if w not in OM: used_draft.append(w)
        cells+=f'<div class="cell"><div class="circ">{icon(w)}</div><div class="lbl">{w}</div></div>\n'
html=f'''<!DOCTYPE html>
<html lang="de"><head><meta charset="utf-8"><title>S-Vokal Bildtafel</title>
<style>
{FONT_CSS}
@page{{size:A4 landscape;margin:0}}
*{{box-sizing:border-box;margin:0;padding:0}}
html,body{{background:#fff;font-family:'Baloo 2',sans-serif;color:#2b2b2b;-webkit-print-color-adjust:exact;print-color-adjust:exact}}
.page{{width:297mm;height:210mm;padding:7mm 8mm 5mm;display:flex;flex-direction:column;gap:2mm;overflow:hidden;margin:0 auto;background:#fff}}
.row{{display:grid;grid-template-columns:repeat(5,1fr);gap:4mm}}
.hdr{{height:22mm;align-items:center;justify-items:center}}
.hd{{width:20mm;height:20mm;border-radius:50%;border:2px solid #2b2b2b;display:flex;align-items:center;justify-content:center;font-size:30px;font-weight:700;line-height:1;padding-top:3px}}
.grid{{flex:1;display:grid;grid-template-columns:repeat(5,1fr);grid-template-rows:repeat(5,1fr);gap:1mm 4mm}}
.cell{{display:flex;flex-direction:column;align-items:center;justify-content:center;gap:0}}
.circ{{width:26mm;height:26mm;border-radius:50%;border:1.5px solid #bdbdbd;background:#fff;display:flex;align-items:center;justify-content:center;overflow:hidden}}
.circ svg{{width:92%;height:92%}}
.circ img{{width:100%;height:100%}}
.lbl{{font-size:15px;font-weight:700;line-height:1.3}}
.foot{{font-size:7.5px;color:#9a968c;text-align:right;font-family:sans-serif}}
@media screen{{body{{padding:16px 0}} .page{{box-shadow:0 1px 6px rgba(0,0,0,.15)}}}}
</style></head><body>
<div class="page">
<div class="row hdr">{head}</div>
<div class="grid">
{cells}</div>
<div class="foot">Symbole: OpenMoji (openmoji.org, CC BY-SA 4.0), ergänzt um eigene Zeichnungen</div>
</div></body></html>'''
open(os.path.join(ROOT,'S-Vokal Bildtafel v2.html'),'w').write(html)
print('draft icons:',used_draft)
