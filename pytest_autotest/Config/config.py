"""
python ConfigParser()模块简介：ConfigParser模块用于生成和修改常见配置文档，文件格式见config.ini
"""
from configparser import ConfigParser
import os


class ReadConfig():
    # 标题
    title = 'private_debug'

    # 值
    tester = 'tester'
    host = 'host'

    def __init__(self):
        self.config_file = os.path.dirname(__file__) + '/config.ini' # 配置文件地址
        self.config = ConfigParser()
        self.config.read(self.config_file) # 读取文件配置

        self.tester = self.get_config(self.title, self.tester) # 测试人
        self.host = self.get_config(self.title, self.host) # 测试地址

    def get_config(self, title, value):
        value = self.config.get(title, value)
        return value

