<div align=center>
<img src="logo.png" width="150" height="150">

<h1>DaYe PhotoStudio-2</h1>

<a href="https://dyblog.online/"><img src="https://img.shields.io/badge/Author-DaYe-orange" alt="Author" /></a>
<img src="https://img.shields.io/github/languages/count/darkmatter2048/DaYePhotoStudio-2" alt="languages-count" />
<img src="https://img.shields.io/github/languages/top/darkmatter2048/DaYePhotoStudio-2?color=yellow" alt="languages-top" />
<img src="https://img.shields.io/github/last-commit/darkmatter2048/DaYePhotoStudio-2" alt="last-commit" />

<h3>完全开源免费的图像处理软件！</h3>
</div>

## 🎨 运行截图 GUI
![show](resource/show.png)

<details>
<summary>
功能列表 🧾
</summary>

- [x] 扣图
- [x] 图片压缩
- [ ] 表格识别
- [ ] 清晰放大
- [x] 位图转矢量
- [x] 修改尺寸
- [ ] 批量重命名
- [x] 格式转换
- [x] 拆分GIF
- [x] 合成GIF
- [ ] 批量打印
- [x] 图片拼接
- [x] 图像旋转
- [x] 圆角裁剪

</details>

## 🖥 支持的操作系统

- <img src="resource/windows.svg" width="16" height="16" />Windows 10,11


## 📦 下载
<a href="https://pan.quark.cn/s/b42aabae0e5f"><img src="resource/2ms.png"></img></a>

## 本地运行
环境要求：Python 3.8+

1. 克隆仓库
```bash
  git clone https://github.com/darkmatter2048/DaYePhotoStudio-2.git
```

2. 安装依赖
```bash
  pip install -r requirements.txt
```

3. 启动应用（自动通过默认浏览器打开）
```bash
  python launcher.py
```

## 📦 应用打包
推荐使用高性能虚拟环境工具 **uv**

1. 安装工具链
```bash
  pip install uv
```

2. 创建并激活虚拟环境
```bash
uv venv
# Windows
.\.venv\Scripts\activate
```

<!--
# macOS/Linux
source .venv/bin/activate
-->

3. 安装打包依赖
```bash
  uv pip install -r requirements.txt -U pyinstaller==5.13.2
```

4. 生成可执行文件
```bash
  uv run pyinstaller -D -i icon.ico launcher.py
```

5. 部署资源文件
将以下内容手动复制至 `dist/launcher` 目录：
- `app.py`
- `pages` 目录
- 其他依赖文件（详见 [note.txt](note.txt)）

生成的可执行文件位于 `dist/launcher` 目录

## 📝未来计划 Future Ideas

- [ ] 增加局域网网盘功能
- [ ] 完善设置功能
- [ ] 支持更多语言

## 🎖 贡献者 Contributors

<a href="https://github.com/darkmatter2048/DaYePhotoStudio-2/graphs/contributors">
  <img src="https://contrib.rocks/image?repo=darkmatter2048/DaYePhotoStudio-2" />
</a>

## 🤝支持DaYePhotoStudio-2的开发

[<img src="https://wc.dyblog.online/images/d.png" alt="Develop Image" style="width: 200px;"/>](https://dyblog.online/donate)

## ⭐ 星标历史 Star History

<a href="https://star-history.com/#darkmatter2048/DaYePhotoStudio-2&Date">
 <picture>
   <source media="(prefers-color-scheme: dark)" srcset="https://api.star-history.com/svg?repos=darkmatter2048/DaYePhotoStudio-2&type=Date&theme=dark" />
   <source media="(prefers-color-scheme: light)" srcset="https://api.star-history.com/svg?repos=darkmatter2048/DaYePhotoStudio-2&type=Date" />
   <img alt="Star History Chart" src="https://api.star-history.com/svg?repos=darkmatter2048/DaYePhotoStudio-2&type=Date" />
 </picture>
</a>

## Copyright & License ⚖

Copyright © 2021.DaYe

<p xmlns:cc="http://creativecommons.org/ns#" xmlns:dct="http://purl.org/dc/terms/"><a property="dct:title" rel="cc:attributionURL" href=#>DaYePhotoStudio-2</a> by <a rel="cc:attributionURL dct:creator" property="cc:attributionName" href="https://www.dyblog.online/">DaYe</a> is licensed under <a href="https://creativecommons.org/licenses/by-nc-sa/4.0/?ref=chooser-v1" target="_blank" rel="license noopener noreferrer" style="display:inline-block;">CC BY-NC-SA 4.0<img style="height:22px!important;margin-left:3px;vertical-align:text-bottom;" src="https://mirrors.creativecommons.org/presskit/icons/cc.svg?ref=chooser-v1" alt=""><img style="height:22px!important;margin-left:3px;vertical-align:text-bottom;" src="https://mirrors.creativecommons.org/presskit/icons/by.svg?ref=chooser-v1" alt=""><img style="height:22px!important;margin-left:3px;vertical-align:text-bottom;" src="https://mirrors.creativecommons.org/presskit/icons/nc.svg?ref=chooser-v1" alt=""><img style="height:22px!important;margin-left:3px;vertical-align:text-bottom;" src="https://mirrors.creativecommons.org/presskit/icons/sa.svg?ref=chooser-v1" alt=""></a></p>
