import streamlit as st
import os

def plus_fuction(list):
    from PIL import Image
    somefiles = list[0]
    folder_path = list[1]

    images = [Image.open(path) for path in somefiles]

    # 计算拼接后的图片的宽度和高度
    max_width = max(i.width for i in images)
    total_height = sum(int(i.height * (max_width / i.width)) for i in images)

    # 创建一个新的空白图片，宽度为最大宽度，高度为所有图片高度之和
    new_image = Image.new('RGB', (max_width, total_height))

    # 将每张图片依次缩放并粘贴到新图片上
    y_offset = 0
    process_bar = st.progress(0)
    with st.spinner("正在合并图片..."):
        for image in images:
            new_height = int(image.height * (max_width / image.width))
            resized_image = image.resize((max_width, new_height))
            new_image.paste(resized_image, (0, y_offset))
            y_offset += new_height
            process_bar.progress((images.index(image) + 1) / len(images)) 

    # 保存拼接后的图片
    output_path = folder_path.replace("\\", "/")
    output_file_path = output_path + "/" + "result.jpg"
    new_image.save(f"{output_file_path}")
    st.success("图片拼接成功！")
    # 清空缓存temp_uploads
    os.system("rd /s /q temp_uploads")