#!f:/Python34/python.exe
import cgi
print("Content-Type: text/html")
print("""
""")
request=cgi.FieldStorage()

uid=request.getvalue('uid')
pwd=request.getvalue('pwd')
db=pymysql.connect(host='localhost',user='root',password='123',db='hackathon')
cmd=db.cursor()
 
cmd.execute("select * from caterer where loginid=")
rows=cmd.fetchall()
if(uid=='india' and pwd=='india'):
 print('<meta HTTP-EQUIV="REFRESH" content="0; url=http://localhost/test/student.py">')
else:
 print('Invalid UID/PWD');








 
