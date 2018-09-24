#!c:/Python34/python.exe
print("Content-Type: text/html")
print("""
  """)
import pymysql
import cgi
from sklearn import neural_network as nn
import pandas as pd
from sklearn import model_selection as cv
from sklearn import preprocessing as pp
import pickle
import numpy as np
print('vivek')


time=req.getvalue("ts");
adult=req.getvalue("ano");
weather=req.getvalue("wr");
ac=req.getvalue("ac");
child=req.getvalue("cno");
var=req.getvalue("var");
holiday=req.getvalue("hd");













scaler=open('scaler.pickle','rb')
scale=pickle.load(scaler)
normaliser=open('normaliser.pickle','rb')
norm=pickle.load(normaliser)
adult=872
child=1350
timeslot=0
aircon=0
variety=1
weather=0
holidaystatus=0
x=[[adult,child,time,ac,var,weather,holiday]]
x=scale.transform(x)
x=norm.transform(x)
print(x)


pic = open('D:\python\hackathon\shadinn.pickle','rb')
model=pickle.load(pic)
df = pd.read_csv('data.csv')
x = df[["adults",
      "child",
      "timeslot",
      "airconditioning",
      "variety",
      "weather",
      "holidaystatus",
     ]]
x = np.array(x)
x=x.reshape(len(x),7)
x=pp.scale(x)
x=pp.normalize(x,norm='l2')
L=model.predict(x)
print(L[1])










 












