import streamlit as st
from backend import graph

st.set_page_config(page_title="LangGraph Chatbot", page_icon="🤖")
st.title("🤖 LangGraph Streaming Chatbot")

if "message_history" not in st.session_state:
    st.session_state.message_history = []

for message in st.session_state.message_history:
    with st.chat_message(message["role"]):
        st.write(message["content"])

user_input = st.chat_input("Type your message here...")

if user_input:
    st.session_state.message_history.append({"role": "user", "content": user_input})

    with st.chat_message("user"):
        st.write(user_input)

    with st.chat_message("assistant"):
        response_placeholder = st.empty()
        full_response = ""

        for chunk in graph.stream(
            {"messages": [{"role": "user", "content": user_input}]},
            stream_mode="values"
        ):
            last_message = chunk["messages"][-1]
            if hasattr(last_message, "content") and last_message.content:
                full_response = last_message.content
                response_placeholder.write(full_response)

        response_placeholder.write(full_response)

    st.session_state.message_history.append({"role": "assistant", "content": full_response})

if st.button("🗑️ Clear Chat"):
    st.session_state.message_history = []
    st.rerun()
