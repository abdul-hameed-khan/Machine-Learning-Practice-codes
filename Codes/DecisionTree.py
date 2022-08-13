# -*- coding: utf-8 -*-
"""
Created on Mon Oct 11 14:33:36 2021

@author: Kashif Bilal
"""

from sklearn.datasets import load_iris
from sklearn.tree import DecisionTreeClassifier

iris = load_iris()
X = iris['data']
y = iris['target']


from sklearn.model_selection import train_test_split
Xtrain,Xtest,Ytrain,Ytest =  train_test_split(X,y,test_size=0.2)



classifier = DecisionTreeClassifier(max_depth=2) #criterion = 'entropy', random_state = 0)
classifier.fit(Xtrain, Ytrain)

# Predicting the Test set results
Ypred = classifier.predict(Xtest)
# Creating the Confusion Matrix
from sklearn.metrics import confusion_matrix
cm = confusion_matrix(Ytest, Ypred)
print ("Decision accuracy " ,  (cm[0,0]+cm[1,1]+cm[2,2])/Ypred.shape)

f = open("iris_tree.dot", 'w')
from sklearn.tree import export_graphviz
a =export_graphviz( classifier,  out_file="iris_tree2.dot", feature_names=iris.feature_names, class_names=iris.target_names, rounded=True, filled=True )

from graphviz import Source

dot_path = "C:/Users/Zulfiqar/Desktop/tree.dot"
output = Source.from_file("iris_tree2.dot", format = "png") # can change png to pdf
output.view()