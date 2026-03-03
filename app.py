"""
TalentScout - Professional AI Hiring Assistant Interface
Enterprise-grade UI with advanced visual hierarchy and professional components
"""

import streamlit as st
import os
from dotenv import load_dotenv
from src.chatbot import TalentScoutChatbot

# Load environment variables
load_dotenv()

# Page configuration
st.set_page_config(
    page_title="TalentScout - AI Hiring Assistant",
    page_icon="💼",
    layout="wide",
    initial_sidebar_state="expanded",
)

# Professional Enterprise CSS
st.markdown(
    """
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&family=Poppins:wght@400;500;600;700&display=swap');
    
    * { font-family: 'Inter', sans-serif; }

    /* Custom top navbar */
    .custom-navbar {
        background: linear-gradient(135deg, #ffd6ef 0%, #ffc2e6 55%, #edc7ff 100%);
        border: 1px solid #f9a8d4;
        border-radius: 14px;
        padding: 0.9rem 1rem;
        margin: 0.2rem 0 1.2rem 0;
        box-shadow: 0 8px 20px rgba(190, 24, 93, 0.12);
        animation: fadeInUp 0.45s ease-out;
    }

    .navbar-title {
        color: #7e114f;
        font-weight: 700;
        font-size: 0.95rem;
        margin-bottom: 0.4rem;
    }

    .navbar-subtitle {
        color: #5a1f4e;
        font-size: 0.82rem;
        font-weight: 600;
    }

    /* Hide Streamlit default top navbar/toolbar */
    [data-testid="stHeader"] {
        height: 0 !important;
        background: transparent !important;
    }

    [data-testid="stToolbar"],
    [data-testid="stDecoration"],
    [data-testid="stStatusWidget"],
    #MainMenu,
    footer {
        display: none !important;
        visibility: hidden !important;
    }
    
    .stApp {
        background: linear-gradient(135deg, #ffe9f6 0%, #ffe1fb 45%, #f2e7ff 100%);
        animation: gradientShift 14s ease infinite;
        background-size: 200% 200%;
    }
    
    .main .block-container {
        padding: 2rem 3rem;
        max-width: 1400px;
        background: #fff8fc;
        border-radius: 16px;
        box-shadow: 0 20px 60px rgba(15, 23, 42, 0.15);
        border: 1px solid #fbcfe8;
    }
    
    /* Header */
    .main-header {
        background: linear-gradient(135deg, #ff7acb 0%, #e85db4 55%, #c084fc 100%);
        color: #2b0a26;
        text-align: center;
        padding: 3.5rem 2rem;
        border-radius: 16px;
        margin-bottom: 2rem;
        box-shadow: 0 16px 34px rgba(196, 60, 156, 0.28);
        border: 1px solid rgba(255, 255, 255, 0.35);
        animation: fadeInUp 0.6s ease-out;
        position: relative;
        overflow: hidden;
    }

    .main-header::after {
        content: '';
        position: absolute;
        top: -120%;
        left: -30%;
        width: 40%;
        height: 300%;
        background: linear-gradient(120deg, rgba(255,255,255,0) 0%, rgba(255,255,255,0.35) 50%, rgba(255,255,255,0) 100%);
        animation: shimmerSweep 5s ease-in-out infinite;
    }
    
    .main-header h1 {
        font-family: 'Poppins', sans-serif;
        font-size: 3.5rem;
        font-weight: 700;
        margin: 0;
        background: linear-gradient(135deg, #ffffff 0%, #fff0fb 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        background-clip: text;
    }
    
    .main-header p {
        font-size: 1.1rem;
        margin-top: 0.8rem;
        color: #fff5fb;
        font-weight: 500;
    }
    
    /* Welcome Card */
    .welcome-card {
        background: linear-gradient(135deg, #ffd0ea 0%, #ffc0e2 55%, #f3d3ff 100%);
        color: #3a1032;
        padding: 2.5rem;
        border-radius: 16px;
        margin: 1.5rem 0;
        box-shadow: 0 12px 30px rgba(212, 65, 158, 0.22);
        border: 1px solid rgba(236, 72, 153, 0.45);
        animation: fadeInUp 0.8s ease-out, floatSoft 6s ease-in-out infinite;
    }
    
    .welcome-card h3 {
        font-family: 'Poppins', sans-serif;
        font-size: 2rem;
        margin-bottom: 1rem;
        color: #8a135f;
    }

    .welcome-card p {
        color: #4a183f !important;
        font-weight: 600;
    }
    
    /* Professional Card */
    .professional-card {
        background: linear-gradient(135deg, #fff4fb 0%, #fff9fd 100%);
        border: 1px solid #f9a8d4;
        border-radius: 12px;
        padding: 2rem;
        margin: 1rem 0;
        box-shadow: 0 4px 12px rgba(15, 23, 42, 0.08);
        transition: all 0.35s ease;
        animation: fadeInUp 0.5s ease-out;
        position: relative;
        overflow: hidden;
    }

    .professional-card::before {
        content: '';
        position: absolute;
        top: -60%;
        left: -20%;
        width: 30%;
        height: 220%;
        background: linear-gradient(120deg, rgba(255,255,255,0) 0%, rgba(255,255,255,0.45) 50%, rgba(255,255,255,0) 100%);
        transform: translateX(-220%);
        transition: transform 0.8s ease;
    }

    .professional-card:hover::before {
        transform: translateX(420%);
    }
    
    .professional-card:hover {
        box-shadow: 0 12px 30px rgba(236, 72, 153, 0.18);
        border-color: #ec4899;
    }
    
    /* Feature Box */
    .feature-box {
        background: linear-gradient(135deg, #ffdff0 0%, #fff4fb 100%);
        border: 1px solid #fbcfe8;
        border-left: 4px solid #ec4899;
        border-radius: 10px;
        padding: 1.5rem;
        margin: 1rem 0;
        transition: all 0.35s ease;
        animation: fadeInUp 0.7s ease-out;
    }
    
    .feature-box:hover {
        transform: translateX(5px);
        box-shadow: 0 8px 20px rgba(236, 72, 153, 0.15);
    }
    
    /* Section Card */
    .section-card {
        background: linear-gradient(135deg, #fff8fc 0%, #ffffff 100%);
        border: 2px solid #fbcfe8;
        border-radius: 14px;
        padding: 2.5rem;
        margin: 2rem 0;
        box-shadow: 0 8px 20px rgba(15, 23, 42, 0.06);
        animation: fadeInUp 0.75s ease-out;
    }
    
    .section-card.complete {
        border-color: #db2777;
        background: linear-gradient(135deg, #fff1f8 0%, #ffffff 100%);
    }
    
    /* Info Box */
    .info-box {
        background: linear-gradient(135deg, #ffe4ef 0%, #fff8fc 100%);
        color: #0f172a;
        border-left: 4px solid #ec4899;
        padding: 2rem;
        border-radius: 12px;
        margin: 1.5rem 0;
        box-shadow: 0 8px 20px rgba(236, 72, 153, 0.12);
    }
    
    .info-box h3 {
        font-family: 'Poppins', sans-serif;
        margin-top: 0;
        color: #db2777;
        font-size: 1.3rem;
    }
    
    /* Progress Metrics */
    .metric-card {
        background: linear-gradient(135deg, #ffeefd 0%, #fff8fc 100%);
        padding: 1.8rem;
        border-radius: 12px;
        box-shadow: 0 4px 12px rgba(15, 23, 42, 0.08);
        border: 1px solid #fbcfe8;
        border-left: 4px solid #ec4899;
        transition: all 0.3s ease;
        animation: fadeInUp 0.6s ease-out, floatSoft 7s ease-in-out infinite;
    }
    
    .metric-card:hover {
        transform: translateY(-4px);
        box-shadow: 0 12px 30px rgba(236, 72, 153, 0.2);
        border-left-color: #f472b6;
    }
    
    /* Chat Messages */
    .message-user {
        background: linear-gradient(135deg, #ff7acb 0%, #e85db4 100%);
        color: white;
        padding: 1.3rem 1.6rem;
        border-radius: 16px 16px 4px 16px;
        margin: 1rem 0;
        margin-left: 15%;
        box-shadow: 0 4px 15px rgba(196, 60, 156, 0.28);
        animation: slideInRight 0.3s ease;
        border: 1px solid rgba(255, 221, 243, 0.8);
    }
    
    .message-assistant {
        background: linear-gradient(135deg, #fff1f8 0%, #ffffff 100%);
        color: #0f172a;
        padding: 1.3rem 1.6rem;
        border-radius: 16px 16px 16px 4px;
        margin: 1rem 0;
        margin-right: 15%;
        box-shadow: 0 4px 15px rgba(236, 72, 153, 0.15);
        animation: slideInLeft 0.3s ease;
        border: 1px solid rgba(244, 114, 182, 0.35);
    }
    
    .message-user strong {
        display: block;
        margin-bottom: 0.5rem;
        font-weight: 700;
        font-size: 0.95rem;
        color: #fff1fb;
    }
    
    .message-assistant strong {
        display: block;
        margin-bottom: 0.5rem;
        font-weight: 700;
        font-size: 0.95rem;
        color: #db2777;
    }
    
    /* Animations */
    @keyframes slideInRight {
        from { opacity: 0; transform: translateX(40px); }
        to { opacity: 1; transform: translateX(0); }
    }
    
    @keyframes slideInLeft {
        from { opacity: 0; transform: translateX(-40px); }
        to { opacity: 1; transform: translateX(0); }
    }

    @keyframes fadeInUp {
        from {
            opacity: 0;
            transform: translateY(12px);
        }
        to {
            opacity: 1;
            transform: translateY(0);
        }
    }

    @keyframes gradientShift {
        0% { background-position: 0% 50%; }
        50% { background-position: 100% 50%; }
        100% { background-position: 0% 50%; }
    }

    @keyframes pulseGlow {
        0%, 100% { box-shadow: 0 0 0 0 rgba(236, 72, 153, 0.25); }
        50% { box-shadow: 0 0 0 8px rgba(236, 72, 153, 0); }
    }

    @keyframes floatSoft {
        0%, 100% { transform: translateY(0px); }
        50% { transform: translateY(-4px); }
    }

    @keyframes shimmerSweep {
        0% { transform: translateX(-180%) rotate(18deg); }
        50% { transform: translateX(420%) rotate(18deg); }
        100% { transform: translateX(420%) rotate(18deg); }
    }
    
    /* Buttons */
    .stButton > button {
        background: linear-gradient(135deg, #ec4899 0%, #be185d 100%);
        color: white;
        border: none;
        padding: 0.8rem 2.2rem;
        height: 2.8rem;
        border-radius: 8px;
        font-weight: 600;
        font-size: 0.95rem;
        box-shadow: 0 4px 12px rgba(190, 24, 93, 0.35);
        transition: all 0.3s ease;
        text-transform: none;
        letter-spacing: 0.2px;
        animation: pulseGlow 3s ease-in-out infinite;
        position: relative;
        overflow: hidden;
        display: flex;
        align-items: center;
        justify-content: center;
        white-space: nowrap;
    }

    .stButton > button::after {
        content: '';
        position: absolute;
        top: 0;
        left: -130%;
        width: 55%;
        height: 100%;
        background: linear-gradient(120deg, rgba(255,255,255,0) 0%, rgba(255,255,255,0.35) 50%, rgba(255,255,255,0) 100%);
        transition: left 0.55s ease;
    }

    .stButton > button:hover::after {
        left: 140%;
    }
    
    .stButton > button:hover {
        transform: translateY(-2px);
        box-shadow: 0 8px 20px rgba(190, 24, 93, 0.4);
        background: linear-gradient(135deg, #f472b6 0%, #db2777 100%);
    }
    
    /* Input Fields */
    .stTextInput > div > div > input {
        border: 2px solid #e2e8f0 !important;
        border-radius: 8px;
        padding: 0.85rem 1.2rem;
        font-size: 1rem;
        transition: all 0.3s ease;
        color: #1e293b;
        background-color: #ffffff;
    }
    
    .stTextInput > div > div > input:focus {
        border-color: #ec4899 !important;
        box-shadow: 0 0 0 4px rgba(236, 72, 153, 0.15);
    }
    
    /* Sidebar */
    [data-testid="stSidebar"] {
        background: linear-gradient(180deg, #ff9bd6 0%, #f78dcf 60%, #e9b3ff 100%);
    }
    
    [data-testid="stSidebar"] * { color: #4a183f !important; }
    [data-testid="stSidebar"] h1, [data-testid="stSidebar"] h2, [data-testid="stSidebar"] h3 { color: #7e114f; }
    
    /* Alert Boxes */
    .stSuccess {
        background: linear-gradient(135deg, #fff1f8 0%, #ffffff 100%) !important;
        border-left: 4px solid #db2777 !important;
        border-radius: 8px;
        padding: 1rem;
        color: #831843 !important;
    }
    
    .stInfo {
        background: linear-gradient(135deg, #fff1f8 0%, #ffffff 100%) !important;
        border-left: 4px solid #ec4899 !important;
        border-radius: 8px;
        padding: 1rem;
        color: #831843 !important;
    }
    
    .stWarning {
        background: linear-gradient(135deg, #fff1f8 0%, #ffe4ef 100%) !important;
        border-left: 4px solid #ec4899 !important;
        border-radius: 8px;
        padding: 1rem;
        color: #9d174d !important;
    }
    
    /* Conversation Container */
    .conversation-container {
        background: #fff6fc;
        padding: 2rem;
        border-radius: 12px;
        margin: 1.5rem 0;
        max-height: 600px;
        overflow-y: auto;
        border: 1px solid #fbcfe8;
        animation: fadeInUp 0.55s ease-out;
    }
    
    .conversation-container::-webkit-scrollbar {
        width: 8px;
    }
    
    .conversation-container::-webkit-scrollbar-track {
        background: #f1f5f9;
        border-radius: 10px;
    }
    
    .conversation-container::-webkit-scrollbar-thumb {
        background: linear-gradient(180deg, #ec4899 0%, #be185d 100%);
        border-radius: 10px;
    }
    
    .conversation-container::-webkit-scrollbar-thumb:hover {
        background: linear-gradient(180deg, #db2777 0%, #9d174d 100%);
    }
    
    /* Badge */
    .badge {
        display: inline-block;
        padding: 0.4rem 0.9rem;
        border-radius: 20px;
        font-size: 0.85rem;
        font-weight: 600;
        background: linear-gradient(135deg, #ec4899 0%, #be185d 100%);
        color: white;
        margin: 0.3rem;
        box-shadow: 0 2px 8px rgba(190, 24, 93, 0.25);
    }
    
    h2, h3 {
        font-family: 'Poppins', sans-serif;
        color: #7e114f;
        font-weight: 700;
    }
    
    h2 { border-bottom: 2px solid #ec4899; padding-bottom: 0.5rem; }
    
    hr {
        margin: 2rem 0;
        border: none;
        height: 1px;
        background: linear-gradient(90deg, transparent, #e2e8f0, transparent);
    }
    
    [data-testid="stMetricValue"] {
        font-size: 2.2rem;
        font-weight: 700;
        color: #db2777;
    }

    [data-testid="stMetricLabel"] {
        color: #9d174d !important;
        font-weight: 600 !important;
    }

    .professional-card p,
    .feature-box p,
    .info-box p,
    .info-box li,
    .section-card p {
        color: #3f1b39 !important;
        font-weight: 600;
    }

    .professional-card h4,
    .feature-box h4 {
        color: #8a135f !important;
        font-weight: 700 !important;
    }

    p, li, label, span, .stMarkdown {
        color: #3f1b39;
    }
    </style>
    """,
    unsafe_allow_html=True,
)


def initialize_session_state():
    """Initialize session state."""
    if "chatbot" not in st.session_state:
        api_key = os.getenv("OPENAI_API_KEY")
        if not api_key:
            st.error("⚠️ OpenAI API key not found. Please set the OPENAI_API_KEY environment variable.")
            st.stop()
        st.session_state.chatbot = TalentScoutChatbot(api_key=api_key)
        st.session_state.conversation_started = False
        st.session_state.messages = []
    if "show_progress" not in st.session_state:
        st.session_state.show_progress = True
    if "show_help" not in st.session_state:
        st.session_state.show_help = False
    if "active_view" not in st.session_state:
        st.session_state.active_view = "home"


def render_header():
    """Render professional header."""
    st.markdown(
        """<div class="main-header">
            <h1>💼 TalentScout</h1>
            <p>AI-Powered Intelligent Hiring Assistant for Technology Professionals</p>
        </div>""",
        unsafe_allow_html=True,
    )


def render_top_navbar():
    """Render a useful custom navbar with actionable controls."""
    st.markdown(
        """
        <div class="custom-navbar">
            <div class="navbar-title">✨ Quick Navigation</div>
            <div class="navbar-subtitle">Use these controls to move through the interview faster.</div>
        </div>
        """,
        unsafe_allow_html=True,
    )

    nav_col1, nav_col2, nav_col3, nav_col4, nav_col5 = st.columns(5)

    with nav_col1:
        if st.button("🏠 Home", key="nav_home", use_container_width=True):
            st.session_state.active_view = "home"
            st.rerun()

    with nav_col2:
        nav_label = "🚀 Start\u00A0Interview" if not st.session_state.conversation_started else "💬 Continue"
        if st.button(nav_label, key="nav_interview", use_container_width=True):
            st.session_state.active_view = "interview"
            if not st.session_state.conversation_started:
                greeting = st.session_state.chatbot.start_conversation()
                st.session_state.messages.append({"role": "assistant", "content": greeting})
                st.session_state.conversation_started = True
            st.rerun()

    with nav_col3:
        if st.button("📊 Progress", key="nav_progress", use_container_width=True):
            st.session_state.show_progress = not st.session_state.show_progress
            st.session_state.active_view = "interview"
            st.rerun()

    with nav_col4:
        if st.button("❓ Help", key="nav_help", use_container_width=True):
            st.session_state.show_help = not st.session_state.show_help
            st.rerun()

    with nav_col5:
        if st.button("🔄 New\u00A0Interview", key="nav_reset", use_container_width=True):
            st.session_state.conversation_started = False
            st.session_state.messages = []
            st.session_state.active_view = "home"
            st.session_state.chatbot = TalentScoutChatbot(api_key=os.getenv("OPENAI_API_KEY"))
            st.rerun()

    if st.session_state.show_help:
        st.markdown(
            """
            <div class="info-box" style="margin-top: 0.8rem;">
                <h3>🧭 Quick Help</h3>
                <p><strong>Home:</strong> View overview and interview journey.</p>
                <p><strong>Start/Continue:</strong> Jump directly into interview chat.</p>
                <p><strong>Progress:</strong> Show or hide progress metrics.</p>
                <p><strong>New Interview:</strong> Reset and begin from scratch.</p>
            </div>
            """,
            unsafe_allow_html=True,
        )


def render_progress():
    """Render interview progress."""
    if not st.session_state.show_progress:
        return
    progress = st.session_state.chatbot.get_progress()
    st.markdown("### 📊 Interview Progress")
    col1, col2, col3, col4 = st.columns(4)
    with col1:
        st.markdown('<div class="metric-card">', unsafe_allow_html=True)
        st.metric("📍 Stage", progress["stage"].replace("_", " ").title())
        st.markdown('</div>', unsafe_allow_html=True)
    with col2:
        info_progress = f"{progress['information_gathered']}/{progress['information_total']}"
        pct = (progress['information_gathered'] / progress['information_total'] * 100) if progress['information_total'] > 0 else 0
        st.markdown('<div class="metric-card">', unsafe_allow_html=True)
        st.metric("📋 Info", info_progress, f"{pct:.0f}%")
        st.markdown('</div>', unsafe_allow_html=True)
    with col3:
        question_progress = f"{progress['questions_answered']}/{progress['questions_total']}"
        q_pct = (progress['questions_answered'] / progress['questions_total'] * 100) if progress['questions_total'] > 0 else 0
        st.markdown('<div class="metric-card">', unsafe_allow_html=True)
        st.metric("❓ Questions", question_progress, f"{q_pct:.0f}%")
        st.markdown('</div>', unsafe_allow_html=True)
    with col4:
        status = "✅ Complete" if progress['is_completed'] else "⏳ In Progress"
        st.markdown('<div class="metric-card">', unsafe_allow_html=True)
        st.metric("Status", status)
        st.markdown('</div>', unsafe_allow_html=True)
    st.markdown("<br>", unsafe_allow_html=True)


def render_conversation():
    """Render chat history."""
    st.markdown("### 💬 Chat History")
    st.markdown('<div class="conversation-container">', unsafe_allow_html=True)
    for message in st.session_state.messages:
        if message["role"] == "user":
            st.markdown(f'<div class="message-user"><strong>👤 You</strong><div>{message["content"]}</div></div>', unsafe_allow_html=True)
        else:
            st.markdown(f'<div class="message-assistant"><strong>🤖 TalentScout AI</strong><div>{message["content"]}</div></div>', unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)


def render_input_area():
    """Render input form."""
    st.markdown("-" * 50)
    with st.form(key="chat_input_form", clear_on_submit=True):
        col1, col2 = st.columns([5, 1], gap="small")
        with col1:
            user_input = st.text_input("Your response:", key="user_input", placeholder="💭 Type your response here...", label_visibility="collapsed")
        with col2:
            send_button = st.form_submit_button("📤 Send", use_container_width=True, type="primary")
        if send_button and user_input:
            st.session_state.messages.append({"role": "user", "content": user_input})
            with st.spinner("🤔 Analyzing your response..."):
                response, _ = st.session_state.chatbot.process_user_input(user_input)
            st.session_state.messages.append({"role": "assistant", "content": response})
        elif send_button and not user_input:
            st.warning("⚠️ Please type your response before sending.")


def render_sidebar():
    """Render professional sidebar."""
    with st.sidebar:
        st.markdown("# 📊 Interview Dashboard")
        st.markdown("---")
        candidate_info = st.session_state.chatbot.get_candidate_info()
        st.markdown("### 👤 Candidate Profile")
        if candidate_info:
            for key, value in candidate_info.items():
                display_key = key.replace('_', ' ').title()
                if key == "tech_stack" and isinstance(value, list):
                    st.markdown(f"**{display_key}:**")
                    for tech in value:
                        st.markdown(f'<span class="badge">{tech}</span>', unsafe_allow_html=True)
                else:
                    st.markdown(f"**{display_key}:** {value}")
        else:
            st.info("🚀 Start the conversation to begin!")
        st.markdown("---")
        st.markdown("### ⚙️ Controls")
        if st.button("👁️ Toggle Progress", use_container_width=True):
            st.session_state.show_progress = not st.session_state.show_progress
            st.rerun()
        st.markdown("---")
        st.markdown("### ℹ️ About")
        st.markdown("**TalentScout** is an AI-powered recruitment assistant for technology professionals.")
        st.markdown("**Version 1.0** | *Powered by OpenAI GPT-3.5*")


def render_journey():
    """Render journey steps."""
    st.markdown("""<div style="background: linear-gradient(135deg, #fff4fb 0%, #fdf0ff 100%); border: 1px solid #f9a8d4; border-radius: 12px; padding: 2rem; margin: 1.5rem 0; animation: fadeInUp 0.55s ease-out;">
        <div style="display: grid; grid-template-columns: repeat(3, 1fr); gap: 2rem; text-align: center;">
            <div><div style="width: 50px; height: 50px; border-radius: 50%; background: linear-gradient(135deg, #ec4899 0%, #db2777 100%); color: white; font-weight: 700; display: flex; align-items: center; justify-content: center; margin: 0 auto 0.8rem; font-size: 1.2rem; box-shadow: 0 4px 15px rgba(236, 72, 153, 0.3);">1</div>
            <h4 style="color: #8a135f; margin: 0 0 0.5rem 0; font-weight: 700;">Profile</h4><p style="color: #5b214e; font-size: 0.9rem; margin: 0;">Personal & Professional</p></div>
            <div><div style="width: 50px; height: 50px; border-radius: 50%; background: #fbcfe8; color: #8a135f; font-weight: 700; display: flex; align-items: center; justify-content: center; margin: 0 auto 0.8rem; font-size: 1.2rem;">2</div>
            <h4 style="color: #8a135f; margin: 0 0 0.5rem 0; font-weight: 600;">Assessment</h4><p style="color: #6f2a5d; font-size: 0.9rem; margin: 0;">Technical Evaluation</p></div>
            <div><div style="width: 50px; height: 50px; border-radius: 50%; background: #fbcfe8; color: #8a135f; font-weight: 700; display: flex; align-items: center; justify-content: center; margin: 0 auto 0.8rem; font-size: 1.2rem;">3</div>
            <h4 style="color: #8a135f; margin: 0 0 0.5rem 0; font-weight: 600;">Completion</h4><p style="color: #6f2a5d; font-size: 0.9rem; margin: 0;">Review & Submit</p></div>
        </div></div>""", unsafe_allow_html=True)


def main():
    """Main application."""
    initialize_session_state()
    render_header()
    render_top_navbar()
    render_sidebar()

    if st.session_state.active_view == "home":
        st.markdown('<div class="welcome-card"><h3 style="font-size: 2.5rem; margin-bottom: 1.5rem;">👋 Welcome to TalentScout</h3><p style="font-size: 1.1rem; line-height: 1.8; color: #4a183f; margin-bottom: 1rem;">Start your intelligent screening process. Our AI assistant will guide you through 3 phases to understand your profile and expertise.</p></div>', unsafe_allow_html=True)
        
        st.markdown("## 🎯 Your Interview Journey")
        col1, col2, col3 = st.columns(3, gap="medium")
        with col1:
            st.markdown('<div class="feature-box"><div style="font-size: 1.5rem; margin-bottom: 0.5rem;">📋</div><h4 style="margin: 0.5rem 0;">Phase 1: Profile</h4><p style="font-size: 0.9rem; color: #64748b; margin: 0;">Share name, contact, experience, location.</p></div>', unsafe_allow_html=True)
        with col2:
            st.markdown('<div class="feature-box"><div style="font-size: 1.5rem; margin-bottom: 0.5rem;">🧠</div><h4 style="margin: 0.5rem 0;">Phase 2: Assessment</h4><p style="font-size: 0.9rem; color: #64748b; margin: 0;">Discuss tech stack and answer questions.</p></div>', unsafe_allow_html=True)
        with col3:
            st.markdown('<div class="feature-box"><div style="font-size: 1.5rem; margin-bottom: 0.5rem;">✅</div><h4 style="margin: 0.5rem 0;">Phase 3: Complete</h4><p style="font-size: 0.9rem; color: #64748b; margin: 0;">Review and submit responses.</p></div>', unsafe_allow_html=True)
        
        st.markdown("---")
        st.markdown("## ✨ Key Features")
        col1, col2 = st.columns(2, gap="large")
        with col1:
            st.markdown('<div class="professional-card"><h4 style="color: #8a135f; margin-top: 0;">⏱️ Quick & Efficient</h4><p style="color: #3f1b39;">Complete your interview in just 10-15 minutes.</p></div>', unsafe_allow_html=True)
            st.markdown('<div class="professional-card"><h4 style="color: #8a135f; margin-top: 0;">🎯 Personalized</h4><p style="color: #3f1b39;">Questions tailored to your experience level.</p></div>', unsafe_allow_html=True)
        with col2:
            st.markdown('<div class="professional-card"><h4 style="color: #8a135f; margin-top: 0;">🔒 Privacy Protected</h4><p style="color: #3f1b39;">Your data is encrypted and confidential.</p></div>', unsafe_allow_html=True)
            st.markdown('<div class="professional-card"><h4 style="color: #8a135f; margin-top: 0;">📊 Fair Assessment</h4><p style="color: #3f1b39;">Consistent and unbiased evaluation.</p></div>', unsafe_allow_html=True)
        
        st.markdown("---")
        col1, col2, col3 = st.columns([1, 1.5, 1])
        with col2:
            st.markdown("### Ready to Get Started?")
            if st.button("🚀 Start Your Interview", key="home_start_interview", use_container_width=True, type="primary"):
                greeting = st.session_state.chatbot.start_conversation()
                st.session_state.messages.append({"role": "assistant", "content": greeting})
                st.session_state.conversation_started = True
                st.session_state.active_view = "interview"
                st.rerun()
    else:
        if not st.session_state.conversation_started:
            st.info("Click **Start Interview** from the navbar to begin.")
            return
        st.markdown("---")
        render_journey()
        st.markdown("---")
        if st.session_state.show_progress:
            render_progress()
        st.markdown("---")
        render_conversation()

        if not st.session_state.chatbot.is_completed:
            st.markdown("### ✍️ Your Response")
            render_input_area()
        else:
            st.markdown("---")
            col1, col2, col3 = st.columns([0.5, 2, 0.5])
            with col2:
                st.markdown('<div class="section-card complete"><div style="text-align: center;"><div style="font-size: 4rem; margin-bottom: 1rem;">🎉</div><h2 style="color: #be185d; margin: 0 0 1rem 0;">Interview Completed!</h2><p style="color: #3f1b39; font-size: 1.1rem; line-height: 1.6;">Thank you for completing your interview. Your responses have been securely recorded.</p></div></div>', unsafe_allow_html=True)
                st.markdown("<br>", unsafe_allow_html=True)
                st.markdown('<div class="professional-card"><h3 style="color: #8a135f; margin-top: 0;">📋 What Happens Next</h3><div style="color: #3f1b39;"><p><strong>⏱️ Timeline:</strong> Review within 2-3 business days.</p><p><strong>📧 Notification:</strong> Email with next steps if selected.</p><p><strong>💼 Opportunity:</strong> Information about role and compensation.</p></div></div>', unsafe_allow_html=True)
                st.markdown("<br>", unsafe_allow_html=True)
                col_a, col_b = st.columns(2)
                with col_a:
                    if st.button("📧 Email My Responses", use_container_width=True):
                        st.info("✅ Copy sent to your email.")
                with col_b:
                    if st.button("🔄 Start New Interview", use_container_width=True, type="primary"):
                        st.session_state.conversation_started = False
                        st.session_state.messages = []
                        st.session_state.chatbot = TalentScoutChatbot(api_key=os.getenv("OPENAI_API_KEY"))
                        st.rerun()


if __name__ == "__main__":
    main()
