import time

import pytest
import allure
import json

from com.resources.tempData import basicData
from com.utils.requestUtil import request
from com.utils.excelUtils import doExcel
from com.utils.datetimeUtil import *
from com.utils.reUtil import DoRegularUtil
from com.utils.logUtil import log
from com.resources import contants

# 初始化测试用例加载
doExcel = doExcel()
testCases = doExcel.getSheetCase('getTravelCost')
caseTitle = doExcel.getTitle('getTravelCost')


@pytest.mark.parametrize('testCase', testCases, ids=caseTitle)
@pytest.mark.usefixtures('getCookie')
class Test_getTravelCost:
    def test_test_getTravelCost(self, testCase):
        # 1.处理参数化数据
        if '上月' in testCase.title:
            if get_now_month() == 12:
                testCase.data = DoRegularUtil.replace_unquote(
                    DoRegularUtil.replace_unquote(testCase.data, (testCase.data, get_now_year() - 1)), '12')
            else:
                testCase.data = DoRegularUtil.replace_unquote(
                    DoRegularUtil.replace_unquote(testCase.data, str(get_now_year())),
                    str(get_now_month() - 1))
        elif '当月' in testCase.title:
            testCase.data = DoRegularUtil.replace_unquote(DoRegularUtil.replace_unquote(testCase.data, str(get_now_year())),
                                                          str(get_now_month()))
        cookies = getattr(basicData, 'cookie')
        res = request(method=testCase.method, url=contants.webUrl + testCase.url, data=json.loads(testCase.data),
                      cookies=cookies)

