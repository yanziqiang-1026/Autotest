# -*- coding: utf-8 -*-
import yaml
import os
import os.path


class Yaml:
    def __init__(self):
        # Yaml文件目录路径
        self.config_path = os.path.join(os.path.dirname(os.path.relpath(__file__)),'Yaml')

    def read_yaml(self,yaml_file):
        # 读取yaml文件中的数据
        try:
            with open(os.path.join(self.config_path,yaml_file),"r",encoding='utf-8') as f:
                return yaml.load(f,Loader=yaml.Loader)
        except Exception as error:
            print(error)
            return False

    # 解析某一条用例的测试数据
    def resolution_yaml(self,yaml_file,case):
        data = self.read_yaml(yaml_file)
        resolution_data = data.get(case)
        return resolution_data

    # 解析每一条用例的信息
    def case_detail(self, yaml_file, case):
        case_dict = self.resolution_yaml(yaml_file, case)

        try:
            url = case_dict['parameters']['url']
            method = case_dict['parameters']['method']
            headers = case_dict['parameters']['headers']
            data = case_dict['parameters']['params']
            expected = case_dict['parameters']['expected']
            return {'url':url,'method':method,'headers':headers,'data':data,'expected':expected}
        except Exception as error:
            print(error)
            return False

# if __name__ == '__main__':
#     test = Yaml()
#     test.read_yaml('SearchUserMobile.yaml')
#     print(test.read_yaml('SearchUserMobile.yaml'))
#     test.resolution_yaml('SearchUserMobile.yaml','search_user_mobile_01')
#     print(test.resolution_yaml('SearchUserMobile.yaml','search_user_mobile_01'))