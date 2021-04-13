import requests


class Request(object):

    def request_get(self, url, data=None, headers=None, cookies=None):
        """
        Requests发送Get请求
        :param url：请求地址
        :param data：Get请求参数
        :param cookie：cookie参数
        :param header：header参数
        """
        res = requests.get(url=url, params=data, headers=headers, cookies=cookies)
        return res

    def request_post(self, url, data=None, headers=None, cookies=None):
        """
        Requests发送Post请求
        :param url：请求地址
        :param data：Post请求参数
        :param cookie：cookie参数
        :param header：header参数
        """
        res = requests.post(url=url, data=data, headers=headers, cookies=cookies)
        return res

    def request_put(self, url, data=None, headers=None, cookies=None):
        """
        Requests发送Put请求
        :param url：请求地址
        :param data：Post请求参数
        :param cookie：cookie参数
        :param header：header参数
        """
        res = requests.put(url=url, data=data, headers=headers, cookies=cookies)
        return res

