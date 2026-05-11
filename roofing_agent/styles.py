CUSTOM_CSS = """
<style>
@import url('https://fonts.googleapis.com/css2?family=Syne:wght@400;500;600;700;800&family=DM+Sans:ital,opsz,wght@0,9..40,300;0,9..40,400;0,9..40,500;1,9..40,400&display=swap');

*, *::before, *::after { box-sizing: border-box; margin: 0; padding: 0; }

html, body, [class*="css"] {
    font-family: 'DM Sans', sans-serif;
    background-color: #0a0b0f;
    color: #dde1ec;
}

#MainMenu, footer, header { visibility: hidden; }

/* ── Page background with subtle texture ── */
.stApp {
    background: #0a0b0f;
    background-image:
        radial-gradient(ellipse 80% 50% at 20% 0%, rgba(247,151,30,0.06) 0%, transparent 60%),
        radial-gradient(ellipse 60% 40% at 80% 100%, rgba(255,210,0,0.04) 0%, transparent 55%);
}

/* ── Hero ── */
.hero-wrap {
    text-align: center;
    padding: 2.5rem 0 1.2rem;
}
.hero-badge {
    display: inline-flex;
    align-items: center;
    gap: 6px;
    background: rgba(247,151,30,0.1);
    border: 1px solid rgba(247,151,30,0.25);
    border-radius: 100px;
    padding: 4px 14px;
    font-size: 0.7rem;
    font-weight: 600;
    letter-spacing: 0.08em;
    text-transform: uppercase;
    color: #f7971e;
    margin-bottom: 1rem;
}
.hero-badge span { font-size: 0.85rem; }
.main-title {
    font-family: 'Syne', sans-serif;
    font-size: 2.4rem;
    font-weight: 800;
    color: #ffffff;
    letter-spacing: -0.02em;
    line-height: 1.1;
    margin-bottom: 0.5rem;
}
.main-title .accent {
    background: linear-gradient(90deg, #f7971e, #ffd200);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    background-clip: text;
}
.subtitle {
    color: rgba(221,225,236,0.45);
    font-size: 0.88rem;
    font-weight: 400;
    max-width: 480px;
    margin: 0 auto;
    line-height: 1.6;
}
.hero-divider {
    border: none;
    border-top: 1px solid rgba(255,255,255,0.06);
    margin: 1.5rem 0 0.5rem;
}

/* ── Chat bubbles ── */
.msg-user {
    display: flex;
    justify-content: flex-end;
    margin: 0.6rem 0;
}
.msg-user .bubble {
    background: linear-gradient(135deg, #f7971e 0%, #ffd200 100%);
    color: #1a1200;
    border-radius: 20px 20px 5px 20px;
    padding: 0.7rem 1.1rem;
    max-width: 70%;
    font-weight: 500;
    font-size: 0.9rem;
    line-height: 1.55;
    box-shadow: 0 4px 20px rgba(247,151,30,0.2);
}

/* ── Bot message container (override Streamlit chat_message) ── */
[data-testid="stChatMessage"] {
    background: rgba(255,255,255,0.03) !important;
    border: 1px solid rgba(255,255,255,0.07) !important;
    border-radius: 16px !important;
    padding: 1rem 1.2rem !important;
    margin: 0.6rem 0 !important;
}

/* ── Sources box ── */
.sources-box {
    margin-top: 0.8rem;
    background: rgba(255,210,0,0.05);
    border: 1px solid rgba(255,210,0,0.15);
    border-radius: 12px;
    padding: 0.65rem 1rem;
    font-size: 0.8rem;
    color: rgba(255,255,255,0.5);
}
.sources-box strong {
    color: rgba(255,210,0,0.8);
    display: block;
    margin-bottom: 0.4rem;
    font-size: 0.78rem;
    letter-spacing: 0.03em;
    text-transform: uppercase;
}
.sources-box a {
    display: inline-flex;
    align-items: center;
    gap: 4px;
    margin: 0.2rem 0.4rem 0.2rem 0;
    color: rgba(255,210,0,0.75);
    text-decoration: none;
    font-size: 0.8rem;
    background: rgba(255,210,0,0.07);
    border: 1px solid rgba(255,210,0,0.15);
    border-radius: 6px;
    padding: 2px 8px;
    transition: all 0.15s;
}
.sources-box a:hover {
    background: rgba(255,210,0,0.13);
    border-color: rgba(255,210,0,0.3);
    color: #ffd200;
}

/* ── Status badges ── */
.status-badge {
    display: inline-flex;
    align-items: center;
    gap: 6px;
    padding: 0.35rem 0.9rem;
    border-radius: 100px;
    font-size: 0.8rem;
    font-weight: 500;
    letter-spacing: 0.01em;
    animation: pulse 2s ease-in-out infinite;
}
@keyframes pulse {
    0%, 100% { opacity: 1; }
    50% { opacity: 0.65; }
}
.badge-search  {
    background: rgba(99,102,241,0.12);
    color: #a5b4fc;
    border: 1px solid rgba(99,102,241,0.3);
}
.badge-reading {
    background: rgba(245,158,11,0.12);
    color: #fcd34d;
    border: 1px solid rgba(245,158,11,0.3);
}
.badge-thinking {
    background: rgba(16,185,129,0.12);
    color: #6ee7b7;
    border: 1px solid rgba(16,185,129,0.3);
}

/* ── Metric pills (sidebar) ── */
.metric-pill {
    display: flex;
    justify-content: space-between;
    align-items: center;
    background: rgba(255,255,255,0.04);
    border: 1px solid rgba(255,255,255,0.07);
    border-radius: 10px;
    padding: 0.5rem 0.8rem;
    margin-bottom: 0.45rem;
    font-size: 0.82rem;
    color: rgba(255,255,255,0.45);
}
.metric-pill span {
    color: #ffd200;
    font-weight: 600;
    font-size: 0.88rem;
}

/* ── Empty state ── */
.empty-state {
    text-align: center;
    padding: 4rem 1rem;
    color: rgba(255,255,255,0.2);
}
.empty-state .icon {
    font-size: 2.8rem;
    margin-bottom: 1rem;
    filter: grayscale(0.4) opacity(0.5);
}
.empty-state p {
    font-size: 0.9rem;
    line-height: 1.7;
    color: rgba(255,255,255,0.25);
}

/* ── Input area ── */
.stTextInput > div > div > input {
    background: rgba(255,255,255,0.04) !important;
    border: 1px solid rgba(255,255,255,0.1) !important;
    border-radius: 12px !important;
    color: #dde1ec !important;
    font-family: 'DM Sans', sans-serif !important;
    font-size: 0.9rem !important;
    padding: 0.65rem 1rem !important;
    transition: border-color 0.2s, box-shadow 0.2s !important;
}
.stTextInput > div > div > input:focus {
    border-color: rgba(247,151,30,0.45) !important;
    box-shadow: 0 0 0 3px rgba(247,151,30,0.08) !important;
    outline: none !important;
}
.stTextInput > div > div > input::placeholder {
    color: rgba(255,255,255,0.2) !important;
}

/* ── Primary Ask button ── */
.stButton > button[kind="primary"],
.stButton > button[data-testid="baseButton-primary"] {
    background: linear-gradient(135deg, #f7971e, #ffd200) !important;
    color: #1a1200 !important;
    font-weight: 700 !important;
    font-family: 'DM Sans', sans-serif !important;
    border: none !important;
    border-radius: 12px !important;
    font-size: 0.88rem !important;
    letter-spacing: 0.01em !important;
    transition: opacity 0.15s, transform 0.1s !important;
    box-shadow: 0 4px 16px rgba(247,151,30,0.25) !important;
}
.stButton > button[kind="primary"]:hover,
.stButton > button[data-testid="baseButton-primary"]:hover {
    opacity: 0.9 !important;
    transform: translateY(-1px) !important;
    box-shadow: 0 6px 20px rgba(247,151,30,0.35) !important;
}
.stButton > button[kind="primary"]:active {
    transform: translateY(0) !important;
}

/* ── Sidebar buttons (example questions) ── */
section[data-testid="stSidebar"] .stButton > button {
    background: rgba(255,255,255,0.04) !important;
    border: 1px solid rgba(255,255,255,0.08) !important;
    color: rgba(255,255,255,0.6) !important;
    border-radius: 10px !important;
    font-size: 0.8rem !important;
    font-family: 'DM Sans', sans-serif !important;
    text-align: left !important;
    transition: all 0.15s !important;
    padding: 0.5rem 0.75rem !important;
}
section[data-testid="stSidebar"] .stButton > button:hover {
    background: rgba(247,151,30,0.1) !important;
    border-color: rgba(247,151,30,0.3) !important;
    color: #ffd200 !important;
    transform: translateX(3px) !important;
}

/* ── Clear Chat button ── */
section[data-testid="stSidebar"] .stButton > button[kind="secondary"] {
    background: rgba(255,60,60,0.07) !important;
    border-color: rgba(255,60,60,0.2) !important;
    color: rgba(255,120,120,0.8) !important;
}
section[data-testid="stSidebar"] .stButton > button[kind="secondary"]:hover {
    background: rgba(255,60,60,0.13) !important;
    border-color: rgba(255,60,60,0.4) !important;
    color: #ff8080 !important;
    transform: none !important;
}

/* ── Sidebar styling ── */
section[data-testid="stSidebar"] {
    background: #0d0e14 !important;
    border-right: 1px solid rgba(255,255,255,0.05) !important;
}
section[data-testid="stSidebar"] > div {
    background: transparent !important;
}

/* ── Scrollbar ── */
::-webkit-scrollbar { width: 4px; }
::-webkit-scrollbar-track { background: transparent; }
::-webkit-scrollbar-thumb {
    background: rgba(255,255,255,0.1);
    border-radius: 4px;
}
::-webkit-scrollbar-thumb:hover { background: rgba(255,255,255,0.2); }

/* ── Spinner ── */
.stSpinner > div {
    border-top-color: #f7971e !important;
}
</style>
"""
