import streamlit as st
from utils import get_chat_response
from langchain.memory import ConversationBufferMemory

st.title("我的chatgpt")


# with st.sidebar:
#     mobile = st.text_input("请输入你的手机号")
#     st.info("*******************")
if "memory" not in st.session_state:
    st.session_state["memory"] = ConversationBufferMemory(return_messages=True)
    st.session_state["messages"] = [{"role":"ai",
                                     "content":"你好，我是你的小助手，有什么可以帮你的吗"}]
for message in st.session_state["messages"]:
    st.chat_message(message["role"]).write(message["content"])

prompt = st.chat_input()
if prompt:
    st.session_state["messages"].append({"role":"human", "content":prompt})
    st.chat_message("human").write(prompt)

    with st.spinner("生成中,请稍等"):
        response = get_chat_response(prompt, st.session_state["memory"])

    msg = {"role":"ai",
           "content": response}
    st.session_state["messages"].append(msg)
    st.chat_message("ai").write(response)