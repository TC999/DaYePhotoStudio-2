import streamlit as st
import os

from pages.tools import koutu_f
from pages.tools import compress_f
from pages.tools import transformer
from pages.tools import size_f
from pages.tools import toSVG_f

st.header("君子喻于义，小人喻于利。")

type=[
    "jpg", "jpeg", "png", "gif", "bmp", "tiff", "webp", "svg", "ico", "heic", "heif"
]

uploaded_files = st.file_uploader("选择文件", type=type, accept_multiple_files=True)
options = ["抠图","图片压缩","去水印", "超分放大","格式转换","批量改尺寸","位图转SVG"]
selected_option = st.selectbox("选择功能", options)

# 创建一个临时目录来保存上传的文件
temp_dir = "temp_uploads"
if not os.path.exists(temp_dir):
    os.makedirs(temp_dir)

# 保存上传的文件并获取它们的完整路径
file_paths = []
for uploaded_file in uploaded_files:
    file_path = os.path.join(temp_dir, uploaded_file.name)
    with open(file_path, "wb") as f:
        f.write(uploaded_file.getbuffer())
    file_paths.append(file_path)

output_path = "output"


if selected_option == "抠图":
    if uploaded_files:
        u2net_files = [os.path.splitext(f)[0] for f in os.listdir('.u2net') if os.path.isfile(os.path.join('.u2net', f))]
        selected_mode_option = st.selectbox("选择模型", u2net_files)
        mode = st.selectbox("选择抠图模式", ["仅抠图", "抠图并替换背景色","抠图并替换背景图"])
        # 调色板
        color = st.color_picker("选择背景色(仅在模式二有效)", "#000000")
        # 背景图
        background_image = st.file_uploader("选择背景图(仅在模式三有效)", type=type, accept_multiple_files=False)
        output_path = st.text_input("输出路径", output_path)        
        # 收集到的信息
        st.write("选择的文件：", file_paths)
        st.write("选择的模型：", selected_mode_option)
        st.write("选择的抠图模式：", mode)
        st.write("选择的背景色：", color)
        st.write("选择的背景图：", background_image)
        st.write("输出路径：", output_path)
        list = []
        list.append(file_paths)
        list.append(selected_mode_option)
        list.append(mode)
        list.append(color)
        list.append(background_image)
        list.append(output_path)
        if st.button("开始抠图"):
            koutu_f.koutu_fuction(list)
            # 清空列表
            file_paths.clear()
            list.clear()
    else:
        st.write("请选择文件")

if selected_option == "图片压缩":
    if uploaded_files:
        output_path = st.text_input("输出路径", output_path) 
        st.write("选择的文件：", file_paths)
        st.write("输出路径：", output_path)
        list = []
        list.append(file_paths)
        list.append(output_path)
        if st.button("开始压缩"):
            compress_f.compress_fuction(list)
            file_paths.clear()
            list.clear()
    else:
        st.write("请选择文件")

if selected_option == "去水印":
    st.write("敬请期待>_<")

if selected_option == "超分放大":
    st.write("敬请期待>_<")

if selected_option == "格式转换":
    if uploaded_files:
        output_path = st.text_input("输出路径", output_path)
        st.write("选择的文件：", file_paths)
        # 可供选择的格式
        type = ["jpg", "jpeg", "png", "gif", "bmp", "tiff", "webp", "svg", "ico", "heic", "heif"]
        selected_type_option = st.selectbox("选择格式", type)
        st.write("输出路径：", output_path)
        list = []
        list.append(file_paths)
        list.append(output_path)
        list.append(selected_type_option)
        if st.button("开始转换"):
            transformer.transformer_fuction(list)
            file_paths.clear()
            list.clear()

if selected_option == "批量改尺寸":            
    if uploaded_files:
        output_path = st.text_input("输出路径", output_path)
        st.write("选择的文件：", file_paths)
        # 选择尺寸
        width = st.number_input("宽度", min_value=0, max_value=10000, value=1000)
        height = st.number_input("高度", min_value=0, max_value=10000, value=1000)      
        st.write("输出路径：", output_path)
        list = []
        list.append(file_paths)
        list.append(output_path)
        list.append(width)
        list.append(height)
        if st.button("开始处理"):
            size_f.size_fuction(list)
            file_paths.clear()
            list.clear()

if selected_option == "位图转SVG":
    if uploaded_files:
        output_path = st.text_input("输出路径", output_path) 
        st.write("选择的文件：", file_paths)
        st.write("输出路径：", output_path)
        list = []
        list.append(file_paths)
        list.append(output_path)
        if st.button("开始压缩"):
            toSVG_f.toSVG_fuction(list)
            file_paths.clear()
            list.clear()
    else:
        st.write("请选择文件")