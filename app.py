import streamlit as st
import json
import os
from datetime import datetime

# ------------- INITIAL SETUP ----------------
st.set_page_config(
    page_title="GRNEnergy – Powering a Sustainable Future",
    page_icon="🌿",
    layout="wide"
)

# Load CSS
with open("static/style.css") as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

# Blog storage file
BLOG_FILE = "data/blog.json"

if not os.path.exists("data"):
    os.makedirs("data")

if not os.path.exists(BLOG_FILE):
    with open(BLOG_FILE, "w") as f:
        json.dump([], f)

# Load blog posts
def load_posts():
    with open(BLOG_FILE, "r") as f:
        return json.load(f)

# Save blog posts
def save_posts(posts):
    with open(BLOG_FILE, "w") as f:
        json.dump(posts, f, indent=2)

# Session state for admin
if "is_admin" not in st.session_state:
    st.session_state.is_admin = False

# ------------- NAVIGATION (Streamlit version) --------------
st.markdown("""
<nav class="nav">
    <span class="logo">🌿 GRNEnergy</span>
    <a href="#home">Home</a>
    <a href="#about">About</es</a>
    #processProcess</a>
    <a href="#blog">Blog</a>
    <a href="#contact" class="cta">Contact</a>
</nav>
""", unsafe===== HERO SECTION ==================
st.markdown("""
<section id="home" class="hero">
    <div class="hero-badge">Certified Energy Professionals</div>
    <h1 class="hero-title">Smarter Energy.<br>
    <strong>Greener Future.</strong>
    <em>Real Results.</em></h1>

    <p class="hero-sub">
        GRNEnergy delivers expert energy efficiency consulting,
        measurement & verification services, and comprehensive energy audits.
    </p>

    <p>#servicesOur Services ↓</a>
    #contactGet a Free Audit →</a></p>
</section>
""", unsafe_allow_html=True)

# ================== ABOUT ==================
st.markdown("""
<section id="about" class="section">
    <div class="section-label">Who We Are</div>
    <h2 class="section-title">India's Trusted <em>Energy Partner</em></h2>
</section>
""", unsafe_allow_html=True)

st.write("""
GRNEnergy was founded with a singular mission: make industrial and commercial 
operations more energy-efficient, cost-effective, and environmentally responsible.
""")

# ================== SERVICES ==================
st.markdown("""
<section id="services" class="section">
    <div class="section-label">What We Do</div>
    <h2 class="section-title">Comprehensive <em>Energy Solutions</em></h2>
</section>
""", unsafe_allow_html=True)

cols = st.columns(3)
services = [
    ("⚡ Energy Auditing", "Level-1, Level-2 & Level-3 audits (BEE/ASHRAE)."),
    ("📈 Measurement & Verification", "IPMVP compliant energy savings verification."),
    ("🏭 Energy Efficiency Consulting", "Strategic energy management & ISO 50001."),
    ("☀️ Renewable Advisory", "Solar/wind feasibility & implementation."),
    ("💧 Water & Resource Audit", "Steam, compressed air, cooling systems."),
    ("📋 ESG Reporting", "GHG accounting, BRSR, GRI frameworks.")
]

for i, (title, desc) in enumerate(services):
    with cols[i % 3]:
        st.markdown(f"""
        <div class="service-card">
            <div class="service-icon">{title[0]}</div>
            <h3>{title}</h3>
            <p>{desc}</p>
        </div>
        """, unsafe_allow_html=True)

# ================== PROCESS ======================
st.markdown("""
<section id="process" class="section">
    <div class="section-label">How We Work</div>
    <h2 class="section-title">Our Proven <em>4-Step Process</em></h2>
</section>
""", unsafe_allow_html=True)

steps = [
    ("01", "Discovery & Scoping", "Understanding goals and baseline."),
    ("02", "Detailed Audit", "Data collection & analysis."),
    ("03", "Implementation", "ECM execution & monitoring."),
    ("04", "M&V Support", "Savings verification & reporting.")
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

# ================== BLOG SECTION ======================
st.markdown("""
<section id="blog" class="section">
    <div class="section-label">Knowledge Hub</div>
    <h2 class="section-title">Latest <em>Insights & Articles</em></h2>
</section>
""", unsafe_allow_html=True)

posts = load_posts()

if st.session_state.is_admin:
    if st.button("➕ Create New Blog Post"):
        st.session_state.show_editor = True

# Blog Editor
if st.session_state.get("show_editor"):
    st.subheader("✍️ New Blog Post")
    title = st.text_input("Post Title")
    category = st.text_input("Category")
    emoji = st.text_input("Emoji", "📰")
    content = st.text_area("Article Content", height=200)
    author = st.text_input("Author", "GRNEnergy Team")

    if st.button("Publish 🚀"):
        new_post = {
            "id": datetime.now().strftime("%Y%m%d%H%M%S"),
            "title": title,
            "category": category,
            "emoji": emoji,
            "content": content,
            "author": author,
            "date": datetime.now().strftime("%d %b %Y")
        }
        posts.insert(0, new_post)
        save_posts(posts)
        st.success("Published!")
        st.session_state.show_editor = False

# Blog Listing
if posts:
    for p in posts:
        st.markdown(f"""
        <div class="blog-card">
            <div class="blog-thumb">{p['emoji']}</div>
            <h3>{p['title']}</h3>
            <p><b>{p['category']}</b> • {p['date']}</p>
            <p>{p['content'][:200]}...</p>
        </div>
        """, unsafe_allow_html=True)
else:
    st.info("No blog posts yet. Admins can add posts.")

# ================== CONTACT FORM ======================
st.markdown("""
<section id="contact" class="section">
    <div class="section-label">Get In Touch</div>
    <h2 class="section-title">Start Your <em>Energy Journey</em></h2>
</section>
""", unsafe_allow_html=True)

with st.form("contact_form"):
    name = st.text_input("Full Name")
    email = st.text_input("Email")
    message = st.text_area("Message")
    submitted = st.form_submit_button("Send Message →")

if submitted:
    st.success(f"Thank you {name}! We will contact you soon.")

# ================== ADMIN LOGIN ======================
st.sidebar.header("Admin Panel")
password = st.sidebar.text_input("Password", type="password")

if st.sidebar.button("Login"):
    if password == "grnenergy2024":
        st.session_state.is_admin = True
        st.sidebar.success("Admin logged in")
    else:
        st.sidebar.error("Wrong password")