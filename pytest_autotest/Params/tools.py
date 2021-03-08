# -*- coding: utf-8 -*-
import yaml
import os
import os.path

# 获取yaml中的数据转化为python dic
def parse():
    param_paths = ['/User']
    pages = {} # 定义空字典后续存放解析后的yaml数据

    for param_path in param_paths:
        file_path = os.path.dirname(__file__) + param_path # 拼接路由

        # 文件、目录遍历器，遍历目标目录，返回三元组(root,dirs,files)，
        # root是当前正在遍历的这个文件夹本身的地址
        # dirs是一个list，内容是该文件目录下的所有一级目录名字
        # files是一个list，内容是该目录下的所有一级文件
        for root, dirs, files in os.walk(file_path):
            for name in files:
                watch_file_path = os.path.join(root, name)
                # 读取yaml文件
                with open(watch_file_path, encoding='utf-8') as f:
                    page = yaml.safe_load(f) # 只解析基本的yaml标记，用来保证代码的安全性
                    # print(page)
                    # print(type(page))
                    pages.update(page) # 修改当前字典
    return pages

def get_page_list():
    page_list = {} # 定义空字典
    pages = parse() # 调用函数，返回字典
    for page, value in pages.items():
        parameters = value['parameters'] # 元组操作
        data_list = []

        for parameter in parameters:
            data_list.append(parameter)
        page_list[page] = data_list # params以列表方式存放

    return page_list
