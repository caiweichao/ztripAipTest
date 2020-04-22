import requests
import allure

from com.utils.logUtil import log


class request:
    '''
    :param method: 请求方式
    :param url: 请求的url
    :param data: 请求的参数
    :param cookies: 请求中带的cookie
    :param header: 请求头
    '''
    @allure.step("发起请求")
    def __init__(self, method, url, data=None, cookies=None, header=None):
        try:
            log.info(f'开始发起请求: 请求方式{method}， 请求url={url}， \n请求参数={data}')
            if method == 'get':
                self.res = requests.get(url=url, params=data, cookies=cookies)
            elif method == 'post':
                self.res = requests.post(url=url, json=data, cookies=cookies)
            else:
                log.info(f'没有添加{method}这个请求方法请优化Requests类')
        except Exception as e:
            log.error(f'未知异常请检查request请求\n{e}')

    # 获取cookie
    def get_cookie(self):
        return self.res.cookies

    # 获取请求的返回值json模式
    def get_json(self):
        return self.res.json()

    # 获取请求的返回值text模式
    def get_text(self):
        return self.res.text

    # 获取请求的url
    def get_url(self):
        return self.res.url


if __name__ == '__main__':
    res = request(method='post', url='https://passport.z-trip.cn/login',
                  data={"rtnUrl": "https://www.z-trip.cn/home/index.html",
                        "username": "13248231369", "password": "cai123456",
                        "chkpersist": "0"}
                  , cookies=None, header=None)
    print(res.get_json())
