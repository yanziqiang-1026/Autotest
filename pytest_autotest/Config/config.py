"""
python ConfigParser()模块简介：ConfigParser模块用于生成和修改常见配置文档，文件格式见config.ini
"""

import configparser
import os

class Readconfig():

    def __init__(self):
        curpath = os.path.dirname(os.path.relpath(__file__)) # 当前路径
        cf_path = os.path.join(curpath,'config.ini') # 获取配置文件路径

        self.cf = configparser.ConfigParser() # 实例化管理对象
        self.cf.read(cf_path,encoding='utf-8') # 读ini配置文件内容

    def get_config(self,param):
        # sections = self.cf.sections() # 获取所有的sections
        items = dict(self.cf.items(param)) # 获取某个sections中的所有值，将其转化为字典
        return items

# if __name__ == '__main__':
#     test = Readconfig()
#     t = test.get_config('测试环境')
#     print('取某个sections的所有值',t)
