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