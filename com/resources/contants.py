# 路径，常量管理类

import os

# ----------目录路径常量-------------
# 项目的根目录
base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
# Conf文件夹路径
conf_dir = os.path.join(base_dir, 'conf')
# TestData文件夹路径
resources_dir = os.path.join(base_dir, 'resources')
# Logs文件夹路径
logs_dir = os.path.join(base_dir, 'logs')
# 日志文件夹路径
text_log = os.path.join(logs_dir, 'TextLog')

# ----------文件路径常量---------------
# global配置文件
global_conf = os.path.join(conf_dir, 'global.ini')
# sit配置文件
sit_conf = os.path.join(conf_dir, 'SIT.ini')
# uat配置文件
uat_conf = os.path.join(conf_dir, 'UAT.ini')
# pro配置文件
pro_conf = os.path.join(conf_dir, 'PRO.ini')
# 测试用例文件路径
caseFile = os.path.join(resources_dir, 'TestCase.xlsx')

# -----------日志常量管理-----------------
# 日志输出格式
formatter = '%(asctime)s-%(filename)s-%(levelname)s-%(message)s'
# 日志最大保存时间
log_time = 7

# ----------测试接口url------------------
webUrl = f'https://ws.z-trip.cn/'

