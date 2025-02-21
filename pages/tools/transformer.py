import streamlit as st
import os

def transformer_fuction(list):
    from PIL import Image
    files = list[0]
    output_path = list[1]
    form = list[2]
    process_bar = st.progress(0)
    with st.spinner("正在转换格式..."):
        for file in files:
            output_path = output_path.replace("\\", "/")
            output_file_path = output_path + "/" + os.path.splitext(os.path.basename(file))[0] + "." + form
            img = Image.open(file)
            # 转换格式
            img.save(output_file_path)
            process_bar.progress((files.index(file) + 1) / len(files))    

    st.success("图片格式转换成功！")
    # 清空缓存temp_uploads
    os.system("rd /s /q temp_uploads")