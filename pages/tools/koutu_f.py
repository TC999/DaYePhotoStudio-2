'''
mklink
清空缓存
'''
import streamlit as st
import os

def koutu_fuction(list):
    from PIL import Image
    from rembg import remove, new_session

    # 获取当前用户的用户名
    username = os.getlogin()
    # 拼接user/username文件夹的路径
    user_folder = os.path.join("C:\\Users", username)
    # 拼接.u2net文件夹的路径
    u2net_folder = os.path.join(user_folder, ".u2net")
    # 判断.u2net文件夹是否存在
    if not os.path.exists(u2net_folder):
        # 创建.u2net文件夹
        os.mkdir(u2net_folder)
        # mklink到程序目录下的.u2net文件夹
        # os.system("mklink /D " + u2net_folder + " .u2net")
        # 将.u2net文件夹下的所有文件复制到user/username/.u2net文件夹下
        os.system("xcopy .u2net " + u2net_folder + " /e /h /i /y")

    files = list[0]
    mode = list[1]
    way = list[2]
    color = list[3]
    background_image = list[4]
    output_path = list[5]

    process_bar = st.progress(0)

    # 加载模型
    session = new_session(mode)

    with st.spinner("正在处理..."):
        for file in files:
            # 将output_path的\改为/
            output_path = output_path.replace("\\", "/")
            input_path = file
            # 将文件以png格式保存到output_path
            output_file_path = output_path + "/" + os.path.splitext(os.path.basename(file))[0] + ".png"
            input = Image.open(input_path)
            st.write("正在处理：" + file)
            if way == "仅抠图":
                # 使用模型抠图
                output = remove(input, session=session)
                output.save(output_file_path)
            elif way == "抠图并替换背景色":
                # 使用模型抠图,并替换背景色（#000000）
                # 先将背景色转换为RGBA格式
                color = color.lstrip('#')
                color = tuple(int(color[i:i+2], 16) for i in (0, 2, 4))
                color = color + (255,)
                output = remove(input,session=session, bgcolor=color)
                output.save(output_file_path)
            elif way == "抠图并替换背景图":
                original_image = input
                background_image = Image.open(background_image)
                # 调整替换背景图像的尺寸，使其与原始图像尺寸匹配
                background_image = background_image.resize(original_image.size)
                # 将原始图像和替换背景图像转换为RGBA模式
                original_image = original_image.convert("RGBA")
                background_image = background_image.convert("RGBA")
                # 使用rembg库对原始图像进行背景去除处理
                #session = new_session(model_name)
                bg_removed_image = remove(original_image, session=session)
                # 将去除背景的图像与调整后的替换背景图像进行合并
                merged_image = Image.alpha_composite(background_image, bg_removed_image)
                # 保存合并后的图像
                merged_image.save(output_file_path)

            process_bar.progress((files.index(file) + 1) / len(files))    

    st.success("图片抠图成功")
    # 清空缓存temp_uploads
    os.system("rd /s /q temp_uploads")

