from playwright.sync_api import sync_playwright
CSS=open('gen.py').read().split("CSS='''")[1].split("'''")[0]
h='''<div class="glow" style="right:-300px;top:-250px"></div>
<div class="t"><span class="k"><img src="ic_radar.png">BICIS ELÉCTRICAS</span><h1>El GPS va adentro.<br><span>No se ve.</span></h1>
<p>Si alguien se la lleva, vos sabés dónde está.</p></div>
<div style="position:absolute;left:0;right:0;top:560px;height:560px;background:url(bici.png) center/cover;border-top:6px solid #1EBDBA;border-bottom:6px solid #1EBDBA"></div>
<div style="position:absolute;left:80px;right:80px;top:1160px;font-weight:500;font-size:28px;color:#BFE6E4">Probado en una MATE. Gracias a Mate por prestarnos la bici.</div>
<div class="mk"><img src="logo_blanco.png"></div>'''
with sync_playwright() as p:
    b=p.chromium.launch(); pg=b.new_page(viewport={'width':1080,'height':1350})
    open('s.html','w').write(f'<html><head><style>{CSS}</style></head><body>{h}</body></html>')
    pg.goto('file:///home/claude/apps/s.html'); pg.wait_for_timeout(400); pg.screenshot(path='p_bici.png'); b.close()
