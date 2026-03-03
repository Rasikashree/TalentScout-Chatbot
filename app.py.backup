"""
TalentScout - Professional Hiring Assistant Interface
Modern, attractive UI for candidate screening
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

# Professional Custom CSS
st.markdown(
    """
    <style>
    /* Import Google Fonts */
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&family=Poppins:wght@400;500;600;700&display=swap');
    
    /* Color Variables */
    :root {
        --primary: #0f172a;
        --primary-light: #1e293b;
        --primary-lighter: #334155;
        --accent: #0d9488;
        --accent-light: #06b6d4;
        --accent-dark: #0f6942;
        --success: #16a34a;
        --text-dark: #1e293b;
        --text-light: #475569;
        --bg-light: #f8fafc;
        --border-light: #e2e8f0;
    }
    
    /* Global Styles */
    * {
        font-family: 'Inter', sans-serif;
    }
    
    /* Main Background with Professional Navy Gradient */
    .stApp {
        background: linear-gradient(135deg, #0f172a 0%, #1e293b 50%, #064e3b 100%);
    }
    
    /* Main Content Area */
    .main .block-container {
        padding: 2rem 3rem;
        max-width: 1400px;
        background: #ffffff;
        border-radius: 16px;
        box-shadow: 0 20px 60px rgba(15, 23, 42, 0.15);
        border: 1px solid #e2e8f0;
    }
    
    /* Header Section */
    .main-header {
        background: linear-gradient(135deg, #0f172a 0%, #1e293b 100%);
        color: white;
        text-align: center;
        padding: 3.5rem 2rem;
        border-radius: 16px;
        margin-bottom: 2rem;
        box-shadow: 0 15px 40px rgba(15, 23, 42, 0.2);
        border: 1px solid rgba(255, 255, 255, 0.1);
    }
    
    .main-header h1 {
        font-family: 'Poppins', sans-serif;
        font-size: 3.5rem;
        font-weight: 700;
        margin: 0;
        background: linear-gradient(135deg, #ffffff 0%, #06b6d4 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        background-clip: text;
    }
    
    .main-header p {
        font-size: 1.1rem;
        margin-top: 0.8rem;
        color: #cbd5e1;
        font-weight: 400;
    }
    
    /* Welcome Card */
    .welcome-card {
        background: linear-gradient(135deg, #0f172a 0%, #1e293b 100%);
        color: white;
        padding: 2.5rem;
        border-radius: 16px;
        margin: 1.5rem 0;
        box-shadow: 0 12px 35px rgba(15, 23, 42, 0.15);
        border: 1px solid rgba(13, 148, 136, 0.2);
    }
    
    .welcome-card h3 {
        font-family: 'Poppins', sans-serif;
        font-size: 2rem;
        margin-bottom: 1rem;
        color: #06b6d4;
    }
    
    .welcome-card p {
        color: #cbd5e1;
        line-height: 1.6;
    }
    
    /* Info Box */
    .info-box {
        background: linear-gradient(135deg, #f0fdfa 0%, #ecfdf5 100%);
        color: #0f172a;
        border-left: 4px solid #0d9488;
        padding: 2rem;
        border-radius: 12px;
        margin: 1.5rem 0;
        box-shadow: 0 8px 20px rgba(13, 148, 136, 0.1);
    }
    
    .info-box h3 {
        font-family: 'Poppins', sans-serif;
        margin-top: 0;
        color: #0d9488;
        font-size: 1.3rem;
    }
    
    .info-box p, .info-box li {
        color: #475569;
        font-weight: 500;
    }
    
    /* Progress Metrics */
    .metric-card {
        background: linear-gradient(135deg, #ffffff 0%, #f8fafc 100%);
        padding: 1.8rem;
        border-radius: 12px;
        box-shadow: 0 4px 12px rgba(15, 23, 42, 0.08);
        border: 1px solid #e2e8f0;
        border-left: 4px solid #0d9488;
        transition: all 0.3s ease;
    }
    
    .metric-card:hover {
        transform: translateY(-4px);
        box-shadow: 0 12px 30px rgba(13, 148, 136, 0.15);
        border-left-color: #06b6d4;
    }
    
    /* Chat Messages */
    .message-user {
        background: linear-gradient(135deg, #0f172a 0%, #1e293b 100%);
        color: white;
        padding: 1.3rem 1.6rem;
        border-radius: 16px 16px 4px 16px;
        margin: 1rem 0;
        margin-left: 15%;
        box-shadow: 0 4px 15px rgba(15, 23, 42, 0.2);
        animation: slideInRight 0.3s ease;
        border: 1px solid rgba(255, 255, 255, 0.1);
    }
    
    .message-assistant {
        background: linear-gradient(135deg, #f0fdfa 0%, #ecfdf5 100%);
        color: #0f172a;
        padding: 1.3rem 1.6rem;
        border-radius: 16px 16px 16px 4px;
        margin: 1rem 0;
        margin-right: 15%;
        box-shadow: 0 4px 15px rgba(13, 148, 136, 0.15);
        animation: slideInLeft 0.3s ease;
        border: 1px solid rgba(13, 148, 136, 0.2);
    }
    
    .message-user strong {
        display: block;
        margin-bottom: 0.5rem;
        font-weight: 700;
        font-size: 0.95rem;
        color: #06b6d4;
    }
    
    .message-assistant strong {
        display: block;
        margin-bottom: 0.5rem;
        font-weight: 700;
        font-size: 0.95rem;
        color: #0d9488;
    }
    
    /* Animations */
    @keyframes slideInRight {
        from {
            opacity: 0;
            transform: translateX(40px);
        }
        to {
            opacity: 1;
            transform: translateX(0);
        }
    }
    
    @keyframes slideInLeft {
        from {
            opacity: 0;
            transform: translateX(-40px);
        }
        to {
            opacity: 1;
            transform: translateX(0);
        }
    }
    
    /* Buttons */
    .stButton > button {
        background: linear-gradient(135deg, #0d9488 0%, #0f6942 100%);
        color: white;
        border: none;
        padding: 0.8rem 2.2rem;
        border-radius: 8px;
        font-weight: 600;
        font-size: 1rem;
        box-shadow: 0 4px 12px rgba(13, 148, 136, 0.3);
        transition: all 0.3s ease;
        text-transform: uppercase;
        letter-spacing: 0.5px;
    }
    
    .stButton > button:hover {
        transform: translateY(-2px);
        box-shadow: 0 8px 20px rgba(13, 148, 136, 0.4);
        background: linear-gradient(135deg, #06b6d4 0%, #0d9488 100%);
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
        border-color: #0d9488 !important;
        box-shadow: 0 0 0 4px rgba(13, 148, 136, 0.1);
    }
    
    .stTextInput > div > div > input::placeholder {
        color: #94a3b8;
    }
    
    /* Sidebar */
    [data-testid="stSidebar"] {
        background: linear-gradient(180deg, #0f172a 0%, #1e293b 100%);
    }
    
    [data-testid="stSidebar"] * {
        color: #e2e8f0 !important;
    }
    
    [data-testid="stSidebar"] .stMarkdown {
        color: #e2e8f0;
    }
    
    [data-testid="stSidebar"] h1, 
    [data-testid="stSidebar"] h2,
    [data-testid="stSidebar"] h3 {
        color: #06b6d4;
    }
    
    /* Success/Info Boxes */
    .stSuccess {
        background: linear-gradient(135deg, #f0fdf4 0%, #e8f5e9 100%) !important;
        border-left: 4px solid #16a34a !important;
        border-radius: 8px;
        padding: 1rem;
        color: #15803d !important;
    }
    
    .stInfo {
        background: linear-gradient(135deg, #f0fdfa 0%, #ecfdf5 100%) !important;
        border-left: 4px solid #0d9488 !important;
        border-radius: 8px;
        padding: 1rem;
        color: #0f6942 !important;
    }
    
    .stWarning {
        background: linear-gradient(135deg, #fffbeb 0%, #fef3c7 100%) !important;
        border-left: 4px solid #d97706 !important;
        border-radius: 8px;
        padding: 1rem;
        color: #b45309 !important;
    }
    
    /* Divider */
    hr {
        margin: 2rem 0;
        border: none;
        height: 1px;
        background: linear-gradient(90deg, transparent, #e2e8f0, transparent);
    }
    
    /* Metric Values */
    [data-testid="stMetricValue"] {
        font-size: 2.2rem;
        font-weight: 700;
        color: #0d9488;
    }
    
    /* Section Headers */
    h2, h3 {
        font-family: 'Poppins', sans-serif;
        color: #0f172a;
        font-weight: 600;
    }
    
    h2 {
        border-bottom: 2px solid #0d9488;
        padding-bottom: 0.5rem;
    }
    
    /* Conversation Container */
    .conversation-container {
        background: #f8fafc;
        padding: 2rem;
        border-radius: 12px;
        margin: 1.5rem 0;
        max-height: 600px;
        overflow-y: auto;
        border: 1px solid #e2e8f0;
    }
    
    /* Scrollbar */
    .conversation-container::-webkit-scrollbar {
        width: 8px;
    }
    
    .conversation-container::-webkit-scrollbar-track {
        background: #f1f5f9;
        border-radius: 10px;
    }
    
    .conversation-container::-webkit-scrollbar-thumb {
        background: linear-gradient(180deg, #0d9488 0%, #06b6d4 100%);
        border-radius: 10px;
    }
    
    .conversation-container::-webkit-scrollbar-thumb:hover {
        background: linear-gradient(180deg, #0f6942 0%, #0d9488 100%);
    }
    
    /* Badge */
    .badge {
        display: inline-block;
        padding: 0.4rem 0.9rem;
        border-radius: 20px;
        font-size: 0.85rem;
        font-weight: 600;
        background: linear-gradient(135deg, #0d9488 0%, #06b6d4 100%);
        color: white;
        margin: 0.3rem;
        box-shadow: 0 2px 8px rgba(13, 148, 136, 0.2);
    }
    
    /* Card Hover Effects */
    .hover-card {
        transition: all 0.3s ease;
    }
    
    .hover-card:hover {
        transform: translateY(-5px);
        box-shadow: 0 15px 35px rgba(13, 148, 136, 0.15);
    }
    </style>
    """,
    unsafe_allow_html=True,
)


def initialize_session_state():
    """Initialize Streamlit session state variables."""
    if "chatbot" not in st.session_state:
        api_key = os.getenv("OPENAI_API_KEY")
        if not api_key:
            st.error(
                "⚠️ OpenAI API key not found. Please set the OPENAI_API_KEY environment variable."
            )
            st.stop()

        st.session_state.chatbot = TalentScoutChatbot(api_key=api_key)
        st.session_state.conversation_started = False
        st.session_state.messages = []

    if "show_progress" not in st.session_state:
        st.session_state.show_progress = True

    if "show_info" not in st.session_state:
        st.session_state.show_info = True


def render_header():
    """Render the professional application header."""
    st.markdown(
        """
        <div class="main-header">
            <h1>💼 TalentScout</h1>
            <p>AI-Powered Intelligent Hiring Assistant for Technology Professionals</p>
        </div>
        """,
        unsafe_allow_html=True,
    )


def render_progress():
    """Render conversation progress with modern design."""
    if not st.session_state.show_progress:
        return

    progress = st.session_state.chatbot.get_progress()
    
    st.markdown("### 📊 Progress Overview")
    
    col1, col2, col3, col4 = st.columns(4)

    with col1:
        st.markdown('<div class="metric-card">', unsafe_allow_html=True)
        st.metric(
            "📍 Current Stage",
            progress["stage"].replace("_", " ").title(),
        )
        st.markdown('</div>', unsafe_allow_html=True)

    with col2:
        info_progress = f"{progress['information_gathered']}/{progress['information_total']}"
        percentage = (progress['information_gathered'] / progress['information_total'] * 100) if progress['information_total'] > 0 else 0
        st.markdown('<div class="metric-card">', unsafe_allow_html=True)
        st.metric("📋 Information Collected", info_progress, f"{percentage:.0f}%")
        st.markdown('</div>', unsafe_allow_html=True)

    with col3:
        question_progress = f"{progress['questions_answered']}/{progress['questions_total']}"
        q_percentage = (progress['questions_answered'] / progress['questions_total'] * 100) if progress['questions_total'] > 0 else 0
        st.markdown('<div class="metric-card">', unsafe_allow_html=True)
        st.metric("❓ Questions Answered", question_progress, f"{q_percentage:.0f}%")
        st.markdown('</div>', unsafe_allow_html=True)
    
    with col4:
        status = "✅ Complete" if progress['is_completed'] else "⏳ In Progress"
        st.markdown('<div class="metric-card">', unsafe_allow_html=True)
        st.metric("Status", status)
        st.markdown('</div>', unsafe_allow_html=True)
    
    st.markdown("<br>", unsafe_allow_html=True)


def render_conversation():
    """Render the conversation history with modern chat interface."""
    st.markdown("### 💬 Chat History")
    
    st.markdown('<div class="conversation-container">', unsafe_allow_html=True)

    # Display messages
    for i, message in enumerate(st.session_state.messages):
        if message["role"] == "user":
            st.markdown(
                f'''<div class="message-user">
                    <strong>👤 You</strong>
                    <div>{message["content"]}</div>
                </div>''',
                unsafe_allow_html=True,
            )
        else:
            st.markdown(
                f'''<div class="message-assistant">
                    <strong>🤖 TalentScout AI</strong>
                    <div>{message["content"]}</div>
                </div>''',
                unsafe_allow_html=True,
            )
    
    st.markdown('</div>', unsafe_allow_html=True)


def render_input_area():
    """Render professional input area with modern styling."""
    # Input container with styling
    st.markdown('<div class="input-container">', unsafe_allow_html=True)

    with st.form(key="chat_input_form", clear_on_submit=True):
        col1, col2 = st.columns([5, 1])

        with col1:
            user_input = st.text_input(
                "Your response:",
                key="user_input",
                placeholder="💭 Type your response here...",
                label_visibility="collapsed",
            )

        with col2:
            send_button = st.form_submit_button(
                "📤 Send", use_container_width=True, type="primary"
            )

        if send_button and user_input:
            st.session_state.messages.append({"role": "user", "content": user_input})

            with st.spinner("🤔 Analyzing your response..."):
                response, should_end = st.session_state.chatbot.process_user_input(user_input)

            st.session_state.messages.append({"role": "assistant", "content": response})
        elif send_button and not user_input:
            st.warning("⚠️ Please enter a response before sending.")

    st.markdown('</div>', unsafe_allow_html=True)


def render_sidebar():
    """Render the sidebar with professional design."""
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
            st.info("🚀 Start the conversation to begin collecting candidate information!")

        st.markdown("---")

        # Controls
        st.markdown("### ⚙️ View Controls")
        
        if st.button("👁️ Toggle Progress", use_container_width=True):
            st.session_state.show_progress = not st.session_state.show_progress
            st.rerun()

        if st.button("📝 Toggle Details", use_container_width=True):
            st.session_state.show_info = not st.session_state.show_info
            st.rerun()

        st.markdown("---")
        
        # About
        st.markdown("### ℹ️ About TalentScout")
        st.markdown(
            """
            **TalentScout** is an advanced AI-powered recruitment assistant that streamlines 
            the initial screening process for technology professionals.
            
            **🎯 Key Features:**
            - 🧠 Intelligent conversation flow
            - 📊 Dynamic question generation
            - 🎓 Experience-level adaptation
            - 🔒 Privacy-first data handling
            - ⚡ Real-time assessment
            """
        )

        st.markdown("---")
        
        # Quick Guide
        st.markdown("### 📖 Quick Guide")
        st.markdown(
            """
            **Step 1:** Click 'Start Conversation'
            
            **Step 2:** Provide your professional details
            
            **Step 3:** Share your tech stack
            
            **Step 4:** Answer technical questions
            
            **Step 5:** Review and submit
            
            💡 **Tip:** Type 'exit', 'goodbye', or 'quit' to end anytime
            """
        )
        
        st.markdown("---")
        st.markdown("**Powered by OpenAI GPT-3.5**")
        st.markdown("*Version 1.0 - March 2026*")


def main():
    """Main application with professional interface."""
    initialize_session_state()
    render_header()

    # Sidebar
    render_sidebar()

    # Main content
    if not st.session_state.conversation_started:
        # Welcome Screen
        st.markdown(
            """
            <div class="welcome-card">
                <h3>👋 Welcome to TalentScout AI Hiring Assistant!</h3>
                <p style="font-size: 1.1rem; margin-top: 1rem;">
                We're excited to learn more about you and your technical expertise. 
                This intelligent assistant will guide you through a personalized screening process.
                </p>
            </div>
            """,
            unsafe_allow_html=True,
        )
        
        col1, col2, col3 = st.columns([1, 2, 1])
        with col2:
            st.markdown(
                """
                <div class="info-box">
                    <h3>📋 What to Expect</h3>
                    <p><strong>Duration:</strong> 10-15 minutes</p>
                    <br>
                    <p><strong>Phase 1: Profile Information</strong><br>
                    We'll collect your basic professional details including name, contact, experience, and location.</p>
                    <br>
                    <p><strong>Phase 2: Technical Assessment</strong><br>
                    Share your tech stack and answer 3-5 customized technical questions based on your skills.</p>
                    <br>
                    <p><strong>Phase 3: Review</strong><br>
                    We'll inform you about the next steps in the hiring process.</p>
                </div>
                """,
                unsafe_allow_html=True,
            )
            
            st.markdown("<br>", unsafe_allow_html=True)
            
            if st.button("🚀 Start Your Interview", use_container_width=True, type="primary"):
                # Start conversation
                greeting = st.session_state.chatbot.start_conversation()
                st.session_state.messages.append({"role": "assistant", "content": greeting})
                st.session_state.conversation_started = True
                st.rerun()
                
            st.markdown("<br>", unsafe_allow_html=True)
            
            # Features showcase
            feat_col1, feat_col2, feat_col3 = st.columns(3)
            with feat_col1:
                st.markdown("### 🎯")
                st.markdown("**Personalized**")
                st.caption("Questions tailored to your experience level")
            with feat_col2:
                st.markdown("### 🔒")
                st.markdown("**Secure**")
                st.caption("Your data is anonymized and protected")
            with feat_col3:
                st.markdown("### ⚡")
                st.markdown("**Fast**")
                st.caption("Complete your screening in minutes")
                
    else:
        # Show progress
        if st.session_state.show_progress:
            render_progress()

        # Show conversation
        render_conversation()

        # Show input area if not completed
        if not st.session_state.chatbot.is_completed:
            st.markdown("---")
            st.markdown("### ✍️ Your Response")
            render_input_area()
        else:
            st.markdown("---")
            st.success("✅ **Interview Completed Successfully!**")
            
            col1, col2, col3 = st.columns([1, 2, 1])
            with col2:
                st.markdown(
                    """
                    <div class="info-box">
                        <h3>🎉 Thank You!</h3>
                        <p>Your interview has been recorded and our team will review your responses.</p>
                        <br>
                        <p><strong>Next Steps:</strong></p>
                        <ul>
                            <li>Our recruitment team will review your profile within 2-3 business days</li>
                            <li>If selected, you'll receive an email with next steps</li>
                            <li>We appreciate your time and interest in joining our team!</li>
                        </ul>
                    </div>
                    """,
                    unsafe_allow_html=True,
                )
                
                st.markdown("<br>", unsafe_allow_html=True)

                if st.button("🔄 Start New Interview", use_container_width=True, type="primary"):
                    st.session_state.conversation_started = False
                    st.session_state.messages = []
                    st.session_state.chatbot = TalentScoutChatbot(
                        api_key=os.getenv("OPENAI_API_KEY")
                    )
                    st.rerun()


if __name__ == "__main__":
    main()
