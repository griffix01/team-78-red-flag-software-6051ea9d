from levelup.position import Position

class Map:
    numPositions = 100

    def __init__(self):
        pass

    def calculatePosition(self, start, direction):
        new = start

        if direction == "w":
            new.y += 1
            
        return new