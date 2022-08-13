
import matplotlib.pyplot as plt 

x=[5,10,15,20,25,30]
y=[2,4,6,8,10,12]

n = len(x)
m=0
c=0
error=[]
mval=[]

for count in range(20):
    sum=0
    for i in range(n):
        sum+=(x[i]*m+c-y[i])**2
    j=sum/(2*n)
    print('error with m = ','%.2f' %m,' and c = ',c,' is ','%.2f' %j)
    mval.append(m)
    error.append(j)
    m+=0.1
   

plt.scatter(mval,error)
plt.show()




"""

x=[5,10,15,20,25,30]
y=[2,4,6,8,10,12]

n = len(x)

m=0.40
c=0



for i in range(n):
    
    sum=(x[i]*m+c-y[i])**2
j=sum/(2*n)
print('error with m = ','%.2f' %m,' and c = ',c,' is ','%.2f' %j)
   

x1=int(input("Enter the value of x to predict : "))
h=(m*x1)+c
print('the predicted value is ',h)
"""