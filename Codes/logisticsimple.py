# -*- coding: utf-8 -*-
"""
Created on Sun Mar  7 14:47:59 2021

@author: Admin
"""
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

# Importing the dataset
dataset = pd.read_csv('Ads.csv')
x = dataset.iloc[:, [2, 3]].values
y = dataset.iloc[:, -1].values
x2 = np.zeros((300,2))
# Splitting the dataset into the Training set and Test set
from sklearn.model_selection import train_test_split
X_t, X_test, y_train, y_test = train_test_split(x, y, test_size = 0.25, random_state = 0)

# Feature Scaling



x2[:,0] = (X_t[:,0] - X_t[:,0].mean())/X_t[:,0].std()
x2[:,1] = (X_t[:,1] - X_t[:,1].mean())/X_t[:,1].std() 



m=0
c=0
i=0
def loadcsvdata(name):
 for line in open(name):
    vals = line.split(',')
    x.append(float(vals[0]))
    y.append (float(vals[1]))
#loadcsvdata("data_1d.csv")   
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
   
 lr = 0.01
 m=0
 c=0
 res=[]
 epocs = 200 
 for i in range (epocs):
        
    res.append(CostFunSimple(m,c))
    m,c = GD(m,c,lr)
 res = ['%.2f' %i for i in res]
 print (m,c , res)
 
def comparePlt(x,y,m,c):
    plt.scatter(x,y)
    resp = []
    for i in range(count):
        resp.append(m*x[i]+c)
    plt.plot (x,resp)
    plt.show()
    
    
def classLearning():
  
 lr = 0.1
 m=0
 c=0
 epocs = 10
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
#GDLearning()
