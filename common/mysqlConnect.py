import pymysql

from common.config import ConfigLoader
from common.logs import log


# 连接数据库建立游标，执行sql，关闭数据库

class mysqlUtil:

    def __init__(self, connectName):
        config = ConfigLoader()
        host = config.get(connectName, 'host')
        user = config.get(connectName, 'user')
        pwd = config.get(connectName, 'pwd')
        port = config.getint(connectName, 'port')
        try:
            self.db = pymysql.connect(host=host, user=user, password=pwd, database=None, port=int(port))
        except TimeoutError as e:
            log.error(f'数据库链接超时请检查，地址{host}，用户名{user}，密码{pwd}，端口号{port} \n {e}')
            raise e
        except IndentationError as e:
            log.error(f'数据库链接用户名不存在请检查 用户名：{user} \n {e}')
        except pymysql.err.OperationalError as e:
            log.error(f'用户名或密码错误请检查 用户名：{user} 密码：{pwd} \n {e}')

    # 查询单条数据并且返回 可以通过sql查询指定的值 也可以通过索引去选择指定的值
    def fetch_one(self, sqlValue, name=None):
        # 修改返回值为数组键值对 cursor=pymysql.cursors.DictCursor
        cursor = self.db.cursor(cursor=pymysql.cursors.DictCursor)
        try:
            # 按照sql进行查询
            cursor.execute(sqlValue)
            if name is None:
                # 返回一条数据 还有 all size（自己控制）
                data = cursor.fetchone()
                return data
            elif name is not None:
                data = cursor.fetchone()
                return data[name]
        except Exception as e:
            log.error(f"请检查sql是否正确 sql={sqlValue}")
            raise e

    def fetch_all(self, sqlValue):  # 查询多条数据并且返回
        # 修改返回值为数组键值对 cursor=pymysql.cursors.DictCursor
        cursor = self.db.cursor(cursor=pymysql.cursors.DictCursor)
        try:
            # 按照sql进行查询
            cursor.execute(sqlValue)
            # 返回一条数据 还有 all size（自己控制）
            data = cursor.fetchall()
        except pymysql.err.ProgrammingError as e:
            log.error(f"请检查sql是否正确 sql={sqlValue}")
            raise e
        return data

    def close_connect(self):
        # 关闭数据库链接
        self.db.close()


if __name__ == '__main__':
    mysql = mysqlUtil('mysql_ota')
    x= mysql.fetch_one("select BIZ_TYPE from tem_oms.ota_order where ID= 103121812443264;",'BIZ_TYPE')
    print(x)
