import streamlit as st
from utils import  generate_script

st.title("🎬 视频脚本生成器")

with st.sidebar:
    st.text_input("请输入秘钥",type="password")
    st.markdown("[获取openai秘钥](https://www.baidu.com)")

subject = st.text_input("💡 请输入视频的主题")
video_length = st.number_input("请输入视频的时长",min_value=0.1, step=0.1)
creativity = st.slider("请输入视频的创造力",min_value=0.0, max_value=1.0, value=0.2, step = 0.1)
submit= st.button("一键生成")

if submit and not subject:
    st.info("请输入视频的主题")
    st.stop()
if submit and not video_length >= 0.1:
    st.info("视频长度需要大于或等于0.1")
    st.stop()
if submit:
    with st.spinner("ai正在思考,请稍等"):
        search_result, title, script =  generate_script(subject, video_length, creativity)
    st.success("视频脚本已生成！")
    st.subheader("🔥标题:")
    st.write(title)
    st.subheader("🏠 视频脚本:")
    st.write(script)
    with st.expander("维基百科搜索结果👁"):
        st.info(search_result)