import allure
import pytest
from pytest_autotest.Common import Request
from pytest_autotest.Params import tools
from pytest_autotest.Config import config

class TestUser(object):
    request = Request.Request()
    config = config.Readconfig()

    # def setup(self):
    #     print('运行于测试用例之前,初始化')
    #
    # def teardown(self):
    #     print('运行于测试用例之后,清数据')
    #
    # @pytest.mark.usefixtures('initialization')
    # @pytest.mark.skip()
    # @pytest.mark.xfail()
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

if __name__ == '__main__':
    test = TestUser().test_success_search_01()
    print(test)
