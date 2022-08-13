# -*- coding: utf-8 -*-
"""
Created on Mon Aug 23 16:05:21 2021

@author: Zulfiqar

*****steps for trainig a model**********

structured data 
load using pandas
cleaning
Matrix (.values) --> we always convert data (specifically text) into numbers using label 
encoder

imputer (average)
fit_tansform 
fit -> take mean
transform ->will put mean in empty cells

Capital Letter.......L -> class
small Letters........=i -> package name


Data Scaling and splitting 
Fittting MOdels
********************

Actual-------pred
+--------+......TP
+=========-......fN
-===========-...TN
-===========+....FP



.....
Binary Classificaton----2 classes
Multi class Classification----3 or more classes



"""

import pandas as pd

import matplotlib as plt
df = pd.read_csv("datasetLinear.csv")
X = df.iloc[:,0:1].values
Y = df.iloc[:,1:2].values

from sklearn.model_selection import train_test_split
Xtrn,Xtest,Ytest,Ytrn = train_test_split(X,Y,test_size=0.2,shuffle=1)

from sklearn.linear_model import LinearRegression
lr = LinearRegression()
lr.fit(Xtrn,Ytrn)
print(lr.intercept_, lr.coef_)

predictions = lr.predict(Xtest)
plt.scatter(Xtrn,Ytrn,color='red')

plt.plot(Xtest,lr.predicy(Xtest), color = 'blue')
plt.show()

