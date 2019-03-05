from DBHelp import *

db = DBHelp(host="localhost",port=3306,user='root',password='123456',database='BQG',charset='utf8')
#db.openDB();
sql = "INSERT INTO pystroy (storyurl,storyname,status) VALUES (%s,%s,%s)"
data = ('fffff','eeeeee',1)
db.cud(sql,('jjjjjjj','kkkkkk',9))

#create table if not exists 'pystory' ('storyid' INT UNSIGNED AUTO_INCREMENT,'storyurl' VARCHAR(100) NOT NULL,'storyname' VARCHAR(100) NOT NULL,'status' INT(10) NOT NULL, PRIMARY KEY ('storyid'))ENGINE=InnoDB CHARSET=utf8;

# import pymysql.cursors
#
# # Connect to the database
# connection = pymysql.connect(host='localhost',
#                              user='root',
#                              password='123456',
#                              db='BQG',
#                              charset='utf8')
#
# try:
#     with connection.cursor() as cursor:
#         # Create a new record
#         sql = "INSERT INTO pystroy (storyurl,storyname,status) VALUES (%s,%s,%s)"#"INSERT INTO `pystory` (`email`, `password`) VALUES (%s, %s)"
#         cursor.execute(sql,('jjjjjjj','kkkkkk',9))
#
#     # connection is not autocommit by default. So you must commit to save
#     # your changes.
#     connection.commit()
#
#     # with connection.cursor() as cursor:
#     #     # Read a single record
#     #     sql = "SELECT `id`, `password` FROM `users` WHERE `email`=%s"
#     #     cursor.execute(sql, ('webmaster@python.org',))
#     #     result = cursor.fetchone()
#     #     print(result)
# finally:
#     connection.close()