import sqlite3
import os.path
#user
'''
conn = sqlite3.connect('polling.db')
c = conn.cursor()
# username = "snmt"
# db=conn.execute("SELECT * FROM user WHERE username = :username ",{"username":username})
c.execute("""select * from user""")
# c.execute("""CREATE TABLE IF NOT EXISTS `user` ( `username` varchar(100) NOT NULL, `password` varchar(100) NOT NULL )""")
# c.execute("""select * from g_list""")
# c.execute("""INSERT INTO user(username, password)
#                   VALUES("snmt", "1234")""")
conn.commit()
rows = c.fetchall()
print(rows)
'''
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
db_path = os.path.join(BASE_DIR, "polling.db")
with sqlite3.connect(db_path) as database:
    db = database.cursor()
    username = "admin"
    password = "1234"
    db.execute("""CREATE TABLE IF NOT EXISTS `admin` ( `username` varchar(100) NOT NULL, `password` varchar(100) NOT NULL )""")
    db.execute("INSERT INTO admin(username, password)" " VALUES( :username, :password)",
                {"username": username, "password": password})
    database.commit()
    # db.execute("""select * from admin""")
    # database.commit()
    # rows = db.fetchall()
    # print(rows)
#
#
conn = sqlite3.connect('polling.db')
c = conn.cursor()
#
#
# # c.execute("""CREATE TABLE IF NOT EXISTS `admin` ( `username` varchar(100) NOT NULL, `password` varchar(100) NOT NULL )""")
# # c.execute("""INSERT INTO admin(username, password)
# #                      VALUES("admin", "1234")""")
c.execute("""select * from admin""")
rows = c.fetchall()
print(rows)
