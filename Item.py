import enum

import pandas as pd
from PIL import Image
import scipy
from scipy import cluster
import numpy as np
from scipy.spatial import distance
import tensorflow as tf
from tensorflow import keras
import matplotlib as plt

class ClothingType(enum.Enum):
    Tshirt = 0
    Trouser = 1
    Pullover = 2
    Dress = 3
    Coat = 4
    Sandal = 5
    Shirt = 6
    Sneaker = 7
    Bag = 8
    Boot = 9

class FabricType(enum.Enum):
    cotton = 1
    polyester = 2
    synthetic = 3
    nylon = 4
    pique = 5
    silk = 6
    fleece = 7
    linen = 8
    lycra = 9

class ItemShape(enum.Enum):
    skinny = 1
    fit = 2
    average = 3
    loose = 4

class ItemThickness(enum.Enum):
    light = 1
    medium = 2
    thick = 3

def findFabricColor(picture_path : str, clusterParameter=3):
    imageMatrix = plt.image.imread(picture_path)[190:290, 190:290, :]
    df = pd.DataFrame()
    df['r'] = pd.Series(imageMatrix[:,:,0].flatten())
    df['g'] = pd.Series(imageMatrix[:,:,1].flatten())
    df['b'] = pd.Series(imageMatrix[:,:,2].flatten())
    df['processedR'] = scipy.cluster.vq.whiten(df['r'])
    df['processedG'] = scipy.cluster.vq.whiten(df['g'])
    df['processedB'] = scipy.cluster.vq.whiten(df['b'])
    clusterNodes, distortionParameter = scipy.cluster.vq.kmeans(df[['processedR','processedG','processedB']], clusterParameter)
    extractedColors = []
    stdvR, stdvG, stdvB = df[['r','g','b']].std()
    for color in clusterNodes:
        extractedColors.append((stdvR*color[0], stdvG*color[1], stdvB*color[2]))
    if (distance.euclidean(extractedColors[1],extractedColors[2]) < 16) or\
            (distance.euclidean(extractedColors[0],extractedColors[2]) < 16):
        extractedColors.remove(extractedColors[2])
    if distance.euclidean(extractedColors[0],extractedColors[1]) < 16:
        extractedColors.remove(extractedColors[1])
    return extractedColors

class Item:
    def __init__(self, picture_path , clothing_type):
        self.colors = findFabricColor(picture_path)
        self.picture_path = picture_path
        self.clothing_type = clothing_type
