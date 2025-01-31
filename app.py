import streamlit as st

st.set_page_config(page_title="DaYe PhotoStudio", page_icon="logo.png", layout="centered", initial_sidebar_state="auto", menu_items=None)
# 隐藏右上角的按钮
hide_streamlit_style = """
    <style>
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
    </style>
    """
st.markdown(hide_streamlit_style, unsafe_allow_html=True)

page1 = st.Page("pages/home.py", title="🏠 主页")
page2 = st.Page("pages/settings.py", title="🛠️ 设置")
page3 = st.Page("pages/about.py", title="ℹ️ 关于")
page4 = st.Page("pages/donate.py", title="❤️ 捐赠")

pg = st.navigation([page1, page2, page3, page4])
pg.run()
