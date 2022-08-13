# -*- coding: utf-8 -*-
"""
Created on Fri Oct  1 11:31:58 2021

@author: Kashif Bilal
"""

'''
Steps :
    1. Some labeled data
        We are working on points
        We need to have x and y value for each 
        We need to have a label for each point
        
        Then 
        We will introduce a new point with no class
        and we will try top predict the class/value for new point
        
'''

import numpy as np

x = np.random.randint(0,10,20)
y = np.random.randint(0,10,20)
labels = np.random.randint(0,2,20)

points = np.random.randint(0,10,(20,2))

# bax = []
# bay = []
# rax = []
# ray = []

# for i in range (len (labels)):# range (20)
#     if labels[i]==0:
#         bax.append(x[i])
#         bay.append(y[i])
#     else:
#         rax.append(x[i])
#         ray.append(y[i])
bx = x[labels==0] 
'''it meansselect only those values from x where oncorresonding index 
of labels class is 0'''

nx = np.random.randint(0,10,1)
ny = np.random.randint(0,10,1)

from matplotlib  import pyplot as plt
# We want to show the point with label 0 in blue and the point with label 1 in red  
plt.scatter(x[labels==0],y[labels==0],c='blue')
plt.scatter(x[labels==1],y[labels==1], c='red')
plt.scatter(nx,ny, c='black')

dist = np.zeros(20)
for i in range(len (x)):
    dist[i] = np.sqrt( ((nx - x[i])**2) + ((ny - y[i])**2) )
k=3
inds = np.argsort(dist)[:k] # argsort return the indexes in sorted order. We may slice it to get smallest k inexes


zr =0 
on = 0
for i in inds:
    if (labels[i]==0):
        zr+=1
    else:
        on+=1
if (zr>on):
    print ('point is labeld blue with class 0 with blue  neighbors ', zr , ' red labels ', on)
else:
     print ('point is labeld red with class 1 with 1 neighbors ', on)
    