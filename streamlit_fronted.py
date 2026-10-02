import streamlit as st
from backend import graph

st.title("🤖 LangGraph Chatbot")

if "message_history" not in st.session_state:
    st.session_state.message_history = []

for message in st.session_state.message_history:
    with st.chat_message(message["role"]):
        st.write(message["content"])

user_input = st.chat_input("Type here...")

if user_input:
    st.session_state.message_history.append({"role": "user", "content": user_input})

    with st.chat_message("user"):
        st.write(user_input)

    with st.chat_message("assistant"):
        response_placeholder = st.empty()
        full_response = ""

        for chunk, metadata in graph.stream(
            {"messages": [{"role": "user", "content": user_input}]},
            stream_mode="messages"
        ):
            if hasattr(chunk, "content"):
                full_response += chunk.content
                response_placeholder.write(full_response + "▌")

        response_placeholder.write(full_response)

    st.session_state.message_history.append({"role": "assistant", "content": full_response})
