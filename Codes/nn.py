# -*- coding: utf-8 -*-
"""
Created on Sat Jun 26 11:38:39 2021

@author: eisha
"""

import pandas as pd

#Reading CSV data file into Python
dataset = pd.read_csv('Medical_data.csv')
X = dataset.iloc[:, 0:8].values
y = dataset.iloc[:, 8].values

# Dividing dataset into Training set and Testing set
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.2, random_state = 0)

# Scaling Inputs
from sklearn.preprocessing import StandardScaler
sc = StandardScaler()
X_train = sc.fit_transform(X_train)
X_test = sc.transform(X_test)

# Importing Keras libraries
from keras.models import Sequential
from keras.layers import Dense

classifier = Sequential()

# Adding input layer and first hidden layer
classifier.add(Dense(units = 5, activation = 'relu', input_dim = 8))

# Adding second hidden layer
classifier.add(Dense(units = 10, activation = 'relu'))

# # Adding 3rd hidden layer
classifier.add(Dense(units = 10, activation = 'relu'))

# Adding 4th hidden layer
classifier.add(Dense(units = 5, activation = 'relu'))

# Adding output layer
classifier.add(Dense(units = 1,  activation = 'sigmoid'))

# Compiling ANN Algorithm
classifier.compile(optimizer = 'adam', loss = 'binary_crossentropy', metrics = ['accuracy'])

# Fitting ANN Algorithm to Training set
classifier.fit(X_train, y_train, batch_size = 10, epochs = 500)

# # Predicting y_test using X_test 
y_pred = classifier.predict(X_test)
y_pred = (y_pred >= 0.5)

# #Creating Confusion Matrix
from sklearn.metrics import confusion_matrix
cm = confusion_matrix(y_test, y_pred)