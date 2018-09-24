#!c:/Python34/python.exe
import pymysql
import cgi
print("Content-Type: text/html")
print("""
  """)
 

req=cgi.FieldStorage()
db=pymysql.connect(host='localhost',user='root',password='123',db='hackathon')

cmd=db.cursor()
pincode=req.getvalue("pcd")
name=req.getvalue("oname")
phone=req.getvalue("cnum")
q="insert into organization values('{}',{},{})".format(name,pincode,phone)
cmd.execute(q)
db.commit()
print("Record Submitted....")


 












