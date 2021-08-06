import mysql.connector
from do.do1.do1 import random_codes


def random_codes_to_mysql(charlen, numlen, count):
    codes = random_codes(charlen, numlen, count)
    mysqldb = mysql.connector.connect(host="localhost", user="root", passwd="123456", database="test")
    cur = mysqldb.cursor()
    cur.execute('create table if not exists code(id int ,code varchar(50))')
    i = 1
    for code in codes:
        cur.execute("INSERT INTO code VALUES (%s,%s)", (i, code))
        i += 1
    mysqldb.commit()
    cur.close()
    mysqldb.close()


random_codes_to_mysql(4, 4, 100)
