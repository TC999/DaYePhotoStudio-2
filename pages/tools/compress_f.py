import streamlit as st
import os

def compress_fuction(list):
    from PIL import Image
    files = list[0]
    output_path = list[1]
    process_bar = st.progress(0)
    with st.spinner("正在压缩图片..."):
        for file in files:
            output_path = output_path.replace("\\", "/")
            output_file_path = output_path + "/" + os.path.splitext(os.path.basename(file))[0] + ".jpg"
            img = Image.open(file)
            img.save(output_file_path, optimize=True, quality=50)
            img.close()
            process_bar.progress((files.index(file) + 1) / len(files))    

    st.success("图片压缩成功！")
    # 清空缓存temp_uploads
    os.system("rd /s /q temp_uploads")

'''      
这个功能我考虑了好久到底要不要把它单独拿出来[严肃],
因为实现它只需要两行简单的代码[笑哭]。
但是在很多平台上，这个功能都需要收智商税[再笑哭]。
对于厚颜无耻的狗资本家，我已经无语了。
画个让代码显得不那么空荡[doge]

 *                    _ooOoo_
 *                   o8888888o
 *                   88" . "88
 *                   (| -_- |)
 *                    O\ = /O
 *                ____/`---'\____
 *              .   ' \\| |// `.
 *               / \\||| : |||// \
 *             / _||||| -:- |||||- \
 *               | | \\\ - /// | |
 *             | \_| ''\---/'' | |
 *              \ .-\__ `-` ___/-. /
 *           ___`. .' /--.--\ `. . __
 *        ."" '< `.___\_<|>_/___.' >'"".
 *       | | : `- \`.;`\ _ /`;.`/ - ` : | |
 *         \ \ `-. \_ __\ /__ _/ .-` / /
 * ======`-.____`-.___\_____/___.-`____.-'======
 *                    `=---='
 *
 * .............................................
 '''