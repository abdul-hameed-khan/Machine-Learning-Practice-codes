# -*- coding: utf-8 -*-
"""
Created on Sun Mar  7 15:10:19 2021

Kashif Bilal

@author: Admin
"""



import numpy as np



cols=6
def loadcsvdata(name):
 
 i=0
 
 rows = 500
 flag = True
 x = np.zeros((rows,cols))
 x2 = np.zeros((rows,cols+3))
 y = np.zeros(rows)
 for line in open(name):
    if (flag):
        flag= False
        continue
    vals = line.split(',')
    x[i][0]=1
    for j in range(cols-1):
     x[i][j+1] = (float(vals[j]))
    y[i] = (int(vals[cols-1]))
    i=i+1
    count = len(x)
    
 #snp.random.shuffle(x)
 x2[:,0:5] = x[:,0:5]
 for i in range(500):
    a = int ( x[i][5])
    x2[i][(a+5)]=1
 xtrain = x2[0:-100,:]
 ytrain = y[0:-100]
 xtest = x2[-100:,:]
 ytest= y[-100:]
 
 for i in ( 2,3):
    m = xtrain[:,i].mean()
    s = xtrain[:,i].std()
    xtrain[:,i] = (xtrain[:,i] - m) / s
    xtest[:,i] = (xtest[:,i] - m) / s
 np.savetxt("oxt.csv",xtrain)
# for i in (1,2): 
#     
#  xtrain[:,i] = (xtrain[:,i] - xtrain[:,i].mean())/xtrain[:,i].std()
#  xtest[:,i] = (xtest[:,i] - xtest[:,i].mean())/xtest[:,i].std()
# 
 return  xtrain, ytrain, xtest, ytest


def get_binary_data_own():
  # return only the data where y is either 0 or 1
  
  Xtrain, Ytrain, Xtest, Ytest = loadcsvdata("ecommerce_data.csv") 
  
  X2train = Xtrain[Ytrain <= 1]
  Y2train = Ytrain[Ytrain <= 1]
  X2test = Xtest[Ytest <= 1]
  Y2test = Ytest[Ytest <= 1]
  
  return X2train, Y2train, X2test, Y2test
m  = np.random.rand(9)
def hypothesisNormal (m,c,row):
    sum = 0
    for i in range (len(m)):
        sum+=m[i]*row[i]
    
    
    hyp = 1/ (1 + np.exp(-sum))
    return hyp
def hypothesis (m, row):
  
    z = row.dot(m) 
      
    hyp = 1/ (1 + np.exp(-z))
   
    return hyp

def logisticCostFun(m):
    
    count = len(ytrain)
    sum = 0
    for i in range(count):
      hyp = hypothesis(m,xtrain[i])
      l1 = np.log(hyp)
      l2 = np.log((1- hyp))
      sum+=  ytrain[i]* l1 + (1-ytrain[i]) * l2
 
    cost = (-1 * sum) /count
    return cost

def logisticGD(m, lr):
    tm = np.zeros(cols+3)
    rows = len(ytrain)
    ct= 0
    for i in range(len(tm)):
        for j in range(rows):
            tm[i]+=(hypothesis(m,xtrain[j]) - ytrain[j] ) * xtrain[j][i]  
        
    for i in range(len(tm)):
        m[i] = m[i] - (lr * tm[i])
    
    return m
#xtrain, ytrain, xtest, ytest =   get_binary_data()
from process import get_binary_data

# get the data
xtrain, ytrain, xtest, ytest = get_binary_data_own()

xtrain1, ytrain1, xtest1, ytest1 = get_binary_data()

def Accuracy(m):
    rp =0
    wp = 0
    pred = []
    for i in range(len(ytest)):
        h = hypothesis(m,xtest[i])
        
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


epocs = 500
lr = 0.0001
res = []
for i in range(epocs):
    res.append(logisticCostFun(m) )
    #print (c , m )
    m = logisticGD(m,lr)
print ( m, "res = ")
Accuracy(m)