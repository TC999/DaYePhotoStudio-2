# 使用OOP和tkinter实现文件多选对话框
import tkinter as tk
from tkinter import filedialog

class FileDialog:
    def __init__(self, title, filetypes):
        self.root = tk.Tk()
        self.root.withdraw()  # 隐藏主窗口
        self.title = title
        self.filetypes = filetypes
        self.file_paths = []
        self.root.attributes('-topmost', True)  # 添加窗口置顶属性

    def open_dialog(self):
        self.root.deiconify()  # 显示窗口
        self.file_paths = filedialog.askopenfilenames(title=self.title, filetypes=self.filetypes)
        self.root.withdraw()  # 完成操作后再次隐藏
        return self.file_paths

    def close_dialog(self):
        self.root.destroy()  # 彻底销毁Tk实例