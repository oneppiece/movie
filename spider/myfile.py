#!/usr/bin/python3
# Filename: myfile.py
import time  # 引入time模块

# open(file, mode='r', buffering=-1, encoding=None, errors=None, newline=None, closefd=True, opener=None)

# 将文件内容写入文件 title：标题 text：内容
def writeToFile(title, text):
    title = title + time.strftime('%Y-%m-%d%H:%M:%S', time.localtime())
    file = open(title, 'a+', -1, 'utf8')
    file.write(text)
    file.close()



