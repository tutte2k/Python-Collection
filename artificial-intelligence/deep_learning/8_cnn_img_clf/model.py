import pickle

import tensorflow as tf
from keras import datasets,layers,models
import matplotlib.pyplot as plt
import numpy as np


(X_train,y_train),(X_test,y_test) = datasets.cifar10.load_data()

y_train = y_train.reshape(-1,)


X_train = X_train/255
X_test = X_test/255

cnn = models.Sequential([
    layers.Conv2D(filters=32, kernel_size=(3, 3), activation='relu', input_shape=(32, 32, 3)),
    layers.MaxPooling2D((2, 2)),
    
    layers.Conv2D(filters=64, kernel_size=(3, 3), activation='relu'),
    layers.MaxPooling2D((2, 2)),
    
    layers.Flatten(),
    layers.Dense(64, activation='relu'),
    layers.Dense(10, activation='softmax')
])


cnn.compile(optimizer='adam',
              loss='sparse_categorical_crossentropy',
              metrics=['accuracy'])

cnn.fit(X_train,y_train,epochs=10)

with open('model_pickle','wb') as f:
    pickle.dump(cnn,f)