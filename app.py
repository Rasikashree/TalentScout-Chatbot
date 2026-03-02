"""
Streamlit UI for TalentScout Hiring Assistant Chatbot
Clean, intuitive interface for candidate interactions
"""

import streamlit as st
import os
from dotenv import load_dotenv
from src.chatbot import TalentScoutChatbot

# Load environment variables
load_dotenv()

# Page configuration
st.set_page_config(
    page_title="TalentScout - Hiring Assistant",
    page_icon="🤖",
    layout="wide",
    initial_sidebar_state="collapsed",
)

# Custom CSS for better styling
st.markdown(
    """
    <style>
    .main-header {
        color: #1f77b4;
        text-align: center;
        padding: 20px 0;
        border-bottom: 2px solid #1f77b4;
        margin-bottom: 20px;
    }
    .info-box {
        background-color: #f0f8ff;
        border-left: 4px solid #1f77b4;
        padding: 15px;
        border-radius: 4px;
        margin: 10px 0;
    }
    .progress-bar-container {
        width: 100%;
        height: 8px;
        background-color: #e0e0e0;
        border-radius: 4px;
        overflow: hidden;
        margin: 10px 0;
    }
    .progress-bar-fill {
        height: 100%;
        background-color: #1f77b4;
        transition: width 0.3s ease;
    }
    .message-user {
        background-color: #e3f2fd;
        padding: 10px 15px;
        border-radius: 8px;
        margin: 8px 0;
        border-left: 4px solid #1f77b4;
    }
    .message-assistant {
        background-color: #f5f5f5;
        padding: 10px 15px;
        border-radius: 8px;
        margin: 8px 0;
        border-left: 4px solid #4caf50;
    }
    .button-container {
        display: flex;
        gap: 10px;
        margin: 20px 0;
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
    """Render the application header."""
    st.markdown(
        """
        <div class="main-header">
            <h1>🤖 TalentScout</h1>
            <p style="color: #666; font-size: 16px;">Intelligent Hiring Assistant for Technology Placements</p>
        </div>
        """,
        unsafe_allow_html=True,
    )


def render_progress():
    """Render conversation progress."""
    if not st.session_state.show_progress:
        return

    progress = st.session_state.chatbot.get_progress()

    col1, col2, col3 = st.columns(3)

    with col1:
        st.metric(
            "Stage",
            progress["stage"].replace("_", " ").title(),
        )

    with col2:
        info_progress = f"{progress['information_gathered']}/{progress['information_total']}"
        st.metric("Information", info_progress)

    with col3:
        question_progress = f"{progress['questions_answered']}/{progress['questions_total']}"
        st.metric("Questions", question_progress)


def render_conversation():
    """Render the conversation history."""
    st.subheader("💬 Conversation")

    # Display messages
    message_container = st.container()

    for i, message in enumerate(st.session_state.messages):
        if message["role"] == "user":
            with message_container:
                st.markdown(
                    f'<div class="message-user"><strong>You:</strong> {message["content"]}</div>',
                    unsafe_allow_html=True,
                )
        else:
            with message_container:
                st.markdown(
                    f'<div class="message-assistant"><strong>TalentScout Assistant:</strong> {message["content"]}</div>',
                    unsafe_allow_html=True,
                )


def render_input_area():
    """Render the input area and handle user interaction."""
    col1, col2 = st.columns([4, 1])

    with col1:
        user_input = st.text_input(
            "Your response:",
            key="user_input",
            placeholder="Type your response here...",
        )

    with col2:
        send_button = st.button("Send", key="send_button", use_container_width=True)

    if send_button and user_input:
        # Add user message to display
        st.session_state.messages.append({"role": "user", "content": user_input})

        # Process with chatbot
        response, should_end = st.session_state.chatbot.process_user_input(user_input)

        # Add assistant response to display
        st.session_state.messages.append({"role": "assistant", "content": response})

        # Clear input
        st.rerun()


def render_sidebar():
    """Render the sidebar with information and controls."""
    with st.sidebar:
        st.title("📊 Session Info")

        candidate_info = st.session_state.chatbot.get_candidate_info()

        st.subheader("Gathered Information")
        if candidate_info:
            for key, value in candidate_info.items():
                if key == "tech_stack" and isinstance(value, list):
                    st.write(f"**{key.replace('_', ' ').title()}:** {', '.join(value)}")
                else:
                    st.write(f"**{key.replace('_', ' ').title()}:** {value}")
        else:
            st.info("No information gathered yet. Start the conversation to begin!")

        st.divider()

        # Controls
        st.subheader("Controls")
        col1, col2 = st.columns(2)

        with col1:
            if st.button("Show/Hide Progress"):
                st.session_state.show_progress = not st.session_state.show_progress

        with col2:
            if st.button("Show/Hide Info"):
                st.session_state.show_info = not st.session_state.show_info

        # About
        st.divider()
        st.subheader("About")
        st.info(
            """
            🏢 **TalentScout** is an AI-powered hiring assistant designed to streamline the initial screening process for technology professionals.
            
            **Features:**
            - Intelligent candidate information gathering
            - Dynamic technical question generation
            - Context-aware conversations
            - Professional and friendly interactions
            """
        )

        # Instructions
        st.subheader("Instructions")
        st.markdown(
            """
            1. **Start the conversation** by clicking the button below
            2. **Answer questions** about yourself and your background
            3. **Share your tech stack** when asked
            4. **Respond to technical questions** to assess your proficiency
            5. **Type 'exit' or 'goodbye'** to end the conversation gracefully
            """
        )


def main():
    """Main application logic."""
    initialize_session_state()
    render_header()

    # Sidebar
    render_sidebar()

    # Main content
    if not st.session_state.conversation_started:
        st.markdown(
            """
            <div class="info-box">
                <h3>👋 Welcome to TalentScout!</h3>
                <p>This is an intelligent hiring assistant designed to help us get to know you better and assess your technical skills.</p>
                <p><strong>What to expect:</strong></p>
                <ul>
                    <li>We'll ask for your background information (name, contact, experience)</li>
                    <li>You'll tell us about your technical skills</li>
                    <li>We'll ask 3-5 tailored technical questions</li>
                    <li>The whole process takes about 10-15 minutes</li>
                </ul>
            </div>
            """,
            unsafe_allow_html=True,
        )

        if st.button("🚀 Start Conversation", use_container_width=True):
            # Start conversation
            greeting = st.session_state.chatbot.start_conversation()
            st.session_state.messages.append({"role": "assistant", "content": greeting})
            st.session_state.conversation_started = True
            st.rerun()
    else:
        # Show progress
        if st.session_state.show_progress:
            render_progress()

        # Show conversation
        render_conversation()

        # Show input area if not completed
        if not st.session_state.chatbot.is_completed:
            st.divider()
            render_input_area()
        else:
            st.success("✅ Thank you for completing the interview!")
            st.info(
                "Your responses have been recorded. You will hear from us within 5-7 business days."
            )

            if st.button("🔄 Start New Conversation"):
                st.session_state.conversation_started = False
                st.session_state.messages = []
                st.session_state.chatbot = TalentScoutChatbot(
                    api_key=os.getenv("OPENAI_API_KEY")
                )
                st.rerun()


if __name__ == "__main__":
    main()
