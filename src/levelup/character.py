class Character:
    name = ""
    position = []

    def __init__(self, character_name):
        self.name = character_name

    def enterMap(self, map):
        self.position = [0,0]

    def move(self, direction):
        pass