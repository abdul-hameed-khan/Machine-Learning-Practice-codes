import matplotlib.pyplot as plt

import math

params = 6
x = []
y = []
tt = []
ln=0
m = [0,0,0,0,0,0]
norm = [1,7,5.75,7880,1074218,3.5,7700000]

def loadcsvdata(name):
 ln = 0
 for line in open(name):
    
    vals = line.split(',')
    x.append([1,0,0,0,0,0])
    for i in range(1,params):
          
        x[ln][i]=  float(vals[i+3])/norm[i];
    tt.append(ln)
    ln+=1
    y.append(float(vals[2]))
    if ln>=1000:
        break
loadcsvdata("kc_house_data_2.csv")   
n = len (x)
#plt.scatter(tt,y)
#plt.show()

def calcErrorMVR(m):
    error = 0;
    for i in range(n):
        sum=0.0;
        for j in range(params):
            sum = sum +  x[i][j] * m[j];
        error += (sum - y[i])**2
    error = error/(2*n)
    return error

def GDMVR(m):
    
    stop = 0
    tm = [0,0,0,0,0,0]
    for j in range(params):
       
       for i in range(n): 
           tmp =0
           for k in range (params):
               tmp+=m[k]*x[i][k]
           tm[j] +=(tmp - y[i]) * x[i][j] 
           #((m[0]*x[i][0] + m[1]*x[i][1] + m[2]*x[i][2]) - y[i])*x[i][j]
          
       tm[j] = (1/n) * tm[j]
    
       m[j]= m[j] - lr *  tm[j]
     #if (abs(m-temp1)) <0.000001) and (abs(c-temp2))<0.000001)):
     #   stop=1
    return m,stop
errors = []
lr = 0.000003
err1= calcErrorMVR(m)*2
xaxis = []

for i in range (10000):
    if (i%30==0):
     err = calcErrorMVR(m)
     errors.append(err)
     print (err)
     xaxis.append(i)
     if (err>=err1):
        print (err - err1 , i)
        break
     err1 = err
#    if i>0:
#     yhat = []
#     for i in range(n):
#        y2 = (m*x[i]+c)
#        yhat.append(y2);
# 
#     plt.scatter(x,y)
#     plt.plot(x,yhat)    
#     plt.show()

    #ma.append(m)
    #ca.append(c)
    #e.append(err)
    
       
    m,stop = GDMVR(m)
    if (stop==1):
        print ('stopped at ',i)
        break;
err = calcErrorMVR(m) 
print (err)  
#plt.scatter(xaxis,errors)
#plt.show()    
#print(errors[len(xaxis)-1])   