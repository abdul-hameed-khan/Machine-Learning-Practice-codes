# -*- coding: utf-8 -*-
"""
Created on Sun Mar  7 14:47:59 2021

@author: Admin
"""
import matplotlib.pyplot as plt
import numpy as np

params = 3
x = np.zeros((100,params))
y = np.zeros(100)
mm = np.zeros(params)

def loadcsvdata(name):
 i=0
 for line in open(name):
    vals = line.split(',')
    x[i][0] = 1#(float(vals[0]))
    for j in range(params-1):
        
     x[i][j+1] = (float(vals[j]))
     
    y[i] = (float(vals[params-1]))
    i=i+1
loadcsvdata("data_2d_1.csv")   
count = len(x)

def plotit(x,y):
    plt.plot(x,y)
    plt.show()

def hypothesis( inp1,inp2, m1,m2, c):
    h = c + inp1 * m1 + inp2*m2
    return h
def CostFunSimple(m1,m2,c):
    sum = 0
    for i in range (count):
        sum+= ((m1*x[i][1] + m2*x[i][2]+ c * x[i][0])-y[i]) ** 2
    error = sum/(2*count)
   
    return error
def GD2VSimple(m1,m2,c,lr):
    um1=0
    um2=0
    uc=0
    for i in range (count):
      um1+=  (m1*x[i][1] + m2*x[i][2] + c - y[i]) * x[i][1]
      um2+=  (m1*x[i][1] + m2*x[i][2] +c - y[i]) * x[i][2]
      uc =   (m1*x[i][1] + m2*x[i][2] +c - y[i]) * x [i][0]
    m1 =  m1 - lr * um1  /count
    m2 =  m2 - lr * um2 / count
    c =  c - lr * uc / count
    
    return m1,m2,c 


def GDLearning():
 print ("Start")  
 lr = 0.0002
 m1=0;m2=0;c=0
 res=[]
 epocs = 10
 for i in range (epocs):
        
    res.append(CostFunSimple(m1,m2,c))
    m1,m2,c = GD2VSimple(m1,m2,c,lr)
 res = ['%.2f' %i for i in res]
 #print (res)
 return (m1,m2,c,res)



def comparePlt(x,y,m,c):
    plt.scatter(x,y)
    resp = []
    for i in range(count):
        resp.append(m*x[i]+c)
    plt.plot (x,resp)
    plt.show()
    
    
def classLearning():
  
 lr = 0.001
 m=0
 c=0
 epocs = 19
 res = []
 marr = []
 for i in range (epocs):
    marr.append(m)
    res.append(CostFunSimple(m,c))
    comparePlt(x,y,m,c)
    m+=lr
 res = ['%.2f' %i for i in res]
 
 plotit(marr,res)
 print (res)
 
#classLearning()
m1,m2,c,res = GDLearning()
print (c,m1,m2, res)