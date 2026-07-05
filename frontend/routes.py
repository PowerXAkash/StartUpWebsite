from fastapi import APIRouter
from fastapi.responses import HTMLResponse

router = APIRouter(tags=["frontend"])


def render_service_page(
    title: str,
    hero_title: str,
    intro: str,
    features: list[tuple[str, str]],
    how_it_works: list[tuple[str, str]],
    benefits: list[str],
    cta_text: str = "Request a demo",
) -> str:
    feature_items = "".join(
        f"""<div class="reveal feature-card">
            <div class="feature-glow"></div>
            <div class="feature-icon">{chr(0x2699)}</div>
            <h3>{item}</h3>
            <p>{desc}</p>
        </div>"""
        for item, desc in features
    )
    hiw_items = "".join(
        f"""<div class="reveal step-item" style="transition-delay:{i*0.15}s">
            <div class="step-ring">
                <span>{i+1}</span>
            </div>
            <h4>{title}</h4>
            <p>{desc}</p>
        </div>"""
        for i, (title, desc) in enumerate(how_it_works)
    )
    benefit_items = "".join(
        f"""<li class="reveal" style="transition-delay:{i*0.08}s">
            <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round"><polyline points="20 6 9 17 4 12"/></svg>
            {b}
        </li>"""
        for i, b in enumerate(benefits)
    )

    html = """<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width,initial-scale=1.0">
<title>""" + title + """ | SeedStudio</title>
<link href="https://fonts.googleapis.com/css2?family=Space+Grotesk:wght@300;400;500;600;700;800&display=swap" rel="stylesheet">
<style>
* { margin:0; padding:0; box-sizing:border-box; }
:root { --p:#6C5CE7; --s:#00D2FF; --g:#00E676; --w:#ffffff; --b:#0a0a1a; --t:rgba(255,255,255,0.7); }
html { scroll-behavior:smooth; }
body { font-family:'Space Grotesk',sans-serif; background:var(--b); color:var(--w); overflow-x:hidden; }
canvas#bg { position:fixed; top:0; left:0; width:100vw; height:100vh; z-index:0; pointer-events:none; }
.page { position:relative; z-index:1; }
.section { min-height:100vh; display:flex; align-items:center; position:relative; padding:80px 0; }
.section-inner { width:min(1200px,calc(100%-48px)); margin:0 auto; position:relative; z-index:2; }
header { position:fixed; top:0; left:0; right:0; z-index:100; padding:16px 0; transition:.4s; }
header.scrolled { background:rgba(10,10,26,0.9); backdrop-filter:blur(20px); border-bottom:1px solid rgba(108,92,231,0.15); }
.nav { display:flex; align-items:center; justify-content:space-between; width:min(1200px,calc(100%-48px)); margin:0 auto; }
.brand { font-size:1.4rem; font-weight:800; background:linear-gradient(135deg,var(--p),var(--s)); -webkit-background-clip:text;-webkit-text-fill-color:transparent; background-clip:text; }
.brand span { color:var(--w); -webkit-text-fill-color:var(--w); }
.nav-links { display:flex; gap:28px; align-items:center; }
.nav-links a { color:var(--t); font-weight:500; font-size:.9rem; transition:.3s; position:relative; text-decoration:none; }
.nav-links a:hover { color:var(--w); }
.btn-glow { padding:10px 24px; background:linear-gradient(135deg,var(--p),var(--s)); border-radius:50px; color:#fff!important; font-weight:600!important; box-shadow:0 0 30px rgba(108,92,231,0.3); transition:.3s!important; }
.btn-glow:hover { transform:translateY(-2px); box-shadow:0 0 50px rgba(108,92,231,0.5)!important; }
.m-toggle { display:none; flex-direction:column; gap:5px; cursor:pointer; background:none; border:none; padding:5px; }
.m-toggle span { width:24px; height:2px; background:var(--w); border-radius:2px; transition:.3s; }
.hero-grid { display:grid; grid-template-columns:1.1fr .9fr; gap:60px; align-items:center; min-height:100vh; padding:120px 0 60px; }
.hero-badge { display:inline-flex; align-items:center; gap:8px; padding:6px 14px; border:1px solid rgba(108,92,231,.3); border-radius:50px; font-size:.8rem; color:var(--p); margin-bottom:20px; text-transform:uppercase; letter-spacing:1px; }
.hero-badge .d { width:6px; height:6px; background:var(--p); border-radius:50%; }
.hero h1 { font-size:clamp(2.2rem,4.5vw,3.8rem); font-weight:800; line-height:1.1; margin-bottom:16px; letter-spacing:-1px; }
.hero h1 .g { background:linear-gradient(135deg,var(--p),var(--s)); -webkit-background-clip:text;-webkit-text-fill-color:transparent; background-clip:text; }
.hero p { font-size:1.05rem; color:var(--t); max-width:520px; margin-bottom:28px; line-height:1.8; }
.hero-actions { display:flex; gap:14px; flex-wrap:wrap; }
.btn { display:inline-flex; align-items:center; gap:8px; padding:14px 28px; border-radius:50px; font-weight:600; font-size:.95rem; transition:.3s; cursor:pointer; border:none; text-decoration:none; }
.btn-p { background:linear-gradient(135deg,var(--p),#5A52D5); color:#fff; box-shadow:0 10px 40px rgba(108,92,231,0.3); }
.btn-p:hover { transform:translateY(-3px); box-shadow:0 15px 50px rgba(108,92,231,0.45); }
.btn-s { background:rgba(255,255,255,.05); color:var(--w); border:1px solid rgba(255,255,255,.1); backdrop-filter:blur(10px); }
.btn-s:hover { background:rgba(255,255,255,.1); transform:translateY(-3px); }
.hero-card { background:rgba(255,255,255,.03); border:1px solid rgba(255,255,255,.08); border-radius:24px; padding:32px; backdrop-filter:blur(10px); }
.hero-card h3 { font-size:1.15rem; font-weight:700; margin-bottom:6px; }
.hero-card>p { font-size:.85rem; color:var(--t); margin-bottom:20px; }
.mg { display:grid; grid-template-columns:1fr 1fr; gap:10px; }
.m { padding:14px; background:rgba(108,92,231,.05); border:1px solid rgba(108,92,231,.1); border-radius:12px; transition:.3s; }
.m:hover { background:rgba(108,92,231,.1); transform:translateY(-2px); }
.m strong { display:block; font-size:.95rem; color:var(--p); margin-bottom:2px; }
.m span { font-size:.8rem; color:var(--t); }
.hero-visual { position:relative; }
.hero-glow-box { width:100%; aspect-ratio:1; border-radius:30px; background:linear-gradient(135deg,rgba(108,92,231,.1),rgba(0,210,255,.05)); border:1px solid rgba(108,92,231,.15); display:flex; align-items:center; justify-content:center; position:relative; overflow:hidden; }
.hero-glow-box::before { content:''; position:absolute; width:200%; height:200%; background:conic-gradient(from 0deg,var(--p),var(--s),var(--p)); animation:spin 10s linear infinite; opacity:.15; }
@keyframes spin { to { transform:rotate(360deg); } }
.hero-glow-box .inner { position:relative; z-index:1; text-align:center; }
.hero-glow-box .inner .big-icon { font-size:6rem; }
.hero-glow-box .inner p { font-size:.9rem; color:var(--t); margin-top:12px; }
.sh-s { text-align:center; margin-bottom:50px; }
.sh-l { display:inline-block; padding:6px 14px; border:1px solid rgba(108,92,231,.25); border-radius:50px; font-size:.75rem; font-weight:600; color:var(--p); text-transform:uppercase; letter-spacing:1px; margin-bottom:14px; }
.sh-t { font-size:clamp(1.8rem,3vw,2.6rem); font-weight:800; margin-bottom:10px; }
.sh-p { color:var(--t); font-size:1rem; max-width:500px; margin:0 auto; }
.fg { display:grid; grid-template-columns:repeat(auto-fit,minmax(300px,1fr)); gap:20px; }
.feature-card { background:rgba(255,255,255,.02); border:1px solid rgba(255,255,255,.06); border-radius:20px; padding:30px; transition:.5s; position:relative; overflow:hidden; cursor:default; }
.feature-card::before { content:''; position:absolute; inset:0; background:linear-gradient(135deg,rgba(108,92,231,.08),transparent); opacity:0; transition:.5s; }
.feature-card:hover::before { opacity:1; }
.feature-card:hover { transform:translateY(-8px); border-color:rgba(108,92,231,.3); box-shadow:0 30px 80px rgba(0,0,0,.4); }
.feature-glow { position:absolute; top:-50%; right:-50%; width:100%; height:100%; background:radial-gradient(circle,rgba(108,92,231,.08),transparent 70%); opacity:0; transition:.5s; }
.feature-card:hover .feature-glow { opacity:1; }
.feature-icon { font-size:2rem; margin-bottom:16px; }
.feature-card h3 { font-size:1.15rem; font-weight:700; margin-bottom:8px; }
.feature-card p { color:var(--t); font-size:.9rem; line-height:1.7; }
.sg { display:grid; grid-template-columns:repeat(3,1fr); gap:30px; }
.step-item { text-align:center; padding:40px 20px; background:rgba(255,255,255,.02); border:1px solid rgba(255,255,255,.06); border-radius:20px; transition:.5s; }
.step-item:hover { transform:translateY(-8px); border-color:rgba(108,92,231,.3); }
.step-ring { width:72px; height:72px; border-radius:50%; margin:0 auto 18px; display:flex; align-items:center; justify-content:center; background:linear-gradient(135deg,rgba(108,92,231,.15),rgba(0,210,255,.1)); border:1px solid rgba(108,92,231,.2); font-size:1.5rem; font-weight:800; color:var(--p); }
.step-item h4 { font-size:1.05rem; font-weight:700; margin-bottom:8px; }
.step-item p { color:var(--t); font-size:.85rem; }
.bc { background:rgba(255,255,255,.02); border:1px solid rgba(255,255,255,.06); border-radius:24px; padding:48px; max-width:800px; margin:0 auto; }
.bc ul { list-style:none; display:grid; grid-template-columns:1fr 1fr; gap:14px; }
.bc li { display:flex; align-items:center; gap:12px; padding:14px 18px; background:rgba(108,92,231,.04); border:1px solid rgba(108,92,231,.1); border-radius:12px; font-size:.9rem; transition:.3s; }
.bc li:hover { background:rgba(108,92,231,.08); transform:translateX(4px); }
.bc li svg { width:18px; height:18px; color:var(--g); flex-shrink:0; }
.cta-b { text-align:center; padding:80px 40px; background:linear-gradient(135deg,rgba(108,92,231,.08),rgba(0,210,255,.04)); border:1px solid rgba(108,92,231,.15); border-radius:32px; position:relative; overflow:hidden; }
.cta-b::before { content:''; position:absolute; inset:0; background:url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 200 200'%3E%3Cdefs%3E%3Cpattern id='g' x='25' y='25' width='50' height='50' patternUnits='userSpaceOnUse'%3E%3Ccircle cx='25' cy='25' r='1' fill='rgba(108,92,231,.1)'/%3E%3C/pattern%3E%3C/defs%3E%3Crect width='200' height='200' fill='url(%23g)'/%3E%3C/svg%3E"); opacity:.5; }
.cta-b h2 { font-size:2rem; font-weight:800; margin-bottom:10px; position:relative; }
.cta-b p { color:var(--t); margin-bottom:24px; position:relative; }
.cta-b .btn { position:relative; }
.reveal { opacity:0; transform:translateY(40px); transition:all .8s cubic-bezier(.22,1,.36,1); }
.reveal.v { opacity:1; transform:translateY(0); }
.bg-layer { position:fixed; top:0; left:0; width:100%; height:100%; z-index:-1; transition:opacity 1.2s ease; }
.bg-layer-1 { background:radial-gradient(ellipse at 20% 50%,#0a0a2e,#0a0a1a); opacity:1; }
.bg-layer-2 { background:radial-gradient(ellipse at 80% 30%,#1a0a2e,#0a0a1a); opacity:0; }
.bg-layer-3 { background:radial-gradient(ellipse at 50% 80%,#0a1a2e,#0a0a1a); opacity:0; }
.bg-layer-4 { background:radial-gradient(ellipse at 30% 70%,#2e0a1a,#0a0a1a); opacity:0; }
@media(max-width:860px) {
    .hero-grid { grid-template-columns:1fr; gap:40px; padding:100px 0 40px; }
    .fg,.sg,.bc ul { grid-template-columns:1fr; }
    .nav-links { display:none; position:fixed; top:0; left:0; right:0; bottom:0; background:rgba(10,10,26,.98); flex-direction:column; justify-content:center; align-items:center; gap:24px; z-index:99; }
    .nav-links.active { display:flex; }
    .m-toggle { display:flex; z-index:100; }
    .m-toggle.active span:nth-child(1) { transform:rotate(45deg) translate(5px,5px); }
    .m-toggle.active span:nth-child(2) { opacity:0; }
    .m-toggle.active span:nth-child(3) { transform:rotate(-45deg) translate(5px,-5px); }
}
</style>
</head>
<body>
<canvas id="bg"></canvas>
<div class="bg-layer bg-layer-1" id="bg1"></div>
<div class="bg-layer bg-layer-2" id="bg2"></div>
<div class="bg-layer bg-layer-3" id="bg3"></div>
<div class="bg-layer bg-layer-4" id="bg4"></div>
<header id="h">
    <div class="nav">
        <a class="brand" href="/">Seed<span>Studio</span></a>
        <nav class="nav-links" id="nl">
            <a href="/">Home</a>
            <a href="/education-ai/student-learning">Education</a>
            <a href="/industry-ai/healthcare">Industry</a>
            <a href="/agricultural-ai/crop-monitoring">Agriculture</a>
            <a class="btn-glow" href="mailto:hello@seedstudio.example">Get Started</a>
        </nav>
        <button class="m-toggle" id="mt" aria-label="Menu"><span></span><span></span><span></span></button>
    </div>
</header>
<div class="page">
    <div class="section" id="s1">
        <div class="section-inner">
            <div class="hero-grid">
                <div>
                    <div class="hero-badge"><span class="d"></span> AI-Powered Innovation</div>
                    <h1>""" + hero_title + """</h1>
                    <p>""" + intro + """</p>
                    <div class="hero-actions">
                        <a class="btn btn-p" href="mailto:hello@seedstudio.example">
                            """ + cta_text + """
                            <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round"><line x1="5" y1="12" x2="19" y2="12"/><polyline points="12 5 19 12 12 19"/></svg>
                        </a>
                        <a class="btn btn-s" href="#feat">Explore</a>
                    </div>
                </div>
                <div class="hero-visual">
                    <div class="hero-glow-box">
                        <div class="inner">
                            <div class="big-icon">""" + chr(0x2728) + """</div>
                            <p>Next-Gen AI Technology</p>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </div>
    <div class="section" id="s2">
        <div class="section-inner">
            <div class="sh-s reveal"><div class="sh-l">Features</div><h2 class="sh-t">What's Included</h2><p class="sh-p">Cutting-edge capabilities designed for the future.</p></div>
            <div class="fg">""" + feature_items + """</div>
        </div>
    </div>
    <div class="section" id="s3">
        <div class="section-inner">
            <div class="sh-s reveal"><div class="sh-l">Process</div><h2 class="sh-t">How It Works</h2><p class="sh-p">Simple, powerful, and efficient.</p></div>
            <div class="sg">""" + hiw_items + """</div>
        </div>
    </div>
    <div class="section" id="s4">
        <div class="section-inner">
            <div class="sh-s reveal"><div class="sh-l">Benefits</div><h2 class="sh-t">Why Choose Us</h2><p class="sh-p">Proven results that transform businesses.</p></div>
            <div class="bc reveal"><ul>""" + benefit_items + """</ul></div>
        </div>
    </div>
    <div class="section" id="s5">
        <div class="section-inner">
            <div class="cta-b reveal">
                <h2>Ready to Get Started?</h2>
                <p>Let's build the future together.</p>
                <a class="btn btn-p" href="mailto:hello@seedstudio.example">
                    Schedule a Consultation
                    <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round"><line x1="5" y1="12" x2="19" y2="12"/><polyline points="12 5 19 12 12 19"/></svg>
                </a>
            </div>
        </div>
    </div>
</div>
<script>
const h=document.getElementById('h');
window.addEventListener('scroll',function(){if(window.scrollY > 50){h.classList.add('scrolled')}else{h.classList.remove('scrolled')}});
const mt=document.getElementById('mt'),nl=document.getElementById('nl');
mt.addEventListener('click',function(){mt.classList.toggle('active');nl.classList.toggle('active');});
nl.querySelectorAll('a').forEach(function(l){l.addEventListener('click',function(){mt.classList.remove('active');nl.classList.remove('active');});});
const obs=new IntersectionObserver(function(e){e.forEach(function(e){if(e.isIntersecting)e.target.classList.add('v');});},{threshold:.15});
document.querySelectorAll('.reveal').forEach(function(el){obs.observe(el);});
const sections=document.querySelectorAll('.section');
const bgLayers=[document.getElementById('bg1'),document.getElementById('bg2'),document.getElementById('bg3'),document.getElementById('bg4')];
function updateBg(){
    const scrollY=window.scrollY+window.innerHeight/2;
    let activeIdx=0;
    sections.forEach(function(sec,i){
        const top=sec.offsetTop,bottom=top+sec.offsetHeight;
        if(scrollY>=top&&scrollY<bottom)activeIdx=i;
    });
    bgLayers.forEach(function(layer,i){
        layer.style.opacity=i===activeIdx?'1':'0';
    });
}
window.addEventListener('scroll',updateBg);
window.addEventListener('resize',updateBg);
updateBg();
const c=document.getElementById('bg'),ctx=c.getContext('2d');
c.width=window.innerWidth;c.height=window.innerHeight;
window.addEventListener('resize',function(){c.width=window.innerWidth;c.height=window.innerHeight;});
const particles=[];
const colors=['#6C5CE7','#00D2FF','#00E676','#FF6584'];
for(let i=0;i<80;i++){
    particles.push({
        x:Math.random()*c.width,y:Math.random()*c.height,
        vx:(Math.random()-.5)*.5,vy:(Math.random()-.5)*.5,
        r:Math.random()*2+1,c:colors[Math.floor(Math.random()*colors.length)],
        a:Math.random()*.4+.1
    });
}
function draw(){
    ctx.clearRect(0,0,c.width,c.height);
    particles.forEach(function(p){
        p.x+=p.vx;p.y+=p.vy;
        if(p.x<0||p.x>c.width)p.vx*=-1;
        if(p.y<0||p.y>c.height)p.vy*=-1;
        ctx.beginPath();
        ctx.arc(p.x,p.y,p.r,0,Math.PI*2);
        ctx.fillStyle=p.c;
        ctx.globalAlpha=p.a;
        ctx.fill();
        ctx.globalAlpha=1;
    });
    for(let i=0;i<particles.length;i++){
        for(let j=i+1;j<particles.length;j++){
            const dx=particles[i].x-particles[j].x,dy=particles[i].y-particles[j].y;
            const dist=Math.sqrt(dx*dx+dy*dy);
            if(dist<150){
                ctx.beginPath();
                ctx.moveTo(particles[i].x,particles[i].y);
                ctx.lineTo(particles[j].x,particles[j].y);
                ctx.strokeStyle='rgba(108,92,231,'+(.06*(1-dist/150))+')';
                ctx.stroke();
            }
        }
    }
    requestAnimationFrame(draw);
}
draw();
</script>
</body>
</html>"""
    return html


@router.get("/", response_class=HTMLResponse)
async def frontend_index():
    return """<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width,initial-scale=1.0">
<title>SeedStudio | Future of AI</title>
<link href="https://fonts.googleapis.com/css2?family=Space+Grotesk:wght@300;400;500;600;700;800&display=swap" rel="stylesheet">
<style>
*{margin:0;padding:0;box-sizing:border-box}
:root{--p:#6C5CE7;--s:#00D2FF;--g:#00E676;--w:#ffffff;--b:#0a0a1a;--t:rgba(255,255,255,0.7)}
html{scroll-behavior:smooth}
body{font-family:'Space Grotesk',sans-serif;background:var(--b);color:var(--w);overflow-x:hidden}
canvas#bg{position:fixed;top:0;left:0;width:100vw;height:100vh;z-index:0;pointer-events:none}
.bg-layer{position:fixed;top:0;left:0;width:100%;height:100%;z-index:-1;transition:opacity 1.2s ease}
.bg-layer-1{background:radial-gradient(ellipse at 20% 50%,#0a0a2e,#0a0a1a);opacity:1}
.bg-layer-2{background:radial-gradient(ellipse at 80% 30%,#1a0a2e,#0a0a1a);opacity:0}
.bg-layer-3{background:radial-gradient(ellipse at 50% 80%,#0a1a2e,#0a0a1a);opacity:0}
.bg-layer-4{background:radial-gradient(ellipse at 30% 70%,#2e0a1a,#0a0a1a);opacity:0}
.page{position:relative;z-index:1}
.section{min-height:100vh;display:flex;align-items:center;position:relative;padding:80px 0}
.section-inner{width:min(1200px,calc(100%-48px));margin:0 auto;position:relative;z-index:2}
header{position:fixed;top:0;left:0;right:0;z-index:100;padding:16px 0;transition:.4s}
header.scrolled{background:rgba(10,10,26,0.9);backdrop-filter:blur(20px);border-bottom:1px solid rgba(108,92,231,0.15)}
.nav{display:flex;align-items:center;justify-content:space-between;width:min(1200px,calc(100%-48px));margin:0 auto}
.brand{font-size:1.4rem;font-weight:800;background:linear-gradient(135deg,var(--p),var(--s));-webkit-background-clip:text;-webkit-text-fill-color:transparent;background-clip:text}
.brand span{color:var(--w);-webkit-text-fill-color:var(--w)}
.nav-links{display:flex;gap:28px;align-items:center}
.nav-links a{color:var(--t);font-weight:500;font-size:.9rem;transition:.3s;position:relative;text-decoration:none}
.nav-links a:hover{color:var(--w)}
.btn-glow{padding:10px 24px;background:linear-gradient(135deg,var(--p),var(--s));border-radius:50px;color:#fff!important;font-weight:600!important;box-shadow:0 0 30px rgba(108,92,231,0.3);transition:.3s!important}
.btn-glow:hover{transform:translateY(-2px);box-shadow:0 0 50px rgba(108,92,231,0.5)!important}
.m-toggle{display:none;flex-direction:column;gap:5px;cursor:pointer;background:none;border:none;padding:5px}
.m-toggle span{width:24px;height:2px;background:var(--w);border-radius:2px;transition:.3s}
.hero-grid{display:grid;grid-template-columns:1.1fr .9fr;gap:60px;align-items:center;min-height:100vh;padding:120px 0 60px}
.hero-badge{display:inline-flex;align-items:center;gap:8px;padding:6px 14px;border:1px solid rgba(108,92,231,.3);border-radius:50px;font-size:.8rem;color:var(--p);margin-bottom:20px;text-transform:uppercase;letter-spacing:1px}
.hero-badge .d{width:6px;height:6px;background:var(--p);border-radius:50%}
.hero h1{font-size:clamp(2.2rem,4.5vw,3.8rem);font-weight:800;line-height:1.1;margin-bottom:16px;letter-spacing:-1px}
.hero h1 .g{background:linear-gradient(135deg,var(--p),var(--s));-webkit-background-clip:text;-webkit-text-fill-color:transparent;background-clip:text}
.hero p{font-size:1.05rem;color:var(--t);max-width:520px;margin-bottom:28px;line-height:1.8}
.hero-actions{display:flex;gap:14px;flex-wrap:wrap}
.btn{display:inline-flex;align-items:center;gap:8px;padding:14px 28px;border-radius:50px;font-weight:600;font-size:.95rem;transition:.3s;cursor:pointer;border:none;text-decoration:none}
.btn-p{background:linear-gradient(135deg,var(--p),#5A52D5);color:#fff;box-shadow:0 10px 40px rgba(108,92,231,0.3)}
.btn-p:hover{transform:translateY(-3px);box-shadow:0 15px 50px rgba(108,92,231,0.45)}
.btn-s{background:rgba(255,255,255,.05);color:var(--w);border:1px solid rgba(255,255,255,.1);backdrop-filter:blur(10px)}
.btn-s:hover{background:rgba(255,255,255,.1);transform:translateY(-3px)}
.hero-card{background:rgba(255,255,255,.03);border:1px solid rgba(255,255,255,.08);border-radius:24px;padding:32px;backdrop-filter:blur(10px)}
.hero-card h3{font-size:1.15rem;font-weight:700;margin-bottom:6px}
.hero-card>p{font-size:.85rem;color:var(--t);margin-bottom:20px}
.mg{display:grid;grid-template-columns:1fr 1fr;gap:10px}
.m{padding:14px;background:rgba(108,92,231,.05);border:1px solid rgba(108,92,231,.1);border-radius:12px;transition:.3s}
.m:hover{background:rgba(108,92,231,.1);transform:translateY(-2px)}
.m strong{display:block;font-size:.95rem;color:var(--p);margin-bottom:2px}
.m span{font-size:.8rem;color:var(--t)}
.hero-visual{position:relative}
.hero-glow-box{width:100%;aspect-ratio:1;border-radius:30px;background:linear-gradient(135deg,rgba(108,92,231,.1),rgba(0,210,255,.05));border:1px solid rgba(108,92,231,.15);display:flex;align-items:center;justify-content:center;position:relative;overflow:hidden}
.hero-glow-box::before{content:'';position:absolute;width:200%;height:200%;background:conic-gradient(from 0deg,var(--p),var(--s),var(--p));animation:spin 10s linear infinite;opacity:.15}
@keyframes spin{to{transform:rotate(360deg)}}
.hero-glow-box .inner{position:relative;z-index:1;text-align:center}
.hero-glow-box .inner .big-icon{font-size:6rem}
.hero-glow-box .inner p{font-size:.9rem;color:var(--t);margin-top:12px}
.services-showcase{padding:40px 0}
.service-floating-card{display:grid;grid-template-columns:1fr 1fr;gap:40px;align-items:center;padding:60px 48px;margin-bottom:40px;border-radius:32px;background:rgba(255,255,255,.02);border:1px solid rgba(255,255,255,.06);transition:.5s;position:relative;overflow:hidden}
.service-floating-card:hover{border-color:rgba(108,92,231,.2);transform:translateY(-4px);box-shadow:0 30px 80px rgba(0,0,0,.3)}
.service-floating-card .card-glow{position:absolute;top:-50%;right:-30%;width:50%;height:200%;background:radial-gradient(circle,rgba(108,92,231,.06),transparent 70%);pointer-events:none}
.service-floating-card:nth-child(2) .card-glow{left:-30%;right:auto}
.service-floating-card:nth-child(3) .card-glow{top:auto;bottom:-50%}
.sfc-icon{font-size:3.5rem;margin-bottom:16px}
.sfc-content h3{font-size:1.6rem;font-weight:700;margin-bottom:12px}
.sfc-content p{color:var(--t);font-size:.95rem;line-height:1.8;margin-bottom:20px}
.sfc-grid{display:grid;grid-template-columns:1fr 1fr;gap:12px}
.sfc-item{padding:12px 16px;background:rgba(108,92,231,.04);border:1px solid rgba(108,92,231,.1);border-radius:12px;font-size:.85rem;transition:.3s}
.sfc-item:hover{background:rgba(108,92,231,.08);transform:translateX(3px)}
.sfc-item strong{display:block;color:var(--p);font-size:.9rem;margin-bottom:2px}
.sfc-item span{color:var(--t);font-size:.8rem}
.sfc-visual{display:flex;align-items:center;justify-content:center}
.sfc-visual .globe{width:200px;height:200px;border-radius:50%;background:linear-gradient(135deg,rgba(108,92,231,.15),rgba(0,210,255,.08));border:1px solid rgba(108,92,231,.2);display:flex;align-items:center;justify-content:center;font-size:4rem;position:relative}
.sfc-visual .globe::before{content:'';position:absolute;inset:-10px;border-radius:50%;border:1px solid rgba(108,92,231,.1);animation:pulse-ring 3s ease-in-out infinite}
@keyframes pulse-ring{0%,100%{transform:scale(1);opacity:1}50%{transform:scale(1.05);opacity:.5}}
.sh-s{text-align:center;margin-bottom:50px}
.sh-l{display:inline-block;padding:6px 14px;border:1px solid rgba(108,92,231,.25);border-radius:50px;font-size:.75rem;font-weight:600;color:var(--p);text-transform:uppercase;letter-spacing:1px;margin-bottom:14px}
.sh-t{font-size:clamp(1.8rem,3vw,2.6rem);font-weight:800;margin-bottom:10px}
.sh-p{color:var(--t);font-size:1rem;max-width:500px;margin:0 auto}
.about-card{background:rgba(255,255,255,.02);border:1px solid rgba(255,255,255,.06);border-radius:24px;padding:48px;text-align:center;max-width:800px;margin:0 auto}
.about-card p{color:var(--t);font-size:1.05rem;line-height:1.9}
.cta-b{text-align:center;padding:80px 40px;background:linear-gradient(135deg,rgba(108,92,231,.08),rgba(0,210,255,.04));border:1px solid rgba(108,92,231,.15);border-radius:32px;position:relative;overflow:hidden}
.cta-b::before{content:'';position:absolute;inset:0;background:url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 200 200'%3E%3Cdefs%3E%3Cpattern id='g' x='25' y='25' width='50' height='50' patternUnits='userSpaceOnUse'%3E%3Ccircle cx='25' cy='25' r='1' fill='rgba(108,92,231,.1)'/%3E%3C/pattern%3E%3C/defs%3E%3Crect width='200' height='200' fill='url(%23g)'/%3E%3C/svg%3E");opacity:.5}
.cta-b h2{font-size:2rem;font-weight:800;margin-bottom:10px;position:relative}
.cta-b p{color:var(--t);margin-bottom:24px;position:relative}
.cta-b .btn{position:relative}
.chat-l{position:fixed;right:28px;bottom:28px;width:56px;height:56px;border-radius:50%;display:flex;align-items:center;justify-content:center;background:linear-gradient(135deg,var(--p),#5A52D5);color:#fff;border:none;box-shadow:0 10px 30px rgba(108,92,231,.3);cursor:pointer;z-index:20;font-size:1.4rem;transition:.3s}
.chat-l:hover{transform:scale(1.1);box-shadow:0 15px 40px rgba(108,92,231,.4)}
.chat-p{position:fixed;right:24px;bottom:96px;width:360px;max-width:calc(100%-32px);background:rgba(15,15,35,.95);backdrop-filter:blur(20px);border:1px solid rgba(255,255,255,.08);border-radius:20px;box-shadow:0 30px 80px rgba(0,0,0,.5);overflow:hidden;display:none;z-index:20}
.chat-p.active{display:block}
.chat-h{padding:14px 18px;background:linear-gradient(135deg,var(--p),#5A52D5);color:#fff;display:flex;justify-content:space-between;align-items:center}
.chat-h h4{margin:0;font-size:.95rem;font-weight:600}
.chat-x{width:26px;height:26px;display:flex;align-items:center;justify-content:center;border-radius:50%;background:rgba(255,255,255,.2);cursor:pointer;font-weight:700;font-size:1rem;transition:.3s}
.chat-x:hover{background:rgba(255,255,255,.3)}
.chat-ms{max-height:300px;overflow-y:auto;padding:16px 18px;background:rgba(0,0,0,.2)}
.chat-m{margin-bottom:12px;display:flex}
.chat-m.u{justify-content:flex-end}
.chat-m.b{justify-content:flex-start}
.bub{display:inline-block;padding:10px 14px;border-radius:16px;max-width:85%;line-height:1.5;font-size:.85rem}
.chat-m.u .bub{background:linear-gradient(135deg,var(--p),#5A52D5);color:white;border-bottom-right-radius:4px}
.chat-m.b .bub{background:rgba(255,255,255,.06);color:var(--w);border-bottom-left-radius:4px}
.chat-i{display:flex;gap:10px;border-top:1px solid rgba(255,255,255,.06);padding:12px 16px;background:rgba(0,0,0,.2)}
.chat-i input{flex:1;background:rgba(255,255,255,.04);border:1px solid rgba(255,255,255,.08);border-radius:10px;padding:10px 12px;font-size:.85rem;color:var(--w);outline:none;transition:.3s}
.chat-i input:focus{border-color:var(--p)}
.chat-i button{border:none;border-radius:10px;padding:10px 16px;background:linear-gradient(135deg,var(--p),#5A52D5);color:#fff;cursor:pointer;font-weight:600;font-size:.85rem;transition:.3s}
.chat-i button:hover{transform:translateY(-2px);box-shadow:0 5px 15px rgba(108,92,231,.3)}
.reveal{opacity:0;transform:translateY(40px);transition:all .8s cubic-bezier(.22,1,.36,1)}
.reveal.v{opacity:1;transform:translateY(0)}
@media(max-width:860px){
    .hero-grid,.service-floating-card{grid-template-columns:1fr;gap:30px}
    .sfc-grid{grid-template-columns:1fr}
    .nav-links{display:none;position:fixed;top:0;left:0;right:0;bottom:0;background:rgba(10,10,26,.98);flex-direction:column;justify-content:center;align-items:center;gap:24px;z-index:99}
    .nav-links.active{display:flex}
    .m-toggle{display:flex;z-index:100}
    .m-toggle.active span:nth-child(1){transform:rotate(45deg) translate(5px,5px)}
    .m-toggle.active span:nth-child(2){opacity:0}
    .m-toggle.active span:nth-child(3){transform:rotate(-45deg) translate(5px,-5px)}
    .service-floating-card{padding:32px 24px}
    .sfc-visual .globe{width:140px;height:140px;font-size:3rem}
}
</style>
</head>
<body>
<canvas id="bg"></canvas>
<div class="bg-layer bg-layer-1" id="bg1"></div>
<div class="bg-layer bg-layer-2" id="bg2"></div>
<div class="bg-layer bg-layer-3" id="bg3"></div>
<div class="bg-layer bg-layer-4" id="bg4"></div>
<header id="h">
    <div class="nav">
        <a class="brand" href="/">Seed<span>Studio</span></a>
        <nav class="nav-links" id="nl">
            <a href="#services">Services</a>
            <a href="#about">About</a>
            <a href="#contact">Contact</a>
            <a class="btn-glow" href="mailto:hello@seedstudio.example">Get Started</a>
        </nav>
        <button class="m-toggle" id="mt" aria-label="Menu"><span></span><span></span><span></span></button>
    </div>
</header>
<div class="page">
    <div class="section">
        <div class="section-inner">
            <div class="hero-grid">
                <div>
                    <div class="hero-badge"><span class="d"></span> The Future of AI</div>
                    <h1>Intelligent <span class="g">AI solutions</span> for education & industry</h1>
                    <p>We build next-gen AI platforms for schools, healthcare, manufacturing, and agriculture — simplifying learning, optimizing operations, and driving smarter decisions.</p>
                    <div class="hero-actions">
                        <a class="btn btn-p" href="#contact">
                            Book a Consultation
                            <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round"><line x1="5" y1="12" x2="19" y2="12"/><polyline points="12 5 19 12 12 19"/></svg>
                        </a>
                        <a class="btn btn-s" href="#services">Explore</a>
                    </div>
                </div>
                <div class="hero-visual">
                    <div class="hero-glow-box">
                        <div class="inner">
                            <div class="big-icon">✨</div>
                            <p>Next-Gen AI Platform</p>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </div>
    <div class="section" id="services">
        <div class="section-inner">
            <div class="sh-s reveal"><div class="sh-l">Our Solutions</div><h2 class="sh-t">AI Services</h2><p class="sh-p">Cutting-edge AI tailored for every industry.</p></div>
            <div class="services-showcase">
                <div class="service-floating-card reveal">
                    <div class="card-glow"></div>
                    <div class="sfc-content">
                        <div class="sfc-icon">🎓</div>
                        <h3>Education AI</h3>
                        <p>Transform learning with personalized AI tutoring, real-time teacher analytics, and parent engagement portals.</p>
                        <div class="sfc-grid">
                            <a href="/education-ai/student-learning" class="sfc-item" style="text-decoration:none;display:block"><strong>Student Learning</strong><span>Adaptive AI tutoring</span></a>
                            <a href="/education-ai/teacher-dashboard" class="sfc-item" style="text-decoration:none;display:block"><strong>Teacher Dashboard</strong><span>Real-time analytics</span></a>
                            <a href="/education-ai/parent-portal" class="sfc-item" style="text-decoration:none;display:block"><strong>Parent Portal</strong><span>Progress tracking</span></a>
                            <div class="sfc-item"><strong>24/7 Support</strong><span>Always available</span></div>
                        </div>
                    </div>
                    <div class="sfc-visual"><div class="globe">📚</div></div>
                </div>
                <div class="service-floating-card reveal">
                    <div class="card-glow"></div>
                    <div class="sfc-visual"><div class="globe">🏭</div></div>
                    <div class="sfc-content">
                        <div class="sfc-icon">🏭</div>
                        <h3>Industry AI</h3>
                        <p>Revolutionize healthcare, manufacturing, and automation with AI-powered diagnostics, predictive maintenance, and intelligent workflows.</p>
                        <div class="sfc-grid">
                            <a href="/industry-ai/healthcare" class="sfc-item" style="text-decoration:none;display:block"><strong>Healthcare AI</strong><span>Diagnostic support</span></a>
                            <a href="/industry-ai/mechanical" class="sfc-item" style="text-decoration:none;display:block"><strong>Mechanical AI</strong><span>Predictive maintenance</span></a>
                            <a href="/industry-ai/automation" class="sfc-item" style="text-decoration:none;display:block"><strong>Automation</strong><span>Process optimization</span></a>
                            <div class="sfc-item"><strong>Analytics</strong><span>Data-driven insights</span></div>
                        </div>
                    </div>
                </div>
                <div class="service-floating-card reveal">
                    <div class="card-glow"></div>
                    <div class="sfc-content">
                        <div class="sfc-icon">🌾</div>
                        <h3>Agricultural AI</h3>
                        <p>Boost crop yields with satellite monitoring, precision farming, and AI-powered weather intelligence for smarter agriculture.</p>
                        <div class="sfc-grid">
                            <a href="/agricultural-ai/crop-monitoring" class="sfc-item" style="text-decoration:none;display:block"><strong>Crop Monitoring</strong><span>Real-time field health</span></a>
                            <a href="/agricultural-ai/precision-farming" class="sfc-item" style="text-decoration:none;display:block"><strong>Precision Farming</strong><span>Resource optimization</span></a>
                            <a href="/agricultural-ai/weather-intelligence" class="sfc-item" style="text-decoration:none;display:block"><strong>Weather AI</strong><span>Smart forecasting</span></a>
                            <div class="sfc-item"><strong>Sustainability</strong><span>Eco-friendly farming</span></div>
                        </div>
                    </div>
                    <div class="sfc-visual"><div class="globe">🌱</div></div>
                </div>
            </div>
        </div>
    </div>
    <div class="section" id="about">
        <div class="section-inner">
            <div class="sh-s reveal"><div class="sh-l">About</div><h2 class="sh-t">Why SeedStudio?</h2></div>
            <div class="about-card reveal">
                <p>We build practical AI solutions that help organizations modernize learning, improve efficiency, and unlock smarter operations across education and industry. Our platforms combine cutting-edge technology with intuitive design — built for real-world impact.</p>
            </div>
        </div>
    </div>
    <div class="section" id="contact">
        <div class="section-inner">
            <div class="cta-b reveal">
                <h2>Ready to Transform Your Business?</h2>
                <p>Let's build intelligent solutions tailored to your goals.</p>
                <a class="btn btn-p" href="mailto:hello@seedstudio.example">
                    Contact Us
                    <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round"><line x1="5" y1="12" x2="19" y2="12"/><polyline points="12 5 19 12 12 19"/></svg>
                </a>
            </div>
        </div>
    </div>
</div>
<button class="chat-l" id="chatL" aria-label="Chat">🤖</button>
<div class="chat-p" id="chatP">
    <div class="chat-h"><h4>SeedStudio AI</h4><div class="chat-x" id="chatX">×</div></div>
    <div class="chat-ms" id="chatMs"><div class="chat-m b"><div class="bub">Hi! Ask me about our AI solutions for education, industry, or agriculture.</div></div></div>
    <div class="chat-i">
        <input id="chatIn" type="text" placeholder="Type a message..." />
        <button id="chatSd" type="button">Send</button>
    </div>
</div>
<script>
const h=document.getElementById('h');
window.addEventListener('scroll',function(){if(window.scrollY>50){h.classList.add('scrolled')}else{h.classList.remove('scrolled')}});
const mt=document.getElementById('mt'),nl=document.getElementById('nl');
mt.addEventListener('click',function(){mt.classList.toggle('active');nl.classList.toggle('active')});
nl.querySelectorAll('a').forEach(function(l){l.addEventListener('click',function(){mt.classList.remove('active');nl.classList.remove('active')})});
const obs=new IntersectionObserver(function(e){e.forEach(function(e){if(e.isIntersecting)e.target.classList.add('v')})},{threshold:.1});
document.querySelectorAll('.reveal').forEach(function(el){obs.observe(el)});
const sections=document.querySelectorAll('.section');
const bl=[document.getElementById('bg1'),document.getElementById('bg2'),document.getElementById('bg3'),document.getElementById('bg4')];
function ub(){const sy=window.scrollY+window.innerHeight/2;let ai=0;
sections.forEach(function(s,i){const t=s.offsetTop,b=t+s.offsetHeight;if(sy>=t&&sy<b)ai=i});
bl.forEach(function(l,i){l.style.opacity=i===ai?'1':'0'})}
window.addEventListener('scroll',ub);window.addEventListener('resize',ub);ub();
const c=document.getElementById('bg'),ctx=c.getContext('2d');
c.width=window.innerWidth;c.height=window.innerHeight;
window.addEventListener('resize',function(){c.width=window.innerWidth;c.height=window.innerHeight});
const pts=[],cols=['#6C5CE7','#00D2FF','#00E676','#FF6584'];
for(let i=0;i<80;i++){pts.push({x:Math.random()*c.width,y:Math.random()*c.height,vx:(Math.random()-.5)*.5,vy:(Math.random()-.5)*.5,r:Math.random()*2+1,c:cols[Math.floor(Math.random()*cols.length)],a:Math.random()*.4+.1})}
function dr(){ctx.clearRect(0,0,c.width,c.height);
pts.forEach(function(p){p.x+=p.vx;p.y+=p.vy;if(p.x<0||p.x>c.width)p.vx*=-1;if(p.y<0||p.y>c.height)p.vy*=-1;
ctx.beginPath();ctx.arc(p.x,p.y,p.r,0,Math.PI*2);ctx.fillStyle=p.c;ctx.globalAlpha=p.a;ctx.fill();ctx.globalAlpha=1});
for(let i=0;i<pts.length;i++){for(let j=i+1;j<pts.length;j++){const dx=pts[i].x-pts[j].x,dy=pts[i].y-pts[j].y;
if(Math.sqrt(dx*dx+dy*dy)<150){ctx.beginPath();ctx.moveTo(pts[i].x,pts[i].y);ctx.lineTo(pts[j].x,pts[j].y);
ctx.strokeStyle='rgba(108,92,231,'+(.06)+')';ctx.stroke()}}}
requestAnimationFrame(dr)}
dr();
const chatL=document.getElementById('chatL'),chatP=document.getElementById('chatP'),chatX=document.getElementById('chatX');
const chatMs=document.getElementById('chatMs'),chatIn=document.getElementById('chatIn'),chatSd=document.getElementById('chatSd');
function aM(r,t){const m=document.createElement('div');m.className='chat-m '+r;
const b=document.createElement('div');b.className='bub';b.textContent=t;
m.appendChild(b);chatMs.appendChild(m);chatMs.scrollTop=chatMs.scrollHeight}
function rM(t){const n=t.toLowerCase();
if(/hello|hi|hey/.test(n))return"Hi! I'm the SeedStudio assistant. Ask me about our AI solutions.";
if(/education|student|teacher|parent/.test(n))return"Our Education AI includes tutoring, teacher dashboards, and parent portals.";
if(/healthcare|medical|hospital/.test(n))return"Our Healthcare AI supports diagnostics, workflow automation, and patient engagement.";
if(/farm|crop|agriculture|weather/.test(n))return"Our Agriculture AI offers crop monitoring, precision farming, and weather intelligence.";
if(/automation|industry|mechanical/.test(n))return"We provide Industry AI for equipment maintenance, production automation, and analytics.";
return"Great question! We can help you build AI solutions for your business. Tell me more about your goals.";}
chatL.addEventListener('click',function(){chatP.classList.toggle('active')});
chatX.addEventListener('click',function(){chatP.classList.remove('active')});
chatSd.addEventListener('click',function(){const t=chatIn.value.trim();if(!t)return;aM('u',t);chatIn.value='';setTimeout(function(){aM('b',rM(t))},500)});
chatIn.addEventListener('keydown',function(e){if(e.key==='Enter'){e.preventDefault();chatSd.click()}});
</script>
</body>
</html>"""


@router.get("/education-ai/student-learning", response_class=HTMLResponse)
async def education_student_learning():
    return render_service_page(
        title="Student Learning Agent",
        hero_title="Personalized <span class='g'>AI tutoring</span> for every student.",
        intro="Our adaptive learning AI tutors students individually, adjusting difficulty based on performance and providing step-by-step guidance through complex concepts.",
        features=[
            ("Adaptive Learning", "Content difficulty adjusts based on student performance in real-time."),
            ("Multiple Subjects", "Coverage across math, science, languages, and more."),
            ("Step-by-Step Guidance", "Interactive problem-solving with hints and explanations."),
            ("Progress Tracking", "Detailed analytics on student strengths and weak areas."),
            ("24/7 Availability", "Learning support available anytime, anywhere."),
            ("Engagement Metrics", "Keep students motivated with achievement badges and progress reports."),
        ],
        how_it_works=[
            ("Assessment", "The AI assesses the student's current knowledge level."),
            ("Personalized Path", "Creates a customized learning journey based on goals and pace."),
            ("Practice & Feedback", "Students practice with instant feedback and guidance."),
        ],
        benefits=[
            "Improve test scores by 20-30% on average",
            "Reduce learning anxiety with personalized support",
            "Build confidence through achievable milestones",
            "Identify knowledge gaps early for intervention",
            "Support diverse learning styles and paces",
            "Complement classroom teaching with extra practice",
        ],
    )


@router.get("/education-ai/teacher-dashboard", response_class=HTMLResponse)
async def education_teacher_dashboard():
    return render_service_page(
        title="Teacher Dashboard",
        hero_title="Classroom management <span class='g'>powered by AI</span> insights.",
        intro="Monitor student engagement, track individual progress, and get actionable recommendations to improve teaching effectiveness.",
        features=[
            ("Real-Time Analytics", "Live view of student engagement and performance metrics."),
            ("Individual Profiles", "Detailed progress reports for each student."),
            ("Class Overview", "Identify struggling students and success patterns."),
            ("Automated Grading", "Save time with AI-assisted assignment evaluation."),
            ("Lesson Planning Tools", "Suggestions for improving lessons based on class data."),
            ("Parent Communication", "Easy sharing of reports with parents and guardians."),
        ],
        how_it_works=[
            ("Login & Setup", "Connect your class roster and learning materials."),
            ("Monitor Progress", "View real-time student activity and performance data."),
            ("Act on Insights", "Use recommendations to adjust teaching and provide support."),
        ],
        benefits=[
            "Save 5-10 hours per week on grading and reporting",
            "Identify at-risk students early for targeted help",
            "Improve class performance by data-driven teaching",
            "Streamline communication with parents",
            "More time for meaningful student interaction",
            "Better understanding of individual learning needs",
        ],
    )


@router.get("/education-ai/parent-portal", response_class=HTMLResponse)
async def education_parent_portal():
    return render_service_page(
        title="Parent Portal",
        hero_title="Stay connected to your <span class='g'>child's learning</span> journey.",
        intro="Get clear updates on your child's progress, strengths, and areas for improvement with actionable recommendations for home support.",
        features=[
            ("Progress Reports", "Weekly and monthly summaries of learning achievements."),
            ("Strength & Gaps", "Clear breakdown of what your child excels at and where to focus."),
            ("Recommendations", "Specific suggestions for homework help and practice."),
            ("Achievement Tracking", "Celebrate milestones and skill mastery."),
            ("Communication Hub", "Direct messaging with teachers for updates and concerns."),
            ("Learning Resources", "Curated materials and tips for supporting at home."),
        ],
        how_it_works=[
            ("Access Portal", "Receive login credentials at school enrollment."),
            ("Review Updates", "Check progress reports and insights weekly."),
            ("Take Action", "Use recommendations to support learning at home."),
        ],
        benefits=[
            "Understand your child's learning better",
            "Identify issues early and address them quickly",
            "Support learning with targeted home practice",
            "Build stronger school-home partnerships",
            "Celebrate progress and build confidence",
            "Stay informed without guessing or worrying",
        ],
    )


@router.get("/industry-ai/healthcare", response_class=HTMLResponse)
async def industry_healthcare():
    return render_service_page(
        title="Healthcare AI",
        hero_title="Smarter healthcare <span class='g'>operations with AI</span> support.",
        intro="Improve diagnostics, optimize workflows, and reduce administrative burden with AI-powered healthcare solutions.",
        features=[
            ("Diagnostic Support", "AI assists in analyzing medical images and patient data."),
            ("Workflow Optimization", "Streamline patient intake, scheduling, and operations."),
            ("Risk Assessment", "Predict high-risk patients for early intervention."),
            ("Resource Planning", "Optimize staffing and equipment allocation."),
            ("Compliance Monitoring", "Automated tracking of healthcare regulations and standards."),
            ("Patient Communication", "Chatbots for common questions and appointment management."),
        ],
        how_it_works=[
            ("Integration", "Connect existing hospital systems and data sources."),
            ("AI Training", "Models trained on your healthcare data for accuracy."),
            ("Deployment", "Roll out with staff training and ongoing support."),
        ],
        benefits=[
            "Reduce diagnostic errors by 15-20%",
            "Improve patient throughput by 25-30%",
            "Lower administrative costs significantly",
            "Enhance staff satisfaction with automation",
            "Better compliance and documentation",
            "Improve patient outcomes and satisfaction",
        ],
    )


@router.get("/industry-ai/mechanical", response_class=HTMLResponse)
async def industry_mechanical():
    return render_service_page(
        title="Mechanical AI",
        hero_title="Predictive maintenance and <span class='g'>equipment intelligence</span>.",
        intro="Monitor equipment health, predict failures before they happen, and reduce downtime with AI-powered mechanical systems.",
        features=[
            ("Equipment Monitoring", "Real-time sensor data analysis for equipment health."),
            ("Failure Prediction", "Identify potential breakdowns before they occur."),
            ("Maintenance Scheduling", "Optimize maintenance windows to minimize downtime."),
            ("Performance Analytics", "Track efficiency trends and identify improvements."),
            ("Alert System", "Instant notifications for critical equipment issues."),
            ("Historical Analysis", "Learn from past failures to prevent future ones."),
        ],
        how_it_works=[
            ("Install Sensors", "Deploy monitoring sensors on critical equipment."),
            ("Data Collection", "Continuous collection and analysis of equipment data."),
            ("Predictive Action", "Schedule maintenance and prevent failures proactively."),
        ],
        benefits=[
            "Reduce unexpected downtime by 40-50%",
            "Lower maintenance costs through better planning",
            "Extend equipment lifespan",
            "Improve production efficiency",
            "Safer operations with fewer failures",
            "Data-driven maintenance decisions",
        ],
    )


@router.get("/industry-ai/automation", response_class=HTMLResponse)
async def industry_automation():
    return render_service_page(
        title="Industrial Automation",
        hero_title="Automate repetitive tasks and <span class='g'>boost productivity</span>.",
        intro="Reduce manual work, minimize errors, and improve throughput with intelligent industrial automation solutions.",
        features=[
            ("Process Automation", "Automate repetitive workflows and manual tasks."),
            ("Quality Control", "AI-powered inspection and defect detection."),
            ("Error Reduction", "Minimize human errors in production and operations."),
            ("Throughput Optimization", "Increase output while maintaining quality."),
            ("Cost Reduction", "Lower labor and operational costs significantly."),
            ("Scalability", "Easily scale operations without proportional cost increase."),
        ],
        how_it_works=[
            ("Process Audit", "Identify automation opportunities in your operations."),
            ("Solution Design", "Build custom automation workflows for your needs."),
            ("Implementation", "Deploy and train staff on new automated processes."),
        ],
        benefits=[
            "Reduce operational costs by 30-40%",
            "Improve production consistency and quality",
            "Increase throughput by 50% or more",
            "Reduce manual errors to near-zero",
            "Free staff for higher-value tasks",
            "Scale efficiently without adding headcount",
        ],
    )


@router.get("/agricultural-ai/crop-monitoring", response_class=HTMLResponse)
async def agricultural_crop_monitoring():
    return render_service_page(
        title="Crop Monitoring",
        hero_title="Real-time field health <span class='g'>monitoring with AI</span>.",
        intro="Use satellite and sensor data to monitor crop health, detect issues early, and take action before problems spread.",
        features=[
            ("Satellite Imaging", "High-resolution field monitoring using satellite data."),
            ("Sensor Networks", "Ground-level sensors for detailed crop and soil monitoring."),
            ("Disease Detection", "AI identifies signs of disease or stress early."),
            ("Pest Alerts", "Early warning system for pest infestations."),
            ("Health Index", "Overall crop health score and trend analysis."),
            ("Action Recommendations", "Specific interventions based on detected issues."),
        ],
        how_it_works=[
            ("Setup Monitoring", "Deploy sensors and connect satellite data sources."),
            ("Daily Analysis", "AI analyzes data to detect issues and changes."),
            ("Act Quickly", "Get alerts and recommendations for timely intervention."),
        ],
        benefits=[
            "Detect crop issues 2-3 weeks earlier than visual inspection",
            "Reduce crop losses from disease by 20-30%",
            "Minimize pesticide use with targeted applications",
            "Improve early warning for environmental stress",
            "Data-backed decisions for interventions",
            "Increase yield through proactive management",
        ],
    )


@router.get("/agricultural-ai/precision-farming", response_class=HTMLResponse)
async def agricultural_precision_farming():
    return render_service_page(
        title="Precision Farming",
        hero_title="Optimize every resource for <span class='g'>maximum yield</span>.",
        intro="Use AI-driven insights to optimize irrigation, fertilization, and resource allocation for better harvests and lower costs.",
        features=[
            ("Irrigation Optimization", "AI determines ideal watering schedules and amounts."),
            ("Fertilization Recommendations", "Targeted nutrient application based on soil analysis."),
            ("Yield Prediction", "Forecast harvest volume and quality."),
            ("Resource Efficiency", "Minimize water, fertilizer, and input waste."),
            ("Soil Health Monitoring", "Track soil conditions and long-term productivity."),
            ("ROI Analysis", "Calculate return on investment for each practice."),
        ],
        how_it_works=[
            ("Data Collection", "Gather soil, weather, and field performance data."),
            ("AI Optimization", "Models optimize resource use for your specific conditions."),
            ("Implementation", "Apply recommendations to fields and monitor results."),
        ],
        benefits=[
            "Reduce water usage by 25-35%",
            "Cut fertilizer costs by 20-30%",
            "Increase crop yield by 15-25%",
            "Improve soil health and sustainability",
            "Reduce environmental impact",
            "Better profitability per acre",
        ],
    )


@router.get("/agricultural-ai/weather-intelligence", response_class=HTMLResponse)
async def agricultural_weather_intelligence():
    return render_service_page(
        title="Weather Intelligence",
        hero_title="Make better farm decisions with <span class='g'>AI weather insights</span>.",
        intro="Access AI-powered weather forecasting and recommendations tailored to your farm for smarter planning and reduced risk.",
        features=[
            ("Predictive Forecasting", "Hyper-local weather predictions for your farm."),
            ("Frost & Freeze Alerts", "Early warning for temperature extremes."),
            ("Rainfall Forecasting", "Precise rain predictions for irrigation planning."),
            ("Planting Windows", "Recommendations for optimal planting times."),
            ("Harvest Timing", "Weather-based harvest recommendations."),
            ("Risk Assessment", "Evaluate weather risks for crop insurance decisions."),
        ],
        how_it_works=[
            ("Location Setup", "Configure your farm location and crop types."),
            ("Weather Data", "AI aggregates multiple weather data sources."),
            ("Recommendations", "Get daily insights and planning recommendations."),
        ],
        benefits=[
            "Plan irrigation and field work more accurately",
            "Reduce frost and weather-related crop losses",
            "Optimize planting timing for better germination",
            "Improve harvest timing and quality",
            "Reduce irrigation waste with precise forecasts",
            "Better risk management and insurance decisions",
        ],
    )


@router.get("/frontend/info")
async def frontend_info():
    return {
        "frontend": "placeholder package",
        "message": "Frontend package created for UI routes and assets.",
    }