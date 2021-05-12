'''
database连接
'''

import pymysql
from pytest_autotest.Config import config

class Connect():
    def __init__(self):
        self.db_info = config.Readconfig().get_config('DB')

        self.host = self.db_info['host']
        self.port = self.db_info['port']
        self.username = self.db_info['username']
        self.password = self.db_info['password']
        self.database = self.db_info['database']
        self.charset = self.db_info['charset']

    def connet(self,sql):
        db_connect = pymysql.connect(host=self.host, user=self.username, password=self.password,port=int(self.port),
                                     database=self.database, charset=self.charset)
        cursor = db_connect.cursor()
        cursor.execute(sql)
        data = cursor.fetchall() # 返回tuple
        cursor.close()
        db_connect.close()
        print(data)
        return data


# if __name__ == '__main__':
#     test = Connect()
#     sql = 'select * from tscore where id = 9 limit 1'
#     test.connet(sql)