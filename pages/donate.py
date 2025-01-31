import streamlit as st

# 隐藏右上角的按钮
hide_streamlit_style = """
    <style>
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
    </style>
    """
st.markdown(hide_streamlit_style, unsafe_allow_html=True)

st.title("捐赠")
st.write("这是一个简单的图像处理软件示例。")