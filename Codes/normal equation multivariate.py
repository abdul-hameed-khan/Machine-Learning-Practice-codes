import matplotlib.pyplot as plt
import numpy as np
params = 2

x = np.zeros((100,params))

y = np.zeros(100);

theta = np.zeros(params)
def loadcsvdata(name, head):
 ln = 0
 for line in open(name):
    vals = line.split(',')
    if head==1:
       
        head=0
        continue
    x[ln][0] = 1
    for i in range(params-1):
        x[ln][i+1]=float(vals[i])
    y[ln] = float(vals[params-1])
    #y.append(float(vals[2]))
    ln=ln+1
loadcsvdata("data_1d.csv",0)   
count = len(x)
n = len (x)
def NormalEquation(x, y):
#    xt = x.transpose()
#    x1 = xt.dot(x);
#    xinv = np.linalg.pinv(x1)
#    
#    x2 = np.dot (xinv,xt)
#    tht = np.dot(x2,y)
    tht = np.linalg.pinv(x.T.dot(x)).dot( x.T.dot(y))
    return tht
theta = NormalEquation(x,y)
print ("Theta is " , theta)
def calcErrorNormal():
 error =0
 error =  np.sum((x.dot(np.transpose(theta)) - y)**2) /(2*count)
 #for i in range(count):
    #print (x[i] , y[i])
    #t = ((m*x[i][1]+c)-y[i]) ** 2
    #error += t
   
 #error = error/(2*n)
 return error

print ("Error is : " , calcErrorNormal())