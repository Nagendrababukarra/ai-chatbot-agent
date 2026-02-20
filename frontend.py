import streamlit as st
import requests
from datetime import datetime

# PAGE CONFIG
st.set_page_config(
    page_title="AI Agent Pro",
    page_icon="🤖",
    layout="wide"
)

# CUSTOM CSS (Professional Look)

st.markdown("""
<style>
.main-title {
    font-size: 42px;
    font-weight: 700;
    text-align: center;
    margin-bottom: 10px;
}
.sub-title {
    text-align: center;
    color: gray;
    margin-bottom: 30px;
}
.block-container {
    padding-top: 2rem;
}
.chat-container {
    border-radius: 15px;
    padding: 20px;
}
.footer {
    text-align: center;
    color: gray;
    font-size: 12px;
    margin-top: 40px;
}
</style>
""", unsafe_allow_html=True)

# HEADER

st.markdown('<div class="main-title">🤖 AI Chatbot Agent Pro</div>', unsafe_allow_html=True)
st.markdown('<div class="sub-title">Groq / OpenAI Powered | LangGraph + FastAPI</div>', unsafe_allow_html=True)

API_URL = "https://ai-chatbot-agent.onrender.com/chat"

# SIDEBAR CONFIGURATION

with st.sidebar:
    st.header("⚙ Agent Configuration")

    system_prompt = st.text_area(
        "System Prompt",
        placeholder="Define AI personality...",
        height=120
    )

    provider = st.radio("Select Provider", ["Groq", "OpenAI"])

    MODELS = {
        "Groq": ["llama-3.3-70b-versatile", "mixtral-8x7b-32768"],
        "OpenAI": ["gpt-4o-mini"]
    }

    selected_model = st.selectbox("Select Model", MODELS[provider])

    allow_web_search = st.checkbox("Allow Web Search")

    st.divider()

    if st.button("🧹 Clear Chat"):
        st.session_state.chat_history = []

# SESSION STATE
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []


# DISPLAY CHAT HISTORY

for chat in st.session_state.chat_history:
    with st.chat_message(chat["role"]):
        st.markdown(chat["content"])
        st.caption(chat["time"])


# USER INPUT

user_query = st.chat_input("Type your message...")

if user_query:

    timestamp = datetime.now().strftime("%H:%M")

    # Add user message
    st.session_state.chat_history.append({
        "role": "user",
        "content": user_query,
        "time": timestamp
    })

    with st.chat_message("user"):
        st.markdown(user_query)
        st.caption(timestamp)

    payload = {
        "model_name": selected_model,
        "model_provider": provider,
        "system_prompt": system_prompt,
        "messages": [user_query],
        "allow_search": allow_web_search
    }

    try:
        with st.spinner("🤖 Thinking..."):
            response = requests.post(API_URL, json=payload)

        if response.status_code == 200:
            response_data = response.json()

            if isinstance(response_data, dict) and "error" in response_data:
                assistant_reply = response_data["error"]
            else:
                assistant_reply = response_data

        else:
            assistant_reply = f"⚠ Error {response.status_code}: {response.text}"

    except requests.exceptions.ConnectionError:
        assistant_reply = "Backend is not running. Start FastAPI server."

    # Add assistant message
    timestamp = datetime.now().strftime("%H:%M")

    st.session_state.chat_history.append({
        "role": "assistant",
        "content": assistant_reply,
        "time": timestamp
    })

    with st.chat_message("assistant"):
        st.markdown(assistant_reply)
        st.caption(timestamp)


# FOOTER

st.markdown(
    '<div class="footer">Built with LangGraph • FastAPI • Streamlit</div>',
    unsafe_allow_html=True
)