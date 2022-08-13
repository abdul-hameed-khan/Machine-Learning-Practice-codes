# -*- coding: utf-8 -*-
"""
Created on Thu Apr 29 16:08:35 2021

@author: Admin
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_csv("ecommerce_data.csv")


df2 = df.loc[df["user_action"]<=1]

X = df2.iloc[:,:-1].values
Y = df2.iloc[:,5].values

from sklearn.model_selection import train_test_split
Xtrain,Xtest,Ytrain,Ytest =  train_test_split(X,Y,test_size=0.2)

# scale column 2 and 3

from sklearn.preprocessing import StandardScaler

sc = StandardScaler()
Xtrain[:,1:3] = sc.fit_transform(Xtrain[:,1:3])
#print ("mean " , sc.mean_,"var ", sc.var_,sc.scale_)
Xtest[:,1:3] = sc.transform(Xtest[:,1:3])
#print (sc.mean_, sc.var_,sc.scale_)


from sklearn.preprocessing import OneHotEncoder
from sklearn.compose import ColumnTransformer # categorical feature is removed 

#ohe = OneHotEncoder(categorical_features = [4]) # depricated and not working
ohe = ColumnTransformer([('encoder', OneHotEncoder(), [4])],     remainder='passthrough')
# first argument is just aa name, second is one hotencoder class , and third is column numer. reminder means that dont change other features
#Xtrain = ohe.fit_transform(Xtrain).toarray()
#Xtest = ohe.fit_transform(Xtest).toarray()
Xtrain = ohe.fit_transform(Xtrain)
Xtest = ohe.fit_transform(Xtest)
# Remove toarray() as well 

from sklearn.linear_model import LogisticRegression
classifier = LogisticRegression()
classifier.fit(Xtrain,Ytrain)

Ypred = classifier.predict(Xtest)

from sklearn.metrics import confusion_matrix
cm = confusion_matrix(Ytest,Ypred)
print ("LR accuracy " ,
       (cm[0,0]+cm[1,1])/Ypred.shape)

from sklearn.metrics import classification_report
#print(classification_report(Ytest,Ypred))


from sklearn.neighbors import KNeighborsClassifier

#for i in range(1):
classifier = KNeighborsClassifier(n_neighbors=10)
classifier.fit(Xtrain,Ytrain)
#
Ypred = classifier.predict(Xtest)
cm = confusion_matrix(Ytest,Ypred)
print ("Kmean accurcy: ",1," ", (cm[0,0]+cm[1,1])/Ypred.shape)
 

from sklearn.svm import SVC

classifier = SVC(kernel = 'poly', degree=2)
classifier.fit(Xtrain,Ytrain)

Yp = classifier.predict(Xtest)

cm = confusion_matrix(Ytest,Yp)
print ("SVM accuracy " ,  (cm[0,0]+cm[1,1])/Ypred.shape)

from sklearn.tree import DecisionTreeClassifier
classifier = DecisionTreeClassifier(criterion = 'entropy', random_state = 0)
classifier.fit(Xtrain, Ytrain)

# Predicting the Test set results
Ypred = classifier.predict(Xtest)
# Creating the Confusion Matrix
from sklearn.metrics import confusion_matrix
cm = confusion_matrix(Ytest, Ypred)
print ("Decision accuracy " ,  (cm[0,0]+cm[1,1])/Ypred.shape)

from sklearn.ensemble import RandomForestClassifier
classifier = RandomForestClassifier(n_estimators = 100, criterion = 'entropy', random_state = 0)
classifier.fit(Xtrain, Ytrain)

# Predicting the Test set results
Ypred = classifier.predict(Xtest)

# Creating the Confusion Matrix
from sklearn.metrics import confusion_matrix
cm = confusion_matrix(Ytest, Ypred)
print ("Random Forest" ,  (cm[0,0]+cm[1,1])/Ypred.shape)

from sklearn.naive_bayes import GaussianNB
classifier = GaussianNB()
classifier.fit(Xtrain, Ytrain)

# Predicting the Test set results
Ypred = classifier.predict(Xtest)
# Creating the Confusion Matrix
from sklearn.metrics import confusion_matrix
cm = confusion_matrix(Ytest, Ypred)
print ("Naive Bayese accuracy " ,  (cm[0,0]+cm[1,1])/Ypred.shape)

