import streamlit as st
from langchain.memory import ConversationBufferMemory
from utils import call_with_stream

# Streamlit 应用
st.title("海科chat")

with st.sidebar:
    mobile = st.text_input("请输入你的手机号")
    if not mobile:
        st.warning("请先输入你的手机号以开始对话。")

if "user_memories" not in st.session_state:
    st.session_state["user_memories"] = {}

if mobile not in st.session_state["user_memories"]:
    st.session_state["user_memories"][mobile] = {
        "memory": ConversationBufferMemory(return_messages=True),
        "messages": [{"role": "ai", "content": "你好,我是你的小助手,有什么可以帮你的吗"}]
    }

user_memory = st.session_state["user_memories"][mobile]["memory"]
user_messages = st.session_state["user_memories"][mobile]["messages"]

# 展示之前的聊天记录
for message in user_messages:
    st.chat_message(message["role"]).write(message["content"])

prompt = st.chat_input("请输入你的问题")
if prompt:
    # 将用户的输入添加到消息列表中
    user_messages.append({"role": "human", "content": prompt})
    st.chat_message("human").write(prompt)

    # 将用户的提问保存到内存中
    user_memory.chat_memory.add_message({"role": "user", "content": prompt})  # 更新内存


    # 调用流式响应，传递历史消息和用户输入
    response_generator = call_with_stream(prompt, user_memory)

    # 创建一个占位符
    placeholder = st.empty()

    response_text = ""
    for chunk in response_generator:
        response_text += chunk
        # 使用占位符更新内容，而不是重复调用 write()
        # Format the response text
        formatted_text = response_text.replace("\n", "<br>")  # Replace newlines with HTML line breaks
        placeholder.markdown(formatted_text, unsafe_allow_html=True)  # 实时更新消息

    # 将完整的响应添加到会话中
    user_messages.append({"role": "ai", "content": response_text})  # 将AI的响应添加到消息列表
    user_memory.chat_memory.add_message({"role": "ai", "content": response_text})  # 更新内存