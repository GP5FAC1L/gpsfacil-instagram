# Carrusel flotas "¿Cuántos km hizo tu flota?" — capturas oficiales de GF Service + HTML + Playwright
import os
from playwright.sync_api import sync_playwright
from PIL import Image

ROOT = os.path.abspath(os.path.dirname(__file__) + '/..')
OUT = f'{ROOT}/2026-11/flota-km'
os.makedirs(OUT, exist_ok=True)
for n in ['service_flota', 'service_avisos', 'service_gastos']:
    Image.open(f'{ROOT}/assets/apps/{n}.png').convert('RGB').crop((95, 290, 715, 1440)).save(f'{OUT}/_{n}.png')
F = '/usr/share/fonts/truetype/google-fonts'
CSS = f'''@font-face{{font-family:P;src:url({F}/Poppins-Bold.ttf);font-weight:700}}
@font-face{{font-family:P;src:url({F}/Poppins-Medium.ttf);font-weight:500}}
*{{box-sizing:border-box}}body{{margin:0;width:1080px;height:1350px;font-family:P;overflow:hidden;position:relative;background:#0F2A33;color:#fff}}
.t{{position:absolute;left:80px;right:80px;top:90px}}
.k{{display:inline-flex;align-items:center;gap:14px;background:rgba(255,255,255,.08);font-weight:700;font-size:24px;letter-spacing:3px;padding:10px 22px 10px 12px;border-radius:40px}}
.k img{{width:48px;height:48px;border-radius:12px}}
h1{{font-weight:700;font-size:84px;line-height:1.03;margin:28px 0 18px}}h1 span{{color:#3FD6D2}}
p{{font-weight:500;font-size:34px;margin:0;line-height:1.35;color:#BFE6E4}}
.ph{{position:absolute;border-radius:48px 48px 0 0;overflow:hidden;box-shadow:0 40px 90px rgba(0,0,0,.5);border:10px solid #1b1f22;border-bottom:none}}
.ph img{{display:block;width:100%}}
.mk{{position:absolute;left:60px;bottom:44px;z-index:3}}.mk img{{height:62px;display:block}}
.pg{{position:absolute;right:60px;bottom:58px;font-weight:500;font-size:26px;color:#8FBFBD;z-index:3}}
.glow{{position:absolute;width:900px;height:900px;border-radius:50%;background:radial-gradient(circle,rgba(30,189,186,.33),rgba(30,189,186,0) 70%)}}
.fade{{position:absolute;left:0;right:0;bottom:0;height:200px;background:linear-gradient(180deg,rgba(15,42,51,0),#0F2A33 75%);z-index:2}}
.li{{font-weight:700;font-size:40px;line-height:1.3;margin:0 0 30px;display:flex;gap:22px;align-items:flex-start}}
.li b{{flex:none;width:54px;height:54px;border-radius:16px;background:#1EBDBA;color:#0F2A33;display:flex;align-items:center;justify-content:center;font-size:30px}}
.li small{{display:block;font-weight:500;font-size:28px;color:#BFE6E4}}
'''
A = f'file://{ROOT}/assets'
IC = f'<img src="{A}/logos/ic_service.png">'
MK = f'<div class="mk"><img src="{A}/logos/logo_blanco.png"></div>'
def phone(src, style): return f'<div class="ph" style="{style}"><img src="file://{OUT}/_{src}.png"></div><div class="fade"></div>'
pages = {
 1: f'''<div class="glow" style="right:-300px;top:-200px"></div>
<div class="t"><span class="k">{IC}FLOTAS · REMISES · CAMIONES</span><h1>¿Cuántos km<br>hizo cada vehículo<br><span>este mes?</span></h1>
<p>Si tuviste que pensarlo, deslizá →</p></div>
<div style="position:absolute;left:80px;top:740px;display:flex;gap:20px;align-items:flex-end"><div style="width:140px;height:190px;border-radius:24px;background:#123540;border:3px solid #1EBDBA;display:flex;align-items:center;justify-content:center;font-weight:700;font-size:120px;color:#3FD6D2">?</div><div style="width:140px;height:190px;border-radius:24px;background:#123540;border:3px solid #1EBDBA;display:flex;align-items:center;justify-content:center;font-weight:700;font-size:120px;color:#3FD6D2">?</div><div style="width:140px;height:190px;border-radius:24px;background:#123540;border:3px solid #1EBDBA;display:flex;align-items:center;justify-content:center;font-weight:700;font-size:120px;color:#3FD6D2">?</div><div style="width:140px;height:190px;border-radius:24px;background:#123540;border:3px solid #1EBDBA;display:flex;align-items:center;justify-content:center;font-weight:700;font-size:120px;color:#3FD6D2">?</div><div style="width:140px;height:190px;border-radius:24px;background:#123540;border:3px solid #1EBDBA;display:flex;align-items:center;justify-content:center;font-weight:700;font-size:120px;color:#3FD6D2">?</div><div style="font-weight:700;font-size:60px;margin-left:6px">km</div></div><div style="position:absolute;left:80px;top:1000px;font-weight:500;font-size:30px;color:#8FBFBD">Cada auto, cada remís, cada camión.</div>{MK}<div class="pg">1/4</div>''',
 2: f'''<div class="glow" style="left:-350px;top:-250px"></div>
<div class="t"><span class="k">{IC}GF SERVICE</span><h1>Los km<br><span>se cargan solos.</span></h1>
<p>Salen del GPS de cada vehículo.<br>Nadie tiene que anotar nada.</p></div>
{phone('service_flota','left:200px;right:200px;top:640px')}{MK}<div class="pg">2/4</div>''',
 3: f'''<div class="glow" style="right:-350px;top:-250px"></div>
<div class="t"><span class="k">{IC}GF SERVICE</span><h1>Te avisa<br><span>antes del service.</span></h1>
<p>Aceite, filtros, VTV: vencidos,<br>próximos y al día, de un vistazo.</p></div>
{phone('service_avisos','left:200px;right:200px;top:640px')}{MK}<div class="pg">3/4</div>''',
 4: f'''<div class="glow" style="left:-300px;bottom:-250px"></div>
<div class="t" style="top:150px"><span class="k">{IC}GF SERVICE</span>
<h1 style="font-size:80px">Gratis para<br><span>clientes GPS Fácil.</span></h1>
<div style="margin-top:90px">
<div class="li"><b>✓</b><div>Sin contrato ni permanencia</div></div>
<div class="li"><b>✓</b><div>Instalamos en Mendoza y Buenos Aires<small>o lo instala tu técnico</small></div></div>
<div class="li"><b>✓</b><div>Ubicación en tiempo real<small>y los km de cada vehículo, en tu celular</small></div></div>
</div></div>
<div style="position:absolute;left:80px;bottom:160px;font-weight:700;font-size:38px;line-height:1.45">Consultanos<br><span style="color:#3FD6D2">www.gpsfacil.com</span> · 261 533-8863</div>
{MK}<div class="pg">4/4</div>''',
}
with sync_playwright() as p:
    b = p.chromium.launch(); pg = b.new_page(viewport={'width': 1080, 'height': 1350})
    tmp = f'{OUT}/_s.html'
    for n, h in pages.items():
        open(tmp, 'w').write(f'<html><head><meta charset="utf-8"><style>{CSS}</style></head><body>{h}</body></html>')
        pg.goto(f'file://{tmp}'); pg.wait_for_timeout(400); pg.screenshot(path=f'{OUT}/_t.png')
        Image.open(f'{OUT}/_t.png').convert('RGB').save(f'{OUT}/flota-km_{n}.jpg', quality=92)
    b.close()
for f in os.listdir(OUT):
    if f.startswith('_'): os.remove(f'{OUT}/{f}')
print('ok')
