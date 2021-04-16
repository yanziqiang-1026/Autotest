import allure
import pytest
from pytest_autotest.Common import Request
from pytest_autotest.Params import tools
from pytest_autotest.Config import config

class TestUser(object):
    request = Request.Request()
    config = config.Readconfig()

    def test_success_search_01(self):
        t = tools.Yaml().case_detail('SearchUserMobile.yaml', 'search_user_mobile_01')
        host = self.config.get_config('测试环境').get('host')
        url = t.get('url')
        headers = t.get('headers')
        method = t.get('method')
        data = t.get('data')
        expect = t.get('expected')

        if method == 'GET':
            response = self.request.request_get(url=host+url, data=data, headers=headers).json()
            assert response['code'] == expect['code'], 'code与预期不一致'
            assert response['data'][0]['id'] == expect['id'],'userid与预期不一致'

    def test_success_search_02(self):
        t = tools.Yaml().case_detail('SearchUserMobile.yaml', 'search_user_mobile_02')
        print(t)
        host = self.config.get_config('测试环境').get('host')
        url = t.get('url')
        headers = t.get('headers')
        method = t.get('method')
        data = t.get('data')
        expect = t.get('expected')

        if method == 'GET':
            response = self.request.request_get(url=host+url, data=data, headers=headers).json()
            assert response['code'] == expect['code'], 'code与预期不一致'
            assert response['data'] == expect['data'], 'data与预期不一致'

# if __name__ == '__main__':
#     test = TestUser().test_success_search_02()
#     print(test)
