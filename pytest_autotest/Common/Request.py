import requests


class Request(object):

    def request_get(self, url, params=None, headers=None, cookies=None):
        res = requests.get(url=url, params=params, headers=headers, cookies=cookies)
        return res

    def request_post(self, url, data=None, headers=None, cookies=None):
        res = requests.post(url=url, data=data, headers=headers, cookies=cookies)
        return res

    def request_put(self, url, data=None, headers=None, cookies=None):
        res = requests.put(url=url, data=data, headers=headers, cookies=cookies)
        return res

