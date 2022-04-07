import numpy as np
import torch
from torchvision import transforms, datasets
from torch import nn
from torch import optim


class RecognitionNetwork:
    def __init__(self, epochs=50):
        self.transform = transforms.Compose(
            [transforms.ToTensor(), transforms.Normalize((0.5,), (0.5,))])
        self.trainset = datasets.FashionMNIST('~/.pytorch/F_MNIST_data/',
                                              download=True, train=True,
                                              transform=self.transform)
        self.trainloader = torch.utils.data.DataLoader(self.trainset,
                                                       batch_size=64,
                                                       shuffle=True)
        self.model = nn.Sequential(nn.Linear(784, 392), nn.ReLU(),
                                   nn.Linear(392, 196), nn.ReLU(),
                                   nn.Linear(196, 98), nn.ReLU(),
                                   nn.Linear(98, 49), nn.ReLU(),
                                   nn.Linear(49, 10), nn.ReLU())
        self.optimizer = optim.SGD(self.model.parameters(), lr=0.1)
        self.lossFunc = nn.NLLLoss()
        self.epochs = epochs
        self.score = 0
        self.loss = None
        self.itemTypes = ['T-shirt/top', 'Trouser', 'Pullover', 'Dress', 'Coat'
                          , 'Sandal', 'Shirt', 'Sneaker', 'Bag', 'Ankle Boot']

    def train(self):
        for iter in range(self.epochs):
            iterLoss = 0
            for image, clothingType in self.trainloader:
                currCloth = image.view(image.shape[0], -1)
                self.optimizer.zero_grad()
                self.score = self.model(currCloth)
                self.loss = self.lossFunc(self.score, clothingType)
                self.loss.backward()
                self.optimizer.step()
                iterLoss += self.loss.item()

    def classify(self, image):
        result = torch.exp(self.model(image))
        classification = np.argmax(result)
        return self.itemTypes[classification]
