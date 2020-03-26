import pytest
import allure
import json
from common.request import request
from common.doExcel import doExcel
from common.logs import log
from datas.tempData import basicData
from common.contans import *

# 初始化加载测试用例
doExcel = doExcel(fileName=caseFile)
caseData = doExcel.getSheetCase(sheetName='passport_login')
caseTitle = doExcel.getTitle(sheetName='passport_login')


@pytest.mark.parametrize('testCase', caseData, ids=caseTitle)
class Test_get_ecCode:
    def test_login(self, testCase):
        allure.attach(f'用例参数{testCase.data}')
        res = request(method=testCase.method, url=passport_url + testCase.url, data=json.loads(testCase.data))
        if res.get_json()['code'] == '0':
            setattr(basicData, 'cookie', res.get_cookie())
            # 获取cookie，其他接口登录可以使用
            log.debug(f'将cookie反射入BASIC类，{res.get_cookie()}')
        else:
            log.info('获取登录cookie失败\n{}'.format(res.get_text()))
        try:
            print(res.get_json()['code'],str(testCase.expected))
            assert res.get_json()['code'] == str(testCase.expected)
            doExcel.writeExcel(sheetName='passport_login', caseId=testCase.caseId, actual=res.get_json()['code'],
                               result='Pass')
            log.info('用例执行pass')
        except AssertionError:
            log.info('用例执行fail')
            assert res.get_cookie()['code'] == str(testCase.expected)
            doExcel.writeExcel(sheetName='passport_login', caseId=testCase.caseId, actual=res.get_json()['code'],
                               result='Fail')
