import allure

from pytest_autotest.Common import Request
from pytest_autotest.Params import user_params
from pytest_autotest.Config import config


@allure.feature('获取用户信息')
class TestUser(object):
    request = Request.Request()
    config = config.ReadConfig()

    @allure.severity('blocker')
    @allure.story('输入用户手机号用例')
    def test_success_search_01(self):
        """ 搜索成功用例 """
        allure.dynamic.title("搜索成功")

        data = user_params.SearchSuccess()
        host = self.config.host
        url = data.url[0]
        params = data.data[0]
        headers = data.headers[0]
        api_url = host + url

        response = self.request.request_get(url=api_url, params=params, headers=headers).json()
        # print(response)
        # allure.attach('{0}'.format(response), '返回的结果')
        assert response['code'] == 0

    @allure.severity('blocker')
    @allure.story('输入用户手机号用例')
    def test_success_search_02(self):
        """ 搜索失败用例 """
        allure.dynamic.title("搜索失败")

        data = user_params.SearchError()
        host = self.config.host
        url = data.url[0]
        params = data.data[0]
        headers = data.headers[0]
        api_url = host + url

        response = self.request.request_get(url=api_url, params=params, headers=headers).json()
        # print(response)
        # allure.attach('{0}'.format(response), '返回的结果')
        assert response['code'] == 0
        assert response['data'] == []
        