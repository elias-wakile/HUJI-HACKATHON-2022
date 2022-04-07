import numpy as np
import pandas as pd
import torch
import matplotlib.pyplot as plt
from keras.models import Sequential
from keras.optimizer_v2.adamax import Adamax
from keras.utils.np_utils import to_categorical
import keras.layers
from keras.layers import Dense,MaxPooling2D, Conv2D, Flatten,Dropout,BatchNormalization
from keras.preprocessing.image import ImageDataGenerator
import torch.optim.adamax
from keras.callbacks import TensorBoard
from torchvision import transforms, datasets
from torch import nn
from torch import optim


class RecognitionNetwork:
    def __init__(self):
        self.train_set = np.array(pd.read_csv("../input/fashionmnist/fashion-mnist_train.csv"), dtype='float32')
        self.test_set = np.array(pd.read_csv("../input/fashionmnist/fashion-mnist_test.csv"), dtype='float32')
        trainX = self.train_set[:, 1:]
        trainY = self.train_set[:, 0]
        trainY = to_categorical[trainY[:,0]]
        testX = self.test_set[:, 1:]
        testY = self.test_set[:, 0]
        testY = to_categorical[testY[:,0]]
        trainX = trainX.reshape(trainX.shape[0], 28, 28, 1) / 255
        testX = testX.reshape(testX.shape[0], 28, 28, 1) / 255
        self.model = nn.Sequential()
        self.model.add(Conv2D(256,kernel_size=(3,3), input_shape=(28,28,1)))
        self.model.add(MaxPooling2D(pool_size=(2, 2)))
        self.model.add(BatchNormalization())
        self.model.add(LeakyReLu(0.1))
        self.model.add(Dropout(0.1))
        self.model.add(Conv2D(128, (3, 3)))
        self.model.add(BatchNormalization())
        self.model.add(LeakyReLu(0.1))
        self.model.add(Dropout(0.1))
        self.model.add(Flatten())
        self.model.add(Dense(256))
        self.model.add(LeakyReLu(0.1))
        self.model.add(BatchNormalization())
        self.model.add(Dropout(0.1))
        self.model.add(Dense(10, activation='softmax'))
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
        self.itemTypes = ['T-shirt/top', 'Trouser', 'Pullover', 'Dress', 'Coat'
                          , 'Sandal', 'Shirt', 'Sneaker', 'Bag', 'Ankle Boot']
        self.model.fit(trainX, trainY, batch_size=25, epochs=5,
                       verbose=1, validation_data=(testX, testY))
        ###########
        y_head = self.model.predict(testX)
        y_predict = np.argmax(y_head, axis=1)
        y_true = np.argmax(testY, axis=1)
        comparison = pd.DataFrame()
        comparison["prediction"] = y_predict
        comparison["true"] = y_true
        comparison['correct'] = comparison.prediction == comparison.true
        comparison["correct"].value_counts()
        comparison[comparison['correct'] == False]
        print(comparison.shape)

    def classify(self, image):
        result = torch.exp(self.model(image))
        classification = np.argmax(result)
        return self.itemTypes[classification]
