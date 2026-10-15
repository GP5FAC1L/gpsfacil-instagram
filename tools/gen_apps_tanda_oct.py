from PIL import Image
from playwright.sync_api import sync_playwright
import os
# 1) wrap 9:16 store screenshots into 4:5 slides
def wrap(src,out):
    im=Image.open(src).convert('RGB'); W,H=1080,1350
    s=im.resize((round(im.width*H/im.height),H),Image.LANCZOS)
    bg=Image.new('RGB',(W,H))
    left=s.crop((0,0,4,H)).resize(((W-s.width)//2+2,H)); right=s.crop((s.width-4,0,s.width,H)).resize((W-(W-s.width)//2-s.width+2,H))
    bg.paste(left,(0,0)); bg.paste(right,((W-s.width)//2+s.width-1,0)); bg.paste(s,((W-s.width)//2,0)); bg.save(out)
for i in [1,2,3,4,5,6,8,9,10,11,13,14,15,16,17]: wrap(f'src_{i:02d}.png',f'w_{i:02d}.png')
# phone crops (phone region of screenshot) for covers
for i in [1,9,14,15,17]:
    Image.open(f'src_{i:02d}.png').crop((80,280,730,1440)).save(f'ph_{i:02d}.png')
CSS='''@font-face{font-family:P;src:url(/usr/share/fonts/truetype/google-fonts/Poppins-Bold.ttf);font-weight:700}
@font-face{font-family:P;src:url(/usr/share/fonts/truetype/google-fonts/Poppins-Medium.ttf);font-weight:500}
*{box-sizing:border-box}body{margin:0;width:1080px;height:1350px;font-family:P;overflow:hidden;position:relative;background:#0F2A33;color:#fff}
.t{position:absolute;left:80px;right:80px;top:90px}
.k{display:inline-flex;align-items:center;gap:14px;background:rgba(255,255,255,.08);font-weight:700;font-size:24px;letter-spacing:3px;padding:10px 22px 10px 12px;border-radius:40px}
.k img{width:48px;height:48px;border-radius:12px}
h1{font-weight:700;font-size:84px;line-height:1.03;margin:28px 0 18px}h1 span{color:#3FD6D2}
p{font-weight:500;font-size:34px;margin:0;line-height:1.35;color:#BFE6E4}
.ph{position:absolute;border-radius:56px;overflow:hidden;box-shadow:0 40px 90px rgba(0,0,0,.5)}
.ph img{display:block;width:100%}
.mk{position:absolute;left:60px;bottom:44px}.mk img{height:62px;display:block}
.glow{position:absolute;width:900px;height:900px;border-radius:50%;background:radial-gradient(circle,rgba(30,189,186,.35),rgba(30,189,186,0) 70%)}
.foot{position:absolute;left:0;right:0;bottom:0;height:220px;background:#fff;display:flex;align-items:center;justify-content:space-between;padding:0 72px}
.foot img{height:290px;margin-left:-40px}.foot div{text-align:right;font-weight:500;font-size:30px;color:#222;line-height:1.6}.foot b{color:#1EBDBA}
.bar{position:absolute;left:0;right:0;bottom:220px;height:10px;background:#1EBDBA}
.gp{display:inline-flex;align-items:center;gap:14px;background:#fff;color:#0F2A33;border-radius:20px;padding:16px 28px;font-weight:700;font-size:30px}
.gp svg{width:40px;height:40px}
'''
GP='<svg viewBox="0 0 24 24"><path fill="#0F2A33" d="M3.6 1.8 13.5 12l-9.9 10.2c-.4-.2-.6-.6-.6-1.1V2.9c0-.5.2-.9.6-1.1zm11 11.3 2.6 2.6-11.6 6.6 9-9.2zm3.7-3.7 2.9 1.7c.8.5.8 1.3 0 1.8l-2.9 1.7-2.8-2.6 2.8-2.6zM5.6 1.7l11.6 6.6-2.6 2.6-9-9.2z"/></svg>'
MK='<div class="mk"><img src="logo_blanco.png"></div>'
def cover(icon,kick,h1,p,ph,phstyle):
    return f'''<div class="glow" style="right:-300px;bottom:-200px"></div>
<div class="t"><span class="k"><img src="{icon}">{kick}</span><h1>{h1}</h1><p>{p}</p></div>
<div class="ph" style="{phstyle}"><img src="{ph}"></div>{MK}'''
def cta(app,icon,line):
    return f'''<div class="glow" style="left:-300px;top:-300px"></div>
<div class="t" style="top:110px"><img src="{icon}" style="width:150px;border-radius:34px">
<h1 style="font-size:76px;margin-top:36px">{app}<br><span>gratis para clientes.</span></h1>
<p>{line}</p><div style="margin-top:44px"><span class="gp">Consultanos por WhatsApp</span></div></div>
<div class="bar"></div><div class="foot"><img src="logo.png"><div><b>www.gpsfacil.com</b><br>261 533-8863</div></div>'''
pages={
 'service_00':cover('ic_service.png','GF SERVICE','Tu flota,<br><span>siempre al día.</span>','Services, vencimientos y gastos<br>de cada vehículo, en una app.','ph_01.png','right:70px;top:560px;width:470px;transform:rotate(-5deg)'),
 'service_99':cta('GF Service','ic_service.png','Los kilómetros se cargan solos<br>desde tu equipo GPS Fácil.'),
 'radar_00':cover('ic_radar.png','GF RADAR','¿Dónde está?<br><span>La app te lleva.</span>','Vehículos, mascotas y objetos:<br>distancia, dirección y cómo llegar.','ph_14.png','right:70px;top:560px;width:470px;transform:rotate(-5deg)'),
 'radar_99':cta('GF Radar','ic_radar.png','Funciona con los equipos y tags<br>de GPS Fácil.'),
 'estetica_00':cover('ic_estetica.png','GF ESTÉTICA','Tus equipos,<br><span>bajo control.</span>','Horas de uso, mantenimientos<br>y bloqueo, desde tu celular.','ph_09.png','right:70px;top:560px;width:470px;transform:rotate(-5deg)'),
 'estetica_99':cta('GF Estética','ic_estetica.png','Funciona con los equipos GPS Fácil<br>instalados en tus máquinas.'),
 'mascota':f'''<div class="glow" style="right:-300px;bottom:-250px"></div>
<div class="t"><span class="k"><img src="ic_radar.png">MASCOTAS</span><h1>¿Se escapó?<br><span>Un pip te guía.</span></h1>
<p>Con el tag GPS Fácil en el collar,<br>GF Radar te lleva hasta la zona<br>y la brújula, los últimos metros.</p></div>
<div class="ph" style="right:70px;top:610px;width:440px;transform:rotate(-5deg)"><img src="ph_15.png"></div>
<div style="position:absolute;left:80px;top:990px;font-weight:700;font-size:40px;line-height:1.25">🐾 En el collar<br>📍 En el mapa<br>🧭 Con brújula</div>{MK}''',
 'bloqueo':f'''<div class="glow" style="right:-300px;bottom:-250px"></div>
<div class="t"><span class="k"><img src="ic_radar.png">BLOQUEO REMOTO</span><h1>Bloqueá tu vehículo<br><span>desde el celular.</span></h1>
<p>Un botón en la app y listo.</p></div>
<div class="ph" style="right:70px;top:560px;width:460px;transform:rotate(-5deg)"><img src="ph_17.png"></div>
<div style="position:absolute;left:80px;top:760px;width:440px;font-weight:500;font-size:28px;line-height:1.45;color:#BFE6E4;background:rgba(255,255,255,.06);border-left:6px solid #1EBDBA;border-radius:18px;padding:26px 28px">Requiere que el GPS se instale <b style="color:#fff">con corte de motor</b>. ¿No sabés si el tuyo lo tiene? Consultanos.</div>{MK}''',
 'apps':f'''<div class="glow" style="left:-300px;top:-300px"></div>
<div class="t"><span class="k" style="padding-left:22px">EL SET DE APPS</span><h1 style="font-size:78px">Una app para<br><span>cada necesidad.</span></h1></div>
<div style="position:absolute;left:80px;right:80px;top:470px;display:flex;flex-direction:column;gap:34px">
''' + ''.join(f'''<div style="display:flex;align-items:center;gap:34px;background:rgba(255,255,255,.06);border-radius:32px;padding:26px 30px">
<img src="{i}" style="width:130px;border-radius:30px;flex:none"><div><div style="font-weight:700;font-size:42px">{n}</div><div style="font-weight:500;font-size:28px;color:#BFE6E4;line-height:1.3">{d}</div></div></div>''' for i,n,d in [
 ('ic_radar.png','GF Radar','Dónde está lo tuyo y cómo llegar'),
 ('ic_service.png','GF Service','Services, vencimientos y gastos de tu flota'),
 ('ic_estetica.png','GF Estética','Horas de uso y mantenimiento de tus equipos')]) + f'''</div>
<div style="position:absolute;left:80px;bottom:120px"><span class="gp">Incluidas gratis para clientes GPS Fácil</span></div>{MK}''',
}
with sync_playwright() as p:
    b=p.chromium.launch(); pg=b.new_page(viewport={'width':1080,'height':1350})
    for n,h in pages.items():
        open('s.html','w').write(f'<html><head><style>{CSS}</style></head><body>{h}</body></html>')
        pg.goto('file:///home/claude/apps/s.html'); pg.wait_for_timeout(350); pg.screenshot(path=f'p_{n}.png')
    b.close()
# assemble final sets
os.makedirs('out',exist_ok=True)
sets={'service':['p_service_00']+[f'w_{i:02d}' for i in [1,2,3,4,5,6]]+['p_service_99'],
      'radar':['p_radar_00']+[f'w_{i:02d}' for i in [13,14,15,16]]+['p_radar_99'],
      'estetica':['p_estetica_00']+[f'w_{i:02d}' for i in [8,9,10,11]]+['p_estetica_99'],
      'mascota':['p_mascota'],'bloqueo':['p_bloqueo'],'apps':['p_apps']}
for k,v in sets.items():
    for j,f in enumerate(v,1): Image.open(f+'.png').convert('RGB').save(f'out/{k}_{j}.jpg',quality=92)
    ims=[Image.open(f+'.png').resize((216,270)) for f in v]
    c=Image.new('RGB',(226*len(ims),270),'white')
    for j,im in enumerate(ims): c.paste(im,(j*226,0))
    c.save(f'prev_{k}.png')
