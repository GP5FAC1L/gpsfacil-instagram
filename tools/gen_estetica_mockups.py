from playwright.sync_api import sync_playwright
CSS='''@font-face{font-family:P;src:url(/usr/share/fonts/truetype/google-fonts/Poppins-Bold.ttf);font-weight:700}
@font-face{font-family:P;src:url(/usr/share/fonts/truetype/google-fonts/Poppins-Bold.ttf);font-weight:600}
@font-face{font-family:P;src:url(/usr/share/fonts/truetype/google-fonts/Poppins-Medium.ttf);font-weight:500}
*{box-sizing:border-box}
body{margin:0;width:1080px;height:1350px;font-family:P;overflow:hidden;position:relative;background:#0F2A33;color:#fff}
.lt{background:#F2F7F7;color:#0F2A33}
.t{position:absolute;left:80px;right:80px;top:90px}
.k{display:inline-block;background:#1EBDBA;color:#fff;font-weight:700;font-size:24px;letter-spacing:3px;padding:8px 20px;border-radius:40px}
h1{font-weight:700;font-size:80px;line-height:1.04;margin:24px 0 16px}
h1 span{color:#1EBDBA}
body:not(.lt) h1 span{color:#3FD6D2}
p{font-weight:500;font-size:34px;margin:0;line-height:1.35;opacity:.85}
.n{position:absolute;right:60px;bottom:48px;font-weight:500;font-size:24px;opacity:.6}
.mk{position:absolute;left:60px;bottom:40px;display:flex;align-items:center;gap:10px;font-weight:700;font-size:26px}
.mk img{height:44px}
body:not(.lt) .mk img{filter:brightness(0) invert(1)}
.ph{position:absolute;width:430px;height:860px;border-radius:64px;background:#0B1F26;padding:18px;box-shadow:0 40px 80px rgba(0,0,0,.35)}
.sc{width:100%;height:100%;border-radius:48px;background:#fff;color:#0F2A33;overflow:hidden;position:relative;padding:70px 30px 30px}
.nt{position:absolute;top:18px;left:50%;transform:translateX(-50%);width:130px;height:34px;border-radius:20px;background:#0B1F26}
.ah{font-weight:700;font-size:30px;margin-bottom:22px;display:flex;align-items:center;gap:10px}
.ah img{height:38px}
.cd{background:#F2F7F7;border-radius:24px;padding:22px 24px;margin-bottom:16px}
.cl{font-weight:500;font-size:20px;color:#5B7178}
.cv{font-weight:700;font-size:44px}
.bar{height:14px;border-radius:8px;background:#DDE8E8;margin-top:12px;overflow:hidden}
.bar i{display:block;height:100%;background:#1EBDBA;border-radius:8px}
.row{display:flex;justify-content:space-between;align-items:center;font-weight:600;font-size:22px;padding:14px 0;border-bottom:1px solid #E3ECEC}
.dot{width:16px;height:16px;border-radius:50%;display:inline-block;margin-right:10px}
.al{background:#FFF3E5;border-left:8px solid #F59E0B;border-radius:18px;padding:18px 20px;margin-bottom:14px;font-weight:600;font-size:22px}
.al small{display:block;font-weight:500;font-size:18px;color:#7A5A2E;margin-top:4px}
.bt{border-radius:30px;padding:28px;text-align:center;font-weight:700;font-size:30px;color:#fff}
.tg{width:60px;height:34px;border-radius:20px;background:#1EBDBA;position:relative}
.tg:after{content:"";position:absolute;right:4px;top:4px;width:26px;height:26px;border-radius:50%;background:#fff}
'''
def mk(): return '<div class="mk"><img src="pin.png">GPS Fácil</div>'
def head(): return '<div class="nt"></div><div class="ah"><img src="pin.png">Estética</div>'
S=[]
# 1 portada
S.append(('lt','''<div class="t"><span class="k">EQUIPOS DE ESTÉTICA</span>
<h1>Tu equipo trabaja.<br><span>¿Vos sabés cuánto?</span></h1>
<p>Ubicación, horas de uso y control,<br>desde tu celular.</p></div>
<img src="maq_blanca.png" style="position:absolute;left:250px;top:560px;width:640px;mix-blend-mode:multiply">'''+mk()))
# 2 ubicacion
S.append(('','''<div style="position:absolute;inset:0;background:url(maq_real.png) center 70%/cover"></div>
<div style="position:absolute;inset:0;background:linear-gradient(180deg,rgba(15,42,51,.95) 0%,rgba(15,42,51,.75) 30%,rgba(15,42,51,.1) 55%,rgba(15,42,51,.7) 100%)"></div>
<div style="position:absolute;right:70px;bottom:130px;width:440px;background:#fff;border-radius:32px;padding:20px;box-shadow:0 30px 60px rgba(0,0,0,.4);color:#0F2A33">
<svg width="400" height="230" viewBox="0 0 400 230" style="display:block;border-radius:20px;background:#E9F1EF">
<g stroke="#fff" stroke-width="14" fill="none"><path d="M-10 70 L410 120"/><path d="M120 -10 L160 240"/><path d="M300 -10 L260 240"/></g>
<g stroke="#fff" stroke-width="6" fill="none"><path d="M-10 180 L410 200"/><path d="M40 -10 L60 240"/></g>
<circle cx="210" cy="118" r="46" fill="#1EBDBA" opacity=".18"/>
<path d="M210 70c-18 0-32 14-32 32 0 24 32 52 32 52s32-28 32-52c0-18-14-32-32-32z" fill="#1EBDBA"/><circle cx="210" cy="102" r="12" fill="#fff"/></svg>
<div style="display:flex;justify-content:space-between;align-items:center;margin-top:16px;padding:0 6px">
<div><div style="font-weight:700;font-size:26px">Equipo 1</div><div style="font-weight:500;font-size:20px;color:#5B7178">Gabinete Centro · ahora</div></div>
<div style="background:#E6F7F6;color:#1EBDBA;font-weight:700;font-size:20px;padding:8px 16px;border-radius:20px">En línea</div></div></div>
<div class="t"><span class="k">UBICACIÓN</span><h1>Sabé dónde está<br><span>cada máquina.</span></h1>
<p>En el gabinete, en traslado o en otro local:<br>la ves en el mapa en tiempo real.</p></div>'''+mk()))
# 3 horas
S.append(('lt','''<div class="t"><span class="k">HORAS DE USO</span><h1>Cada hora,<br><span>registrada.</span></h1>
<p>Sabé cuánto trabajó cada equipo,<br>sin depender de lo que te cuenten.</p></div>
<div class="ph" style="right:90px;top:520px;transform:rotate(-4deg);height:760px"><div class="sc">'''+head()+'''
<div class="cd"><div class="cl">Láser diodo · Equipo 1</div><div class="cv">126 h</div><div class="cl">este mes</div><div class="bar"><i style="width:72%"></i></div></div>
<div class="row"><span><i class="dot" style="background:#1EBDBA"></i>Lunes</span><span>6,5 h</span></div>
<div class="row"><span><i class="dot" style="background:#1EBDBA"></i>Martes</span><span>8 h</span></div>
<div class="row"><span><i class="dot" style="background:#1EBDBA"></i>Miércoles</span><span>7,2 h</span></div>
</div></div>
<div style="position:absolute;left:80px;top:700px;width:420px">
<div style="font-weight:700;font-size:40px;line-height:1.25">Ideal si<br><span style="color:#1EBDBA">alquilás equipos</span><br>o tenés varios<br>locales.</div></div>'''+mk()))
# 4 mantenimiento
S.append(('','''<div class="t"><span class="k">MANTENIMIENTO</span><h1>La app te avisa<br><span>antes de que falle.</span></h1>
<p>Service, cambio de filtros y revisiones,<br>todo agendado y notificado.</p></div>
<div class="ph" style="left:325px;top:540px;height:760px"><div class="sc">'''+head()+'''
<div class="al">Cambio de filtro<small>Equipo 2 · en 15 horas de uso</small></div>
<div class="al" style="background:#E6F7F6;border-color:#1EBDBA">Service programado<small style="color:#2E6B68">Equipo 1 · 22/10</small></div>
<div class="cd"><div class="cl">Equipos activos</div><div class="cv">3</div></div>
<div class="row"><span><i class="dot" style="background:#1EBDBA"></i>Equipo 1</span><span style="color:#1EBDBA">Al día</span></div>
<div class="row"><span><i class="dot" style="background:#F59E0B"></i>Equipo 2</span><span style="color:#F59E0B">Filtro</span></div>
<div class="row"><span><i class="dot" style="background:#1EBDBA"></i>Equipo 3</span><span style="color:#1EBDBA">Al día</span></div>
</div></div>'''+mk()))
# 5 bloqueo
S.append(('lt','''<div class="t"><span class="k">CONTROL DE USO</span><h1>Un botón.<br><span>Equipo bloqueado.</span></h1>
<p>Limitá el uso cuando lo necesites,<br>estés donde estés.</p></div>
<div class="ph" style="left:325px;top:560px;height:740px"><div class="sc">'''+head()+'''
<div class="cd"><div class="cl">Equipo 2 · Láser diodo</div><div class="cv" style="font-size:36px">Habilitado</div></div>
<div class="row"><span>Uso permitido</span><div class="tg"></div></div>
<div style="height:40px"></div>
<div class="bt" style="background:#E5484D">Restringir uso</div>
<div style="text-align:center;font-weight:500;font-size:19px;color:#5B7178;margin-top:18px">Podés volver a habilitarlo<br>en cualquier momento</div>
</div></div>'''+mk()))
# 6 cierre
S.append(('','''<img src="pin.png" style="position:absolute;right:-170px;top:-130px;width:720px;opacity:.10">
<div class="t" style="top:120px"><h1 style="font-size:76px">Monitoreo<br><span>autogestionado.</span></h1>
<div style="margin-top:50px;font-weight:500;font-size:36px;line-height:1.9">
<div>📍 Ubicación en tiempo real</div><div>⏱️ Horas de uso</div><div>🔧 Mantenimientos y filtros</div><div>🔒 Bloqueo remoto</div></div>
<p style="color:#9FDCDA;margin-top:44px;font-size:30px">Instalación en Mendoza y Buenos Aires,<br>o con tu técnico de confianza.</p></div>
<div style="position:absolute;left:0;right:0;bottom:0;height:220px;background:#fff;display:flex;align-items:center;justify-content:space-between;padding:0 72px">
<img src="logo.png" style="height:290px;margin-left:-40px"><div style="text-align:right;font-weight:500;font-size:30px;color:#222;line-height:1.6"><b style="color:#1EBDBA">www.gpsfacil.com</b><br>261 533-8863</div></div>
<div style="position:absolute;left:0;right:0;bottom:220px;height:10px;background:#1EBDBA"></div>'''))
with sync_playwright() as p:
    b=p.chromium.launch(); pg=b.new_page(viewport={'width':1080,'height':1350})
    for i,(cls,s) in enumerate(S,1):
        nn='' if i==6 else f'<div class="n">{i}/6</div>'
        open('s.html','w').write(f'<html><head><style>{CSS}</style></head><body class="{cls}">{s}{nn}</body></html>')
        pg.goto('file:///home/claude/estetica/s.html'); pg.wait_for_timeout(400)
        pg.screenshot(path=f'estetica_{i}.png')
    b.close()
from PIL import Image
ims=[Image.open(f'estetica_{i}.png').resize((360,450)) for i in range(1,7)]
c=Image.new('RGB',(370*3,460*2),'white')
for i,im in enumerate(ims): c.paste(im,((i%3)*370,(i//3)*460))
c.save('preview.png')
