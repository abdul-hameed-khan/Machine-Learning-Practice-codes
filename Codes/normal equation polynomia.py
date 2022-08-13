import matplotlib.pyplot as plt
import numpy as np
features = 3
ox= np.zeros(100)
x = np.zeros((100,features))
y = np.zeros(100)
m = np.zeros(3) # quardratic function ax+bx^2+c
count = len(y)

def loadcsvdata(name):
 i=0
 for line in open(name):
    vals = line.split(',')
    x[i][0] =1
    x[i][1] = (float(vals[0])* float(vals[0]))
    x[i][2] = (float(vals[0]))
    ox[i]=(float(vals[0]))
    y[i] = (float(vals[1]))
    i=i+1
loadcsvdata("data_poly.csv")   
count = len(x)


n = len (x)
def NormalEquation(x, y):
    xt = x.transpose()
    x1 = xt.dot(x);
    xinv = np.linalg.pinv(x1)
    
    x2 = np.dot (xinv,xt)
    tht = np.dot(x2,y)
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