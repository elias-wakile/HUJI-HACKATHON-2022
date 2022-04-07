import enum

class dressingType(enum.Enum):
    comfy = 1
    casual = 2
    elegant = 3

class Outfit:
    def __init__(self, weather, dressingType):