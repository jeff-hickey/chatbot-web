import streamlit as st
from openai import OpenAI
import os

openai_api_key = os.getenv("OPENAI_API_KEY")
print(openai_api_key)

with st.sidebar:
    # openai_api_key = st.text_input("OpenAI API Key", key="", type="password")
    "[![Open in GitHub Codespaces](https://github.com/codespaces/badge.svg)](https://codespaces.new/jeff-hickey/chatbot-web?quickstart=1)"
    # "[Team Three Presentation](https://docs.google.com/presentation/d/1Vq_Ya4rfMQS8H4ZXq9hFsPCMIlDVWwev_M2-6UEccCU/edit?usp=sharing)"
    # "[Chat with Your Data](https://docs.google.com/document/d/1Q94i7sC2rOP9nFRDOo_uEGntvBbdDxom2CfHNZYURjQ/edit?usp=sharing)"
st.title("💬 Customer Service Chatbot")

if "messages" not in st.session_state:
    st.session_state["messages"] = [{"role": "assistant", "content": "How can I help you?"}]

for msg in st.session_state.messages:
    st.chat_message(msg["role"]).write(msg["content"])

if prompt := st.chat_input():
    if not openai_api_key:
        st.info("Please add your OpenAI API key to continue.")
        st.stop()

    client = OpenAI(api_key=openai_api_key)
    st.session_state.messages.append({"role": "user", "content": prompt})
    st.chat_message("user").write(prompt)
    response = client.chat.completions.create(model="gpt-3.5-turbo-0125", messages=st.session_state.messages)
    msg = response.choices[0].message.content
    st.session_state.messages.append({"role": "assistant", "content": msg})
    st.chat_message("assistant").write(msg)
