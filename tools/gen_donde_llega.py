# Carrusel "¿Hasta dónde llega GPS Fácil?" — mapas de puntos (global-land-mask) + HTML + Playwright
# Uso: python3 tools/gen_donde_llega.py  (desde la raíz del repo)
import os, math, numpy as np
from global_land_mask import globe
from playwright.sync_api import sync_playwright
from PIL import Image

ROOT = os.path.abspath(os.path.dirname(__file__) + '/..')
OUT = f'{ROOT}/2026-11/donde-llega'
os.makedirs(OUT, exist_ok=True)
F = '/usr/share/fonts/truetype/google-fonts'
CSS = f'''@font-face{{font-family:P;src:url({F}/Poppins-Bold.ttf);font-weight:700}}
@font-face{{font-family:P;src:url({F}/Poppins-Medium.ttf);font-weight:500}}
*{{box-sizing:border-box}}body{{margin:0;width:1080px;height:1350px;font-family:P;overflow:hidden;position:relative;background:#0F2A33;color:#fff}}
.t{{position:absolute;left:80px;right:80px;top:90px}}
.k{{display:inline-flex;align-items:center;gap:12px;background:rgba(255,255,255,.08);font-weight:700;font-size:24px;letter-spacing:3px;padding:12px 24px;border-radius:40px}}
.k.tq{{background:#1EBDBA;color:#0F2A33}}
h1{{font-weight:700;font-size:84px;line-height:1.03;margin:28px 0 18px}}h1 span{{color:#3FD6D2}}
p{{font-weight:500;font-size:34px;margin:0;line-height:1.35;color:#BFE6E4}}
.mk{{position:absolute;left:60px;bottom:44px}}.mk img{{height:62px;display:block}}
.pg{{position:absolute;right:60px;bottom:58px;font-weight:500;font-size:26px;color:#8FBFBD}}
.glow{{position:absolute;width:900px;height:900px;border-radius:50%;background:radial-gradient(circle,rgba(30,189,186,.30),rgba(30,189,186,0) 70%)}}
.card{{position:absolute;left:60px;right:60px;border-radius:44px;overflow:hidden;background:#123540;box-shadow:0 30px 70px rgba(0,0,0,.35)}}
.tag{{position:absolute;background:#1EBDBA;color:#0F2A33;font-weight:700;font-size:28px;padding:10px 22px;border-radius:30px;white-space:nowrap}}
'''
LOGO = f'file://{ROOT}/assets/logos/logo_blanco.png'
MK = f'<div class="mk"><img src="{LOGO}"></div>'
PIN = '<svg viewBox="0 0 24 24" width="{s}" height="{s}" style="position:absolute;left:{x}px;top:{y}px;transform:translate(-50%,-100%);filter:drop-shadow(0 6px 10px rgba(0,0,0,.4))"><path fill="#1EBDBA" d="M12 1.5a8 8 0 0 0-8 8c0 6 8 13 8 13s8-7 8-13a8 8 0 0 0-8-8z"/><circle cx="12" cy="9.5" r="3.2" fill="#0F2A33"/></svg>'

def dotmap(w, h, lon0, lon1, lat0, lat1, step, r, color='#2E6A72'):
    """SVG de puntos de tierra en proyección equirectangular. Devuelve (svg, proj)."""
    def proj(lat, lon):
        return (lon - lon0) / (lon1 - lon0) * w, (lat1 - lat) / (lat1 - lat0) * h
    dots = []
    nx, ny = int(w / step), int(h / step)
    for j in range(ny + 1):
        for i in range(nx + 1):
            x, y = i * step + step / 2, j * step + step / 2
            lon = lon0 + x / w * (lon1 - lon0); lat = lat1 - y / h * (lat1 - lat0)
            if -90 < lat < 90 and globe.is_land(lat, ((lon + 180) % 360) - 180):
                dots.append(f'<circle cx="{x:.1f}" cy="{y:.1f}" r="{r}"/>')
    return f'<g fill="{color}">{"".join(dots)}</g>', proj

def arc(p0, p1, bend=0.25):
    (x0, y0), (x1, y1) = p0, p1
    mx, my = (x0 + x1) / 2, (y0 + y1) / 2
    d = math.hypot(x1 - x0, y1 - y0)
    cx, cy = mx, my - d * bend
    return f'<path d="M{x0:.0f},{y0:.0f} Q{cx:.0f},{cy:.0f} {x1:.0f},{y1:.0f}" fill="none" stroke="#3FD6D2" stroke-width="4" stroke-dasharray="2 12" stroke-linecap="round"/>'

MZA = (-32.89, -68.83)
pages = {}

# 1 — portada: mundo con arcos desde Mendoza
W, H = 960, 560
svg, pr = dotmap(W, H, -170, 190, -58, 75, 12, 3.6)
pts = {'Mendoza': MZA, 'Paraná': (-33.0, -60.0), 'Barcelona': (41.39, 2.17), 'Sídney': (-33.87, 151.2)}
P = {k: pr(*v) for k, v in pts.items()}
del P['Paraná']
arcs = arc(P['Mendoza'], P['Barcelona'], .3) + arc(P['Mendoza'], P['Sídney'], .28)
pins = ''.join(PIN.format(s=46, x=f'{x:.0f}', y=f'{y:.0f}') for x, y in P.values())
labels = ''.join(f'<div style="position:absolute;left:{x+18:.0f}px;top:{y-6:.0f}px;font-weight:700;font-size:22px;color:#fff;text-shadow:0 2px 8px #0F2A33">{n}</div>'
                 for n, (x, y) in P.items())
pages[1] = f'''<div class="glow" style="right:-300px;top:-250px"></div>
<div class="t"><span class="k tq">CASOS REALES</span><h1>¿Hasta dónde<br><span>llega un GPS Fácil?</span></h1>
<p>Más lejos de lo que pensás. Deslizá →</p></div>
<div class="card" style="top:540px;height:640px;background:#0F2A33;box-shadow:none">
<div style="position:absolute;left:0;top:50px;width:{W}px;height:{H}px"><svg width="{W}" height="{H}">{svg}{arcs}</svg>{pins}{labels}</div></div>
{MK}<div class="pg">1/6</div>'''

def case_slide(n, kicker, title, sub, region, place, label, extra=''):
    lon0, lon1, lat0, lat1, step, r = region
    w, h = 960, 640
    svg, pr = dotmap(w, h, lon0, lon1, lat0, lat1, step, r)
    x, y = pr(*place)
    return f'''<div class="glow" style="left:-350px;top:-300px"></div>
<div class="t"><span class="k">{kicker}</span><h1>{title}</h1><p>{sub}</p></div>
<div class="card" style="top:590px;height:{h}px"><svg width="{w}" height="{h}">{svg}
<circle cx="{x:.0f}" cy="{y:.0f}" r="70" fill="rgba(30,189,186,.18)"/><circle cx="{x:.0f}" cy="{y:.0f}" r="34" fill="rgba(30,189,186,.30)"/></svg>
{PIN.format(s=86, x=f"{x:.0f}", y=f"{y+10:.0f}")}{extra}
<div class="tag" style="{f"right:{w-x+60:.0f}px" if x>w-320 else f"left:{x+60:.0f}px"};top:{y-30:.0f}px">{label}</div></div>
{MK}<div class="pg">{n}/6</div>'''

pages[2] = case_slide(2, 'EMBARCACIONES', 'Lanchas en<br><span>el río Paraná.</span>', 'Cada lancha, en el mapa en tiempo real.',
                      (-84, -34, -50, -12, 13, 4.6), (-32.4, -60.6), '🚤 Río Paraná')
pages[3] = case_slide(3, 'EQUIPOS', 'Sillones masajeadores<br><span>en Barcelona.</span>', 'Un cliente en España sabía dónde<br>estaba cada uno de sus equipos.',
                      (-14, 26, 30, 56, 13, 4.6), (41.39, 2.17), '📍 Barcelona')
pages[4] = case_slide(4, 'PERSONAS', 'De Mendoza<br><span>a Sídney.</span>', 'Seguimiento de una persona<br>del otro lado del mundo.',
                      (108, 165, -46, -8, 13, 4.6), (-33.87, 151.2), '📍 Sídney')
# 5 — Aconcagua con foto real
foto = f'file://{ROOT}/assets/fotos/aconcagua_andinista.jpg'
pages[5] = f'''<div style="position:absolute;inset:0;background:url({foto}) 62% 50%/cover"></div>
<div style="position:absolute;inset:0;background:linear-gradient(180deg,rgba(15,42,51,.92) 0%,rgba(15,42,51,.55) 38%,rgba(15,42,51,0) 60%,rgba(15,42,51,.75) 100%)"></div>
<div class="t"><span class="k tq">ACONCAGUA · 6.962 m</span><h1>Hasta la cumbre,<br><span>sin señal.</span></h1>
<p>Lo probamos donde no llega el celular.</p></div>
{MK}<div class="pg" style="color:#fff">5/6</div>'''
pages[6] = f'''<div class="glow" style="right:-300px;bottom:-200px"></div>
<div class="t" style="top:150px"><span class="k tq">¿Y VOS?</span>
<h1 style="font-size:92px">Si le entra<br>un GPS,<br><span>lo monitoreás.</span></h1>
<p>Autos, flotas, camiones, máquinas,<br>equipos de estética, bicis, mascotas.<br><br>¿Qué querés tener ubicado?<br>Contanos en los comentarios 👇</p></div>
<div style="position:absolute;left:80px;bottom:150px;font-weight:700;font-size:34px;line-height:1.5"><span style="color:#3FD6D2">www.gpsfacil.com</span><br>261 533-8863</div>
{MK}<div class="pg">6/6</div>'''

with sync_playwright() as p:
    b = p.chromium.launch(); pg = b.new_page(viewport={'width': 1080, 'height': 1350})
    tmp = f'{OUT}/_s.html'
    for n, h in pages.items():
        open(tmp, 'w').write(f'<html><head><meta charset="utf-8"><style>{CSS}</style></head><body>{h}</body></html>')
        pg.goto(f'file://{tmp}'); pg.wait_for_timeout(400)
        pg.screenshot(path=f'{OUT}/_t.png')
        Image.open(f'{OUT}/_t.png').convert('RGB').save(f'{OUT}/donde-llega_{n}.jpg', quality=92)
    b.close(); os.remove(tmp); os.remove(f'{OUT}/_t.png')
print('ok')
