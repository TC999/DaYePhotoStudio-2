import streamlit as st
import os

def devidegif_fuction(list):
    from PIL import Image,ImageSequence
    files = list[0]
    output_path = list[1]
    process_bar = st.progress(0)
    with st.spinner("正在拆分GIF..."):
        for file in files:
            output_path = output_path.replace("\\", "/")
            #output_file_path = output_path + "/" + os.path.splitext(os.path.basename(file))[0] + ".jpg"
            gif_image = Image.open(file)
            # 获取GIF文件的名称
            gif_name = os.path.splitext(os.path.basename(file))[0]
            # 创建一个与GIF文件同名的文件夹
            os.makedirs(f'{output_path}/{gif_name}', exist_ok=True)
            # 拆分GIF文件的每一帧
            frames = [frame.copy() for frame in ImageSequence.Iterator(gif_image)]

            # 保存每一帧为单独的图片文件
            for i, frame in enumerate(frames):
                frame.save(f'{output_path}/{gif_name}/output_frame_{i}.png', format='PNG')

            process_bar.progress((files.index(file) + 1) / len(files))    

    st.success("GIF拆分成功！")
    # 清空缓存temp_uploads
    os.system("rd /s /q temp_uploads")