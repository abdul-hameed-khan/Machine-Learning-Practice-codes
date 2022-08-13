# -*- coding: utf-8 -*-
"""
Created on Sun Mar  7 15:10:19 2021

@author: Admin
"""

import numpy as np

import numpy as np
import matplotlib.pyplot as plt
#x = np.array([1,  3,  4,  6])
#y = np.array([4, 11, 14 ,22])

features = 3
x = np.zeros((100,features))
y = np.zeros(100)
m = np.zeros(3) #quardratic function ax+bx^2+c
count = len(y)

def loadcsvdata(name):
 i=0
 for line in open(name):
    vals = line.split(',')
    x[i][0] =1
    x[i][1] = (float(vals[0])* float(vals[0]))
    x[i][2] = (float(vals[0]))
    y[i] = (float(vals[1]))
    i=i+1
loadcsvdata("data_poly.csv")
#plt.scatter(x[1], y)   
count = len(x)
def hypothesis( m, c):
    h = m[0] + x[1] * m[1] + x[2]* m[2]
    return h
def CostFunNpm(m):
    #error =  np.sum((np.sum ((m*x) - y))**2) /(2*count) # double summation implementation
    error =  np.sum((x.dot(np.transpose(m)) - y)**2) /(2*count)
    
    return error

def GDNpm(m,lr):
    tm = np.zeros(features)
    for i in range(features):
        #tm[i] =np.sum((np.sum ((x*m)  - y))* x[:,i])
        tm[i] = np.sum((x.dot(np.transpose(m)) - y) * x[:,i]) 
       
    for i in range(3):
          tm[i] = m[i] - lr*tm[i]/count        

    return tm

lr = 0.00000007

res=[]
epocs =700000
for i in range (epocs):
        
    res.append(CostFunNpm(m))
    m = GDNpm(m,lr)
res = ['%.4f' %i for i in res]
print (m,res[-1])

