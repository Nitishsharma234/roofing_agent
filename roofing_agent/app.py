import streamlit as st
import html as html_lib
from styles import CUSTOM_CSS
from scraper import ROOFING_BLOGS, run_agent

st.set_page_config(
    page_title="Roofing AI Agent",
    page_icon="🏠",
    layout="wide",
    initial_sidebar_state="expanded",
)

st.markdown(CUSTOM_CSS, unsafe_allow_html=True)

if "messages" not in st.session_state:
    st.session_state.messages = []
if "total_queries" not in st.session_state:
    st.session_state.total_queries = 0
if "last_processed_query" not in st.session_state:
    st.session_state.last_processed_query = ""

# ── Sidebar ──
with st.sidebar:
    st.markdown("""
    <div style='padding: 1.4rem 0 1rem'>
        <div style='font-size:2.2rem; margin-bottom:0.5rem'>🏠</div>
        <div style='font-family: Syne, sans-serif; font-size:1.1rem; font-weight:800; color:#ffffff; letter-spacing:-0.01em'>
            Roofing AI Agent
        </div>
        <div style='color:rgba(255,255,255,0.25); font-size:0.7rem; margin-top:0.25rem; letter-spacing:0.06em; text-transform:uppercase'>
            FeedSpot Top 100 · 2026
        </div>
    </div>
    <hr style='margin: 0 0 1rem; border:none; border-top:1px solid rgba(255,255,255,0.06)'>
    """, unsafe_allow_html=True)

    st.markdown("<div style='font-size:0.75rem; font-weight:600; color:rgba(255,255,255,0.35); letter-spacing:0.06em; text-transform:uppercase; margin-bottom:0.5rem'>Session Stats</div>", unsafe_allow_html=True)
    st.markdown(f"""
    <div class='metric-pill'>Queries answered <span>{st.session_state.total_queries}</span></div>
    <div class='metric-pill'>Sources indexed <span>{len(ROOFING_BLOGS)}</span></div>
    """, unsafe_allow_html=True)

    st.markdown("<hr style='margin: 1rem 0; border:none; border-top:1px solid rgba(255,255,255,0.06)'>", unsafe_allow_html=True)
    st.markdown("<div style='font-size:0.75rem; font-weight:600; color:rgba(255,255,255,0.35); letter-spacing:0.06em; text-transform:uppercase; margin-bottom:0.5rem'>Try asking</div>", unsafe_allow_html=True)

    example_qs = [
        "What is the best roofing material?",
        "How much does a roof replacement cost?",
        "How long does an asphalt shingle roof last?",
        "What are signs I need a new roof?",
        "Metal roof vs asphalt shingles comparison",
        "How to fix a roof leak?",
        "Best time of year to replace a roof?",
    ]
    for q in example_qs:
        if st.button(q, key=f"ex_{q[:20]}", use_container_width=True):
            st.session_state["prefill_query"] = q
            st.rerun()

    st.markdown("<hr style='margin: 1rem 0; border:none; border-top:1px solid rgba(255,255,255,0.06)'>", unsafe_allow_html=True)
    if st.button("🗑️ Clear Chat", use_container_width=True):
        st.session_state.messages = []
        st.session_state.total_queries = 0
        st.session_state.last_processed_query = ""
        st.rerun()

# ── Hero ──
st.markdown("""
<div class='hero-wrap'>
    <div class='hero-badge'><span>🏠</span> AI-Powered Roofing Expert</div>
    <div class='main-title'>Ask anything about <span class='accent'>roofing</span></div>
    <div class='subtitle'>Answers sourced live from FeedSpot's Top 100 Roofing Blogs 2026 — costs, materials, repairs & more</div>
</div>
<hr class='hero-divider'>
""", unsafe_allow_html=True)

# ── Chat history ──
with st.container():
    if not st.session_state.messages:
        st.markdown("""
        <div class='empty-state'>
            <div class='icon'>💬</div>
            <p>No questions yet.<br>Type a roofing question below or pick one from the sidebar.</p>
        </div>
        """, unsafe_allow_html=True)
    else:
        for msg in st.session_state.messages:
            if msg["role"] == "user":
                escaped = html_lib.escape(msg["content"])
                st.markdown(f"""
                <div class='msg-user'>
                    <div class='bubble'>{escaped}</div>
                </div>
                """, unsafe_allow_html=True)
            else:
                with st.chat_message("assistant", avatar="🤖"):
                    st.markdown(msg["content"])
                    if msg.get("sources"):
                        links = "".join(
                            f'<a href="{s["url"]}" target="_blank">🔗 {s["name"]}</a>'
                            for s in msg["sources"]
                        )
                        st.markdown(f"""
                        <div class='sources-box'>
                            <strong>📚 Sources Used</strong>{links}
                        </div>
                        """, unsafe_allow_html=True)

# ── Input ──
st.markdown("<div style='height:1.2rem'></div>", unsafe_allow_html=True)
prefill_val = st.session_state.pop("prefill_query", "")

col1, col2 = st.columns([5, 1])
with col1:
    user_input = st.text_input(
        label="Ask a roofing question",
        value=prefill_val,
        placeholder="e.g. How much does a metal roof cost?",
        key="user_input_field",
        label_visibility="collapsed",
    )
with col2:
    send_clicked = st.button("Ask →", use_container_width=True, type="primary")

# ── Process ──
should_process = send_clicked or bool(prefill_val)
query_text = user_input.strip()

if should_process and query_text and query_text != st.session_state.last_processed_query:
    st.session_state.last_processed_query = query_text
    st.session_state.messages.append({"role": "user", "content": query_text})
    st.session_state.total_queries += 1

    status_area = st.empty()
    with st.spinner("Thinking..."):
        try:
            result = run_agent(query_text, status_area)
            answer = result["answer"]
            sources = result["sources"]
        except Exception as e:
            answer = (
                f"⚠️ Something went wrong: `{str(e)}`\n\n"
                "Please check that your `GROQ_API_KEY` is valid."
            )
            sources = []

    status_area.empty()
    st.session_state.messages.append({
        "role": "assistant",
        "content": answer,
        "sources": sources,
    })
    st.rerun()
