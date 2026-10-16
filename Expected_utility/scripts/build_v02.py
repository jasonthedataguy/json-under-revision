from __future__ import annotations
import os, re, math, html, json, textwrap, subprocess, shutil
from pathlib import Path
from PIL import Image,ImageDraw,ImageFont,ImageEnhance,ImageFilter
from reportlab.pdfgen import canvas
from reportlab.lib.colors import HexColor
from reportlab.lib.utils import ImageReader
from reportlab.lib.pagesizes import A5
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, PageBreak, KeepTogether, Image as RLImage
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.enums import TA_LEFT, TA_CENTER

ROOT=Path(__file__).resolve().parents[1]
A=ROOT/'assets'; WEB=ROOT/'web'; SOCIAL=ROOT/'social'; VIDEO=ROOT/'video'; BOOK=ROOT/'book'
GREEN='#0c2c24'; PINK='#e78fac'; CREAM='#f4ead5'; DARK='#10191a'; MUTED='#a0baa5'; INK='#192e28'
POSTER=Image.open(A/'poster_original.png').convert('RGB')
fontdir='/usr/share/fonts/truetype/noto'
regular=f'{fontdir}/NotoSerif-Regular.ttf'; bold=f'{fontdir}/NotoSerif-Bold.ttf'; sans='/usr/share/fonts/truetype/lato/Lato-Regular.ttf'
for name,path in [('Noto',regular),('NotoBold',bold),('Lato',sans)]:pdfmetrics.registerFont(TTFont(name,path))
F_TITLE='/usr/share/fonts/truetype/dejavu/DejaVuSerif.ttf'

def font(sz=32,b=False):return ImageFont.truetype(bold if b else regular,sz)
def f_sans(sz=20):return ImageFont.truetype(sans,sz)

def fit_cover(img,size,anchor=(0.5,0.5)):
    w,h=size; W,H=img.size; s=max(w/W,h/H); NW,NH=round(W*s),round(H*s)
    resized=img.resize((NW,NH),Image.Resampling.LANCZOS)
    x=int((NW-w)*anchor[0]); y=int((NH-h)*anchor[1]); return resized.crop((x,y,x+w,y+h))

def rounded(draw,box,r,fill,outline=None,width=1):draw.rounded_rectangle(box,radius=r,fill=fill,outline=outline,width=width)

def save_jpg(img,path,q=87):img.save(path,quality=q,optimize=True,subsampling=0)

# Art derivatives: avoid presenting these as photographs of a real memory.
save_jpg(fit_cover(POSTER,(1600,860),(0.53,0.56)),WEB/'assets/hero_wide.jpg',90)
save_jpg(fit_cover(POSTER,(1120,1400)),A/'poster_print_crop.jpg',90)
save_jpg(fit_cover(POSTER,(1080,1440),(0.5,0.5)),SOCIAL/'instagram/poster_3x4.jpg',89)
save_jpg(fit_cover(POSTER,(1080,1920),(0.52,0.5)),A/'poster_vertical_9x16.jpg',88)
save_jpg(fit_cover(POSTER,(1600,900),(0.55,0.54)),SOCIAL/'facebook_landscape.jpg',88)
save_jpg(fit_cover(POSTER,(1280,720),(0.5,0.5)),SOCIAL/'youtube_thumbnail.jpg',86)

# Standalone technical art: the *unknown probability tree* in correct proportions.
def draw_tree(size=(1400,960),light=False):
    W,H=size; im=Image.new('RGB',size,CREAM if light else GREEN); d=ImageDraw.Draw(im)
    ink=INK if light else CREAM; line=PINK; faded='#b2ae99' if light else '#89a89b'; shadow='#eee2c9' if light else '#183b31'
    gap=int(W*.035)
    d.rectangle((gap,gap,W-gap,H-gap),outline=PINK,width=max(5,W//250))
    d.text((W*.08,H*.085),'EXPECTED UTILITY  /  AN UNOBSERVED BRANCH',font=font(max(18,W//45),True),fill=ink)
    d.text((W*.08,H*.17),'The future has no debug log.',font=font(max(25,W//31)),fill=line)
    nodes=[(0.50,0.31,'DECIDE'),(.29,.53,'NÓI RA'),(.72,.53,'IM LẶNG'),(.14,.76,'YES?'),(.39,.76,'NO?'),(.62,.76,'REGRET?'),(.86,.76,'RELIEF?')]
    def coord(i):return int(nodes[i][0]*W),int(nodes[i][1]*H)
    for i,j in [(0,1),(0,2),(1,3),(1,4),(2,5),(2,6)]:
        x1,y1=coord(i);x2,y2=coord(j);d.line((x1,y1+28,x2,y2-28),fill=line,width=max(3,W//350))
    for idx,(x,y,t) in enumerate(nodes):
        X,Y=coord(idx); bw=int(W*(.115 if idx>2 else .155));bh=int(H*.08)
        rounded(d,(X-bw,Y-bh//2,X+bw,Y+bh//2),16,shadow,line,3)
        box=d.textbbox((0,0),t,font=f_sans(max(16,W//55)));tw=box[2]-box[0];th=box[3]-box[1]
        d.text((X-tw/2,Y-th/2-2),t,font=f_sans(max(16,W//55)),fill=ink)
    d.text((W*.08,H*.90),'P(outcome) = ?     •     U(outcome) = subjective     •     Counterfactual = unobserved',font=f_sans(max(16,W//63)),fill=faded)
    return im

draw_tree((1400,960)).save(A/'decision_tree_dark.png')
draw_tree((1400,960),True).save(A/'decision_tree_paper.png')

# Social carousel: 3:4 actual feed-ready images, using poster crop and separately typeset text.
slides=[
('01 / THE BUG','Expected_utility','Có một đôi mắt cứ hiện lên giữa màn hình code.'),
('02 / THE MODEL','UTILITY = BENEFIT - COST','Một phép tính đơn giản đến mức đáng ngờ.'),
('03 / THE TREE','NÓI RA  /  IM LẶNG','Mọi branch đều có outcome mình không quan sát được.'),
('04 / MISSING DATA','P(OUTCOME) = ?','Imagination is not a probability distribution.'),
('05 / BACK TO HER','NO STACK TRACE','Vẫn là đôi mắt buồn long lanh dưới ánh đèn mờ.'),
]
for i,(label,title,subtitle) in enumerate(slides,1):
    W,H=1080,1440
    if i in (1,5):
        img=fit_cover(POSTER,(W,H),(.5,.50 if i==1 else .64));img=ImageEnhance.Brightness(img).enhance(.78)
    elif i==3:
        img=Image.new('RGB',(W,H),GREEN)
        tr=draw_tree((1400,960));tr.thumbnail((940,720),Image.Resampling.LANCZOS)
        img.paste(tr,((W-tr.width)//2,340))
    else:
        img=Image.new('RGB',(W,H),GREEN)
        d=ImageDraw.Draw(img)
        d.rectangle((65,65,W-65,H-65),outline=PINK,width=13)
        for j in range(12):d.line((70,H*.42+j*15,W-70,H*.22+j*22),fill='#174435',width=4)
        if i==4:
            d.ellipse((700,490,900,690),fill=PINK)
    d=ImageDraw.Draw(img)
    d.rectangle((0,0,W,225),fill=GREEN)
    d.rectangle((0,H-340,W,H),fill=GREEN)
    d.rectangle((60,59,W-60,67),fill=PINK)
    d.text((70,100),label,font=f_sans(34),fill=PINK)
    # title simple fitting
    size=57
    while d.textlength(title,font=font(size,True))>W-110 and size>26:size-=2
    d.text((62,H-310),title,font=font(size,True),fill=CREAM)
    maxwidth=W-130
    pieces=[];cur=''
    for word in subtitle.split():
        n=(cur+' '+word).strip()
        if d.textlength(n,font=font(29))>maxwidth and cur:pieces.append(cur);cur=word
        else:cur=n
    if cur:pieces.append(cur)
    for n,line in enumerate(pieces[:3]):d.text((68,H-219+n*47),line,font=font(29),fill=CREAM)
    d.text((70,H-70),'.json  /  JASON, UNDER REVISION',font=f_sans(24),fill=PINK)
    save_jpg(img,SOCIAL/f'instagram/slide_{i:02d}_3x4.jpg',88)

# Video poster frames in accurate vertical 9:16; exported proof, not narration.
video_lines=[
('01  /  DEBUGGING','Cà phê. AirPods. Code.'),
('02  /  INTRUSION','Cô ấy vẫn xuất hiện.'),
('03  /  MODEL','Benefit, Cost, Utility.'),
('04  /  BRANCHES','Imagination ≠ probability.'),
('05  /  UNKNOWN','Một branch duy nhất.'),
('06  /  RETURN','Vẫn là đôi mắt ấy.'),
]
for i,(label,caption) in enumerate(video_lines,1):
    bg=fit_cover(POSTER,(720,1280),(.48+(i-3)*.04,.5));bg=ImageEnhance.Brightness(bg).enhance(.7)
    if i==4:
        tr=draw_tree((840,800)); tr=fit_cover(tr,(640,440));bg.paste(tr,(40,470))
    dr=ImageDraw.Draw(bg);dr.rectangle((0,0,720,155),fill=GREEN);dr.rectangle((0,1000,720,1280),fill=GREEN)
    dr.rectangle((28,25,692,30),fill=PINK)
    dr.text((46,70),label,font=f_sans(25),fill=PINK)
    fs=35
    while dr.textlength(caption,font=font(fs,True))>645 and fs>19:fs-=2
    dr.text((35,1041),caption,font=font(fs,True),fill=CREAM)
    dr.text((35,1195),'Expected_utility · .json',font=f_sans(22),fill=PINK)
    save_jpg(bg,VIDEO/f'stills/scene_{i:02d}.jpg',88)

# Four videos seconds per card; 24s proof with silent AAC synthesized bed retained from v01 only.
files_txt=VIDEO/'stills/concat.txt'
with files_txt.open('w') as f:
    for i in range(1,7):
        f.write(f"file '{(VIDEO/f'stills/scene_{i:02d}.jpg').resolve()}'\n")
        f.write('duration 4\n')
    f.write(f"file '{(VIDEO/'stills/scene_06.jpg').resolve()}'\n")
# audio generated: very quiet synthetic room tone; avoid presenting as captured historical audio.
audio=Path('/mnt/data/expected_utility_v01/video/ambient_study.wav')
cmd=['ffmpeg','-y','-hide_banner','-loglevel','error','-f','concat','-safe','0','-i',str(files_txt),'-stream_loop','-1','-i',str(audio),'-t','24','-vf','fps=24,format=yuv420p','-c:v','libx264','-preset','ultrafast','-crf','24','-c:a','aac','-b:a','96k','-movflags','+faststart',str(VIDEO/'expected_utility_poster_animatic_9x16.mp4')]
subprocess.run(cmd,check=True)

# Printable A5 book proof: cover, intentional visual pause and fully laid out Vietnamese essay.
PAGE_W,PAGE_H=A5
pdf=BOOK/'04_expected_utility_POSTER_A5_PROOF.pdf'
article=(ROOT/'content/proposed-edit.md').read_text(encoding='utf-8')
paragraphs=[p.strip() for p in article.split('\n\n') if p.strip()][1:]
from xml.sax.saxutils import escape
from reportlab.platypus import Flowable
class DecisionArt(Flowable):
    def __init__(self,fn,width=347):super().__init__();self.path=str(fn);self.width=width;self.height=width*960/1400
    def draw(self):self.canv.drawImage(self.path,0,0,self.width,self.height)

styles={
 'body':ParagraphStyle('body',fontName='Noto',fontSize=9.4,leading=15.2,textColor=HexColor(INK),spaceAfter=10.3,allowWidows=0,allowOrphans=0),
 'lead':ParagraphStyle('lead',fontName='NotoBold',fontSize=13.2,leading=21,textColor=HexColor(INK),spaceAfter=25),
 'section':ParagraphStyle('section',fontName='NotoBold',fontSize=24,leading=30,textColor=HexColor(INK),spaceAfter=15),
 'kicker':ParagraphStyle('kicker',fontName='Lato',fontSize=9,leading=12,textColor=HexColor('#a46d82'),spaceAfter=11),
 'caption':ParagraphStyle('caption',fontName='Noto',fontSize=8.6,leading=14,textColor=HexColor('#685c56'),spaceAfter=22),
 'last':ParagraphStyle('last',fontName='NotoBold',fontSize=13.5,leading=23,textColor=HexColor(INK),spaceBefore=20)
}

def paper(c,doc):
    c.saveState()
    c.setFillColor(HexColor(CREAM));c.rect(0,0,PAGE_W,PAGE_H,fill=1,stroke=0)
    c.setStrokeColor(HexColor(PINK)); c.setLineWidth(1.2);c.line(23,PAGE_H-24,PAGE_W-23,PAGE_H-24)
    c.setFont('Lato',7);c.setFillColor(HexColor(GREEN));c.drawString(25,PAGE_H-18,'.json / JASON, UNDER REVISION')
    c.drawRightString(PAGE_W-23,PAGE_H-18,'04 · EXPECTED_UTILITY')
    c.setStrokeColor(HexColor('#9f9184'));c.line(23,26,PAGE_W-23,26)
    c.drawString(25,17,'PROOF / AUTHOR REVIEW');c.drawRightString(PAGE_W-24,17,str(doc.page).zfill(2))
    c.restoreState()

def cover(c,doc):
    c.saveState()
    c.drawImage(ImageReader(POSTER),-(PAGE_H*(POSTER.width/POSTER.height)-PAGE_W)/2,0,width=PAGE_H*(POSTER.width/POSTER.height),height=PAGE_H,mask='auto')
    c.restoreState()

story=[Spacer(1,1),PageBreak()]
story += [Spacer(1,35),Paragraph('CHAPTER 04   /   MODEL SPECIFICATION',styles['kicker']),Paragraph('Expected_utility',styles['section']),Paragraph('về trái tim, lý trí, và những quyết định mà ta không bao giờ biết kết quả',styles['caption']),
          RLImage(str(A/'poster_print_crop.jpg'),width=225,height=281),PageBreak()]
for idx,p in enumerate(paragraphs):
    content=escape(p).replace('`=B2-C2`','<font name="Lato">=B2-C2</font>')
    content=re.sub(r'\*(.+?)\*',r'<i>\1</i>',content)
    if idx==0:story.append(Paragraph(content,styles['lead']))
    elif idx==len(paragraphs)-1:story.append(Paragraph(content,styles['last']))
    else:story.append(Paragraph(content,styles['body']))
    if 'outcome tree phức tạp' in p:
        story.append(KeepTogether([Spacer(1,12),Paragraph('FIGURE 01  /  ALL THE UNOBSERVED BRANCHES',styles['kicker']),DecisionArt(A/'decision_tree_paper.png',width=PAGE_W-74),Spacer(1,12),Paragraph('Đây là hình minh họa cho những kết quả chưa biết, không phải phép tính xác suất hay dự báo về một người cụ thể.',styles['caption'])]))
# final colophon
# Colophon omitted: end on the manuscript's own final sentence, without a moral or extra page.
doc=SimpleDocTemplate(str(pdf),pagesize=A5,rightMargin=38,leftMargin=38,topMargin=46,bottomMargin=42,title='Expected_utility · .json · Poster Proof v0.2',author='Jason')
doc.build(story,onFirstPage=cover,onLaterPages=paper)

# Full proof website with no unapproved deployment, no analytics, all text inline and interactive decision graph.
parts=[]
for p in paragraphs:
    s=html.escape(p)
    s=re.sub(r'\*(.*?)\*',r'<em>\1</em>',s)
    s=s.replace('`=B2-C2`','<code>=B2-C2</code>')
    parts.append('<p>'+s+'</p>')
prose='\n'.join(parts)
web_html='''<!doctype html><html lang="vi"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><meta name="theme-color" content="#0c2c24"><title>.json / 04 — Expected_utility</title><meta name="description" content="Expected_utility: a memoir chapter about imagined branches, uncertainty and the eyes that keep returning."><style>
:root{--pine:#0c2c24;--cream:#f4ead5;--pink:#e78fac;--ink:#192e28}*{box-sizing:border-box}html{scroll-behavior:smooth}body{margin:0;color:var(--cream);background:var(--pine);font-family:Georgia,'Times New Roman',serif}button,a{touch-action:manipulation}a{color:inherit}a:focus-visible,button:focus-visible{outline:3px solid var(--pink);outline-offset:4px}button{cursor:pointer}.skip{position:absolute;top:-100px;background:var(--cream);color:var(--pine);padding:12px;z-index:20}.skip:focus{top:6px}.sitebar{padding:20px max(5vw,20px);display:flex;justify-content:space-between;gap:15px;font:11px monospace;letter-spacing:.13em}.hero{position:relative;min-height:75vh;background:linear-gradient(0deg,var(--pine) 0%,transparent 60%),url('assets/hero_wide.jpg') center 48%/cover;display:flex;align-items:flex-end}.hero-inner{padding:35px max(5vw,22px) 95px;max-width:1100px}.eyebrow{font:12px monospace;color:var(--pink);letter-spacing:.17em}.hero h1{font-weight:normal;font-size:clamp(48px,8vw,115px);line-height:1.05;letter-spacing:-.07em;margin:15px 0}.hero h2{font:normal 21px/1.5 Georgia;max-width:590px}.button{display:inline-block;border:1px solid var(--cream);padding:14px 20px;margin-right:10px;margin-top:15px;text-decoration:none;font:12px monospace;background:var(--cream);color:var(--pine)}.button.alt{color:var(--cream);background:transparent}.meta{padding:22px max(5vw,22px);border-top:1px solid #577263;border-bottom:1px solid #577263;display:flex;flex-wrap:wrap;gap:20px;font:12px monospace;color:#ddc5b2}.paper{background:var(--cream);color:var(--ink);padding:78px 25px}.story{max-width:700px;margin:auto;font-size:clamp(17px,2vw,19px);line-height:1.94}.story p{margin:0 0 1.3em}.story p:first-of-type{font-size:1.35em;line-height:1.65}.story p:last-child{font-weight:700;font-size:1.2em}.art-figure{margin:45px auto;max-width:780px}.art-figure img{width:100%;height:auto;border:7px solid var(--pine);display:block}.art-figure figcaption{font:12px/1.6 monospace;margin:10px 0;color:#62594d}.artifact{padding:90px 25px;max-width:1100px;margin:auto}.artifact h2{font-weight:normal;font-size:clamp(32px,5vw,68px);margin:10px 0 22px}.artifact .intro{max-width:700px;color:#ddd0c0;line-height:1.75}.decision{background:#123a30;border:1px solid #966e86;padding:22px;margin-top:34px}.decision svg{display:block;width:100%;height:auto;max-height:470px}.decision svg .edge{stroke:#a67887;stroke-width:3;fill:none}.decision svg .node{fill:#16382f;stroke:#ba839b;stroke-width:2}.decision svg .node.selected{fill:#ad6482;stroke:var(--pink);stroke-width:4}.decision svg text{fill:#f4ead5;font:16px monospace;pointer-events:none}.chooser{display:flex;flex-wrap:wrap;gap:12px;margin:16px 0}.chooser button{border:1px solid var(--pink);background:transparent;color:var(--cream);font:14px monospace;padding:13px 18px}.chooser button[aria-pressed=true]{background:var(--pink);color:var(--pine);font-weight:bold}.result{background:#0a271f;padding:25px;min-height:115px;border-left:4px solid var(--pink);font-size:18px;line-height:1.55}.notes{font:12px/1.7 monospace;color:#d4c9bb;margin:20px 0}.foot{border-top:1px solid #5e756a;padding:34px max(5vw,22px);font:11px/1.8 monospace;color:#ddd0c0}.imagebadge{display:inline-block;font:10px monospace;letter-spacing:.13em;border:1px solid var(--pink);padding:8px;color:var(--pink)}@media(max-width:640px){.hero{min-height:620px;background-position:49% center}.hero-inner{padding-bottom:48px}.paper{padding:50px 23px}.artifact{padding:55px 18px}.decision{padding:11px}.decision svg text{font-size:13px}.sitebar{font-size:10px}}@media(prefers-reduced-motion:reduce){html{scroll-behavior:auto}}
</style></head><body><a href="#read" class="skip">Skip to chapter</a><header class="sitebar"><span>.json / JASON, UNDER REVISION</span><span>04 / WORKING PROOF</span></header><section class="hero"><div class="hero-inner"><span class="eyebrow">MODEL SPECIFICATION  /  04</span><h1>Expected_utility</h1><h2>Về trái tim, lý trí và những quyết định mà ta không bao giờ biết kết quả.</h2><p><span class="imagebadge">ORIGINAL INTERPRETIVE POSTER ART</span></p><a href="#read" class="button">ĐỌC CHƯƠNG NÀY →</a><a href="#explore" class="button alt">EXPLORE THE BRANCHES ↘</a></div></section><section class="meta"><span>01 / READ</span><span>02 / EXPLORE</span><span>03 / REVISIT</span><span>STATUS / AUTHOR REVIEW · NOT RELEASED</span></section><main><section id="read" class="paper"><article class="story"><div class="eyebrow">THE STORY / PROPOSED EDIT · NOT FINAL</div>'''+prose+'''</article><figure class="art-figure"><img src="assets/decision_tree_paper.jpg" alt="Illustrated decision tree with speaking or staying silent. Outcomes and their probabilities are unknown." loading="lazy"><figcaption>FIG 01. Branches without known probabilities. An illustration of uncertainty, not a prediction.</figcaption></figure></section><section id="explore" class="artifact"><p class="eyebrow">THE ARTIFACT / UNOBSERVED BRANCHES</p><h2>Which branch would you take?</h2><p class="intro">Tất cả những tương lai tôi không chọn đều nằm ngoài tập dữ liệu. Choose a path below. The result is never a fabricated probability; the missing information is the point.</p><div class="decision"><svg viewBox="0 0 900 365" role="img" aria-labelledby="treeTitle treeDesc"><title id="treeTitle">Interactive decision tree</title><desc id="treeDesc">From one decision, two paths: speak up or stay silent. Each has two possible outcomes, all unknown.</desc><path class="edge" d="M450 71 L239 171 M450 71 L663 171 M239 206 L130 288 M239 206 L360 288 M663 206 L552 288 M663 206 L780 288"/><rect class="node" x="346" y="30" width="208" height="42" rx="15"/><text x="450" y="57" text-anchor="middle">DECIDE</text><rect id="node-talk" class="node" x="145" y="168" width="185" height="47" rx="15"/><text x="238" y="197" text-anchor="middle">NÓI RA</text><rect id="node-stay" class="node" x="570" y="168" width="185" height="47" rx="15"/><text x="662" y="197" text-anchor="middle">IM LẶNG</text><g><rect class="node" x="46" y="283" width="176" height="50" rx="12"/><text x="134" y="304" text-anchor="middle">ACCEPT?</text><text x="134" y="322" text-anchor="middle">P = ?</text><rect class="node" x="270" y="283" width="176" height="50" rx="12"/><text x="358" y="304" text-anchor="middle">REJECT?</text><text x="358" y="322" text-anchor="middle">P = ?</text><rect class="node" x="478" y="283" width="176" height="50" rx="12"/><text x="566" y="304" text-anchor="middle">REGRET?</text><text x="566" y="322" text-anchor="middle">P = ?</text><rect class="node" x="695" y="283" width="176" height="50" rx="12"/><text x="783" y="304" text-anchor="middle">RELIEF?</text><text x="783" y="322" text-anchor="middle">P = ?</text></g></svg><div class="chooser" role="group" aria-label="Choose a decision path"><button type="button" data-choice="talk" aria-pressed="false">Tôi sẽ nói ra</button><button type="button" data-choice="stay" aria-pressed="false">Tôi sẽ im lặng</button><button type="button" data-choice="reset">Reset</button></div><div id="result" class="result" role="status" aria-live="polite">No choice selected. Both paths remain possible; neither is observed.</div><p class="notes">E[U(a)] = Σ P(outcome | a) × U(outcome, a). Here, both probabilities and subjective utilities are unknown. No score is calculated.</p></div></section></main><footer class="foot"><p>THE BOOK IS THE STORY. THE ARCHIVE IS WHAT REMAINS.</p><p>Poster artwork is an interpretation, including handwritten numerical doodles. Do not treat decorative numbers or imagined outcomes as probabilities. No accounts, cookies, tracking or real relationship data.</p><p>© Jason / .json · Prototype v0.2 · Not a released publication.</p></footer><script>const out=document.querySelector('#result');const buttons=[...document.querySelectorAll('[data-choice]')];function choose(k){for(const b of buttons){b.setAttribute('aria-pressed',String(b.dataset.choice===k))}for(const n of ['talk','stay'])document.querySelector('#node-'+n).classList.toggle('selected',n===k);if(k==='talk')out.textContent='Branch: NÓI RA. The relationship may change, or not. The response, its probability, and the unchosen path are all unknown.';else if(k==='stay')out.textContent='Branch: IM LẶNG. The feeling may pass, or not. The response, its probability, and the unchosen path are all unknown.';else out.textContent='No choice selected. Both paths remain possible; neither is observed.'}buttons.forEach(b=>b.addEventListener('click',()=>choose(b.dataset.choice)));</script></body></html>'''
(WEB/'index.html').write_text(web_html,encoding='utf-8')
save_jpg(draw_tree((1400,960),True),WEB/'assets/decision_tree_paper.jpg',86)

# Export build manifest.
manifest={'title':'Expected_utility','slug':'expected-utility','version':'0.2.0','source':'content/original.md','proposed':'content/proposed-edit.md','visual_theme':'forest green, muted pink, cream; rough printed poster','asset_origin':'author-supplied illustration generated in earlier conversation','artifact_status':'PROOF / AUTHOR REVIEW','ebook_print_status':'7+ page A5 editorial proof, not PDF/X','website_status':'local static prototype, not deployed','video_status':'24-second ambient-only animatic (9:16), no narrator or synchronized captions','social_status':'3:4 Instagram, 9:16 video stills, landscape thumbnails; drafts not posted','rights_note':'Do not present decorative numbers in original poster as estimated probabilities.'}
(ROOT/'docs/MANIFEST.json').write_text(json.dumps(manifest,ensure_ascii=False,indent=2),encoding='utf-8')
print('DONE',pdf,'bytes',pdf.stat().st_size,'video bytes',(VIDEO/'expected_utility_poster_animatic_9x16.mp4').stat().st_size)
