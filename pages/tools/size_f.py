import streamlit as st
import os

def size_fuction(list):
    from PIL import Image
    files = list[0]
    output_path = list[1]
    width = int(list[2])
    height = int(list[3])
    process_bar = st.progress(0)
    with st.spinner("正在修改尺寸..."):
        for file in files:
            output_path = output_path.replace("\\", "/")
            #output_file_path = output_path + "/" + os.path.splitext(os.path.basename(file))[0] + "." + form
            # 按照原格式保存
            print(list)
            output_file_path = output_path + "/" + os.path.basename(file)
            # 修改尺寸
            img = Image.open(file)
            img = img.resize((width, height))  # Use Resampling.LANCZOS
            img.save(output_file_path)
            process_bar.progress((files.index(file) + 1) / len(files))    

    st.success("图片尺寸更改成功！")
    # 清空缓存temp_uploads
    os.system("rd /s /q temp_uploads")
