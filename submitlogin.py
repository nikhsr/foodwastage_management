#!c:/Python34/python.exe
import pymysql
import cgi
print("Content-Type: text/html")
print("""
  """)
 

req=cgi.FieldStorage()
db=pymysql.connect(host='localhost',user='root',password='123',db='hackathon')

cmd=db.cursor()
loginid=req.getvalue("lgid");

password=req.getvalue("pwd");

q="select * from caterer where loginid='{}' and password = '{}'".format(loginid,password)

cmd.execute(q)
r=cmd.fetchall()
print(r)
db.commit()






 













