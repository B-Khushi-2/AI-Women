import streamlit as st
import google.generativeai as genai

# Configure Gemini API using Streamlit secrets
# Ensure you have your GOOGLE_API_KEY set in Streamlit Cloud secrets
# For local development, you might set it as an environment variable or a .streamlit/secrets.toml file
genai.configure(api_key=st.secrets["GOOGLE_API_KEY"])

model = genai.GenerativeModel("gemini-2.5-flash")

# Configure page
st.set_page_config(
    page_title="Welcome to your AI Learning Buddy Khushi",
    page_icon="💡",
    layout="wide",
    menu_items={'About': None, 'Report a bug': None, 'Get help': None}
)

st.markdown("<h1 style='text-align: center; color: #FF6347;'>✨Welcome to Khushi's AI Learning Buddy ✨</h1>", unsafe_allow_html=True)
st.markdown("<h3 style='text-align: center; color: #1E90FF;'>Unlock new knowledge with Khushi! 🚀</h3>", unsafe_allow_html=True)

st.write(" ফরিদ آباد-")

# Use columns for a more dynamic input layout
col1, col2 = st.columns(2)

with col1:
    topic = st.text_input("📚 What topic do you want to explore?", placeholder="e.g., Artificial Intelligence, Photosynthesis")

with col2:
    option = st.selectbox(
        "🧠 Choose your learning adventure!",
        [
            "Explain Concept",
            "Real-Life Example",
            "Generate Quiz",
            "Ask Anything"
        ],
        help="Select how you want Khushi to help you learn."
    )

st.write("\n") # Add some space

if st.button("💡 Let's Learn!", use_container_width=True, type="primary"):

    if not topic:
        st.error("⚠️ Please enter a topic to start your learning journey!")
    else:
        # Modified spinner message
        with st.spinner("🧠 Khushi is thinking..."):
            if option == "Explain Concept":
                prompt = f"Explain {topic} in simple, engaging language for a beginner, providing a clear overview and highlighting key takeaways." # Enhanced prompt

            elif option == "Real-Life Example":
                prompt = f"Provide one creative, relatable real-life example of {topic} that a beginner can easily understand and visualize." # Enhanced prompt

            elif option == "Generate Quiz":
                prompt = f"Generate 5 challenging multiple-choice questions on {topic} with four distinct options for each, followed by the correct answers and a brief explanation for each answer." # Enhanced prompt

            else:
                prompt = topic # For 'Ask Anything', directly use the topic as prompt

            try:
                response = model.generate_content(prompt)
                st.markdown("### Your Learning Output:")
                st.markdown(response.text) # Use markdown for better formatting
            except Exception as e:
                st.error(f"🚨 An error occurred while generating content: {e}")
                st.info("💡 Don't worry! Try again or rephrase your topic/question. The AI might be having a moment.")
        st.markdown("</div>", unsafe_allow_html=True)

st.write(" ফরিদ آباد-")
st.markdown("<footer><p style='text-align: center; color: #808080;'>Made by Khushi Borde. Always cross-reference with reliable sources for critical information. Happy Learning! ✨</p></footer>", unsafe_allow_html=True)
