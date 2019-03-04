import pymysql


class DBHelp():

    def __init__(self,host,user,password,database,charset):
        self.host = host
        self.user = user
        self.password = password
        self.database = database
        self.charset = charset
        self.db = None
        self.cursor = None
    def openDB(self):

        self.db = pymysql.connect(host=self.host,user=self.user,password=self.password,database=self.database,charset=self.charset)
        self.cursor = self.db.cursor()
    def close(self):
        self.cursor.close()
        self.db.close()



        # 数据增删改



    def cud(self, sql, params):
        self.openDB()

        try:
            self.cursor.execute(sql, params)
            self.db.commit()
            print("ok")
        except:

            print('cud出现错误')

            self.db.rollback()

            self.close()

    def find(self, sql, params):
        self.openDB()
        try:
            result = self.cursor.execute(sql, params)
            self.close()
            return result
        except:
            print('find出现错误')