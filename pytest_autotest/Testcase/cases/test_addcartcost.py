import json

import allure
import pytest
from pytest_autotest.Common import Request
from pytest_autotest.Params import tools
from pytest_autotest.Config import config
from pytest_autotest.Common import DB


class TestCost(object):
    request = Request.Request()
    config = config.Readconfig()

    def setup(self):
        print('运行于测试用例之前,初始化')

    def teardown(self):
        print('运行于测试用例之后,清数据')

    # 从数据库读取
    def get_info(self):
        sql = "select id from `user` where mobile = '19916939575';"
        info = DB.Connect().connet(sql)
        user_id = info[0][0]

        info_dic = {
            'user_id': user_id
        }
        # print(info_dic)
        return info_dic

    # 测试用例
    def test_add_cart_cost_01(self):
        t = tools.Yaml().case_detail('AddCartCost.yaml', 'AddCartCost_01')
        # print('t: {}'.format(t))
        host = self.config.get_config('测试环境').get('host')
        # print(self.get_info())
        url = t.get('url').format(**self.get_info())
        # print(url)
        headers = t.get('headers')
        # print(headers)
        method = t.get('method')
        data = t.get('data')
        # print(data)
        expect = t.get('expected')

        if method == 'POST':
            response = self.request.request_post(url=host + url, data=json.dumps(data), headers=headers).json()
            # assert response['code'] == expect['code'], 'code与预期不一致'
            # assert response['data']['paid'] == expect['paid'], 'paid与预期不一致'

if __name__ == '__main__':
    test = TestCost()
    test.test_add_cart_cost_01()
