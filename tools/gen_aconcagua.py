from playwright.sync_api import sync_playwright
CSS='''@font-face{font-family:P;src:url(/usr/share/fonts/truetype/google-fonts/Poppins-Bold.ttf);font-weight:700}
@font-face{font-family:P;src:url(/usr/share/fonts/truetype/google-fonts/Poppins-Medium.ttf);font-weight:500}
body{margin:0;width:1080px;height:1350px;font-family:P;overflow:hidden;position:relative;background:#0F2A33;color:#fff}
.ph{position:absolute;inset:0;background-size:cover}
.g{position:absolute;inset:0}
.t{position:absolute;left:80px;right:80px}
.k{display:inline-block;background:#1EBDBA;font-weight:700;font-size:24px;letter-spacing:3px;padding:8px 20px;border-radius:40px}
h1{font-weight:700;font-size:78px;line-height:1.04;margin:22px 0 14px;text-shadow:0 4px 24px rgba(0,0,0,.35)}
h1 span{color:#3FD6D2}
p{font-weight:500;font-size:34px;margin:0;line-height:1.35;text-shadow:0 2px 12px rgba(0,0,0,.4)}
.n{position:absolute;right:56px;bottom:46px;font-weight:500;font-size:24px;opacity:.85}
.mk{position:absolute;left:56px;bottom:44px}.mk img{height:62px;display:block}
'''
TOP='linear-gradient(180deg,rgba(6,25,35,.82) 0%,rgba(6,25,35,.35) 32%,rgba(0,0,0,0) 50%,rgba(0,0,0,.35) 100%)'
BOT='linear-gradient(0deg,rgba(6,25,35,.88) 0%,rgba(6,25,35,.4) 34%,rgba(0,0,0,0) 55%)'
mark='<div class="mk"><img src="logo_blanco.png"></div>'
def photo(img,pos,grad,text,where,n):
    return f'<div class="ph" style="background-image:url({img});background-position:{pos}"></div><div class="g" style="background:{grad}"></div><div class="t" style="{where}">{text}</div>{mark}<div class="n">{n}/7</div>'
waves='''<svg style="position:absolute;left:340px;top:560px" width="400" height="400" viewBox="0 0 400 400">
<g fill="none" stroke="#3FD6D2" stroke-linecap="round">
<circle cx="200" cy="200" r="22" fill="#3FD6D2" stroke="none"/>
<circle cx="200" cy="200" r="70" stroke-width="9" opacity=".9"/>
<circle cx="200" cy="200" r="125" stroke-width="7" opacity=".6"/>
<circle cx="200" cy="200" r="185" stroke-width="5" opacity=".3"/></g></svg>'''
S=[
 photo('mulas.jpg','10% 50%',TOP,'<span class="k">MENDOZA · ARGENTINA</span><h1>Aconcagua.<br><span>Sin señal.</span></h1><p>Ahí quisimos probar nuestra tecnología.</p>','top:80px',1),
 photo('andinista.jpg','52% 50%',TOP,'<h1>Subimos con<br><span>GPS Fácil</span><br>en la mochila.</h1>','top:80px',2),
 photo('refugio.jpg','40% 50%','linear-gradient(180deg,rgba(6,25,35,.55),rgba(6,25,35,.35) 40%,rgba(6,25,35,.85))',waves+'<span class="k">PLAZA DE MULAS · 4.300 m</span><h1>Montamos<br><span>nuestra propia red.</span></h1>','top:80px',3),
 photo('mochila.jpg','50% 40%',BOT,'<h1>Un dispositivo.<br><span>Un botón.</span></h1><p>Liviano, a mano, siempre encendido.</p>','bottom:120px',4),
 photo('equipo.jpg','70% 30%',TOP,'<h1>Seguimiento<br><span>en tiempo real.</span></h1><p>Donde el celular no tiene cobertura.</p>','top:80px',5),
 photo('cumbre.jpg','50% 40%',TOP,'<span class="k">CUMBRE</span><h1>6.962 metros.<br><span>Y seguía<br>transmitiendo.</span></h1>','top:80px',6),
 '''<img src="pin.png" style="position:absolute;right:-170px;top:-130px;width:720px;opacity:.10">
<div class="t" style="top:380px"><h1 style="font-size:84px">Tecnología que llega<br><span>donde otros no.</span></h1>
<p style="color:#9FDCDA;margin-top:30px">Desarrollo propio, probado en el techo de América.</p></div>
<div style="position:absolute;left:0;right:0;bottom:0;height:230px;background:#fff;display:flex;align-items:center;justify-content:space-between;padding:0 72px;box-sizing:border-box">
<img src="logo.png" style="height:300px;margin-left:-40px"><div style="text-align:right;font-weight:500;font-size:30px;color:#222;line-height:1.6"><b style="color:#1EBDBA">www.gpsfacil.com</b><br>261 533-8863</div></div>
<div style="position:absolute;left:0;right:0;bottom:230px;height:10px;background:#1EBDBA"></div>''',
]
with sync_playwright() as p:
    b=p.chromium.launch(); pg=b.new_page(viewport={'width':1080,'height':1350})
    for i,s in enumerate(S,1):
        open('s.html','w').write(f'<html><head><style>{CSS}</style></head><body>{s}</body></html>')
        pg.goto('file:///home/claude/aconcagua/s.html'); pg.wait_for_timeout(400)
        pg.screenshot(path=f'aconcagua_{i}.png')
    b.close()
