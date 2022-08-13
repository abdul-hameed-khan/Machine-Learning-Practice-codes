# -*- coding: utf-8 -*-
"""
Created on Sun Mar  7 14:47:59 2021

@author: Admin
"""
import matplotlib.pyplot as plt

#x = [1,2,3,4,5,6] #[1,  3,  4,  6]
#y = [3,6,9,12,15,18]#[4, 11, 14 ,22]

x = []
y = []

m=0
c=0
i=0
def loadcsvdata(name):
 for line in open(name):
    vals = line.split(',')
    x.append(float(vals[0]))
    y.append (float(vals[1]))
loadcsvdata("data_poly.csv")   
plt.scatter(x,y)
count = len(x)

def plotit(x,y):
    plt.plot(x,y)
    plt.show()

def hypothesis( inp, m, c):
    h = c + inp * m
    return h
def CostFunSimple(m,c):
    sum = 0
    for i in range (count):
        sum+= ((m*x[i] + c)-y[i]) ** 2
    error = sum/(2*count)
    return error
def GD(m,c,lr):
    um=0
    uc=0
    for i in range (count):
      um+=  (m*x[i] + c - y[i]) * x[i]
      uc =  (m*x[i] + c - y[i])
    m =  m - lr * um/count
    c =  c - lr * uc/count
    return m,c 



def GDLearning():
   
 lr = 0.0005
 m=0
 c=0
 res=[]
 epocs = 80000
 for i in range (epocs):
        
    res.append(CostFunSimple(m,c))
    m,c = GD(m,c,lr)
 res = ['%.2f' %i for i in res]
 print (c, m , res[epocs -1])



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
GDLearning()