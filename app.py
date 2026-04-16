import streamlit as st
import json
import os
from datetime import datetime

st.set_page_config(
    page_title="GRN Energy – Energy Audit & M&V Services",
    page_icon="🌿",
    layout="wide"
)

with open("static/style.css") as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

BLOG_FILE = "data/blog.json"

SEED_POSTS = [
    {
        "id": "20250315120000",
        "title": "IPMVP Protocol: A Complete Guide to M&V in India",
        "category": "Measurement & Verification",
        "emoji": "📊",
        "content": "The International Performance Measurement and Verification Protocol (IPMVP) is the globally recognised framework for quantifying and verifying energy savings from energy conservation measures (ECMs).\n\nAs India accelerates its energy transition under the PAT scheme and NAPCC, credible M&V has never been more important. IPMVP provides the gold standard for this verification.\n\nIPMVP defines four options:\n• Option A – Partially Measured Retrofit Isolation: Measures key parameter(s) with stipulation of others.\n• Option B – Retrofit Isolation: All parameters measured for highest accuracy.\n• Option C – Whole Facility: Uses utility meter data. Best for multiple ECMs.\n• Option D – Calibrated Simulation: Computer simulation. Suitable for new construction.\n\nA robust M&V plan includes: ECM boundary definition, baseline period and conditions, measurement frequency and instruments, adjustment methodology, and reporting requirements.\n\nGRN Energy's IPMVP-certified M&V professionals have implemented M&V programs across textile, pharmaceutical, food processing, and commercial building sectors in Maharashtra. Contact us to learn how IPMVP-compliant M&V can add credibility to your energy efficiency investments.",
        "author": "GRN Energy Team",
        "date": "15 Mar 2025"
    },
    {
        "id": "20250228110000",
        "title": "How Energy Auditing Can Cut Industrial Costs by 20–30%",
        "category": "Energy Auditing",
        "emoji": "⚡",
        "content": "For Indian industries facing rising energy tariffs, a BEE-certified energy audit consistently identifies savings potential of 15–30% of total energy expenditure.\n\nA Detailed Energy Audit (DEA) involves thorough analysis of all energy flows — instrumented measurements, data logging, and rigorous analysis of each energy-consuming system.\n\nTop savings areas in Maharashtra manufacturing:\n• Compressed Air Systems (15–25% savings): Leak detection, pressure optimisation, VSD on compressors\n• Pumping Systems (10–20%): Right-sizing, impeller trimming, VSD installation\n• Lighting (20–40%): LED retrofits with occupancy and daylight sensors\n• HVAC (15–30%): Chiller optimisation, cooling tower improvements\n• Waste Heat Recovery (5–15%): Heat exchangers, economisers\n\nOur auditors follow a systematic 4-phase process: pre-audit preparation, audit execution (measurements & observations), analysis (benchmarking & opportunity identification), and reporting with prioritised recommendations.\n\nFor a facility spending Rs 1 crore per year on energy, we typically identify Rs 20–30 lakh in annual savings — paying back the audit cost within 3–6 months. Contact GRN Energy for a no-obligation initial assessment.",
        "author": "Ganesh Nikam",
        "date": "28 Feb 2025"
    },
    {
        "id": "20250120090000",
        "title": "ISO 50001:2018 Energy Management System — What It Means for Indian Industry",
        "category": "Energy Management",
        "emoji": "🏆",
        "content": "ISO 50001:2018 is the international standard for Energy Management Systems (EnMS). Built on the Plan-Do-Check-Act (PDCA) cycle, it provides organisations with a systematic framework to improve energy performance on a continual basis.\n\nThe PDCA framework for ISO 50001:\n• Plan: Conduct energy review, establish baseline, set EnPIs and objectives\n• Do: Implement action plans, operational controls, training programs\n• Check: Monitor and measure energy performance against baseline and targets\n• Act: Take corrective actions, review effectiveness, identify new opportunities\n\nBenefits for Indian industries:\n• 10–20% energy cost reduction in first 3 years\n• Alignment with BEE PAT scheme requirements for Designated Consumers\n• Enhanced ESG reporting credentials and corporate sustainability profile\n• Competitive advantage in export markets and international procurement\n• Reduced carbon footprint and improved regulatory compliance\n\nGRN Energy has supported 20+ organisations in Maharashtra through their ISO 50001 journey — from initial gap analysis through certification audit. Contact us for a complimentary ISO 50001 readiness assessment.",
        "author": "GRN Energy Team",
        "date": "20 Jan 2025"
    },
    {
        "id": "20241210080000",
        "title": "Understanding India's BEE Perform Achieve Trade (PAT) Scheme",
        "category": "Policy & Compliance",
        "emoji": "📋",
        "content": "The Perform Achieve Trade (PAT) scheme is India's flagship market-based energy efficiency program under the Bureau of Energy Efficiency (BEE). It is one of the largest such programs in the world.\n\nHow PAT works: Energy-intensive industries (Designated Consumers or DCs) receive specific energy consumption (SEC) reduction targets. Over-achievers earn tradeable Energy Saving Certificates (ESCerts). Under-achievers must purchase ESCerts — creating a strong financial incentive for investment in energy efficiency.\n\nSectors covered under PAT include:\n• Thermal Power Plants\n• Iron & Steel\n• Cement\n• Aluminium and Fertilisers\n• Textile mills and Chlor-alkali plants\n• Pulp & paper, Railways, Commercial buildings\n\nPAT Cycle I (2012–2015) covered 478 DCs and achieved 8.67 million TOE in savings. Subsequent cycles have progressively tightened targets as India moves toward its Paris Agreement commitments.\n\nGRN Energy provides end-to-end PAT support: SEC baseline assessment, target negotiation, ECM identification and implementation, M&V of savings, and BEE reporting. Our clients consistently achieve targets and often earn ESCerts for additional revenue.",
        "author": "Ganesh Nikam",
        "date": "10 Dec 2024"
    },
    {
        "id": "20241105070000",
        "title": "Solar Energy ROI: Calculating Payback Period for Maharashtra Businesses",
        "category": "Renewable Energy",
        "emoji": "☀️",
        "content": "With solar PV costs down over 80% since 2010 and Maharashtra commercial tariffs at Rs 7–12 per kWh, rooftop solar offers 4–6 year paybacks for most commercial and industrial installations.\n\nSample 100 kWp system calculation for Pune:\n• System cost: Rs 50 lakh (at Rs 50,000/kWp)\n• Annual generation: ~1,45,000 kWh (4 peak sun hours/day)\n• Annual savings: Rs 10.15 lakh (at Rs 7/kWh)\n• Simple payback: ~4.9 years\n• 25-year net savings: ~Rs 2 crore (without tariff escalation)\n\nKey factors affecting solar ROI:\n• Roof orientation, tilt, and shading\n• Electricity tariff category\n• DISCOM net-metering policy\n• Financing method (own funds vs loan vs RESCO)\n• PM Surya Ghar Yojana subsidy eligibility\n\nGRN Energy provides independent, vendor-neutral feasibility studies and Detailed Project Reports (DPRs) that help you make informed investment decisions. We also support DISCOM net-metering approvals and technical oversight during execution. Contact us for a complimentary preliminary solar feasibility assessment.",
        "author": "GRN Energy Team",
        "date": "05 Nov 2024"
    }
]


def ensure_blog_file():
    os.makedirs("data", exist_ok=True)
    if not os.path.exists(BLOG_FILE):
        with open(BLOG_FILE, "w") as f:
            json.dump(SEED_POSTS, f, indent=2)


def load_posts():
    ensure_blog_file()
    with open(BLOG_FILE, "r") as f:
        posts = json.load(f)
    return posts if posts else SEED_POSTS


def save_posts(posts):
    os.makedirs("data", exist_ok=True)
    with open(BLOG_FILE, "w") as f:
        json.dump(posts, f, indent=2)


if "is_admin" not in st.session_state:
    st.session_state.is_admin = False
if "show_editor" not in st.session_state:
    st.session_state.show_editor = False
if "selected_post" not in st.session_state:
    st.session_state.selected_post = None

# ── NAVIGATION ──────────────────────────────────────────────────────────────
st.markdown("""
<nav class="nav">
    <span class="logo">🌿 GRN Energy</span>
    <a href="#home">Home</a>
    <a href="#about">About</a>
    <a href="#services">Services</a>
    <a href="#process">Process</a>
    <a href="#blog">Blog</a>
    <a href="#contact" class="cta-link">Contact</a>
</nav>
""", unsafe_allow_html=True)

# ── HERO ─────────────────────────────────────────────────────────────────────
st.markdown("""
<section id="home" class="hero">
    <div class="hero-badge">BEE Certified Energy Consultants &middot; Pune, Maharashtra</div>
    <h1 class="hero-title">
        Smarter Energy.<br>
        <strong>Greener Future.</strong><br>
        <em>Real Results.</em>
    </h1>
    <p class="hero-sub">
        GRN Energy delivers expert energy efficiency consulting, IPMVP-compliant
        measurement &amp; verification, and comprehensive BEE-certified energy audits
        for industries across Maharashtra.
    </p>
    <div class="hero-actions">
        <a href="#services" class="btn-hero">Our Services ↓</a>
        <a href="#contact" class="btn-hero-outline">Get a Free Audit →</a>
    </div>
</section>
""", unsafe_allow_html=True)

# ── STATS ────────────────────────────────────────────────────────────────────
st.markdown("""
<div class="stats-bar">
    <div class="stat-item">
        <div class="stat-num">150+</div>
        <div class="stat-label">Energy Audits Completed</div>
    </div>
    <div class="stat-item">
        <div class="stat-num">200+</div>
        <div class="stat-label">MW Savings Identified</div>
    </div>
    <div class="stat-item">
        <div class="stat-num">50+</div>
        <div class="stat-label">M&amp;V Projects Delivered</div>
    </div>
    <div class="stat-item">
        <div class="stat-num">15+</div>
        <div class="stat-label">Years of Experience</div>
    </div>
</div>
""", unsafe_allow_html=True)

# ── ABOUT ────────────────────────────────────────────────────────────────────
st.markdown("""
<section id="about" class="section">
    <div class="section-label">Who We Are</div>
    <h2 class="section-title">Maharashtra's Trusted <em>Energy Efficiency Partner</em></h2>
    <p class="section-sub">Founded in Pune, GRN Energy has spent 15+ years helping Indian industries reduce energy consumption, lower operating costs, and meet regulatory compliance requirements.</p>
    <div class="about-grid">
        <div class="about-text">
            <p>Our team of BEE-certified energy auditors and IPMVP-certified M&amp;V professionals brings deep technical expertise and a practical, results-focused approach to every engagement. We have served 50+ industries across Maharashtra — from mid-size manufacturers to large Designated Consumers under the PAT scheme.</p>
            <div class="cert-row">
                <span class="cert-pill">BEE Certified</span>
                <span class="cert-pill">IPMVP</span>
                <span class="cert-pill">ISO 50001</span>
                <span class="cert-pill">ISO 14064</span>
            </div>
        </div>
        <div class="about-visual">
            <div class="about-icon">⚡</div>
            <h3>Certified Excellence</h3>
            <p>Internationally recognised credentials in energy auditing, M&amp;V, and management systems.</p>
        </div>
    </div>
</section>
""", unsafe_allow_html=True)

# ── SERVICES ─────────────────────────────────────────────────────────────────
st.markdown("""
<section id="services" class="section section-alt">
    <div class="section-label">What We Do</div>
    <h2 class="section-title">Comprehensive <em>Energy Solutions</em></h2>
    <p class="section-sub">End-to-end energy consultancy — from identifying savings to verifying and sustaining them.</p>
</section>
""", unsafe_allow_html=True)

services_data = [
    ("⚡", "Energy Auditing",
     "BEE-certified Level-1, Level-2 & Level-3 energy audits for industrial, commercial, and infrastructure clients.",
     ["BEE-compliant audit reports", "15–30% savings identified", "Payback period analysis"]),
    ("📊", "Measurement & Verification",
     "IPMVP Options A–D M&V services for ESCOs, financiers, and PAT Designated Consumers.",
     ["IPMVP-certified professionals", "Third-party verification", "ESCert-ready documentation"]),
    ("🏆", "ISO 50001 EnMS",
     "Full-cycle ISO 50001:2018 Energy Management System implementation — gap analysis to certification.",
     ["Gap analysis & EnMS design", "Energy baselines & EnPIs", "Staff training programs"]),
    ("🌱", "Carbon Footprint",
     "GHG emission inventories per ISO 14064 and GHG Protocol — Scope 1, 2 & 3 accounting.",
     ["Scope 1, 2 & 3 accounting", "GHG reduction roadmap", "Sustainability reporting"]),
    ("☀️", "Solar & Renewables",
     "Vendor-neutral feasibility studies, DPRs, and financial modelling for solar and renewable energy projects.",
     ["Solar feasibility & DPR", "ROI and payback analysis", "DISCOM net-metering support"]),
    ("⭐", "BEE Star Rating & PAT",
     "BEE star label applications and complete PAT scheme compliance support for Designated Consumers.",
     ["PAT target setting", "SEC reduction strategy", "ESCerts guidance"]),
]

cols = st.columns(3)
for i, (icon, title, desc, benefits) in enumerate(services_data):
    with cols[i % 3]:
        b_html = "".join(f"<li>{b}</li>" for b in benefits)
        st.markdown(f"""
        <div class="service-card">
            <div class="service-icon">{icon}</div>
            <h3>{title}</h3>
            <p>{desc}</p>
            <ul class="service-benefits">{b_html}</ul>
        </div>
        """, unsafe_allow_html=True)

# ── PROCESS ──────────────────────────────────────────────────────────────────
st.markdown("""
<section id="process" class="section">
    <div class="section-label">How We Work</div>
    <h2 class="section-title">Our Proven <em>4-Step Process</em></h2>
    <p class="section-sub">A structured, data-driven approach that delivers measurable results every time.</p>
</section>
""", unsafe_allow_html=True)

steps = [
    ("01", "Discovery & Scoping",
     "Initial site visit, data collection, energy spend review, and project scoping at no charge."),
    ("02", "Detailed Audit",
     "Instrumented measurements, energy balance analysis, benchmarking, and opportunity identification."),
    ("03", "Implementation Support",
     "ECM prioritisation, contractor coordination, and project management during implementation."),
    ("04", "M&V & Reporting",
     "IPMVP-based savings verification, BEE/PAT reporting, and ongoing performance monitoring."),
]

cols = st.columns(4)
for i, (num, title, desc) in enumerate(steps):
    with cols[i]:
        st.markdown(f"""
        <div class="step">
            <div class="step-num">{num}</div>
            <h4>{title}</h4>
            <p>{desc}</p>
        </div>
        """, unsafe_allow_html=True)

# ── BLOG ─────────────────────────────────────────────────────────────────────
st.markdown("""
<section id="blog" class="section section-alt">
    <div class="section-label">Knowledge Hub</div>
    <h2 class="section-title">Latest <em>Insights &amp; Articles</em></h2>
    <p class="section-sub">Expert articles on energy auditing, M&amp;V best practices, PAT scheme updates, and renewable energy trends in India.</p>
</section>
""", unsafe_allow_html=True)

posts = load_posts()

if st.session_state.is_admin:
    if st.button("➕ Write New Post"):
        st.session_state.show_editor = not st.session_state.show_editor
        st.rerun()

if st.session_state.get("show_editor"):
    with st.container():
        st.markdown('<div class="blog-editor">', unsafe_allow_html=True)
        st.subheader("✍️ New Blog Post")
        new_title = st.text_input("Post Title")
        c1, c2, c3 = st.columns(3)
        with c1:
            new_category = st.text_input("Category", "Energy Auditing")
        with c2:
            new_emoji = st.text_input("Emoji", "📰")
        with c3:
            new_author = st.text_input("Author", "GRN Energy Team")
        new_content = st.text_area("Article Content", height=220,
                                   placeholder="Write your article here...")
        c_pub, c_cancel = st.columns([1, 4])
        with c_pub:
            if st.button("Publish 🚀"):
                if new_title and new_content:
                    new_post = {
                        "id": datetime.now().strftime("%Y%m%d%H%M%S"),
                        "title": new_title,
                        "category": new_category,
                        "emoji": new_emoji,
                        "content": new_content,
                        "author": new_author,
                        "date": datetime.now().strftime("%d %b %Y")
                    }
                    posts.insert(0, new_post)
                    save_posts(posts)
                    st.success("✅ Post published!")
                    st.session_state.show_editor = False
                    st.rerun()
                else:
                    st.error("Title and content are required.")
        with c_cancel:
            if st.button("Cancel"):
                st.session_state.show_editor = False
                st.rerun()
        st.markdown('</div>', unsafe_allow_html=True)

if posts:
    # Full post view
    if st.session_state.selected_post is not None:
        post = next((p for p in posts if p["id"] == st.session_state.selected_post), None)
        if post:
            st.markdown(f"""
            <div class="post-full">
                <span class="blog-cat">{post['category']}</span>
                <h2>{post['emoji']} {post['title']}</h2>
                <p class="post-meta-line">✍️ {post['author']} &nbsp;·&nbsp; 📅 {post['date']}</p>
                <div class="post-body">{post['content'].replace(chr(10), '<br><br>')}</div>
            </div>
            """, unsafe_allow_html=True)
            c1, c2, c3 = st.columns([1, 1, 5])
            with c1:
                if st.button("← Back"):
                    st.session_state.selected_post = None
                    st.rerun()
            if st.session_state.is_admin:
                with c2:
                    if st.button("🗑️ Delete"):
                        posts = [p for p in posts if p["id"] != st.session_state.selected_post]
                        save_posts(posts)
                        st.session_state.selected_post = None
                        st.rerun()
    else:
        # Blog grid
        cols = st.columns(3)
        for i, post in enumerate(posts):
            with cols[i % 3]:
                excerpt = post["content"].replace("\n", " ")[:180] + "…"
                st.markdown(f"""
                <div class="blog-card">
                    <div class="blog-thumb">{post['emoji']}</div>
                    <span class="blog-cat">{post['category']}</span>
                    <h3>{post['title']}</h3>
                    <p class="blog-meta">{post['author']} &nbsp;·&nbsp; {post['date']}</p>
                    <p class="blog-excerpt">{excerpt}</p>
                </div>
                """, unsafe_allow_html=True)
                if st.button("Read More →", key=f"read_{post['id']}"):
                    st.session_state.selected_post = post["id"]
                    st.rerun()
else:
    st.info("No blog posts yet.")

# ── CONTACT ──────────────────────────────────────────────────────────────────
st.markdown("""
<section id="contact" class="section">
    <div class="section-label">Get In Touch</div>
    <h2 class="section-title">Start Your <em>Energy Journey</em></h2>
    <p class="section-sub">Ready to reduce your energy costs? We respond within one business day.</p>
</section>
""", unsafe_allow_html=True)

col_form, col_info = st.columns([1.3, 1])

with col_form:
    with st.form("contact_form"):
        st.subheader("Request a Free Assessment")
        r1c1, r1c2 = st.columns(2)
        with r1c1:
            name = st.text_input("Full Name *")
            email = st.text_input("Email Address *")
        with r1c2:
            company = st.text_input("Company / Organisation")
            service_choice = st.selectbox("Service of Interest", [
                "— Select —",
                "Energy Auditing",
                "Measurement & Verification (M&V)",
                "ISO 50001 EnMS Implementation",
                "Carbon Footprint Assessment",
                "Solar & Renewable Energy",
                "BEE Star Rating & PAT",
                "Other / Not Sure"
            ])
        message = st.text_area("Tell us about your facility *",
                               placeholder="Facility type, location, annual energy spend, goals…")
        submitted = st.form_submit_button("Send Message →")

    if submitted:
        if name and email and message:
            st.success(f"✅ Thank you, {name}! We'll get back to you within one business day.")
        else:
            st.error("Please fill in all required fields (Name, Email, Message).")

with col_info:
    st.markdown("""
    <div class="contact-info-box">
        <h3>Contact GRN Energy</h3>
        <div class="ci-row"><span>📍</span><span>Pune, Maharashtra, India</span></div>
        <div class="ci-row"><span>✉️</span><a href="mailto:nikamganesh.r@gmail.com">nikamganesh.r@gmail.com</a></div>
        <div class="ci-row"><span>🌐</span><a href="http://grnenergy.in" target="_blank">grnenergy.in</a></div>
        <div class="ci-row"><span>🕐</span><span>Response within 1 business day</span></div>
        <hr>
        <p><strong>Sectors served:</strong> Manufacturing, Pharmaceuticals, Textiles, Food Processing, Commercial Buildings, Healthcare, Chemicals, and more.</p>
    </div>
    """, unsafe_allow_html=True)

# ── FOOTER ───────────────────────────────────────────────────────────────────
st.markdown("""
<footer class="site-footer">
    <div class="footer-grid">
        <div>
            <div class="footer-logo">🌿 GRN Energy</div>
            <p>BEE-certified energy auditing and IPMVP-compliant measurement &amp; verification consultancy, Pune, Maharashtra.</p>
        </div>
        <div>
            <strong>Services</strong>
            <ul>
                <li>Energy Auditing</li>
                <li>Measurement &amp; Verification</li>
                <li>ISO 50001 EnMS</li>
                <li>Carbon Footprint</li>
                <li>Solar &amp; Renewables</li>
                <li>BEE Star Rating &amp; PAT</li>
            </ul>
        </div>
        <div>
            <strong>Contact</strong>
            <ul>
                <li>nikamganesh.r@gmail.com</li>
                <li>grnenergy.in</li>
                <li>Pune, Maharashtra</li>
            </ul>
        </div>
    </div>
    <div class="footer-bottom">
        &copy; 2025 GRN Energy &nbsp;&middot;&nbsp; BEE Certified &nbsp;&middot;&nbsp; IPMVP Certified
    </div>
</footer>
""", unsafe_allow_html=True)

# ── ADMIN SIDEBAR ─────────────────────────────────────────────────────────────
with st.sidebar:
    st.header("🔐 Admin Panel")
    if not st.session_state.is_admin:
        pwd = st.text_input("Password", type="password")
        if st.button("Login"):
            if pwd == "grnenergy2024":
                st.session_state.is_admin = True
                st.rerun()
            else:
                st.error("Incorrect password")
    else:
        st.success("✅ Admin logged in")
        st.info("You can now create and delete blog posts.")
        if st.button("Logout"):
            st.session_state.is_admin = False
            st.rerun()
