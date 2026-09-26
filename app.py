import streamlit as st

st.set_page_config(page_title="Pocket Smart AI", page_icon="🤖", layout="wide")

# Title
st.title("🤖 Pocket Smart AI")
st.markdown("Your personal AI assistant")

# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display chat history
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

# Chat input
if prompt := st.chat_input("Ask anything..."):
    # User message
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    # AI response (demo logic - you can connect OpenAI/Groq here later)
    with st.chat_message("assistant"):
        response = f"You said: **{prompt}**\n\nI am your Pocket Smart AI. I can help you with questions, writing, coding, and ideas. How can I help you further?"
        st.markdown(response)
    
    st.session_state.messages.append({"role": "assistant", "content": response})

# Sidebar
with st.sidebar:
    st.header("Pocket Smart AI")
    st.write("A simple and fast AI assistant.")
    if st.button("Clear Chat"):
        st.session_state.messages = []
        st.rerun()
