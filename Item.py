import enum

class clothingType(enum.Enum):
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

class selectBox(enum.Enum):
    sportive = 1
    comfy = 2
    casual = 3
    elegant = 4

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

class itemThickness(enum.Enum):
    light = 1
    medium = 2
    thick = 3



class Item:
    def __init__(self, picture_path: str, fabric_path: str, clothing_type, color: str):
        self.color = color
        self.fabric_path = fabric_path
        self.picture_path = picture_path