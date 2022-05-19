import pickle

import numpy as np
import pandas as pd
import torch
import pickle
import torch.optim.adamax
from torchvision.datasets import FashionMNIST
from keras.layers import Dense, MaxPooling2D, Conv2D, Flatten, Dropout, BatchNormalization, LeakyReLU
from keras.optimizer_v2.adamax import Adamax
from keras.models import Sequential
from keras.preprocessing.image import ImageDataGenerator
from keras.utils.np_utils import to_categorical
from torch import nn


class RecognitionNetwork:
    def __init__(self):
        self.train_set = np.array(pd.read_csv("fashion-mnist_train.csv"), dtype='float32')
        self.test_set = np.array(pd.read_csv("fashion-mnist_test.csv"), dtype='float32')
        trainX = self.train_set[:, 1:]
        trainY = to_categorical(self.train_set[:, 0])
        testX = self.test_set[:, 1:]
        testY = to_categorical(self.test_set[:, 0])
        trainX = trainX.reshape(trainX.shape[0], 28, 28, 1) / 255
        testX = testX.reshape(testX.shape[0], 28, 28, 1) / 255
        self.model = Sequential()
        self.model.add(Conv2D(256,kernel_size=(3,3), input_shape=(28,28,1)))
        self.model.add(MaxPooling2D(pool_size=(2, 2)))
        self.model.add(BatchNormalization())
        self.model.add(LeakyReLU(0.1))
        self.model.add(Dropout(0.1))
        self.model.add(Conv2D(128, (3, 3)))
        self.model.add(BatchNormalization())
        self.model.add(LeakyReLU(0.1))
        self.model.add(Dropout(0.1))
        self.model.add(Flatten())
        self.model.add(Dense(256))
        self.model.add(LeakyReLU(0.1))
        self.model.add(BatchNormalization())
        self.model.add(Dropout(0.1))
        self.model.add(Dense(10, activation='softmax'))
        self.model.summary()
        self.data_generator = ImageDataGenerator()
        self.data_generator.get_random_transform(img_shape=(28,28,1),seed=3)
        self.data_generator.flow(x=trainX, y=trainY, batch_size=25, shuffle=True,
                                 sample_weight=None, seed=None, save_to_dir=None,
                                 save_prefix='', save_format='png', subset=None)
        self.data_generator.fit(trainX)
        self.model.compile(optimizer=Adamax(), loss='categorical_crossentropy',
                           metrics=['accuracy'])
        self.score = 0
        self.loss = None
        self.model.fit(trainX, trainY, batch_size=25, epochs=20,
                       verbose=1, validation_data=(testX, testY))

    def predict(self, x):
        prediction = self.model.predict(x)
        prediction = prediction.astype('int')
        return prediction

if __name__ == '__main__':
    neuralNetwork = RecognitionNetwork()
    pickle.dump(neuralNetwork, open('/Users/ylias.2001/Desktop/OUTFIT/NeuralNetwork.sav','wb'))