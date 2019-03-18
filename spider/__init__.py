#!/usr/bin/python3
# -*- coding: utf-8 -*-


# 拉源码
# 按类型找



import time
import urllib.request  # 获取网址模块

url = "http://yongjiuzy.cc/"


# 获取源代码
def get_html():
    papg = urllib.request.urlopen(url)  # 打开图片的网址
    html = papg.read()  # 用read方法读成网页源代码，格式为字节对象
    html = html.decode('UTF-8')  # 定义编码格式解码字符串(字节转换为字符串)
    return html


# 写入文件

def write_file(title, text):
    title = time.strftime('%Y-%m-%d%H:%M:%S', time.localtime())
    file = open(title, 'a+', -1, 'utf8')
    file.writelines(text)
    file.close()


# 调用函数
# html = gethtml()

text = get_html()
write_file(url, text)

print(text)
