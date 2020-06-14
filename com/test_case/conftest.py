import pytest
from com.resources.tempData import basicData
from com.utils.jsonUtil import jsonUtil
from com.utils.requestUtil import request

_passportUrl = 'https://passport.z-trip.cn/jsonp/login.json'
_datas = "service=https://ws.z-trip.cn&username=13248231369&password=cai000000"


# 获取登录的cookie不在测试登录
@pytest.fixture(scope='session')
def getCookie():
    _getCookieUrl = 'https://ws.z-trip.cn/login.json?'
    getEC = request(method='get', url=_passportUrl, data=_datas)
    clientKey = jsonUtil.jsonToOneValue(getEC.get_json(), '$.clientKey')
    login = request(method='get', url=_getCookieUrl + f"KI4SO_CLIENT_EC={clientKey}")
    setattr(basicData, 'cookie', login.get_cookie())


def pytest_collection_modifyitems(items):
    """
    测试用例收集完成时，将收集到的item的name和nodeid的中文显示在控制台上
    :return:
    """
    for item in items:
        item.name = item.name.encode("utf-8").decode("unicode_escape")
        item._nodeid = item.nodeid.encode("utf-8").decode("unicode_escape")


if __name__ == '__main__':
    getCookie()
