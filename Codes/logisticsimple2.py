# -*- coding: utf-8 -*-
"""
Created on Sun Mar  7 15:10:19 2021

Kashif Bilal

@author: Admin
"""



import numpy as np


 
rows = 500

cols=5
x = np.zeros((rows,cols))
x2 = np.zeros((rows,cols+3))
y = np.zeros(rows)
def loadcsvdata(name):
 
 i=0

 flag = True
 for line in open(name):
    if (flag):
        flag= False
        continue
    vals = line.split(',')
    for j in range(cols):
     x[i][j] = (float(vals[j]))
    y[i] = (int(vals[cols]))
    i=i+1
    count = len(x)

 #np.random.shuffle(x)
 x2[:,0:4] = x[:,0:4]
 for i in range(500):
    a = int ( x[i][4])
    x2[i][(a+4)]=1
 xtrain = x2[0:-100,:]
 ytrain = y[0:-100]
 xtest = x2[-100:,:]
 ytest= y[-100:]
 
 for i in (1, 2):
    m = xtrain[:,i].mean()
    s = xtrain[:,i].std()
    xtrain[:,i] = (xtrain[:,i] - m) / s
    xtest[:,i] = (xtest[:,i] - m) / s
 
# for i in (1,2): 
#     
#  xtrain[:,i] = (xtrain[:,i] - xtrain[:,i].mean())/xtrain[:,i].std()
#  xtest[:,i] = (xtest[:,i] - xtest[:,i].mean())/xtest[:,i].std()
# 
 return  xtrain, ytrain, xtest, ytest


def get_binary_data_own():
  # return only the data where y is either 0 or 1
  
  Xtrain, Ytrain, Xtest, Ytest = loadcsvdata("ecommerce_data.csv") 
  
  X2train = xtrain[Ytrain <= 1]
  Y2train = Ytrain[Ytrain <= 1]
  X2test = Xtest[Ytest <= 1]
  Y2test = Ytest[Ytest <= 1]
  
  return X2train, Y2train, X2test, Y2test
m  = np.random.rand(8)
c = 0
def hypothesisNormal (m,c,row):
    sum = 0
    for i in range (len(m)):
        sum+=m[i]*row[i]
    sum+=c
    
    hyp = 1/ (1 + np.exp(-sum))
    return hyp
def hypothesis (m,c, row):
  
    z = row.dot(m) + c 
      
    hyp = 1/ (1 + np.exp(-z))
   
    return hyp

def logisticCostFun(m,c):
    
    count = len(ytrain)
    sum = 0
    for i in range(count):
      hyp = hypothesis(m,c,xtrain[i])
      l1 = np.log(hyp)
      l2 = np.log((1- hyp))
      sum+=  ytrain[i]* l1 + (1-ytrain[i]) * l2
 
    c = (-1 * sum) /count
    return c

def logisticGD(m,c, lr):
    tm = np.zeros(cols+3)
    rows = len(ytrain)
    ct= 0
    for i in range(len(tm)): # for theta j i.e. all parameter
        for j in range(rows): # rows
            tm[i]+=(hypothesis(m,c,xtrain[j]) - ytrain[j] ) * xtrain[j][i]  
        
    for j in range(rows):
            ct+=(hypothesis(m,c,xtrain[j]) - ytrain[j] )   
    for i in range(len(tm)):
       m[i] = m[i] - (lr * tm[i])
    c = c - (lr *ct)
    return m,c
#xtrain, ytrain, xtest, ytest =   get_binary_data()
from process import get_binary_data

# get the data
xtrain, ytrain, xtest, ytest = get_binary_data()

xtrain1, ytrain1, xtest1, ytest1 = get_binary_data()

def Accuracy(m,c):
    rp =0
    wp = 0
    pred = []
    for i in range(len(ytest)):
        h = hypothesis(m,c,xtest[i])
        
        hp = h
        pred.append(h)
        if (h>=0.5):
            h=1
        else:
            h=0
        if (h==ytest[i]):
            rp+=1
        else:
            print (hp, ytest[i])
            wp+=1
    acc = rp/len(ytest)
    print ("Accuracy " ,rp, wp, acc)
    
m= np.zeros(cols+3)
c = 0

epocs = 500
lr = 0.0001
res = []
for i in range(epocs):
    res.append(logisticCostFun(m,c) )
    #print (c , m )
    m,c = logisticGD(m,c,lr)
print (c, m, "res = ")
Accuracy(m,c)