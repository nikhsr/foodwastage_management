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
address=req.getvalue("hadd");
password=req.getvalue("pwd");
pincode=req.getvalue("pcd");
name=req.getvalue("hname");
cphone=req.getvalue("cno")
q="insert into caterer values('{}','{}','{}',{},'{}',{})".format(loginid,password,name,pincode,address,cphone)
cmd.execute(q)
db.commit()
print('    <meta http-equiv="refresh" content="0;url=http://localhost/login.py" />')


 












