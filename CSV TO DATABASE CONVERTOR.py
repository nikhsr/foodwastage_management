import pymysql
import pandas as pd

df = pd.read_csv("C:/Users/Lenovo/Desktop/data.csv")
a = df["adults"]
a=list(a)
b = df["airconditioning"]
b=list(b)
c = df["chapati"]
c=list(c)
d = df["child"]
d=list(d)
e = df["dal"]
e=list(e)
f = df["holidaystatus"]
f=list(f)
g = df["rice"]
g=list(g)
h = df["sabzi"]
h=list(h)
ii = df["timeslot"]
ii=list(ii)
j = df["variety"]
j=list(j)
k = df["weather"]
k=list(k)

db = pymysql.connect(host= 'localhost', user = 'root', password = '123', db = 'hackathon')
cur = db.cursor()



for i in range(a.__len__()):
     print(i)
     query = "Insert Into data  VALUES (" +str(i)+",'"+ str(a[i]) + "','" + str(b[i]) + "','" + str(c[i]) + "','" + str(d[i]) + "','" + str(e[i]) + "','" + str(f[i]) + "','" + str(g[i]) + "','" + str(h[i]) + "','" + str(ii[i]) + "','" + str(j[i]) + "','" + str(k[i]) + "')"
     cur.execute(query)
     db.commit()
