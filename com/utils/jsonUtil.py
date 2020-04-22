import json
import jsonpath
from com.utils.logUtil import log


class jsonUtil:
    @staticmethod
    def loadJson(data):
        return json.loads(data, ensure_ascii=False, indent=4)

    @staticmethod
    def jsonToOneValue(json, rule):
        try:
            value = jsonpath.jsonpath(json, rule)
            return value[0]
        except Exception as e:
            log.error(f"无法正常获取json内容请检查解析表达式{rule}", e)


if __name__ == '__main__':
    str = {"error": "0","data": "更新差旅计划成功"}
    xx = jsonUtil.jsonToOneValue(str,'$.data')
    print(xx)