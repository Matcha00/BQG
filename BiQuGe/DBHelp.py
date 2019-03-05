import pymysql


class DBHelp():

    def __init__(self,host,port,user,password,database,charset):
        self.host = host
        self.port = port
        self.user = user
        self.password = password
        self.database = database
        self.charset = charset
        self.db = None
        self.cursor = None
    def openDB(self):

        self.db = pymysql.connect(host=self.host,port = self.port,user=self.user,password=self.password,database=self.database,charset=self.charset)
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
        except Exception as e:

            print(e)

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

    def cud_sql(self,sql):
        self.openDB()
        try:
            self.cursor.execute(sql)
            self.db.commit()
            #self.db.close()
            print('ok')
            print(self.db)
            print(self.cursor)
        except Exception as e:
            self.db.rollback()
            self.close()
            print(e)