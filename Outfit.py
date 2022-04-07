import enum

class selectBox(enum.Enum):
    sportive = 1
    comfy = 2
    casual = 3
    elegant = 4

class Outfit:
    def __init__(self, weather, dressingType):