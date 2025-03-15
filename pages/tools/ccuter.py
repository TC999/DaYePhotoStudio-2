import streamlit as st
import os

def ccut_fuction(list):
    from PIL import Image, ImageDraw
    files = list[0]
    output_path = list[1]
    radii = list[2]
    process_bar = st.progress(0)
    with st.spinner("正在裁剪图片..."):
        for file in files:
            output_path = output_path.replace("\\", "/")
            file_name = os.path.basename(file)
            output_file = f'{output_path}/{file_name}.png'
            img = Image.open(file)
            # 画圆（用于分离4个角）
            circle = Image.new('L', (radii * 2, radii * 2), 0)  # 创建黑色方形
            draw = ImageDraw.Draw(circle)
            draw.ellipse((0, 0, radii * 2, radii * 2), fill=255)  # 黑色方形内切白色圆形

            img = img.convert("RGBA")
            w, h = img.size

            alpha = Image.new('L', img.size, 255)
            alpha.paste(circle.crop((0, 0, radii, radii)), (0, 0))  # 左上角
            alpha.paste(circle.crop((radii, 0, radii * 2, radii)),
                        (w - radii, 0))  # 右上角
            alpha.paste(circle.crop((radii, radii, radii * 2, radii * 2)),
                        (w - radii, h - radii))  # 右下角
            alpha.paste(circle.crop((0, radii, radii, radii * 2)),
                        (0, h - radii))  # 左下角

            img.putalpha(alpha)  # 白色区域透明可见，黑色区域不可见
            img.save(output_file, 'png', quality=100)
            process_bar.progress((files.index(file) + 1) / len(files))    

    st.success("图片裁剪成功！")
    # 清空缓存temp_uploads
    os.system("rd /s /q temp_uploads")