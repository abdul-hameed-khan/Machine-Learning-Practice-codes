import matplotlib.pyplot as plt

import math
rows = 100
params = 3
x = []
y = []
tt = []
ln=0
m = [0,0,0]

# h = m0x0 + m1x1^2+m2X2

def loadcsvdata(name):
 ln = 0
 for line in open(name):
    vals = line.split(',')
    x.append([0,0,0])
    x[ln][0]=1
    x[ln][1]=  float(vals[0]) * float(vals[0]) ;
    x[ln][2]=  float(vals[0]) ;
    
    tt.append(float(vals[0]) )
    ln+=1
    
    y.append(float(vals[1]))
loadcsvdata("data_poly.csv")   
n = len (x)
plt.scatter(tt,y)
plt.show()

#
def hypothesis (m):
    h = m[0]*x[0] + m[1]*x[1] +m[2]*x[2]
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
    tm = [0,0,0]
    for j in range(params):#find all parametres , m10, m1, m2 
       
       for i in range(n): # loop for all lines in x matrix 
           tmp =0
           for k in range (params): # for all parameetrs 
               tmp+=m[k]*x[i][k]
           tm[j] +=(tmp - y[i]) * x[i][j] 
           #((m[0]*x[i][0] + m[1]*x[i][1] + m[2]*x[i][2]) - y[i])*x[i][j]
          
       tm[j] = (1/n) * tm[j]
    
    m[0]= m[0] - lr *  tm[0]
    m[1] = m[1] - lr *  tm[1]
    m[2] = m[2] - lr *  tm[2]
    #if (abs(m-temp1)) <0.000001) and (abs(c-temp2))<0.000001)):
     #   stop=1
    #print (m)
    return m,stop
errors = []
lr = 0.000000093
err1=100000000000
xaxis = []
epocs =100000
for i in range (epocs):
    err = calcErrorMVR(m)
   
    errors.append(err)
    
    xaxis.append(i)
#    if (err>err1):
#        print (err - err1 , i)
#        break
#    err1 = err
##    if i>0:
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
   
#plt.scatter(xaxis,errors)
#plt.show()    
print(errors[len(xaxis)-1])   
sm = 0
