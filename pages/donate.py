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
st.markdown("""
### 支持DaYe的开源工作 ❤️
- [爱发电](https://afdian.com/a/donate_daye)
- [微信赞赏](https://dyblog.online/assets/wechatpay.jpg) *(China)*
- [B站充电](https://space.bilibili.com/1847808902?from=dyblog.online)
### 慈善捐赠❤️
- [哔哩哔哩公益](https://love.bilibili.com/?from=dyblog.online)
    
""")