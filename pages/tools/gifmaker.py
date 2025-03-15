import streamlit as st
import os

def makegif_fuction(list):
    from PIL import Image
    files = list[0]
    output_path = list[1]
    process_bar = st.progress(0)
    output_path = output_path.replace("\\", "/")
    # 创建一个新的GIF图像对象
    gif_path = f'{output_path}/output.gif'
    frames = []
    with st.spinner("正在合成GIF..."):
        for file in files:
            #处理
            img = Image.open(file)
            frames.append(img)
            process_bar.progress((files.index(file) + 1) / len(files))    

    # 保存帧到GIF图像中
    frames[0].save(gif_path, save_all=True, append_images=frames[1:], optimize=False, duration=100, loop=0)

    st.success("GIF合成成功！")
    # 清空缓存temp_uploads
    os.system("rd /s /q temp_uploads")