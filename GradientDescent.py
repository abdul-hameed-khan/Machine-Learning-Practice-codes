
import matplotlib.pyplot as plt

x=[2,4,8,16,32,64]
y=[10,20,30,40,50,60]

err=[]
mvals=[]

n=len(x)

def ErrorCalc(m,c):
    sum=0
    for i in range(n):
        sum+=(m*x[i]+c-y[i])**2
    j=sum/(2*n)
    print('error with m = ','%.2f' %m,' and c = ',c,' is ','%.2f' %j)
    return j

def GradientDescent(m,c):
    mt=0
    ct=0
    for i in range(n):
        mt = mt+ ((m*x[i]+c-y[i])*x[i])
        ct = ct+ ((m*x[i]+c-y[i]))
    m = m - lr * (mt / n)
    c = c - lr * (ct / n)
    return m,c
epocs=100
m=0
c=0
lr=0.0001
for counter in range(epocs):
    error = ErrorCalc(m,c)
    mvals.append(m)
    err.append(error)
    m,c=GradientDescent(m, c)


plt.scatter(mvals,err)
plt.show() 
