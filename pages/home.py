import streamlit as st
import os
import ctypes

from pages.tools import koutu_f
from pages.tools import compress_f
from pages.tools import transformer
from pages.tools import size_f
from pages.tools import toSVG_f
from pages.tools import turner
from pages.tools import pluser

st.header("君子喻于义，小人喻于利。")

type=[
    "jpg", "jpeg", "png", "gif", "bmp", "tiff", "webp", "svg", "ico", "heic", "heif"
]

uploaded_files = st.file_uploader("选择文件", type=type, accept_multiple_files=True)
options = ["抠图","图片压缩","去水印", "超分放大","格式转换","批量改尺寸","位图转SVG","图像旋转","批量重命名","图像纵向拼接"]
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

# wxpython 选择文件
def select_files():
    import wx
    app = wx.App()
    dialog = wx.FileDialog(None, "选择文件", style=wx.FD_OPEN | wx.FD_MULTIPLE)
    if dialog.ShowModal() == wx.ID_OK:
        paths = dialog.GetPaths()
    else:
        paths = []
    dialog.Destroy()
    return paths

# wxpython 选择单个文件夹
def select_folder():
    import wx
    app = wx.App()
    dialog = wx.DirDialog(None, "选择文件夹", style=wx.DD_DEFAULT_STYLE)
    if dialog.ShowModal() == wx.ID_OK:
        path = dialog.GetPath()
    else:
        path = ""
    dialog.Destroy()
    return path

def select_output_folder():
    output_path = select_folder()
    # 将输出路径覆盖式保存到temp_output_path.txt文件中
    with open("temp_output_path.txt", "w") as f:
        f.write(output_path)
def get_output_path():
    # 从temp_output_path.txt文件中读取输出路径
    if os.path.exists("temp_output_path.txt"):
        with open("temp_output_path.txt", "r") as f:
            output_path = f.read()
        return output_path
 
if selected_option == "抠图":
    if uploaded_files:
        u2net_files = [os.path.splitext(f)[0] for f in os.listdir('.u2net') if os.path.isfile(os.path.join('.u2net', f))]
        selected_mode_option = st.selectbox("选择模型", u2net_files)
        mode = st.selectbox("选择抠图模式", ["仅抠图", "抠图并替换背景色","抠图并替换背景图"])
        # 调色板
        color = st.color_picker("选择背景色(仅在模式二有效)", "#000000")
        # 背景图
        background_image = st.file_uploader("选择背景图(仅在模式三有效)", type=type, accept_multiple_files=False)
        # output_path = st.text_input("输出路径", output_path)        
        if st.button("选择输出路径"):
            output_path = select_output_folder()
        output_path = get_output_path()
        if output_path == "":
            output_path = "output"
            st.write("输出路径", output_path)  
        else:
            pass  

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
        #output_path = st.text_input("输出路径", output_path) 
        if st.button("选择输出路径"):
            output_path = select_output_folder()
        output_path = get_output_path()
        if output_path == "":
            output_path = "output"
            st.write("输出路径", output_path)  
        else:
            pass  
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
        #output_path = st.text_input("输出路径", output_path)
        if st.button("选择输出路径"):
            output_path = select_output_folder()
        output_path = get_output_path()
        if output_path == "":
            output_path = "output"
            st.write("输出路径", output_path)  
        else:
            pass  
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
        #output_path = st.text_input("输出路径", output_path)
        if st.button("选择输出路径"):
            output_path = select_output_folder()
        output_path = get_output_path()
        if output_path == "":
            output_path = "output"
            st.write("输出路径", output_path)  
        else:
            pass  
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
        #output_path = st.text_input("输出路径", output_path) 
        if st.button("选择输出路径"):
            output_path = select_output_folder()
        output_path = get_output_path()
        if output_path == "":
            output_path = "output"
            st.write("输出路径", output_path)  
        else:
            pass  
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

if selected_option == "图像旋转":
    if uploaded_files:
        #output_path = st.text_input("输出路径", output_path)
        if st.button("选择输出路径"):
            output_path = select_output_folder()
        output_path = get_output_path()
        if output_path == "":
            output_path = "output"
            st.write("输出路径", output_path)  
        else:
            pass  
        st.write("选择的文件：", file_paths)
        # 可供选择的模式
        type = ["左转90度", "右转90度","180度", "水平翻转", "垂直翻转"]
        selected_type_option = st.selectbox("选择模式", type)
        st.write("输出路径：", output_path)
        list = []
        list.append(file_paths)
        list.append(output_path)
        list.append(selected_type_option)
        if st.button("开始转换"):
            turner.turnimg_fuction(list)
            file_paths.clear()
            list.clear()
    else:
        st.write("请选择文件")

if selected_option == "批量重命名":
    st.title("⚠敬请期待>_<")
    # 重命名文件前缀
    front = st.text_input("请输入目标文件名前缀(选填)")
    # 重命名文件后缀
    end = st.text_input("请输入目标文件名后缀(选填)")
    # 起始序号(数字选择器)
    start = st.number_input("请输入起始序号", min_value=-10000, max_value=10000, value=1)
    # 示例
    st.write(f"示例：{front}{start}{end}")
    list = []
    list.append(file_paths)
    list.append(front)
    list.append(end)
    list.append(start)
    if st.button("开始重命名"):
        print(list)
        #turner.rename_fuction(list)
        file_paths.clear()
        list.clear()

if selected_option == "图像纵向拼接":
    if uploaded_files:
        #output_path = st.text_input("输出路径", output_path) 
        if st.button("选择输出路径"):
            output_path = select_output_folder()
        output_path = get_output_path()
        if output_path == "":
            output_path = "output"
            st.write("输出路径", output_path)  
        else:
            pass  
        st.write("选择的文件：", file_paths)
        st.write("输出路径：", output_path)
        list = []
        list.append(file_paths)
        list.append(output_path)
        if st.button("开始执行"):
            pluser.plus_fuction(list)
            file_paths.clear()
            list.clear()
    else:
        st.write("请选择文件")