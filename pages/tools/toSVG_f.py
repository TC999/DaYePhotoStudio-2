import streamlit as st
import os

def toSVG_fuction(list):
    from PIL import Image
    files = list[0]
    output_path = list[1]
    process_bar = st.progress(0)
    with st.spinner("正在转换..."):
        for file in files:
            output_path = output_path.replace("\\", "/")
            outfile = output_path + "/" + os.path.splitext(os.path.basename(file))[0] + "." + "svg"  
            image = Image.open(file).convert('RGBA')
            data = image.load()
            width, height = image.size
            out = open(outfile, "w")
            out.write('<?xml version="1.0" encoding="UTF-8" standalone="no"?>\n')
            out.write('<svg id="svg2" xmlns="http://www.w3.org/2000/svg" version="1.1" \
                        width="%(x)i" height="%(y)i" viewBox="0 0 %(x)i %(y)i">\n' % \
                    {'x': width, 'y': height})

            for y in range(height):
                for x in range(width):
                    rgba = data[x, y]
                    rgb = '#%02x%02x%02x' % rgba[:3]
                    if rgba[3] > 0:
                        out.write('<rect width="1" height="1" x="%i" y="%i" fill="%s" \
                            fill-opacity="%.2f" />\n' % (x, y, rgb, rgba[3] / 255.0))
            out.write('</svg>\n')
            out.close()

            process_bar.progress((files.index(file) + 1) / len(files))  

    st.success("图片转换成功！")
    # 清空缓存temp_uploads
    os.system("rd /s /q temp_uploads")