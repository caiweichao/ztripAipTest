# 正则表达式解析类
import re

import re
from com.utils.logUtil import log


class DoRegularUtil:
    @staticmethod
    # 方法作用是去除文件中的需要的字段解码并且进行替换
    def replace_unquote(target, key):
        pattern_EC = '\$\{(.*?)\}'
        re.search(pattern_EC, target)
        target = re.sub(pattern_EC, key, target, count=1)
        return target

    @staticmethod
    # 方法作用是去除文件中的需要的字段解码并且进行替换
    def free_replace(pattern_EC, target, key):
        while re.search(pattern_EC, target):
            target = re.sub(pattern_EC, key, target, count=1)
        return target

if __name__ == '__main__':
    xx = '{"orgId":"1651","year":"${year}","month":"${month}"}'