import csv,math,os,subprocess
from PIL import Image,ImageDraw,ImageFont,ImageFilter
P=[r for r in csv.DictReader(open('pts.csv')) if '2025-12-05'<=r['t'][:10]<='2025-12-08']
P.sort(key=lambda r:r['t'])
pts=[(float(r['lat']),float(r['lon']),r['t']) for r in P]
# drop jumps > 1.5 km between consecutive points
def dist(a,b):
    R=6371000;p1,p2=math.radians(a[0]),math.radians(b[0]);dp=p2-p1;dl=math.radians(b[1]-a[1])
    return 2*R*math.asin(math.sqrt(math.sin(dp/2)**2+math.cos(p1)*math.cos(p2)*math.sin(dl/2)**2))
clean=[pts[0]]
for p in pts[1:]:
    if dist(clean[-1],p)<600: clean.append(p)
for _ in range(3):
    out=[clean[0]]
    for i in range(1,len(clean)-1):
        a,b,c=out[-1],clean[i],clean[i+1]
        if dist(a,b)>120 and dist(b,c)>120 and dist(a,c)<0.6*min(dist(a,b),dist(b,c)): continue
        out.append(b)
    out.append(clean[-1]); clean=out
sm=[]
for i in range(len(clean)):
    w=clean[max(0,i-2):i+3]; sm.append((sum(p[0] for p in w)/len(w),sum(p[1] for p in w)/len(w),clean[i][2]))
clean=sm
# cut after summit approach (closest point to summit)
S=(-32.6532,-70.0109)
k=min(range(len(clean)),key=lambda i:dist(clean[i],S)); clean=clean[:k+1]
print(len(pts),len(clean),'summit dist',round(dist(clean[-1],S)))
lats=[p[0] for p in clean]; lons=[p[1] for p in clean]
la0,la1=min(lats),max(lats); lo0,lo1=min(lons+[S[1]]),max(lons+[S[1]])
cos=math.cos(math.radians((la0+la1)/2))
def proj(lat,lon,W,H,pad):
    sx=(lo1-lo0)*cos; sy=(la1-la0); s=min((W-2*pad)/sx,(H-2*pad)/sy)
    ox=(W-sx*s)/2; oy=(H-sy*s)/2
    return (ox+(lon-lo0)*cos*s, oy+(la1-lat)*s)
F=lambda w,s: ImageFont.truetype(f'/usr/share/fonts/truetype/google-fonts/Poppins-{w}.ttf',s)
LOGO=Image.open('/home/claude/apps/logo_blanco.png').convert('RGBA')
BG=(15,42,51); T=(30,189,186); T2=(63,214,210)
marks=[('Plaza de Mulas','4.300 m',(-32.6476,-70.0508)),('Nido de Cóndores','5.560 m',(-32.6373,-70.0295)),('Cumbre','6.962 m',S)]
def base(W,H,box):
    im=Image.new('RGB',(W,H),BG); d=ImageDraw.Draw(im)
    x0,y0,x1,y1=box
    # subtle grid
    for gx in range(0,W,60): d.line([(gx,y0),(gx,y1)],fill=(21,52,62),width=1)
    for gy in range(y0,y1,60): d.line([(0,gy),(W,gy)],fill=(21,52,62),width=1)
    return im
def render(W,H,box,n,final,labels_y=True):
    x0,y0,x1,y1=box; im=base(W,H,box)
    P2=[proj(p[0],p[1],x1-x0,y1-y0,150) for p in clean]; P2=[(x+x0,y+y0) for x,y in P2]
    glow=Image.new('RGBA',(W,H),(0,0,0,0)); g=ImageDraw.Draw(glow)
    if n>1: g.line(P2[:n],fill=T+(255,),width=18,joint='curve')
    glow=glow.filter(ImageFilter.GaussianBlur(14)); im.paste(glow,(0,0),glow)
    d=ImageDraw.Draw(im)
    if n>1: d.line(P2[:n],fill=T2,width=7,joint='curve')
    for name,alt,(la,lo) in marks:
        x,y=proj(la,lo,x1-x0,y1-y0,150); x+=x0;y+=y0
        idx=min(range(len(clean)),key=lambda i:dist(clean[i],(la,lo)))
        on=n>idx or final
        col=(255,255,255) if on else (90,120,128)
        d.ellipse([x-14,y-14,x+14,y+14],fill=BG,outline=col,width=5)
        if on: d.ellipse([x-7,y-7,x+7,y+7],fill=T2)
        if name=='Plaza de Mulas': ty=y+40; ax='mt'
        else: ty=y-96; ax='mt'
        d.text((x,ty),name,font=F('Bold',36),fill=col,anchor=ax)
        d.text((x,ty+44),alt,font=F('Medium',30),fill=T2 if on else (90,120,128),anchor=ax)
    if 0<n<=len(P2):
        hx,hy=P2[n-1]
        d.ellipse([hx-16,hy-16,hx+16,hy+16],fill=(255,255,255)); d.ellipse([hx-9,hy-9,hx+9,hy+9],fill=T)
    return im,d
# ---------- static slide 1080x1350
im,d=render(1080,1350,(0,330,1080,1170),len(clean),True)
d.rounded_rectangle([80,90,420,140],radius=25,fill=T); d.text((250,115),'EL RECORRIDO REAL',font=F('Bold',24),fill=(255,255,255),anchor='mm')
d.text((80,165),'Cada punto,',font=F('Bold',74),fill=(255,255,255)); d.text((80,245),'enviado desde la montaña.',font=F('Bold',58),fill=T2)
d.text((80,1180),'5 al 8 de diciembre de 2025 · '+f'{len(clean):,}'.replace(',','.')+' posiciones',font=F('Medium',30),fill=(191,230,228))
lg=LOGO.copy(); lg.thumbnail((240,90)); im.paste(lg,(80,1240),lg)
im.save('slide_recorrido.png')
# ---------- reel 1080x1920
os.makedirs('fr',exist_ok=True)
fps=30; anim=12*fps; hold=3*fps; N=len(clean)
days={'2025-12-05':'5 DIC · Plaza de Mulas','2025-12-06':'6 DIC · Aclimatación','2025-12-07':'7 DIC · Aclimatación','2025-12-08':'8 DIC · Día de cumbre'}
for f in range(anim+hold):
    n=max(2,int(N*min(1,(f+1)/anim)**1.15)) if f<anim else N
    final=f>=anim
    im,d=render(1080,1920,(0,460,1080,1500),n,final)
    d.rounded_rectangle([80,180,470,232],radius=26,fill=T); d.text((275,206),'ACONCAGUA · TIEMPO REAL',font=F('Bold',24),fill=(255,255,255),anchor='mm')
    d.text((80,260),'Seguimos el ascenso',font=F('Bold',64),fill=(255,255,255)); d.text((80,340),'punto por punto.',font=F('Bold',64),fill=T2)
    day=days.get(clean[n-1][2][:10],'')
    d.text((80,1560),'6.962 m · CUMBRE' if final else day,font=F('Bold',46),fill=T2 if final else (255,255,255))
    d.text((80,1625),'Sin cobertura celular. Con red propia.',font=F('Medium',32),fill=(191,230,228))
    lg=LOGO.copy(); lg.thumbnail((300,110)); im.paste(lg,(80,1700),lg)
    im.save(f'fr/{f:04d}.png')
subprocess.run(['ffmpeg','-v','error','-y','-framerate',str(fps),'-i','fr/%04d.png','-c:v','libx264','-pix_fmt','yuv420p','-crf','19','-movflags','+faststart','reel_ruta_aconcagua.mp4'],check=True)
