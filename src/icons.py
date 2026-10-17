"""Shared picture sources: OpenMoji, custom drawings and the original draft's SVGs."""
import re, json, base64, os
BASE=os.path.dirname(os.path.abspath(__file__))
ROOT=os.path.dirname(BASE)
os.chdir(BASE)
src=open(os.path.join(ROOT,'S-Vokal Bildtafel.html')).read()
tpl=json.loads(re.search(r'<script type="__bundler/template">(.*?)</script>',src,re.S).group(1))
man=json.loads(re.search(r'<script type="__bundler/manifest">(.*?)</script>',src,re.S).group(1))
font=man['4c74d001-1f9c-4f69-a28d-a1b2de8f3d61']['data']
fontx=man['745063b7-783f-4514-88b8-580cd2094a20']['data']
draft={}
for m in re.finditer(r'<svg sc-camel-view-box="([^"]+)"[^>]*><title>([^<]+)</title>(.*?)</svg>',tpl,re.S):
    draft[m.group(2)]=f'<svg viewBox="{m.group(1)}"><title>{m.group(2)}</title>{m.group(3)}</svg>'
OM={'Saft':'1F9C3','Salz':'1F9C2','Sandale':'1FA74','Seife':'1F9FC','Segelboot':'26F5',
    'Sessel':'E141','Seil':'1FAA2','Sonne':'2600','Sofa':'1F6CB','Socke':'1F9E6',
    'Soldat':'1F482','Supermarkt':'1F6D2','Suppe':'1F372','Sushi':'1F363','Sultan':'1F473',
    'Susi':'1F467','Zug':'1F682','Zitrone':'1F34B','Salat':'1F957','Zelt':'26FA',
    'Seehund':'1F9AD','Zahnbürste':'1FAA5',
    'Zirkus':'1F3AA','Mütze':'1F9E2','Zebra':'1F993','Ziege':'1F410','Brezel':'1F968',
    'Zauberer':'1F9D9','Hase':'1F407','Katze':'1F408','Pizza':'1F355','Nase':'1F443',
    'Insel':'1F3DD','Esel':'1FACF','Pilze':'1F344','Rose':'1F339','Hose':'1F456',
    'Ameise':'1F41C','Käse':'1F9C0','Kerze':'1F56F'}
# Zahlen im Stil der "7" aus dem Entwurf
for w,d in {'Zwei':'2','Sechs':'6'}.items():
    draft[w]=draft['Sieben'].replace('<title>Sieben','<title>'+w).replace('>7</text>','>'+d+'</text>')
FONT_CSS=f'''@font-face{{font-family:'Baloo 2';font-weight:600 800;src:url(data:font/woff2;base64,{font}) format('woff2');unicode-range:U+0000-00FF,U+2000-206F;}}
@font-face{{font-family:'Baloo 2';font-weight:600 800;src:url(data:font/woff2;base64,{fontx}) format('woff2');unicode-range:U+0100-02BA,U+1E00-1E9F;}}'''
def icon(w):
    if w in OM:
        b=base64.b64encode(open(f'openmoji/{OM[w]}.svg','rb').read()).decode()
        return f'<img alt="{w}" src="data:image/svg+xml;base64,{b}">'
    if os.path.exists(f'custom/{w}.svg'):
        b=base64.b64encode(open(f'custom/{w}.svg','rb').read()).decode()
        return f'<img alt="{w}" src="data:image/svg+xml;base64,{b}">'
    return draft[w]
