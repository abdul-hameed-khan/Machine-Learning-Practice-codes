# -*- coding: utf-8 -*-
"""
Created on Sun Mar  7 15:10:19 2021

@author: Admin
"""

import numpy as np

import numpy as np
#x = np.array([1,  3,  4,  6])
#y = np.array([4, 11, 14 ,22])

features = 3
x = np.zeros((100,features))
y = np.zeros(100)
m = np.zeros(features)
count = len(y)

def loadcsvdata(name):
 i=0
 for line in open(name):
    vals = line.split(',')
    x[i][0] = (float(vals[0]))
    x[i][1] = (float(vals[1]))
    x[i][2] = (float(vals[2]))
    y[i] = (float(vals[3]))
    i=i+1
loadcsvdata("data_2d.csv")   
count = len(x)
def hypothesis( m, c):
    h = c + x * m
    return h
def CostFunNpm(m):
   
    error =  np.sum((x.dot(m) - y)**2) /(2*count)
    
    return error

def GDNpm(m,lr):
    tm = np.zeros(features)
    for i in range(features):
        
        tm[i] = np.sum((x.dot(m) - y) * x[:,i]) 
       
    for i in range(3):
          tm[i] = m[i] - lr*tm[i]/count        

    return tm

lr = 0.00025

res=[]
epocs = 200000

for i in range (epocs):
        
    res.append(CostFunNpm(m))
    m = GDNpm(m,lr)
res = ['%.4f' %i for i in res]

print (m,res[epocs -1 ])


