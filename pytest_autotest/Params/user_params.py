from pytest_autotest.Params import tools

# 引用tools模块，定义获取params方法，传入用例数据名，返回数据列表
def get_params(name):
    data = tools.get_page_list()
    param = data[name]
    return param

# 搜索成功的测试数据
class SearchSuccess():
    param = get_params('user') # 关键字驱动

    url = []
    data = []
    headers = []
    expected = []
    for i in range(0,len(param)):
        url.append(param[i]['url'])
        data.append(param[i]['params'][0])
        headers.append(param[i]['headers'])
        expected.append(param[i]['expected']['response']['code'])


# 搜索失败的测试数据
class SearchError():
    param = get_params('user2')
    url = []
    data = []
    headers = []
    for i in range(0, len(param)):
        url.append(param[i]['url'])
        data.append(param[i]['params'][0])
        headers.append(param[i]['headers'])
