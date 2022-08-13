import matplotlib.pyplot as plt

import math
rows = 100
params = 3
x = []
y = []
tt = []
ln=0
m = [0,0,0]

def loadcsvdata(name):
 ln = 0
 for line in open(name):
    vals = line.split(',')
    x.append([0,0,0])
    for i in range(params):
          
        x[ln][i]=  float(vals[i]);
    tt.append(ln)
    ln+=1
    
    y.append(float(vals[params]))
loadcsvdata("data_2d.csv")   
n = len (x)
plt.scatter(tt,y)
plt.show()

# X * transpose (m)
# where X is feature martix, with x0 =1, and m is parameter vector
def calcErrorMVR(m):
    #𝟏/𝟐𝒎  ∑1_(𝒊=𝟏)^𝒎▒(∑1_(𝑗=0)^𝑛▒〖𝜃_𝑗 𝑥_𝑗^((𝑖))  〗− 𝒚^𝒊  )^𝟐 
    error = 0;
    for i in range(n):
        sum=0.0;
        for j in range(params):
            sum = sum +  x[i][j] * m[j];
        error += (sum - y[i])**2
    error = error/(2*n)
    return error 
    # X * 
    #return error = (np.sum ( X.dot (m) - y )**2)) / (2 * len(m))

def GDMVR(m):
    
    stop = 0
    tm = [0,0,0]
    for j in range(params):#find all parametres , m0, m1, m2 
       
       for i in range(n): # loop for all lines in x matrix 
           tmp =0
           for k in range (params): # for all parameetrs 
               tmp+=m[k]*x[i][k]
           tm[j] +=(tmp - y[i]) * x[i][j] 
           #np.sum (( X.dot (m) - y ) * x[:,j])
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
lr = 0.00025
err1=100000000000
xaxis = []
epocs =200000
for i in range (epocs):
    err = calcErrorMVR(m)
   
    errors.append(err)
    
    xaxis.append(i)
    if (err>err1):
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
   
#plt.scatter(xaxis,errors)
#plt.show()    
print(errors[-1], m)   
sm = 0
