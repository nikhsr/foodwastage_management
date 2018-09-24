#!c:/Python34/python.exe
import pymysql
import cgi
print("Content-Type: text/html")
print("""
  """)
 

req=cgi.FieldStorage()
db=pymysql.connect(host='localhost',user='root',password='123',db='hackathon')

cmd=db.cursor()
ologinid=req.getvalue("lgid");

opassword=req.getvalue("pwd");
opincode=req.getvalue("pcd");
oname=req.getvalue("oname");
phone=req.getvalue("cno")
q="insert into organization values('{}',{},{},'{}','{}')".format(oname,opincode,phone,ologinid,opassword)

cmd.execute(q)
db.commit()
print('    <meta http-equiv="refresh" content="0;url=http://localhost/login.py" />')


 












