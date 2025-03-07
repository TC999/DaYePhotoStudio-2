import streamlit as st
import os

def turnimg_fuction(list):
    from PIL import Image
    files = list[0]
    output_path = list[1]
    mode = list[2]
    process_bar = st.progress(0)
    if mode == "左转90度":
        mode = 0
    elif mode == "右转90度":
        mode = 1
    elif mode == "180度":
        mode = 2 
    elif mode == "水平翻转":
        mode = 3
    elif mode == "垂直翻转":
        mode = 4
        
    with st.spinner("正在修改尺寸..."):
        for file in files:
            input_path = file
            output_path = output_path.replace("\\", "/")
            #output_file_path = output_path + "/" + os.path.splitext(os.path.basename(file))[0] + "." + form
            # 按照原格式保存
            print(list)
            output_file_path = output_path + "/" + os.path.basename(file)
            if mode == 0:
                #左转90度
                # 读取图像文件
                img = Image.open(input_path)
                # 将图像左转90度
                rotated_img = img.rotate(90, expand=True)
                # 保存旋转后的图像
                rotated_img.save(output_file_path)
                process_bar.progress((files.index(file) + 1) / len(files))
            elif mode == 1:
                #右转90
                # 读取图像文件
                img = Image.open(input_path)
                # 将图像左转90度
                rotated_img = img.rotate(-90, expand=True)
                # 保存旋转后的图像
                rotated_img.save(output_file_path)
                process_bar.progress((files.index(file) + 1) / len(files))
            elif mode == 2:
                #180
                # 读取图像文件
                img = Image.open(input_path)
                # 将图像左转90度
                rotated_img = img.rotate(180, expand=True)
                # 保存旋转后的图像
                rotated_img.save(output_file_path)
                process_bar.progress((files.index(file) + 1) / len(files))
            elif mode == 3:
                #左右翻转
                # 读取图像文件
                img = Image.open(input_path)
                # 将图像左右翻转
                flipped_img = img.transpose(Image.FLIP_LEFT_RIGHT)
                # 保存翻转后的图像
                flipped_img.save(output_file_path)
                process_bar.progress((files.index(file) + 1) / len(files))
            else:
                #上下翻转
                # 读取图像文件
                img = Image.open(input_path)
                # 将图像上下翻转
                flipped_img = img.transpose(Image.FLIP_TOP_BOTTOM)
                # 保存翻转后的图像
                flipped_img.save(output_file_path)
                process_bar.progress((files.index(file) + 1) / len(files))

    st.success("图片尺寸更改成功！")
    # 清空缓存temp_uploads
    os.system("rd /s /q temp_uploads")            