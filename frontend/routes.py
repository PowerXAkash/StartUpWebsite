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
        f"<div class=\"card\"><h3>{item}</h3><p>{desc}</p></div>"
        for item, desc in features
    )
    how_it_works_items = "".join(
        f"<div class=\"step\"><div class=\"step-num\">{i+1}</div><h4>{title}</h4><p>{desc}</p></div>"
        for i, (title, desc) in enumerate(how_it_works)
    )
    benefit_items = "".join(f"<li>{b}</li>" for b in benefits)
    
    return f"""
    <!DOCTYPE html>
    <html lang="en">
      <head>
        <meta charset="UTF-8" />
        <meta name="viewport" content="width=device-width, initial-scale=1.0" />
        <title>{title}</title>
        <style>
          :root {{
            --bg: #f4f8fc;
              <a class="brand" href="/">Seed<span>Studio</span></a>
            --surface-2: #eef5ff;
            --text: #14213d;
            --muted: #5d6b82;
            --accent: #1f4ed8;
            --accent-2: #2563eb;
            --accent-soft: #dbeafe;
            --border: #dfe8f6;
            --shadow: 0 18px 45px rgba(20, 33, 61, 0.08);
          }}
          * {{ box-sizing: border-box; }}
          body {{
            margin: 0;
            font-family: "Segoe UI", "Inter", Roboto, Arial, sans-serif;
            background: linear-gradient(135deg, #fbfdff 0%, #f2f7ff 100%);
              <a class="btn btn-primary" href="mailto:hello@seedstudio.example">{cta_text}</a>
            line-height: 1.7;
          }}
          a {{ color: inherit; text-decoration: none; }}
          .container {{ width: min(1180px, calc(100% - 32px)); margin: 0 auto; }}
          header {{
            padding: 20px 0;
            position: sticky;
            top: 0;
            background: rgba(255,255,255,0.86);
            backdrop-filter: blur(12px);
            z-index: 10;
            border-bottom: 1px solid rgba(31, 78, 216, 0.08);
          }}
          .nav {{ display: flex; align-items: center; justify-content: space-between; gap: 20px; }}
          .brand {{ font-size: 1.25rem; font-weight: 700; letter-spacing: 0.03em; color: var(--accent); }}
          .brand span {{ color: var(--text); }}
          .nav-links {{ display: flex; gap: 22px; color: var(--muted); font-weight: 500; }}
          .nav-links a:hover {{ color: var(--accent); }}
          main {{ padding: 40px 0; }}
          .hero {{
            padding: 40px 0 20px;
            border-bottom: 1px solid var(--border);
            margin-bottom: 40px;
          }}
          .eyebrow {{
            display: inline-block;
            padding: 7px 12px;
            border-radius: 999px;
            font-size: 0.78rem;
            font-weight: 700;
            letter-spacing: 0.16em;
            text-transform: uppercase;
            background: var(--accent-soft);
            color: var(--accent);
            margin-bottom: 12px;
          }}
          .hero h1 {{
            font-size: clamp(2rem, 3.3vw, 2.8rem);
            line-height: 1.2;
            margin: 0 0 14px;
            font-weight: 700;
          }}
          .hero p {{ color: var(--muted); font-size: 1.03rem; margin: 0 0 20px; max-width: 760px; }}
          .btn {{
            display: inline-block;
            padding: 12px 18px;
            border-radius: 999px;
            font-weight: 600;
            transition: transform 0.2s ease, box-shadow 0.2s ease;
          }}
          .btn:hover {{ transform: translateY(-2px); }}
          .btn-primary {{ background: linear-gradient(90deg, var(--accent), var(--accent-2)); color: #fff; box-shadow: 0 10px 24px rgba(31,78,216,0.18); }}
          .btn-secondary {{ background: var(--surface); color: var(--text); border: 1px solid var(--border); }}
          
          section {{ margin-bottom: 60px; }}
          .section-title {{
            color: var(--accent);
            text-transform: uppercase;
            letter-spacing: 0.2em;
            font-size: 0.8rem;
            font-weight: 700;
            margin-bottom: 8px;
          }}
          .section-heading {{ font-size: 1.8rem; margin-top: 0; margin-bottom: 12px; }}
          
          .feature-grid {{ display: grid; grid-template-columns: repeat(2, minmax(0, 1fr)); gap: 20px; margin-top: 16px; }}
          .card {{
            background: var(--surface);
            border: 1px solid var(--border);
            border-radius: 18px;
            padding: 22px;
            box-shadow: var(--shadow);
          }}
          .card h3 {{ margin-top: 0; margin-bottom: 8px; }}
          .card p {{ color: var(--muted); margin: 0; }}
          
          .steps {{ display: grid; grid-template-columns: repeat(3, minmax(0, 1fr)); gap: 24px; margin-top: 20px; }}
          .step {{
            display: flex;
            flex-direction: column;
            align-items: center;
            text-align: center;
          }}
          .step-num {{
            width: 52px;
            height: 52px;
            border-radius: 50%;
            background: linear-gradient(90deg, var(--accent), var(--accent-2));
            color: white;
            display: flex;
            align-items: center;
            justify-content: center;
            font-weight: 700;
            font-size: 1.3rem;
            margin-bottom: 12px;
          }}
          .step h4 {{ margin: 8px 0 4px; }}
          .step p {{ color: var(--muted); font-size: 0.95rem; margin: 0; }}
          
          .benefits-list {{
            background: var(--surface);
            border: 1px solid var(--border);
            border-radius: 18px;
            padding: 28px;
            box-shadow: var(--shadow);
          }}
          .benefits-list ul {{ margin: 0; padding-left: 20px; }}
          .benefits-list li {{ margin-bottom: 12px; color: var(--text); }}
          
          .cta {{
            margin-top: 24px;
            padding: 28px;
            border-radius: 24px;
            background: linear-gradient(90deg, rgba(31,78,216,0.08), rgba(37,99,235,0.03));
            border: 1px solid rgba(31,78,216,0.12);
            text-align: center;
          }}
          
          @media (max-width: 860px) {{
            .feature-grid, .steps {{ grid-template-columns: 1fr; }}
            .nav-links {{ display: none; }}
          }}
        </style>
      </head>
      <body>
        <header>
          <div class="container nav">
            <a class="brand" href="/">Seed<span>Studio</span></a>
            <nav class="nav-links">
              <a href="/">Home</a>
              <a href="/education-ai">Education</a>
              <a href="/industry-ai">Industry</a>
              <a href="/agricultural-ai">Agriculture</a>
            </nav>
          </div>
        </header>
        
        <main class="container">
          <section class="hero">
            <div class="eyebrow">{title}</div>
            <h1>{hero_title}</h1>
            <p>{intro}</p>
            <a class="btn btn-primary" href="mailto:hello@novastudio.example">{cta_text}</a>
          </section>
          
          <section>
            <div class="section-title">Key Features</div>
            <h2 class="section-heading">What's included</h2>
            <div class="feature-grid">
              {feature_items}
            </div>
          </section>
          
          <section>
            <div class="section-title">How it works</div>
            <h2 class="section-heading">Three simple steps</h2>
            <div class="steps">
              {how_it_works_items}
            </div>
          </section>
          
          <section>
            <div class="section-title">Why choose us</div>
            <h2 class="section-heading">Core benefits</h2>
            <div class="benefits-list">
              <ul>
                {benefit_items}
              </ul>
            </div>
          </section>
          
          <section class="cta">
            <h2>Ready to get started?</h2>
            <p>Contact us today to discuss how this solution fits your needs.</p>
            <a class="btn btn-primary" href="mailto:hello@seedstudio.example">Schedule a consultation</a>
          </section>
        </main>
      </body>
    </html>
    """



@router.get("/", response_class=HTMLResponse)
async def frontend_index():
    return """
    <!DOCTYPE html>
    <html lang="en">
      <head>
        <meta charset="UTF-8" />
        <meta name="viewport" content="width=device-width, initial-scale=1.0" />
        <title>AI Business Solutions</title>
        <style>
          :root {
            --bg: #f4f8fc;
            --surface: #ffffff;
            --surface-2: #eef5ff;
            --text: #14213d;
            --muted: #5d6b82;
            --accent: #1f4ed8;
            --accent-2: #2563eb;
            --accent-soft: #dbeafe;
            --border: #dfe8f6;
            --shadow: 0 18px 45px rgba(20, 33, 61, 0.08);
          }
          * { box-sizing: border-box; }
          body {
            margin: 0;
            font-family: "Segoe UI", "Inter", Roboto, Arial, sans-serif;
            background: linear-gradient(135deg, #fbfdff 0%, #f2f7ff 100%);
            color: var(--text);
            line-height: 1.7;
          }
          a { color: inherit; text-decoration: none; }
          .container { width: min(1180px, calc(100% - 32px)); margin: 0 auto; }
          header {
            padding: 20px 0;
            position: sticky;
            top: 0;
            background: rgba(255,255,255,0.86);
            backdrop-filter: blur(12px);
            z-index: 10;
            border-bottom: 1px solid rgba(31, 78, 216, 0.08);
          }
          .nav { display: flex; align-items: center; justify-content: space-between; gap: 20px; }
          .brand { font-size: 1.25rem; font-weight: 700; letter-spacing: 0.03em; color: var(--accent); }
          .brand span { color: var(--text); }
          .nav-links { display: flex; gap: 22px; color: var(--muted); font-weight: 500; }
          .nav-links a:hover { color: var(--accent); }
          .hero {
            display: grid;
            grid-template-columns: 1.05fr 0.95fr;
            gap: 40px;
            align-items: center;
            padding: 74px 0 56px;
          }
          .eyebrow {
            display: inline-block;
            padding: 7px 12px;
            border-radius: 999px;
            font-size: 0.78rem;
            font-weight: 700;
            letter-spacing: 0.16em;
            text-transform: uppercase;
            background: var(--accent-soft);
            color: var(--accent);
            margin-bottom: 16px;
          }
          .hero h1 {
            font-size: clamp(2.2rem, 4vw, 3.4rem);
            line-height: 1.15;
            margin: 0 0 16px;
            font-weight: 700;
          }
          .hero p { color: var(--muted); font-size: 1.03rem; margin: 0 0 24px; max-width: 620px; }
          .hero-actions { display: flex; gap: 14px; flex-wrap: wrap; }
          .btn {
            display: inline-block;
            padding: 12px 18px;
            border-radius: 999px;
            font-weight: 600;
            transition: transform 0.2s ease, box-shadow 0.2s ease;
          }
          .btn:hover { transform: translateY(-2px); }
          .btn-primary { background: linear-gradient(90deg, var(--accent), var(--accent-2)); color: #fff; box-shadow: 0 10px 24px rgba(31,78,216,0.18); }
          .btn-secondary { background: var(--surface); color: var(--text); border: 1px solid var(--border); }
          .hero-card {
            background: var(--surface);
            border: 1px solid var(--border);
            border-radius: 24px;
            padding: 24px;
            box-shadow: var(--shadow);
          }
          .metric-grid { display: grid; grid-template-columns: repeat(2, minmax(0, 1fr)); gap: 12px; margin-top: 16px; }
          .metric {
            background: var(--surface-2);
            padding: 16px;
            border-radius: 14px;
          }
          .metric strong { display: block; font-size: 1.1rem; color: var(--accent); }
          section { padding: 26px 0 64px; }
          .section-title {
            color: var(--accent);
            text-transform: uppercase;
            letter-spacing: 0.2em;
            font-size: 0.8rem;
            font-weight: 700;
            margin-bottom: 8px;
          }
          .section-heading { font-size: 1.8rem; margin-top: 0; margin-bottom: 24px; }
          
          .service-category {
            margin-bottom: 40px;
            padding: 24px;
            border-radius: 20px;
            background: linear-gradient(135deg, rgba(31, 78, 216, 0.05), rgba(37, 99, 235, 0.03));
            border: 1px solid rgba(31, 78, 216, 0.1);
          }
          .service-category h3 {
            color: var(--text);
            margin-top: 0;
            margin-bottom: 16px;
            display: flex;
            align-items: center;
            gap: 12px;
            font-size: 1.3rem;
          }
          
          .feature-grid { display: grid; grid-template-columns: repeat(3, minmax(0, 1fr)); gap: 20px; margin-top: 20px; }
          .card {
            background: var(--surface);
            border: 1px solid var(--border);
            border-radius: 18px;
            padding: 22px;
            box-shadow: var(--shadow);
            transition: transform 0.2s ease, box-shadow 0.2s ease;
          }
          .card:hover {
            transform: translateY(-4px);
            box-shadow: 0 24px 60px rgba(31, 78, 216, 0.12);
          }
          .card-icon-wrap {
            width: 62px;
            height: 62px;
            border-radius: 50%;
            display: grid;
            place-items: center;
            margin-bottom: 18px;
            background: linear-gradient(180deg, rgba(255,255,255,0.94), rgba(226, 239, 255, 0.9));
            border: 1px solid rgba(31, 78, 216, 0.12);
            box-shadow: 0 12px 28px rgba(31, 78, 216, 0.08);
          }
          .card-icon {
            width: 30px;
            height: 30px;
            color: var(--accent);
          }
          .card h3 { margin-top: 0; margin-bottom: 8px; }
          .card p { color: var(--muted); margin: 0; }
          .cta {
            text-align: center;
            padding: 32px;
            border-radius: 24px;
            background: linear-gradient(90deg, rgba(31,78,216,0.08), rgba(37,99,235,0.03));
            border: 1px solid rgba(31,78,216,0.12);
          }
          @media (max-width: 860px) {
            .hero, .feature-grid { grid-template-columns: 1fr; }
            .nav-links { display: none; }
          }
        </style>
      </head>
      <body>
        <header>
          <div class="container nav">
            <a class="brand" href="/">Seed<span>Studio</span></a>
            <nav class="nav-links">
              <a href="#services">Services</a>
              <a href="#about">About</a>
              <a href="#contact">Contact</a>
            </nav>
          </div>
        </header>

        <main class="container">
          <section class="hero">
            <div>
              <div class="eyebrow">AI business solutions</div>
              <h1>Intelligent AI solutions for education and industries.</h1>
              <p>We build AI-powered platforms for schools, colleges, healthcare, manufacturing, and agriculture to simplify learning, improve operations, and accelerate smarter decisions.</p>
              <div class="hero-actions">
                <a class="btn btn-primary" href="#contact">Book a consultation</a>
                <a class="btn btn-secondary" href="#services">Explore solutions</a>
              </div>
            </div>
            <div class="hero-card">
              <h3>What we enable</h3>
              <p>Personalized learning support, progress tracking, and industry-ready automation built around real business needs.</p>
              <div class="metric-grid">
                <div class="metric"><strong>Learning AI</strong><span>For students and teachers</span></div>
                <div class="metric"><strong>Industry AI</strong><span>Healthcare, mechanical, agriculture</span></div>
                <div class="metric"><strong>Progress Insights</strong><span>Student growth and evaluation</span></div>
                <div class="metric"><strong>Automation</strong><span>Smarter operations and workflows</span></div>
              </div>
            </div>
          </section>

          <section id="services">
            <div class="section-title">Solutions</div>
            <h2 class="section-heading">Our AI Service Offerings</h2>
            
            <div class="service-category" style="background: linear-gradient(135deg, rgba(59, 130, 246, 0.08), rgba(99, 102, 241, 0.05)) url('data:image/svg+xml,<svg xmlns=%22http://www.w3.org/2000/svg%22 viewBox=%220 0 400 200%22><defs><pattern id=%22dots%22 x=%2240%22 y=%2240%22 width=%2240%22 height=%2240%22 patternUnits=%22userSpaceOnUse%22><circle cx=%2220%22 cy=%2220%22 r=%222%22 fill=%22rgba(59,130,246,0.1)%22/></pattern></defs><rect width=%22400%22 height=%22200%22 fill=%22url(%23dots)%22/></svg>') no-repeat right; background-size: auto, 300px 200px;">
              <h3>🎓 Education AI</h3>
              <div class="feature-grid">
                <a class="card" href="/education-ai/student-learning" style="cursor: pointer;">
                  <div class="card-icon-wrap"><svg class="card-icon" viewBox="0 0 24 24" fill="currentColor"><path d="M12 2C7 2 3.25 5.75 3.25 10.75c0 5.5 4.75 9 8.75 11.25 4-2.25 8.75-5.75 8.75-11.25C20.75 5.75 17 2 12 2zm0 15.5c-2.6 0-4.75-2.1-4.75-4.75S9.4 8 12 8s4.75 2.1 4.75 4.75S14.6 17.5 12 17.5z"/></svg></div>
                  <h3>Student Learning Agent</h3>
                  <p>Personalized AI tutoring that adapts to each student's learning pace and style.</p>
                </a>
                <a class="card" href="/education-ai/teacher-dashboard" style="cursor: pointer;">
                  <div class="card-icon-wrap"><svg class="card-icon" viewBox="0 0 24 24" fill="currentColor"><path d="M5 4h14a1 1 0 0 1 1 1v13.5a.5.5 0 0 1-.5.5H5.5a.5.5 0 0 1-.5-.5V5a1 1 0 0 1 1-1zm2 4h10v2H7V8zm0 4h6v2H7v-2zm0 4h10v1.5H7V16z"/></svg></div>
                  <h3>Teacher Dashboard</h3>
                  <p>Real-time classroom analytics and student engagement tracking tools.</p>
                </a>
                <a class="card" href="/education-ai/parent-portal" style="cursor: pointer;">
                  <div class="card-icon-wrap"><svg class="card-icon" viewBox="0 0 24 24" fill="currentColor"><path d="M12 12a5 5 0 1 0-5-5 5 5 0 0 0 5 5zm0 2c-3.33 0-10 1.67-10 5v2h20v-2c0-3.33-6.67-5-10-5z"/></svg></div>
                  <h3>Parent Portal</h3>
                  <p>Clear dashboards showing student progress and learning recommendations.</p>
                </a>
              </div>
            </div>

            <div class="service-category" style="background: linear-gradient(135deg, rgba(168, 85, 247, 0.08), rgba(139, 92, 246, 0.05)) url('data:image/svg+xml,<svg xmlns=%22http://www.w3.org/2000/svg%22 viewBox=%220 0 400 200%22><defs><pattern id=%22grid%22 x=%2240%22 y=%2240%22 width=%2240%22 height=%2240%22 patternUnits=%22userSpaceOnUse%22><rect x=%221%22 y=%221%22 width=%2238%22 height=%2238%22 fill=%22none%22 stroke=%22rgba(168,85,247,0.1)%22 stroke-width=%220.5%22/></pattern></defs><rect width=%22400%22 height=%22200%22 fill=%22url(%23grid)%22/></svg>') no-repeat right; background-size: auto, 300px 200px;">
              <h3>🏭 Industry AI</h3>
              <div class="feature-grid">
                <a class="card" href="/industry-ai/healthcare" style="cursor: pointer;">
                  <div class="card-icon-wrap"><svg class="card-icon" viewBox="0 0 24 24" fill="currentColor"><path d="M12 2a9 9 0 1 0 9 9 9 9 0 0 0-9-9zm1 12h-2v-2H8v-2h3V8h2v2h3v2h-3v2z"/></svg></div>
                  <h3>Healthcare AI</h3>
                  <p>AI solutions for diagnostic support and hospital workflow optimization.</p>
                </a>
                <a class="card" href="/industry-ai/mechanical" style="cursor: pointer;">
                  <div class="card-icon-wrap"><svg class="card-icon" viewBox="0 0 24 24" fill="currentColor"><path d="M12 7a5 5 0 1 0 5 5 5 5 0 0 0-5-5zm0 8a3 3 0 1 1 3-3 3 3 0 0 1-3 3z"/><path d="M18.4 13.6l1.2-1.2-1.3-2.3-2.1.4a6.2 6.2 0 0 0-1.1-1.1l.4-2.1-2.3-1.3-1.2 1.2a6.2 6.2 0 0 0-2.4 0L8.5 6.6 6.2 7.9l.4 2.1a6.2 6.2 0 0 0-1.1 1.1l-2.1-.4-1.3 2.3 1.2 1.2a6.2 6.2 0 0 0 0 2.4L2.9 16l1.3 2.3 2.1-.4a6.2 6.2 0 0 0 1.1 1.1l-.4 2.1 2.3 1.3 1.2-1.2a6.2 6.2 0 0 0 2.4 0l1.2 1.2 2.3-1.3-.4-2.1a6.2 6.2 0 0 0 1.1-1.1l2.1.4 1.3-2.3-1.2-1.2a6.2 6.2 0 0 0 0-2.4z" opacity=".4"/></svg></div>
                  <h3>Mechanical AI</h3>
                  <p>Equipment monitoring and predictive maintenance for industrial operations.</p>
                </a>
                <a class="card" href="/industry-ai/automation" style="cursor: pointer;">
                  <div class="card-icon-wrap"><svg class="card-icon" viewBox="0 0 24 24" fill="currentColor"><path d="M4 5h16v14H4z" opacity=".2"/><path d="M20 4H4a1 1 0 0 0-1 1v14a1 1 0 0 0 1 1h16a1 1 0 0 0 1-1V5a1 1 0 0 0-1-1zm-1 13H5V6h14v11zm-2-8h-4V7h4zm-6 0H8V7h4zm6 4h-4v-2h4zm-6 0H8v-2h4z"/></svg></div>
                  <h3>Industrial Automation</h3>
                  <p>Automate repetitive processes and improve operational efficiency.</p>
                </a>
              </div>
            </div>

            <div class="service-category" style="background: linear-gradient(135deg, rgba(34, 197, 94, 0.08), rgba(16, 185, 129, 0.05)) url('data:image/svg+xml,<svg xmlns=%22http://www.w3.org/2000/svg%22 viewBox=%220 0 400 200%22><defs><pattern id=%22leaves%22 x=%2260%22 y=%2260%22 width=%2260%22 height=%2260%22 patternUnits=%22userSpaceOnUse%22><path d=%22M30 10 Q40 30 30 50 Q20 30 30 10%22 fill=%22rgba(34,197,94,0.08)%22/></pattern></defs><rect width=%22400%22 height=%22200%22 fill=%22url(%23leaves)%22/></svg>') no-repeat right; background-size: auto, 300px 200px;">
              <h3>🌾 Agricultural AI</h3>
              <div class="feature-grid">
                <a class="card" href="/agricultural-ai/crop-monitoring" style="cursor: pointer;">
                  <div class="card-icon-wrap"><svg class="card-icon" viewBox="0 0 24 24" fill="currentColor"><path d="M12 2C7.5 2 4 5.5 4 10c0 5.25 6 10 8 10s8-4.75 8-10c0-4.5-3.5-8-8-8zm0 8.5A2.5 2.5 0 1 1 14.5 8 2.5 2.5 0 0 1 12 10.5z"/></svg></div>
                  <h3>Crop Monitoring</h3>
                  <p>Real-time field monitoring and early issue detection using AI.</p>
                </a>
                <a class="card" href="/agricultural-ai/precision-farming" style="cursor: pointer;">
                  <div class="card-icon-wrap"><svg class="card-icon" viewBox="0 0 24 24" fill="currentColor"><path d="M12 2l5 9h-3l2 7-4-3-4 3 2-7H7l5-9zm0 2.2L9.6 9h4.8L12 4.2z"/></svg></div>
                  <h3>Precision Farming</h3>
                  <p>AI-optimized irrigation, fertilization, and resource management.</p>
                </a>
                <a class="card" href="/agricultural-ai/weather-intelligence" style="cursor: pointer;">
                  <div class="card-icon-wrap"><svg class="card-icon" viewBox="0 0 24 24" fill="currentColor"><path d="M18.5 10.5a4.5 4.5 0 0 0-8.9-1.4A3.5 3.5 0 0 0 6 13.5h12a3.5 3.5 0 0 0 .5-3z" opacity=".4"/><path d="M16 18h-1.5l1.5-1.5 1.5 1.5H16zm-8 0H6.5l1.5-1.5 1.5 1.5H8z"/></svg></div>
                  <h3>Weather Intelligence</h3>
                  <p>Predictive weather analytics and farm planning recommendations.</p>
                </a>
              </div>
            </div>          </section>

          <section id="about">
            <div class="section-title">About</div>
            <h2 class="section-heading">Why Choose Our AI Solutions</h2>
            <p>We create practical AI business solutions that help organizations modernize learning, improve efficiency, and unlock smarter operations across education and industry. Our platforms are designed with real-world needs in mind, combining cutting-edge technology with intuitive interfaces.</p>
          </section>

          <section id="contact" class="cta">
            <h2>Ready to transform your business with AI?</h2>
            <p>Let’s build intelligent solutions tailored to your goals.</p>
            <a class="btn btn-primary" href="mailto:hello@seedstudio.example">Contact us</a>
          </section>
        </main>
      </body>
    </html>
    """


@router.get("/education-ai/student-learning", response_class=HTMLResponse)
async def education_student_learning():
    return render_service_page(
        title="Student Learning Agent",
        hero_title="Personalized AI tutoring for every student.",
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
        hero_title="Classroom management powered by AI insights.",
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
        hero_title="Stay connected to your child's learning journey.",
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
        hero_title="Smarter healthcare operations with AI support.",
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
        hero_title="Predictive maintenance and equipment intelligence.",
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
        hero_title="Automate repetitive tasks and boost productivity.",
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
        hero_title="Real-time field health monitoring with AI.",
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
        hero_title="Optimize every resource for maximum yield.",
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
        hero_title="Make better farm decisions with AI weather insights.",
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
