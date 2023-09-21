from levelup.position import Position
from levelup.map import Map

class Character:
    name = ""
    position: Position
    map: Map

    def __init__(self, character_name):
        self.name = character_name

    def enterMap(self, map): # set start location
        self.map = map
        self.position = Position(0, 0)

    def move(self, direction):
        self.position = self.map.calculatePosition(self.position, direction)