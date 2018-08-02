#coding=utf8
from pymongo import MongoClient
conn=MongoClient(host='localhost',port=27017)
collection=conn.config
#增加
#collection.tabel1.insert({'_id':1104,'name':'xixi1'})
#删除
#collection.tabel1.remove({'name':'xixi'})
#修改
collection.tabel1.update({'name':'xixi1'},{'$set':{'age':13}})
result=collection.tabel1.find()
for doc in result:
	print(doc)
