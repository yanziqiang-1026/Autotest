from pytest_autotest.Params import tools


def get_params(name):
    data = tools.get_page_list()
    param = data[name]
    return param

# 搜索成功的测试数据
class SearchSuccess():
    param = get_params('user')
    # print(param)
    # print(type(param))
    url = []
    data = []
    headers = []
    for i in range(0,len(param)):
        url.append(param[i]['url'])
        data.append(param[i]['params'][0])
        headers.append(param[i]['headers'])

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
