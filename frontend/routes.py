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
        f"""<div class="feature-card" data-aos="fade-up">
            <div class="feature-icon">
                <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                    <polyline points="22 12 18 12 15 21 9 3 6 12 2 12"></polyline>
                </svg>
            </div>
            <h3>{item}</h3>
            <p>{desc}</p>
        </div>"""
        for item, desc in features
    )
    how_it_works_items = "".join(
        f"""<div class="step-card" data-aos="fade-up" data-aos-delay="{i*100}">
            <div class="step-number">0{i+1}</div>
            <div class="step-line"></div>
            <h4>{title}</h4>
            <p>{desc}</p>
        </div>"""
        for i, (title, desc) in enumerate(how_it_works)
    )
    benefit_items = "".join(
        f"""<li data-aos="fade-up" data-aos-delay="{i*50}">
            <svg class="check-icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round">
                <polyline points="20 6 9 17 4 12"></polyline>
            </svg>
            {b}
        </li>"""
        for i, b in enumerate(benefits)
    )

    return f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <title>{title} | SeedStudio</title>
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800;900&display=swap" rel="stylesheet">
    <style>
        * {{ margin: 0; padding: 0; box-sizing: border-box; }}
        :root {{
            --primary: #6C63FF;
            --primary-dark: #5A52D5;
            --primary-light: #8B85FF;
            --secondary: #FF6584;
            --accent: #00D2FF;
            --bg-dark: #0a0a1a;
            --bg-card: rgba(255,255,255,0.05);
            --bg-card-hover: rgba(255,255,255,0.08);
            --text: #ffffff;
            --text-muted: rgba(255,255,255,0.6);
            --border: rgba(255,255,255,0.1);
            --glass: rgba(255,255,255,0.03);
            --shadow: 0 8px 32px rgba(0,0,0,0.3);
        }}
        html {{ scroll-behavior: smooth; }}
        body {{
            font-family: 'Inter', -apple-system, BlinkMacSystemFont, sans-serif;
            background: var(--bg-dark);
            color: var(--text);
            line-height: 1.7;
            overflow-x: hidden;
        }}
        /* Animated background */
        .bg-animation {{
            position: fixed;
            top: 0; left: 0;
            width: 100%; height: 100%;
            z-index: -1;
            overflow: hidden;
        }}
        .bg-animation .orb {{
            position: absolute;
            border-radius: 50%;
            filter: blur(80px);
            opacity: 0.3;
            animation: orbFloat 20s ease-in-out infinite;
        }}
        .bg-animation .orb:nth-child(1) {{
            width: 600px; height: 600px;
            background: var(--primary);
            top: -200px; left: -200px;
            animation-delay: 0s;
        }}
        .bg-animation .orb:nth-child(2) {{
            width: 500px; height: 500px;
            background: var(--secondary);
            bottom: -150px; right: -150px;
            animation-delay: -7s;
        }}
        .bg-animation .orb:nth-child(3) {{
            width: 400px; height: 400px;
            background: var(--accent);
            top: 50%; left: 50%;
            transform: translate(-50%, -50%);
            animation-delay: -14s;
        }}
        @keyframes orbFloat {{
            0%, 100% {{ transform: translate(0, 0) scale(1); }}
            25% {{ transform: translate(100px, -50px) scale(1.1); }}
            50% {{ transform: translate(-50px, 100px) scale(0.9); }}
            75% {{ transform: translate(80px, 50px) scale(1.05); }}
        }}
        /* Grid overlay */
        .grid-overlay {{
            position: fixed;
            top: 0; left: 0;
            width: 100%; height: 100%;
            background-image: 
                linear-gradient(rgba(108,99,255,0.03) 1px, transparent 1px),
                linear-gradient(90deg, rgba(108,99,255,0.03) 1px, transparent 1px);
            background-size: 60px 60px;
            z-index: -1;
            pointer-events: none;
        }}
        a {{ color: inherit; text-decoration: none; }}
        .container {{ width: min(1200px, calc(100% - 40px)); margin: 0 auto; }}

        /* Header */
        header {{
            position: fixed;
            top: 0; left: 0; right: 0;
            z-index: 1000;
            padding: 16px 0;
            transition: all 0.3s ease;
        }}
        header.scrolled {{
            background: rgba(10,10,26,0.85);
            backdrop-filter: blur(20px);
            border-bottom: 1px solid var(--border);
            padding: 10px 0;
        }}
        .nav {{
            display: flex;
            align-items: center;
            justify-content: space-between;
        }}
        .brand {{
            font-size: 1.5rem;
            font-weight: 800;
            background: linear-gradient(135deg, var(--primary), var(--accent));
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            background-clip: text;
            letter-spacing: -0.5px;
        }}
        .brand span {{ color: var(--text); -webkit-text-fill-color: var(--text); }}
        .nav-links {{ display: flex; gap: 32px; align-items: center; }}
        .nav-links a {{
            color: var(--text-muted);
            font-weight: 500;
            font-size: 0.9rem;
            transition: color 0.3s ease;
            position: relative;
        }}
        .nav-links a::after {{
            content: '';
            position: absolute;
            bottom: -4px; left: 0;
            width: 0; height: 2px;
            background: var(--primary);
            transition: width 0.3s ease;
        }}
        .nav-links a:hover {{ color: var(--text); }}
        .nav-links a:hover::after {{ width: 100%; }}
        .nav-cta {{
            padding: 10px 24px;
            background: linear-gradient(135deg, var(--primary), var(--primary-dark));
            border-radius: 50px;
            color: white !important;
            font-weight: 600 !important;
            transition: transform 0.3s ease, box-shadow 0.3s ease !important;
        }}
        .nav-cta::after {{ display: none !important; }}
        .nav-cta:hover {{
            transform: translateY(-2px);
            box-shadow: 0 10px 30px rgba(108,99,255,0.3);
        }}
        .mobile-toggle {{
            display: none;
            flex-direction: column;
            gap: 5px;
            cursor: pointer;
            background: none;
            border: none;
            padding: 5px;
        }}
        .mobile-toggle span {{
            width: 24px; height: 2px;
            background: var(--text);
            border-radius: 2px;
            transition: all 0.3s ease;
        }}

        /* Hero Section */
        .hero {{
            min-height: 100vh;
            display: flex;
            align-items: center;
            padding: 120px 0 60px;
            position: relative;
        }}
        .hero-content {{
            max-width: 800px;
        }}
        .hero-badge {{
            display: inline-flex;
            align-items: center;
            gap: 8px;
            padding: 8px 16px;
            background: rgba(108,99,255,0.1);
            border: 1px solid rgba(108,99,255,0.2);
            border-radius: 50px;
            font-size: 0.85rem;
            color: var(--primary-light);
            margin-bottom: 24px;
            animation: fadeInUp 0.6s ease;
        }}
        .hero-badge .dot {{
            width: 8px; height: 8px;
            background: var(--primary);
            border-radius: 50%;
            animation: pulse 2s ease-in-out infinite;
        }}
        @keyframes pulse {{
            0%, 100% {{ opacity: 1; transform: scale(1); }}
            50% {{ opacity: 0.5; transform: scale(0.8); }}
        }}
        .hero h1 {{
            font-size: clamp(2.5rem, 5vw, 4rem);
            font-weight: 900;
            line-height: 1.1;
            margin-bottom: 20px;
            letter-spacing: -1px;
            animation: fadeInUp 0.6s ease 0.1s both;
        }}
        .hero h1 .gradient-text {{
            background: linear-gradient(135deg, var(--primary), var(--accent));
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            background-clip: text;
        }}
        .hero p {{
            font-size: 1.15rem;
            color: var(--text-muted);
            max-width: 600px;
            margin-bottom: 32px;
            animation: fadeInUp 0.6s ease 0.2s both;
        }}
        .hero-actions {{
            display: flex;
            gap: 16px;
            flex-wrap: wrap;
            animation: fadeInUp 0.6s ease 0.3s both;
        }}
        .btn {{
            display: inline-flex;
            align-items: center;
            gap: 8px;
            padding: 14px 28px;
            border-radius: 50px;
            font-weight: 600;
            font-size: 0.95rem;
            transition: all 0.3s ease;
            cursor: pointer;
            border: none;
        }}
        .btn-primary {{
            background: linear-gradient(135deg, var(--primary), var(--primary-dark));
            color: white;
            box-shadow: 0 10px 30px rgba(108,99,255,0.25);
        }}
        .btn-primary:hover {{
            transform: translateY(-3px);
            box-shadow: 0 15px 40px rgba(108,99,255,0.35);
        }}
        .btn-secondary {{
            background: var(--glass);
            color: var(--text);
            border: 1px solid var(--border);
            backdrop-filter: blur(10px);
        }}
        .btn-secondary:hover {{
            background: var(--bg-card);
            transform: translateY(-3px);
        }}
        .btn .arrow {{
            transition: transform 0.3s ease;
        }}
        .btn:hover .arrow {{
            transform: translateX(4px);
        }}

        /* Sections */
        section {{ padding: 100px 0; }}
        .section-header {{
            text-align: center;
            margin-bottom: 60px;
        }}
        .section-label {{
            display: inline-block;
            padding: 6px 14px;
            background: rgba(108,99,255,0.1);
            border: 1px solid rgba(108,99,255,0.2);
            border-radius: 50px;
            font-size: 0.8rem;
            font-weight: 600;
            color: var(--primary-light);
            text-transform: uppercase;
            letter-spacing: 1px;
            margin-bottom: 16px;
        }}
        .section-title {{
            font-size: clamp(2rem, 3.5vw, 2.8rem);
            font-weight: 800;
            letter-spacing: -0.5px;
            margin-bottom: 16px;
        }}
        .section-subtitle {{
            color: var(--text-muted);
            font-size: 1.05rem;
            max-width: 600px;
            margin: 0 auto;
        }}

        /* Feature Cards */
        .features-grid {{
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(320px, 1fr));
            gap: 24px;
        }}
        .feature-card {{
            background: var(--bg-card);
            border: 1px solid var(--border);
            border-radius: 20px;
            padding: 32px;
            transition: all 0.4s ease;
            position: relative;
            overflow: hidden;
        }}
        .feature-card::before {{
            content: '';
            position: absolute;
            top: 0; left: 0;
            right: 0; height: 3px;
            background: linear-gradient(90deg, var(--primary), var(--accent));
            transform: scaleX(0);
            transform-origin: left;
            transition: transform 0.4s ease;
        }}
        .feature-card:hover {{
            background: var(--bg-card-hover);
            transform: translateY(-8px);
            box-shadow: 0 20px 60px rgba(0,0,0,0.3);
            border-color: rgba(108,99,255,0.3);
        }}
        .feature-card:hover::before {{
            transform: scaleX(1);
        }}
        .feature-icon {{
            width: 48px; height: 48px;
            border-radius: 14px;
            background: linear-gradient(135deg, rgba(108,99,255,0.15), rgba(0,210,255,0.1));
            display: flex;
            align-items: center;
            justify-content: center;
            margin-bottom: 20px;
            color: var(--primary-light);
        }}
        .feature-icon svg {{
            width: 24px; height: 24px;
        }}
        .feature-card h3 {{
            font-size: 1.2rem;
            font-weight: 700;
            margin-bottom: 10px;
        }}
        .feature-card p {{
            color: var(--text-muted);
            font-size: 0.95rem;
            line-height: 1.6;
        }}

        /* Steps */
        .steps-grid {{
            display: grid;
            grid-template-columns: repeat(3, 1fr);
            gap: 32px;
            position: relative;
        }}
        .step-card {{
            text-align: center;
            padding: 40px 24px;
            background: var(--bg-card);
            border: 1px solid var(--border);
            border-radius: 20px;
            transition: all 0.4s ease;
            position: relative;
        }}
        .step-card:hover {{
            transform: translateY(-8px);
            box-shadow: 0 20px 60px rgba(0,0,0,0.3);
            border-color: rgba(108,99,255,0.3);
        }}
        .step-number {{
            font-size: 3rem;
            font-weight: 900;
            background: linear-gradient(135deg, var(--primary), var(--accent));
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            background-clip: text;
            margin-bottom: 16px;
            line-height: 1;
        }}
        .step-card h4 {{
            font-size: 1.15rem;
            font-weight: 700;
            margin-bottom: 10px;
        }}
        .step-card p {{
            color: var(--text-muted);
            font-size: 0.9rem;
        }}

        /* Benefits */
        .benefits-container {{
            background: var(--bg-card);
            border: 1px solid var(--border);
            border-radius: 24px;
            padding: 48px;
            max-width: 800px;
            margin: 0 auto;
        }}
        .benefits-container ul {{
            list-style: none;
            display: grid;
            grid-template-columns: 1fr 1fr;
            gap: 16px;
        }}
        .benefits-container li {{
            display: flex;
            align-items: center;
            gap: 12px;
            padding: 16px 20px;
            background: rgba(108,99,255,0.05);
            border: 1px solid rgba(108,99,255,0.1);
            border-radius: 12px;
            font-size: 0.95rem;
            transition: all 0.3s ease;
        }}
        .benefits-container li:hover {{
            background: rgba(108,99,255,0.1);
            border-color: rgba(108,99,255,0.2);
            transform: translateX(4px);
        }}
        .check-icon {{
            width: 20px; height: 20px;
            color: var(--primary);
            flex-shrink: 0;
        }}

        /* CTA */
        .cta-section {{
            text-align: center;
            padding: 80px 40px;
            background: linear-gradient(135deg, rgba(108,99,255,0.08), rgba(0,210,255,0.05));
            border: 1px solid rgba(108,99,255,0.15);
            border-radius: 32px;
            position: relative;
            overflow: hidden;
        }}
        .cta-section::before {{
            content: '';
            position: absolute;
            top: -50%; left: -50%;
            width: 200%; height: 200%;
            background: radial-gradient(circle at center, rgba(108,99,255,0.05) 0%, transparent 50%);
            animation: ctaGlow 8s ease-in-out infinite;
        }}
        @keyframes ctaGlow {{
            0%, 100% {{ transform: translate(0, 0); }}
            50% {{ transform: translate(5%, 5%); }}
        }}
        .cta-section h2 {{
            font-size: 2.2rem;
            font-weight: 800;
            margin-bottom: 12px;
            position: relative;
        }}
        .cta-section p {{
            color: var(--text-muted);
            margin-bottom: 28px;
            position: relative;
        }}
        .cta-section .btn {{
            position: relative;
        }}

        /* Animations */
        @keyframes fadeInUp {{
            from {{ opacity: 0; transform: translateY(30px); }}
            to {{ opacity: 1; transform: translateY(0); }}
        }}
        [data-aos] {{
            opacity: 0;
            transform: translateY(30px);
            transition: all 0.6s ease;
        }}
        [data-aos].aos-animate {{
            opacity: 1;
            transform: translateY(0);
        }}

        /* Responsive */
        @media (max-width: 860px) {{
            .nav-links {{
                display: none;
                position: fixed;
                top: 0; left: 0; right: 0; bottom: 0;
                background: rgba(10,10,26,0.98);
                flex-direction: column;
                justify-content: center;
                align-items: center;
                gap: 24px;
                z-index: 999;
            }}
            .nav-links.active {{ display: flex; }}
            .mobile-toggle {{ display: flex; z-index: 1000; }}
            .mobile-toggle.active span:nth-child(1) {{ transform: rotate(45deg) translate(5px, 5px); }}
            .mobile-toggle.active span:nth-child(2) {{ opacity: 0; }}
            .mobile-toggle.active span:nth-child(3) {{ transform: rotate(-45deg) translate(5px, -5px); }}
            .steps-grid {{ grid-template-columns: 1fr; }}
            .benefits-container ul {{ grid-template-columns: 1fr; }}
            .features-grid {{ grid-template-columns: 1fr; }}
            .hero h1 {{ font-size: 2rem; }}
        }}
    </style>
</head>
<body>
    <div class="bg-animation">
        <div class="orb"></div>
        <div class="orb"></div>
        <div class="orb"></div>
    </div>
    <div class="grid-overlay"></div>

    <header id="header">
        <div class="container nav">
            <a class="brand" href="/">Seed<span>Studio</span></a>
            <nav class="nav-links" id="navLinks">
                <a href="/">Home</a>
                <a href="/education-ai/student-learning">Education</a>
                <a href="/industry-ai/healthcare">Industry</a>
                <a href="/agricultural-ai/crop-monitoring">Agriculture</a>
                <a class="nav-cta" href="mailto:hello@seedstudio.example">Get Started</a>
            </nav>
            <button class="mobile-toggle" id="mobileToggle" aria-label="Menu">
                <span></span><span></span><span></span>
            </button>
        </div>
    </header>

    <main>
        <section class="hero">
            <div class="container hero-content">
                <div class="hero-badge">
                    <span class="dot"></span>
                    AI-Powered Solutions
                </div>
                <h1>{hero_title}</h1>
                <p>{intro}</p>
                <div class="hero-actions">
                    <a class="btn btn-primary" href="mailto:hello@seedstudio.example">
                        {cta_text}
                        <svg class="arrow" width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round">
                            <line x1="5" y1="12" x2="19" y2="12"></line>
                            <polyline points="12 5 19 12 12 19"></polyline>
                        </svg>
                    </a>
                    <a class="btn btn-secondary" href="#features">
                        Learn More
                    </a>
                </div>
            </div>
        </section>

        <section id="features">
            <div class="container">
                <div class="section-header" data-aos="fade-up">
                    <div class="section-label">Key Features</div>
                    <h2 class="section-title">What's Included</h2>
                    <p class="section-subtitle">Everything you need to transform your workflow with cutting-edge AI technology.</p>
                </div>
                <div class="features-grid">
                    {feature_items}
                </div>
            </div>
        </section>

        <section>
            <div class="container">
                <div class="section-header" data-aos="fade-up">
                    <div class="section-label">How It Works</div>
                    <h2 class="section-title">Three Simple Steps</h2>
                    <p class="section-subtitle">Get started in minutes and see results immediately.</p>
                </div>
                <div class="steps-grid">
                    {how_it_works_items}
                </div>
            </div>
        </section>

        <section>
            <div class="container">
                <div class="section-header" data-aos="fade-up">
                    <div class="section-label">Why Choose Us</div>
                    <h2 class="section-title">Core Benefits</h2>
                    <p class="section-subtitle">Proven results that speak for themselves.</p>
                </div>
                <div class="benefits-container" data-aos="fade-up">
                    <ul>
                        {benefit_items}
                    </ul>
                </div>
            </div>
        </section>

        <section>
            <div class="container">
                <div class="cta-section" data-aos="fade-up">
                    <h2>Ready to Get Started?</h2>
                    <p>Contact us today to discuss how this solution fits your needs.</p>
                    <a class="btn btn-primary" href="mailto:hello@seedstudio.example">
                        Schedule a Consultation
                        <svg class="arrow" width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round">
                            <line x1="5" y1="12" x2="19" y2="12"></line>
                            <polyline points="12 5 19 12 12 19"></polyline>
                        </svg>
                    </a>
                </div>
            </div>
        </section>
    </main>

    <script>
        // Header scroll effect
        const header = document.getElementById('header');
        window.addEventListener('scroll', () => {{
            header.classList.toggle('scrolled', window.scrollY > 50);
        }});

        // Mobile menu toggle
        const mobileToggle = document.getElementById('mobileToggle');
        const navLinks = document.getElementById('navLinks');
        mobileToggle.addEventListener('click', () => {{
            mobileToggle.classList.toggle('active');
            navLinks.classList.toggle('active');
        }});
        navLinks.querySelectorAll('a').forEach(link => {{
            link.addEventListener('click', () => {{
                mobileToggle.classList.remove('active');
                navLinks.classList.remove('active');
            }});
        }});

        // Scroll animations
        const observer = new IntersectionObserver((entries) => {{
            entries.forEach(entry => {{
                if (entry.isIntersecting) {{
                    entry.target.classList.add('aos-animate');
                }}
            }});
        }}, {{ threshold: 0.1 }});

        document.querySelectorAll('[data-aos]').forEach(el => observer.observe(el));
    </script>
</body>
</html>"""


@router.get("/", response_class=HTMLResponse)
async def frontend_index():
    return """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <title>SeedStudio | AI Business Solutions</title>
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800;900&display=swap" rel="stylesheet">
    <style>
        * { margin: 0; padding: 0; box-sizing: border-box; }
        :root {
            --primary: #6C63FF;
            --primary-dark: #5A52D5;
            --primary-light: #8B85FF;
            --secondary: #FF6584;
            --accent: #00D2FF;
            --bg-dark: #0a0a1a;
            --bg-card: rgba(255,255,255,0.05);
            --bg-card-hover: rgba(255,255,255,0.08);
            --text: #ffffff;
            --text-muted: rgba(255,255,255,0.6);
            --border: rgba(255,255,255,0.1);
            --glass: rgba(255,255,255,0.03);
            --shadow: 0 8px 32px rgba(0,0,0,0.3);
        }
        html { scroll-behavior: smooth; }
        body {
            font-family: 'Inter', -apple-system, BlinkMacSystemFont, sans-serif;
            background: var(--bg-dark);
            color: var(--text);
            line-height: 1.7;
            overflow-x: hidden;
        }
        .bg-animation {
            position: fixed; top: 0; left: 0;
            width: 100%; height: 100%;
            z-index: -1; overflow: hidden;
        }
        .bg-animation .orb {
            position: absolute;
            border-radius: 50%;
            filter: blur(80px);
            opacity: 0.3;
            animation: orbFloat 20s ease-in-out infinite;
        }
        .bg-animation .orb:nth-child(1) { width: 600px; height: 600px; background: var(--primary); top: -200px; left: -200px; }
        .bg-animation .orb:nth-child(2) { width: 500px; height: 500px; background: var(--secondary); bottom: -150px; right: -150px; animation-delay: -7s; }
        .bg-animation .orb:nth-child(3) { width: 400px; height: 400px; background: var(--accent); top: 50%; left: 50%; transform: translate(-50%, -50%); animation-delay: -14s; }
        @keyframes orbFloat {
            0%, 100% { transform: translate(0, 0) scale(1); }
            25% { transform: translate(100px, -50px) scale(1.1); }
            50% { transform: translate(-50px, 100px) scale(0.9); }
            75% { transform: translate(80px, 50px) scale(1.05); }
        }
        .grid-overlay {
            position: fixed; top: 0; left: 0;
            width: 100%; height: 100%;
            background-image: 
                linear-gradient(rgba(108,99,255,0.03) 1px, transparent 1px),
                linear-gradient(90deg, rgba(108,99,255,0.03) 1px, transparent 1px);
            background-size: 60px 60px;
            z-index: -1; pointer-events: none;
        }
        a { color: inherit; text-decoration: none; }
        .container { width: min(1200px, calc(100% - 40px)); margin: 0 auto; }

        header {
            position: fixed; top: 0; left: 0; right: 0;
            z-index: 1000; padding: 16px 0;
            transition: all 0.3s ease;
        }
        header.scrolled {
            background: rgba(10,10,26,0.85);
            backdrop-filter: blur(20px);
            border-bottom: 1px solid var(--border);
            padding: 10px 0;
        }
        .nav { display: flex; align-items: center; justify-content: space-between; }
        .brand {
            font-size: 1.5rem; font-weight: 800;
            background: linear-gradient(135deg, var(--primary), var(--accent));
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            background-clip: text;
            letter-spacing: -0.5px;
        }
        .brand span { color: var(--text); -webkit-text-fill-color: var(--text); }
        .nav-links { display: flex; gap: 32px; align-items: center; }
        .nav-links a {
            color: var(--text-muted); font-weight: 500; font-size: 0.9rem;
            transition: color 0.3s ease; position: relative;
        }
        .nav-links a::after {
            content: ''; position: absolute;
            bottom: -4px; left: 0; width: 0; height: 2px;
            background: var(--primary); transition: width 0.3s ease;
        }
        .nav-links a:hover { color: var(--text); }
        .nav-links a:hover::after { width: 100%; }
        .nav-cta {
            padding: 10px 24px;
            background: linear-gradient(135deg, var(--primary), var(--primary-dark));
            border-radius: 50px; color: white !important; font-weight: 600 !important;
            transition: transform 0.3s ease, box-shadow 0.3s ease !important;
        }
        .nav-cta::after { display: none !important; }
        .nav-cta:hover { transform: translateY(-2px); box-shadow: 0 10px 30px rgba(108,99,255,0.3); }
        .mobile-toggle {
            display: none; flex-direction: column; gap: 5px;
            cursor: pointer; background: none; border: none; padding: 5px;
        }
        .mobile-toggle span { width: 24px; height: 2px; background: var(--text); border-radius: 2px; transition: all 0.3s ease; }

        .hero {
            min-height: 100vh;
            display: grid;
            grid-template-columns: 1.1fr 0.9fr;
            gap: 60px;
            align-items: center;
            padding: 120px 0 60px;
        }
        .hero-badge {
            display: inline-flex; align-items: center; gap: 8px;
            padding: 8px 16px;
            background: rgba(108,99,255,0.1);
            border: 1px solid rgba(108,99,255,0.2);
            border-radius: 50px;
            font-size: 0.85rem; color: var(--primary-light);
            margin-bottom: 24px;
            animation: fadeInUp 0.6s ease;
        }
        .hero-badge .dot {
            width: 8px; height: 8px; background: var(--primary);
            border-radius: 50%; animation: pulse 2s ease-in-out infinite;
        }
        @keyframes pulse { 0%, 100% { opacity: 1; transform: scale(1); } 50% { opacity: 0.5; transform: scale(0.8); } }
        .hero h1 {
            font-size: clamp(2.5rem, 4.5vw, 3.8rem);
            font-weight: 900; line-height: 1.1;
            margin-bottom: 20px; letter-spacing: -1px;
            animation: fadeInUp 0.6s ease 0.1s both;
        }
        .hero h1 .gradient-text {
            background: linear-gradient(135deg, var(--primary), var(--accent));
            -webkit-background-clip: text; -webkit-text-fill-color: transparent;
            background-clip: text;
        }
        .hero p {
            font-size: 1.1rem; color: var(--text-muted);
            max-width: 540px; margin-bottom: 32px;
            animation: fadeInUp 0.6s ease 0.2s both;
        }
        .hero-actions {
            display: flex; gap: 16px; flex-wrap: wrap;
            animation: fadeInUp 0.6s ease 0.3s both;
        }
        .btn {
            display: inline-flex; align-items: center; gap: 8px;
            padding: 14px 28px; border-radius: 50px;
            font-weight: 600; font-size: 0.95rem;
            transition: all 0.3s ease; cursor: pointer; border: none;
        }
        .btn-primary {
            background: linear-gradient(135deg, var(--primary), var(--primary-dark));
            color: white; box-shadow: 0 10px 30px rgba(108,99,255,0.25);
        }
        .btn-primary:hover { transform: translateY(-3px); box-shadow: 0 15px 40px rgba(108,99,255,0.35); }
        .btn-secondary {
            background: var(--glass); color: var(--text);
            border: 1px solid var(--border); backdrop-filter: blur(10px);
        }
        .btn-secondary:hover { background: var(--bg-card); transform: translateY(-3px); }
        .btn .arrow { transition: transform 0.3s ease; }
        .btn:hover .arrow { transform: translateX(4px); }

        .hero-card {
            background: var(--bg-card);
            border: 1px solid var(--border);
            border-radius: 24px;
            padding: 32px;
            backdrop-filter: blur(10px);
            animation: fadeInUp 0.6s ease 0.4s both;
        }
        .hero-card h3 { font-size: 1.2rem; font-weight: 700; margin-bottom: 8px; }
        .hero-card p { color: var(--text-muted); font-size: 0.9rem; margin-bottom: 20px; }
        .metric-grid { display: grid; grid-template-columns: 1fr 1fr; gap: 12px; }
        .metric {
            padding: 16px;
            background: rgba(108,99,255,0.05);
            border: 1px solid rgba(108,99,255,0.1);
            border-radius: 14px;
            transition: all 0.3s ease;
        }
        .metric:hover { background: rgba(108,99,255,0.1); transform: translateY(-2px); }
        .metric strong { display: block; font-size: 1rem; color: var(--primary-light); margin-bottom: 4px; }
        .metric span { font-size: 0.8rem; color: var(--text-muted); }

        section { padding: 100px 0; }
        .section-header { text-align: center; margin-bottom: 60px; }
        .section-label {
            display: inline-block; padding: 6px 14px;
            background: rgba(108,99,255,0.1);
            border: 1px solid rgba(108,99,255,0.2);
            border-radius: 50px;
            font-size: 0.8rem; font-weight: 600;
            color: var(--primary-light);
            text-transform: uppercase; letter-spacing: 1px;
            margin-bottom: 16px;
        }
        .section-title {
            font-size: clamp(2rem, 3.5vw, 2.8rem);
            font-weight: 800; letter-spacing: -0.5px;
            margin-bottom: 16px;
        }
        .section-subtitle { color: var(--text-muted); font-size: 1.05rem; max-width: 600px; margin: 0 auto; }

        .service-category {
            margin-bottom: 40px;
            padding: 40px;
            border-radius: 24px;
            background: var(--bg-card);
            border: 1px solid var(--border);
            transition: all 0.3s ease;
        }
        .service-category:hover { border-color: rgba(108,99,255,0.2); }
        .service-category h3 {
            font-size: 1.4rem; font-weight: 700;
            margin-bottom: 24px;
            display: flex; align-items: center; gap: 12px;
        }
        .feature-grid {
            display: grid;
            grid-template-columns: repeat(3, 1fr);
            gap: 20px;
        }
        .card {
            background: rgba(255,255,255,0.03);
            border: 1px solid var(--border);
            border-radius: 18px;
            padding: 24px;
            transition: all 0.4s ease;
            cursor: pointer;
            display: block;
        }
        .card:hover {
            background: var(--bg-card-hover);
            transform: translateY(-6px);
            box-shadow: 0 20px 50px rgba(0,0,0,0.3);
            border-color: rgba(108,99,255,0.3);
        }
        .card-icon-wrap {
            width: 56px; height: 56px;
            border-radius: 16px;
            display: flex; align-items: center; justify-content: center;
            margin-bottom: 16px;
            background: linear-gradient(135deg, rgba(108,99,255,0.15), rgba(0,210,255,0.1));
        }
        .card-icon { width: 28px; height: 28px; color: var(--primary-light); }
        .card h3 { font-size: 1.1rem; font-weight: 700; margin-bottom: 8px; }
        .card p { color: var(--text-muted); font-size: 0.9rem; line-height: 1.6; }

        .about-section {
            background: var(--bg-card);
            border: 1px solid var(--border);
            border-radius: 24px;
            padding: 48px;
            text-align: center;
            max-width: 800px;
            margin: 0 auto;
        }
        .about-section p { color: var(--text-muted); font-size: 1.05rem; line-height: 1.8; }

        .cta-section {
            text-align: center;
            padding: 80px 40px;
            background: linear-gradient(135deg, rgba(108,99,255,0.08), rgba(0,210,255,0.05));
            border: 1px solid rgba(108,99,255,0.15);
            border-radius: 32px;
            position: relative;
            overflow: hidden;
        }
        .cta-section::before {
            content: '';
            position: absolute; top: -50%; left: -50%;
            width: 200%; height: 200%;
            background: radial-gradient(circle at center, rgba(108,99,255,0.05) 0%, transparent 50%);
            animation: ctaGlow 8s ease-in-out infinite;
        }
        @keyframes ctaGlow { 0%, 100% { transform: translate(0, 0); } 50% { transform: translate(5%, 5%); } }
        .cta-section h2 { font-size: 2.2rem; font-weight: 800; margin-bottom: 12px; position: relative; }
        .cta-section p { color: var(--text-muted); margin-bottom: 28px; position: relative; }
        .cta-section .btn { position: relative; }

        .chat-launcher {
            position: fixed; right: 28px; bottom: 28px;
            width: 60px; height: 60px;
            border-radius: 50%;
            display: flex; align-items: center; justify-content: center;
            background: linear-gradient(135deg, var(--primary), var(--primary-dark));
            color: #fff; border: none;
            box-shadow: 0 10px 30px rgba(108,99,255,0.3);
            cursor: pointer; z-index: 20;
            font-size: 1.5rem;
            transition: all 0.3s ease;
        }
        .chat-launcher:hover { transform: scale(1.1); box-shadow: 0 15px 40px rgba(108,99,255,0.4); }
        .chat-panel {
            position: fixed; right: 24px; bottom: 100px;
            width: 380px; max-width: calc(100% - 32px);
            background: rgba(20,20,40,0.95);
            backdrop-filter: blur(20px);
            border: 1px solid var(--border);
            border-radius: 24px;
            box-shadow: 0 30px 80px rgba(0,0,0,0.5);
            overflow: hidden; display: none; z-index: 20;
        }
        .chat-panel.active { display: block; animation: fadeInUp 0.3s ease; }
        .chat-header {
            padding: 16px 20px;
            background: linear-gradient(135deg, var(--primary), var(--primary-dark));
            color: #fff;
            display: flex; justify-content: space-between; align-items: center;
        }
        .chat-header h4 { margin: 0; font-size: 1rem; font-weight: 600; }
        .chat-close {
            width: 28px; height: 28px;
            display: flex; align-items: center; justify-content: center;
            border-radius: 50%;
            background: rgba(255,255,255,0.2);
            cursor: pointer; font-weight: 700; font-size: 1.1rem;
            transition: background 0.3s ease;
        }
        .chat-close:hover { background: rgba(255,255,255,0.3); }
        .chat-messages {
            max-height: 340px; overflow-y: auto;
            padding: 18px 20px;
            background: rgba(0,0,0,0.2);
        }
        .chat-message { margin-bottom: 14px; display: flex; }
        .chat-message.user { justify-content: flex-end; }
        .chat-message.bot { justify-content: flex-start; }
        .bubble {
            display: inline-block; padding: 12px 16px;
            border-radius: 18px; max-width: 85%;
            line-height: 1.5; font-size: 0.9rem;
        }
        .chat-message.user .bubble {
            background: linear-gradient(135deg, var(--primary), var(--primary-dark));
            color: white; border-bottom-right-radius: 4px;
        }
        .chat-message.bot .bubble {
            background: rgba(255,255,255,0.08);
            color: var(--text); border-bottom-left-radius: 4px;
        }
        .chat-input {
            display: flex; gap: 10px;
            border-top: 1px solid var(--border);
            padding: 14px 16px;
            background: rgba(0,0,0,0.3);
        }
        .chat-input input {
            flex: 1;
            background: rgba(255,255,255,0.05);
            border: 1px solid var(--border);
            border-radius: 12px;
            padding: 12px 14px;
            font-size: 0.9rem;
            color: var(--text);
            outline: none;
            transition: border-color 0.3s ease;
        }
        .chat-input input:focus { border-color: var(--primary); }
        .chat-input input::placeholder { color: var(--text-muted); }
        .chat-input button {
            border: none; border-radius: 12px;
            padding: 12px 18px;
            background: linear-gradient(135deg, var(--primary), var(--primary-dark));
            color: #fff; cursor: pointer;
            font-weight: 600; font-size: 0.9rem;
            transition: all 0.3s ease;
        }
        .chat-input button:hover { transform: translateY(-2px); box-shadow: 0 5px 15px rgba(108,99,255,0.3); }

        @keyframes fadeInUp {
            from { opacity: 0; transform: translateY(30px); }
            to { opacity: 1; transform: translateY(0); }
        }
        [data-aos] { opacity: 0; transform: translateY(30px); transition: all 0.6s ease; }
        [data-aos].aos-animate { opacity: 1; transform: translateY(0); }

        @media (max-width: 860px) {
            .hero { grid-template-columns: 1fr; gap: 40px; padding: 100px 0 40px; }
            .feature-grid { grid-template-columns: 1fr; }
            .nav-links {
                display: none; position: fixed; top: 0; left: 0; right: 0; bottom: 0;
                background: rgba(10,10,26,0.98);
                flex-direction: column; justify-content: center; align-items: center;
                gap: 24px; z-index: 999;
            }
            .nav-links.active { display: flex; }
            .mobile-toggle { display: flex; z-index: 1000; }
            .mobile-toggle.active span:nth-child(1) { transform: rotate(45deg) translate(5px, 5px); }
            .mobile-toggle.active span:nth-child(2) { opacity: 0; }
            .mobile-toggle.active span:nth-child(3) { transform: rotate(-45deg) translate(5px, -5px); }
            .chat-panel { right: 16px; left: 16px; bottom: 90px; width: auto; }
            .service-category { padding: 24px; }
        }
    </style>
</head>
<body>
    <div class="bg-animation">
        <div class="orb"></div>
        <div class="orb"></div>
        <div class="orb"></div>
    </div>
    <div class="grid-overlay"></div>

    <header id="header">
        <div class="container nav">
            <a class="brand" href="/">Seed<span>Studio</span></a>
            <nav class="nav-links" id="navLinks">
                <a href="#services">Services</a>
                <a href="#about">About</a>
                <a href="#contact">Contact</a>
                <a class="nav-cta" href="mailto:hello@seedstudio.example">Get Started</a>
            </nav>
            <button class="mobile-toggle" id="mobileToggle" aria-label="Menu">
                <span></span><span></span><span></span>
            </button>
        </div>
    </header>

    <main>
        <div class="container">
            <section class="hero">
                <div>
                    <div class="hero-badge">
                        <span class="dot"></span>
                        AI Business Solutions
                    </div>
                    <h1>Intelligent <span class="gradient-text">AI solutions</span> for education and industries.</h1>
                    <p>We build AI-powered platforms for schools, colleges, healthcare, manufacturing, and agriculture to simplify learning, improve operations, and accelerate smarter decisions.</p>
                    <div class="hero-actions">
                        <a class="btn btn-primary" href="#contact">
                            Book a Consultation
                            <svg class="arrow" width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round">
                                <line x1="5" y1="12" x2="19" y2="12"></line>
                                <polyline points="12 5 19 12 12 19"></polyline>
                            </svg>
                        </a>
                        <a class="btn btn-secondary" href="#services">Explore Solutions</a>
                    </div>
                </div>
                <div class="hero-card">
                    <h3>What We Enable</h3>
                    <p>Personalized learning support, progress tracking, and industry-ready automation built around real business needs.</p>
                    <div class="metric-grid">
                        <div class="metric"><strong>Learning AI</strong><span>For students and teachers</span></div>
                        <div class="metric"><strong>Industry AI</strong><span>Healthcare, mechanical, agriculture</span></div>
                        <div class="metric"><strong>Progress Insights</strong><span>Student growth and evaluation</span></div>
                        <div class="metric"><strong>Automation</strong><span>Smarter operations and workflows</span></div>
                    </div>
                </div>
            </section>
        </div>

        <section id="services">
            <div class="container">
                <div class="section-header" data-aos="fade-up">
                    <div class="section-label">Solutions</div>
                    <h2 class="section-title">Our AI Service Offerings</h2>
                    <p class="section-subtitle">Cutting-edge AI solutions tailored for every sector.</p>
                </div>

                <div class="service-category" data-aos="fade-up">
                    <h3>🎓 Education AI</h3>
                    <div class="feature-grid">
                        <a class="card" href="/education-ai/student-learning">
                            <div class="card-icon-wrap">
                                <svg class="card-icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                                    <path d="M12 2C7 2 3.25 5.75 3.25 10.75c0 5.5 4.75 9 8.75 11.25 4-2.25 8.75-5.75 8.75-11.25C20.75 5.75 17 2 12 2z"/>
                                    <circle cx="12" cy="10.75" r="4.75"/>
                                </svg>
                            </div>
                            <h3>Student Learning Agent</h3>
                            <p>Personalized AI tutoring that adapts to each student's learning pace and style.</p>
                        </a>
                        <a class="card" href="/education-ai/teacher-dashboard">
                            <div class="card-icon-wrap">
                                <svg class="card-icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                                    <rect x="3" y="3" width="18" height="18" rx="2" ry="2"></rect>
                                    <line x1="3" y1="9" x2="21" y2="9"></line>
                                    <line x1="9" y1="21" x2="9" y2="9"></line>
                                </svg>
                            </div>
                            <h3>Teacher Dashboard</h3>
                            <p>Real-time classroom analytics and student engagement tracking tools.</p>
                        </a>
                        <a class="card" href="/education-ai/parent-portal">
                            <div class="card-icon-wrap">
                                <svg class="card-icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                                    <path d="M17 21v-2a4 4 0 0 0-4-4H5a4 4 0 0 0-4 4v2"></path>
                                    <circle cx="9" cy="7" r="4"></circle>
                                    <path d="M23 21v-2a4 4 0 0 0-3-3.87"></path>
                                    <path d="M16 3.13a4 4 0 0 1 0 7.75"></path>
                                </svg>
                            </div>
                            <h3>Parent Portal</h3>
                            <p>Clear dashboards showing student progress and learning recommendations.</p>
                        </a>
                    </div>
                </div>

                <div class="service-category" data-aos="fade-up">
                    <h3>🏭 Industry AI</h3>
                    <div class="feature-grid">
                        <a class="card" href="/industry-ai/healthcare">
                            <div class="card-icon-wrap">
                                <svg class="card-icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                                    <path d="M22 12h-4l-3 9L9 3l-3 9H2"></path>
                                </svg>
                            </div>
                            <h3>Healthcare AI</h3>
                            <p>AI solutions for diagnostic support and hospital workflow optimization.</p>
                        </a>
                        <a class="card" href="/industry-ai/mechanical">
                            <div class="card-icon-wrap">
                                <svg class="card-icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                                    <circle cx="12" cy="12" r="3"></circle>
                                    <path d="M19.4 15a1.65 1.65 0 0 0 .33 1.82l.06.06a2 2 0 0 1 0 2.83 2 2 0 0 1-2.83 0l-.06-.06a1.65 1.65 0 0 0-1.82-.33 1.65 1.65 0 0 0-1 1.51V21a2 2 0 0 1-2 2 2 2 0 0 1-2-2v-.09A1.65 1.65 0 0 0 9 19.4a1.65 1.65 0 0 0-1.82.33l-.06.06a2 2 0 0 1-2.83 0 2 2 0 0 1 0-2.83l.06-.06A1.65 1.65 0 0 0 4.68 15a1.65 1.65 0 0 0-1.51-1H3a2 2 0 0 1-2-2 2 2 0 0 1 2-2h.09A1.65 1.65 0 0 0 4.6 9a1.65 1.65 0 0 0-.33-1.82l-.06-.06a2 2 0 0 1 0-2.83 2 2 0 0 1 2.83 0l.06.06A1.65 1.65 0 0 0 9 4.68a1.65 1.65 0 0 0 1-1.51V3a2 2 0 0 1 2-2 2 2 0 0 1 2 2v.09a1.65 1.65 0 0 0 1 1.51 1.65 1.65 0 0 0 1.82-.33l.06-.06a2 2 0 0 1 2.83 0 2 2 0 0 1 0 2.83l-.06.06a1.65 1.65 0 0 0-.33 1.82V9a1.65 1.65 0 0 0 1.51 1H21a2 2 0 0 1 2 2 2 2 0 0 1-2 2h-.09a1.65 1.65 0 0 0-1.51 1z"></path>
                                </svg>
                            </div>
                            <h3>Mechanical AI</h3>
                            <p>Equipment monitoring and predictive maintenance for industrial operations.</p>
                        </a>
                        <a class="card" href="/industry-ai/automation">
                            <div class="card-icon-wrap">
                                <svg class="card-icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                                    <rect x="2" y="3" width="20" height="14" rx="2" ry="2"></rect>
                                    <line x1="8" y1="21" x2="16" y2="21"></line>
                                    <line x1="12" y1="17" x2="12" y2="21"></line>
                                </svg>
                            </div>
                            <h3>Industrial Automation</h3>
                            <p>Automate repetitive processes and improve operational efficiency.</p>
                        </a>
                    </div>
                </div>

                <div class="service-category" data-aos="fade-up">
                    <h3>🌾 Agricultural AI</h3>
                    <div class="feature-grid">
                        <a class="card" href="/agricultural-ai/crop-monitoring">
                            <div class="card-icon-wrap">
                                <svg class="card-icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                                    <path d="M12 2C7.5 2 4 5.5 4 10c0 5.25 6 10 8 10s8-4.75 8-10c0-4.5-3.5-8-8-8z"/>
                                    <circle cx="12" cy="10" r="2.5"/>
                                </svg>
                            </div>
                            <h3>Crop Monitoring</h3>
                            <p>Real-time field monitoring and early issue detection using AI.</p>
                        </a>
                        <a class="card" href="/agricultural-ai/precision-farming">
                            <div class="card-icon-wrap">
                                <svg class="card-icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                                    <path d="M12 2l5 9h-3l2 7-4-3-4 3 2-7H7l5-9z"/>
                                </svg>
                            </div>
                            <h3>Precision Farming</h3>
                            <p>AI-optimized irrigation, fertilization, and resource management.</p>
                        </a>
                        <a class="card" href="/agricultural-ai/weather-intelligence">
                            <div class="card-icon-wrap">
                                <svg class="card-icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                                    <path d="M18 10h-1.26A8 8 0 1 0 9 20h9a5 5 0 0 0 0-10z"></path>
                                </svg>
                            </div>
                            <h3>Weather Intelligence</h3>
                            <p>Predictive weather analytics and farm planning recommendations.</p>
                        </a>
                    </div>
                </div>
            </div>
        </section>

        <section id="about">
            <div class="container">
                <div class="section-header" data-aos="fade-up">
                    <div class="section-label">About</div>
                    <h2 class="section-title">Why Choose Our AI Solutions</h2>
                </div>
                <div class="about-section" data-aos="fade-up">
                    <p>We create practical AI business solutions that help organizations modernize learning, improve efficiency, and unlock smarter operations across education and industry. Our platforms are designed with real-world needs in mind, combining cutting-edge technology with intuitive interfaces.</p>
                </div>
            </div>
        </section>

        <section id="contact">
            <div class="container">
                <div class="cta-section" data-aos="fade-up">
                    <h2>Ready to Transform Your Business with AI?</h2>
                    <p>Let's build intelligent solutions tailored to your goals.</p>
                    <a class="btn btn-primary" href="mailto:hello@seedstudio.example">
                        Contact Us
                        <svg class="arrow" width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round">
                            <line x1="5" y1="12" x2="19" y2="12"></line>
                            <polyline points="12 5 19 12 12 19"></polyline>
                        </svg>
                    </a>
                </div>
            </div>
        </section>
    </main>

    <button class="chat-launcher" id="chatLauncher" aria-label="Open AI chat">🤖</button>
    <div class="chat-panel" id="chatPanel">
        <div class="chat-header">
            <h4>SeedStudio AI Assistant</h4>
            <div class="chat-close" id="chatClose">×</div>
        </div>
        <div class="chat-messages" id="chatMessages">
            <div class="chat-message bot"><div class="bubble">Hello! Ask me about our AI services, products, or how SeedStudio can help your business.</div></div>
        </div>
        <div class="chat-input">
            <input id="chatInput" type="text" placeholder="Type a message..." />
            <button id="chatSend" type="button">Send</button>
        </div>
    </div>

    <script>
        const header = document.getElementById('header');
        window.addEventListener('scroll', () => {
            header.classList.toggle('scrolled', window.scrollY > 50);
        });

        const mobileToggle = document.getElementById('mobileToggle');
        const navLinks = document.getElementById('navLinks');
        mobileToggle.addEventListener('click', () => {
            mobileToggle.classList.toggle('active');
            navLinks.classList.toggle('active');
        });
        navLinks.querySelectorAll('a').forEach(link => {
            link.addEventListener('click', () => {
                mobileToggle.classList.remove('active');
                navLinks.classList.remove('active');
            });
        });

        const observer = new IntersectionObserver((entries) => {
            entries.forEach(entry => {
                if (entry.isIntersecting) {
                    entry.target.classList.add('aos-animate');
                }
            });
        }, { threshold: 0.1 });
        document.querySelectorAll('[data-aos]').forEach(el => observer.observe(el));

        const chatLauncher = document.getElementById('chatLauncher');
        const chatPanel = document.getElementById('chatPanel');
        const chatClose = document.getElementById('chatClose');
        const chatMessages = document.getElementById('chatMessages');
        const chatInput = document.getElementById('chatInput');
        const chatSend = document.getElementById('chatSend');

        function addMessage(role, text) {
            const message = document.createElement('div');
            message.className = 'chat-message ' + role;
            const bubble = document.createElement('div');
            bubble.className = 'bubble';
            bubble.textContent = text;
            message.appendChild(bubble);
            chatMessages.appendChild(message);
            chatMessages.scrollTop = chatMessages.scrollHeight;
        }

        function respondToMessage(text) {
            const normalized = text.toLowerCase();
            if (/hello|hi|hey/.test(normalized)) {
                return 'Hi there! I'm the SeedStudio assistant. Ask me about our AI solutions for education, industry, or agriculture.';
            }
            if (/education|student|teacher|parent/.test(normalized)) {
                return 'Our Education AI includes tutoring, teacher dashboards, and parent portals. Which area would you like to explore?';
            }
            if (/healthcare|medical|hospital/.test(normalized)) {
                return 'Our Healthcare AI supports diagnostics, workflow automation, and patient engagement for smarter care.';
            }
            if (/farm|crop|agriculture|weather/.test(normalized)) {
                return 'Our Agriculture AI offers crop monitoring, precision farming, and weather intelligence to improve yields.';
            }
            if (/automation|industry|mechanical/.test(normalized)) {
                return 'We provide Industry AI for equipment maintenance, production automation, and operational analytics.';
            }
            return 'Great question! We can help you build AI solutions for your business. Tell me more about your goals or ask for a specific service.';
        }

        chatLauncher.addEventListener('click', () => {
            chatPanel.classList.toggle('active');
        });

        chatClose.addEventListener('click', () => {
            chatPanel.classList.remove('active');
        });

        chatSend.addEventListener('click', () => {
            const text = chatInput.value.trim();
            if (!text) return;
            addMessage('user', text);
            chatInput.value = '';
            setTimeout(() => addMessage('bot', respondToMessage(text)), 500);
        });

        chatInput.addEventListener('keydown', (event) => {
            if (event.key === 'Enter') {
                event.preventDefault();
                chatSend.click();
            }
        });
    </script>
</body>
</html>"""


@router.get("/education-ai/student-learning", response_class=HTMLResponse)
async def education_student_learning():
    return render_service_page(
        title="Student Learning Agent",
        hero_title="Personalized <span class='gradient-text'>AI tutoring</span> for every student.",
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
        hero_title="Classroom management <span class='gradient-text'>powered by AI</span> insights.",
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
        hero_title="Stay connected to your <span class='gradient-text'>child's learning</span> journey.",
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
        hero_title="Smarter healthcare <span class='gradient-text'>operations with AI</span> support.",
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
        hero_title="Predictive maintenance and <span class='gradient-text'>equipment intelligence</span>.",
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
        hero_title="Automate repetitive tasks and <span class='gradient-text'>boost productivity</span>.",
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
        hero_title="Real-time field health <span class='gradient-text'>monitoring with AI</span>.",
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
        hero_title="Optimize every resource for <span class='gradient-text'>maximum yield</span>.",
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
        hero_title="Make better farm decisions with <span class='gradient-text'>AI weather insights</span>.",
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