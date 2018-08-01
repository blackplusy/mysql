#conding=utf8
import pymysql
#实现场景：小黑跟小强借50
def borrow():
	conn=pymysql.connect(host='localhost',port=3306,user='root',password='admin',db='denglu',charset='utf8')
	cur=conn.cursor()
	#try:
	
	# 小强钱先剪掉50
	result1=cur.execute('update zhangwu set money=money-50 where id=1')
	print(result1)
	#小黑的钱加50
	result2=cur.execute('update zhangwu set money=money+50 where id=3')
	print(result2)
	if result1==0 or result2==0:
		conn.rollback()
	else:
	
		conn.commit()
	#except Exception as e:
	#	conn.rollback()
if __name__=='__main__':
	borrow()
