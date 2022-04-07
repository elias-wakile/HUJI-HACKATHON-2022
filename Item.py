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
    shortSleeve = 1
    longSleeve = 2
    dressShirt = 3
    Hoodie = 4
    sweater = 5
    lightJacket = 6
    jacket = 7
    coat = 8
    trenchCoat = 9
    suit = 10
    vest = 11
    tights = 12
    pants = 13
    jeans = 14
    elegantPants = 15
    skirt = 16
    dress = 17
    dungarees = 18
    sportiveShoes = 19
    casualShoes = 20
    elegantShoes = 21
    cap = 22
    hat = 23
    umbrella = 24

class FabricType(enum.Enum):
    cotton = 1
    polyester = 2
    synthetic = 3
    nylon = 4
    pique = 5
    silk = 6
    fleece = 7
    linen = 8

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
    imageMatrix = plt.image.imread(picture_path)[70:370, 70:370, :]
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
    def __init__(self, picture_path: str,
                 fabric_path: str,
                 clothing_type : ClothingType,
                 item_thickness : ItemThickness,
                 item_shape : ItemShape):
        self.fabric_path = fabric_path
        self.colors = findFabricColor(picture_path)
        self.picture_path = picture_path
        self.clothing_type = clothing_type
        self.item_thickness = item_thickness
        self.item_shape = item_shape