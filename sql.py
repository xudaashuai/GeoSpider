import pymysql
from aliyun_crawer.settings import *
conn = pymysql.connect(host=HOST,port=3306,user='root',password='19980819',database='data',charset='utf8')

cur=conn.cursor()
cur.execute('select * from pois')
for  x in cur.fetchall():
    print(x)
