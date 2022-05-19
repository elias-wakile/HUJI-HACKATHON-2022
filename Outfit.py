from os import listdir
import enum
import ClothsChoiceHeuristic
from ClothsChoiceHeuristic import SearchProblem
from PIL import Image
import pickle
import numpy
from Item import Item
from NeuralNetworkRecognition import RecognitionNetwork
PicturesDirectory = '/Users/ylias.2001/Desktop/OUTFIT/Pictures'
PickleNameFile = '/Users/ylias.2001/Desktop/OUTFIT/outfitDirectory.sav'

class dressingType(enum.Enum):
    comfy = 1
    casual = 2
    elegant = 3

def load_pickle_outfit():
    return pickle.load(open(PickleNameFile,'rb'))

def create_new_pickle(neuralNetwork: RecognitionNetwork):
    outfitList = []
    for imagePath in listdir(PicturesDirectory):
        image = Image.open(PicturesDirectory + '/' + imagePath)
        resizedImage = image.resize((28, 28))
        monochromeImage = resizedImage.convert('L')
        imageArray = numpy.asarray(monochromeImage, dtype='int')
        clothingType = neuralNetwork.predict(imageArray)
        outfitList.append(Item(PicturesDirectory + '/' + imagePath, clothingType))
    pickle.dump(outfitList, open(PickleNameFile, 'wb'))
    return outfitList

def add_to_pickle(imagePath, neuralNetwork: RecognitionNetwork):
    image = Image.open(PicturesDirectory + '/' + imagePath)
    resizedImage = image.resize((28, 28))
    monochromeImage = resizedImage.convert('L')
    imageArray = numpy.asarray(monochromeImage, dtype='int')
    clothingType = neuralNetwork.predict(imageArray)
    outfitList = pickle.load(open(PickleNameFile,'rb'))
    outfitList.append(Item(PicturesDirectory + '/' + imagePath, clothingType))
    pickle.dump(outfitList, open(PickleNameFile, 'wb'))
    return outfitList

def generateOutfit(weatherParameter, casualityParameter, needReload=False, imageUpdate=None):
    neuralNetwork = pickle.load(open('/Users/ylias.2001/Desktop/OUTFIT/NeuralNetwork.sav','rb'))
    if not needReload:
        outfitlist = load_pickle_outfit()
    else:
        if not imageUpdate:
            outfitlist = create_new_pickle(neuralNetwork)
        else:
            outfitlist = add_to_pickle(neuralNetwork, imageUpdate)
    searchProblem = SearchProblem(weatherParameter, casualityParameter, outfitlist)
    result = ClothsChoiceHeuristic.uniform_cost_search(searchProblem)
    return ["imm.jpeg", "imm.jpeg", "imm.jpeg"]