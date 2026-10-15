from playwright.sync_api import sync_playwright
CSS=open('gen.py').read().split("CSS='''")[1].split("'''")[0]
h='''<div class="glow" style="right:-300px;top:-250px"></div>
<div class="t"><span class="k"><img src="ic_radar.png">BICIS ELÉCTRICAS</span><h1>Tu bici,<br><span>siempre ubicada.</span></h1>
<p>Sabé dónde está en todo momento,<br>desde tu celular.</p></div>
<div style="position:absolute;left:60px;right:60px;top:540px;height:600px;border-radius:44px;background:radial-gradient(circle at 50% 55%,#ffffff 0%,#EAF6F6 70%);box-shadow:0 30px 70px rgba(0,0,0,.35);overflow:hidden">
<img src="bici2.png" style="position:absolute;left:50%;top:50%;width:820px;transform:translate(-50%,-50%)"></div>
<div class="mk"><img src="logo_blanco.png"></div>
<div style="position:absolute;right:60px;bottom:52px;font-weight:700;font-size:28px;color:#3FD6D2">261 533-8863</div>'''
with sync_playwright() as p:
    b=p.chromium.launch(); pg=b.new_page(viewport={'width':1080,'height':1350})
    open('s.html','w').write(f'<html><head><style>{CSS}</style></head><body>{h}</body></html>')
    pg.goto('file:///home/claude/apps/s.html'); pg.wait_for_timeout(400); pg.screenshot(path='p_bici.png'); b.close()
