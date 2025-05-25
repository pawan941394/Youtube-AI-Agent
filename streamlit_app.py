import streamlit as st
import requests
from io import BytesIO
from PIL import Image
import os
from css import css_style
from agent import agent_int
# Create directories if they don't exist
os.makedirs("tmp", exist_ok=True)

# Set page config
st.set_page_config(
    page_title="Bharat AI Connect - YouTube Agent",
    page_icon="🎬",
    layout="wide",
)

# Apply custom CSS
st.markdown(css_style(), unsafe_allow_html=True)

# Functions for the sidebar
def display_sidebar():
    with st.sidebar:
        st.image("bharat.png", width=250)
        st.markdown("## Bharat AI Connect")
        st.markdown("### YouTube AI Assistant")
        st.markdown("---")
        st.markdown("""
        Our YouTube AI Assistant helps you:
        - Get video summaries
        - Answer questions about video content
        - Extract key insights from videos
        """)
        st.markdown("---")
        st.markdown("### Connect with us")
        st.markdown("[🌐 Website](https://bharataiconnect.com/)")
        st.markdown("[📺 YouTube Channel](https://www.youtube.com/channel/UClgbj0iYh5mqY_81CMCw25Q)")
        st.markdown("---")
        st.markdown("© 2025 Bharat AI Connect")

# Initialize the agent
@st.cache_resource
def initialize_agent():
    agent = agent_int()
    return agent

# Main application
def main():
    display_sidebar()
    
    # Header
    col1, col2 = st.columns([3, 1])
    with col1:
        st.markdown("<h1 class='main-header'>YouTube AI Assistant</h1>", unsafe_allow_html=True)
        st.markdown("Powered by Bharat AI Connect")
    with col2:
        
        st.image("https://cdn-icons-png.flaticon.com/512/1384/1384060.png", width=100)
    
    st.markdown("---")
    
    # Main container
    st.markdown("<div class='chat-container'>", unsafe_allow_html=True)
    
    # Initialize session state for chat history if it doesn't exist
    if 'messages' not in st.session_state:
        st.session_state.messages = []
    
    # Display chat messages
    for message in st.session_state.messages:
        if message["role"] == "user":
            st.markdown(f"<div class='user-message'><b>You:</b> {message['content']}</div>", unsafe_allow_html=True)
        else:
            st.markdown(f"<div class='bot-message'><b>AI Assistant:</b> {message['content']}</div>", unsafe_allow_html=True)
    
    # Input for YouTube URL/question
    user_input = st.text_input("Enter a YouTube URL or ask a question about a video", key="user_input")
    
    # Initialize the agent
    agent = initialize_agent()
    
    # Process input when submitted
    if st.button("Submit") and user_input:
        # Add user message to chat history
        st.session_state.messages.append({"role": "user", "content": user_input})
        
        # Get AI response
        with st.spinner("Processing your request..."):
            response = agent.run(user_input)
            response =response.content
          # Add AI response to chat history
        st.session_state.messages.append({"role": "assistant", "content": response})
        
        # Rerun to update the UI
        st.rerun()
    
    st.markdown("</div>", unsafe_allow_html=True)
    
    # Footer
    st.markdown("---")
    st.markdown("<center>Transforming Bharat with Intelligent AI</center>", unsafe_allow_html=True)

if __name__ == "__main__":
    main()
