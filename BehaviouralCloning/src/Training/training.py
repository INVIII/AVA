import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import PIL
import cv2
import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.optimizers import Adam
from tensorflow.keras.layers import Conv2D, MaxPooling2D, Dropout, Flatten, Dense, LSTM, Reshape, Input, Concatenate, ZeroPadding2D, GlobalMaxPool2D
from tensorflow.keras.models import Model
import h5py

store = pd.HDFStore('store.h5')
df = store['df']

train_data = np.array(df['images'])

x_test = train_data[8000:]
x_train = train_data[:8000]

def reshapeImg(img):
    img = np.reshape(img, (200, 200, -1))
    img = np.mean(img, axis=2)
    return img


x_train = list(map(reshapeImg, x_train))
x_test = list(map(reshapeImg, x_test))

y_train = []
for i in range(10000):
    temp = [df.iloc[i][1], df.iloc[i][2], df.iloc[i][3]]
    y_train.append(temp)


y_train = np.array(y_train)
x_train = np.array(x_train)
x_test = np.array(x_test)

y_test = y_train[8000:]
y_train = y_train[:8000]

x_train = np.expand_dims(x_train, -1)

def nvidia_modified():
  model = Sequential()

  #1st layer
  model.add(Conv2D(24, kernel_size=(5,5), strides=(2,2), input_shape=(200, 200,1),activation='elu'))

  #2nd layer
  model.add(Conv2D(36, kernel_size=(5,5), strides=(2,2), activation='elu'))

  #3rd layer
  model.add(Conv2D(48, kernel_size=(5,5), strides=(2,2), activation='elu'))

  #4th layer
  model.add(Conv2D(64, kernel_size=(3,3), activation='elu'))

  #5th layer
  model.add(Conv2D(64, kernel_size=(3,3), activation='elu'))


  #1st Dense Layer
  model.add(Flatten())
  model.add(Dense(100, activation='elu'))
  #model.add(Dropout(0.5))

  #2nd Dense Layer
  model.add(Dense(50, activation='elu'))
  #model.add(Dropout(0.5))

  #3rd Dense Layer
  model.add(Dense(10, activation='elu'))
  #model.add(Dropout(0.5))

  #output
  model.add(Dense(3))

  #Compile model
  model.compile(Adam(lr=0.001), loss = 'mse', metrics = ['accuracy'])
  return model

model = nvidia_modified()
r = model.fit(x_train, y_train, epochs=10)
model.save("model")