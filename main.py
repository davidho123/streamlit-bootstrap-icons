import streamlit as st
import os
from cairosvg import svg2png
import io

# 设定SVG文件夹路径
svg_folder_path = 'bootstrap-icons/icons'

def svg_to_image(svg_file_path):
    """将SVG文件转换为PNG图像"""
    png_image = io.BytesIO()
    svg2png(bytestring=open(svg_file_path, 'rb').read(), write_to=png_image)
    png_image.seek(0)
    return png_image

# 清空搜索框内容的函数
def clear_search():
    # 使用 st.session_state 来更新 search_text 的值
    st.session_state.search = ''


def main():
    # 设置搜索行
    row_input = st.columns([4,1,1,13])
    # 添加文本输入框
    search_text = row_input[0].text_input('输入关键词以过滤图标:', key='search')
    # 添加搜索按钮
    row_input[1].text(" ")
    row_input[1].text(" ")
    search_button = row_input[1].button('搜索')
    # 添加清空按钮
    row_input[2].text(" ")
    row_input[2].text(" ")
    clear_button = row_input[2].button('清空',on_click = clear_search)
    # 读取SVG文件夹内的所有文件
    svg_files = [f for f in os.listdir(svg_folder_path) if f.endswith('.svg')]
    # 根据用户输入过滤SVG文件
    if search_text:
        filtered_svg_files = [f for f in svg_files if search_text.lower() in f.lower()]       
    else:
        filtered_svg_files = svg_files
    # 创建一个网格布局
    num_columns = 8  # 设定每行显示的图标数量

    for i, file in enumerate(filtered_svg_files):
        # 计算当前图标应该位于哪一行
        if i % num_columns == 0:
            # 每当到达新的行时，创建一个新的容器
            col = st.columns(num_columns)
        
        # 使用cairosvg将SVG转换为PNG
        img_path = os.path.join(svg_folder_path, file)
        img_data = svg_to_image(img_path)
        col[i % num_columns].image(img_data, width=20)  # 显示图片
        
        # 去掉SVG后缀并显示文件名
        base_name = os.path.splitext(file)[0]
        col[i % num_columns].write(base_name)  # 在图片下方添加文件名（无SVG后缀）

# 运行Streamlit应用
if __name__ == '__main__':
    st.set_page_config(page_title="Bootstrap Icons", page_icon=":icons:",layout="wide")
    st.html("""
        <style>

            /* header的样式 */
            [data-testid="stHeader"] {
                height: 1px;
            }
            /* body的样式 */
            [data-testid="stAppViewBlockContainer"] { 
                padding: 20px 50px;
            }
        </style>

        """)
    st.header('bootstrap-icons搜索')
    
    main()  