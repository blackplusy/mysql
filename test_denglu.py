#condig=utf8
import pymysql
def login():
	try:
		name=input('请输入姓名')
		pwd=input('请输入密码')
		conn=pymysql.connect(host='localhost',port=3306,user='root',password='admin',db='denglu',charset='utf8')
		cur=conn.cursor()
		#sql='select * from user where username="%s" and password="%s"',(name,pwd)
		#print(sql)
		#result=cur.execute('select * from user where username=%s and password=%s',(name,pwd))
		result=cur.execute('update user set password=%s where username=%s',(name,pwd))
	
		if result==1:
			conn.commit()
			print('登录成功')
		else:
		
			print('登录失败')
	except Exception as e:
		conn.rollback()
	
if __name__=='__main__':
	login()
