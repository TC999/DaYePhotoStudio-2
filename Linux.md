# 在 Linux 上运行
> [!warning]
>
> 请严格按照此文档操作，否则极易死机！

环境要求：Python 3.8+

1. 克隆仓库
```bash
  git clone https://github.com/darkmatter2048/DaYePhotoStudio-2.git
  cd DaYePhotoStudio-2
```

2. 在 Linux 上安装 wxPython
  - 首先你需要安装依赖：
    Debian/Ubuntu:
    ```bash
      sudo apt-get update
      sudo apt-get install libgtk-3-dev
      sudo apt-get install libjpeg-dev libtiff-dev libpng-dev libexpat1-dev   libpcre3-dev
      export PKG_CONFIG_PATH=/usr/lib/x86_64-linux-gnu/pkgconfig:$PKG_CONFIG_PATH
    ```
  - 打开[这个页面](https://extras.wxpython.org/wxPython4/extras/linux/gtk3),查找和系统及python 版本对应的 wxPython 版本，下载对应的 whl 文件，直接用`wget`命令下载
  - 导航到下载位置，安装 whl 文件
    ```bash
      pip install <下载文件名>.whl
    ```
3. 安装依赖
  ```bash
    pip install -r requirements.txt
  ```
4. 启动应用（自动通过默认浏览器打开）
  ```bash
    python launcher.py
  ```
