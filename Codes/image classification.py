# -*- coding: utf-8 -*-
"""
Created on Mon Dec 27 17:54:16 2021

@author: Kashif Bilal
"""

import tensorflow as tf
from tensorflow import keras

fashion_mnist = keras.datasets.fashion_mnist
(X_train_full, y_train_full), (X_test, y_test) = fashion_mnist.load_data()
class_names = ["T-shirt/top", "Trouser", "Pullover", "Dress", "Coat",  "Sandal", "Shirt", "Sneaker", "Bag", "Ankle boot"]
X_train_full,X_valid = X_train_full[:5000]/255.0, X_train_full[5000:]/255.0
y_train_full,y_valid = y_train_full[:5000], y_train_full[5000:]
X_test = X_test/255.0
model = keras.models.Sequential()
model.add(keras.layers.Flatten(input_shape=[28, 28]))
model.add(keras.layers.Dense(300, activation="relu"))
model.add(keras.layers.Dense(100, activation="relu"))
model.add(keras.layers.Dense(10, activation="softmax"))

model.compile(loss="sparse_categorical_crossentropy",
 optimizer="adam",
 metrics=["accuracy"])

history = model.fit(X_train_full, y_train_full, epochs=30, validation_data=(X_valid, y_valid))

model.evaluate(X_test,y_test)
prob = model.predict(X_test[:5])
prob.round(2)
model.predict_classes (X_test[:5])