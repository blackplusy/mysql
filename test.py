#coding=utf-8
import pymysql
conn=pymysql.connect(host='localhost',port=3306,user='root',password='admin',db='mybase',charset='utf8')
cur=conn.cursor()
#cur.execute('select * from student')
result=cur.execute('insert into student values(8,"张飞",20,"2001-05-20")')
print(result)
conn.commit()
#result=cur.fetchall()
#for re in result:
	#print(re)
#	print(re[1])
#	print(re[2])



