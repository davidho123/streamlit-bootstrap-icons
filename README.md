# streamlit-bootstrap-icons-search
search-bootstrap-icons
## 一、演示地址
https://bootstrap-icons-search.streamlit.app/
## 二、图标显示方案
#### 1、默认是以 svg 显示，加载会稍慢
#### 2、可以改用 png 显示，加载会快一些
（1）如果用png显示，需要修改代码，导入 cairosvg、io库取消注释，同时将函数svg_to_image，取消注释，53行、54行取消注释
（2）需要用到的库cairosvg
```python
pip install cairosvg
```

## 三、运行图
#### 全部图标
![1](img/1.png)
#### 搜索后图标
![2](img/2.png)
