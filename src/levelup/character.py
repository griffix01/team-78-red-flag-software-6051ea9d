from levelup.position import Position

class Character:
    name = ""
    position: Position

    def __init__(self, character_name):
        self.name = character_name

    def enterMap(self, map): # set start location
        self.position = Position(0, 0)

    def move(self, direction):
        self.position = [1,1]