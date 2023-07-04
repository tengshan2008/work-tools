from dataclasses import dataclass, field
from enum import Enum

import os
import streamlit as st

MODE = os.getenv("MODE", "FAQ")

class Role(Enum):
    SYSTEM = 0
    USER = 1
    ASSISTANT = 2


@dataclass
class Message:
    role: Enum
    content: str
    results: list = field(default_factory=list)


def get_system_prompt():
    return "How can I help?"


def response_from_llm():
    return "reponse_from_llm"


st.title("Chatbot")

# Initialize the chat messages history
# 初始化会话历史
if "messages" not in st.session_state.keys():
    if MODE == "FAQ":
        message = Message(Role.ASSISTANT, "How can I help?")
    else:
        message = Message(Role.SYSTEM, get_system_prompt())
    st.session_state.messages = [message]

# Display the existing chat messages
# 显示刷新对话记录
for message in st.session_state.messages:
    if message.role is Role.SYSTEM:
        continue
    with st.chat_message(message.role.name):
        st.markdown(message.content)
        if len(message.results) > 0:
            st.dataframe(message.results)

# Prompt for user input and save
# 将用户的输入作为提示词保存
if prompt := st.chat_input():
    # Add user message to chat history
    message = Message(Role.USER, prompt)
    st.session_state.messages.append(message)
    # Display user message in chat message container
    with st.chat_message(Role.USER.name):
        st.markdown(prompt)

    # Display assistant reponse in chat message container
    with st.chat_message(Role.ASSISTANT.name):
        with st.spinner("Thinking..."):
            resp_placeholder = st.empty()
            response = response_from_llm()
            resp_placeholder.markdown(response)

    # Add assistant response to chat history
    message = Message(Role.ASSISTANT, response)
    st.session_state.messages.append(message)
