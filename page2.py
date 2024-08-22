import streamlit as st

st.radio("你的性别是什么",["男","女","跨性别"] ,index=1)

st.selectbox("你的性别是什么",["男","女","跨性别"] ,index=1)

st.multiselect("你的性别是什么",["男","女","跨性别"])

st.slider("传入字符串",value=100,max_value=1000)

upload_file = st.file_uploader("上传文件")
if upload_file:
    st.write(f"文件名称是{upload_file.name}")

with st.sidebar:
    st.text_input("请输入侧边栏的内容",key="3")
    with st.sidebar:
        st.text_input("nh", key="4")

c1, c2, c3 = st.columns([1,2,1])
with c1:
    st.multiselect("你的性别是什么", ["男", "女", "跨性别"], key="gender1")
with c2:
    st.multiselect("你的性别是什么", ["男", "女", "跨性别"], key="gender2")
with c3:
    st.multiselect("你的性别是什么", ["男", "女", "跨性别"], key="gender3")

tab1,tab2,tab3 = st.tabs(['11','22','33'])
with tab1:
    st.multiselect("你的性别是什么", ["男", "女", "跨性别"], key="gender11")
with tab2:
    st.multiselect("11", ["男", "女", "跨性别"], key="gender22")
with tab3:
    st.multiselect("333", ["男", "女", "跨性别"], key="gender33")

with st.expander("身高信息"):
    st.write("ghsdlgjkds")