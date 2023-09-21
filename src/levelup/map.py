from levelup.position import Position

class Map:
    numPositions = 100
    minX: int
    minY: int
    maxX: int
    maxY: int

    def __init__(self):
        self.minX = 0
        self.minY = 0
        self.maxX = 9
        self.maxY = 9

    def calculatePosition(self, start, direction):
        new = Position(start.x, start.y)

        if direction == "w":
            new.y += 1
        elif direction == "s":
            new.y -= 1
        elif direction == "a":
            new.x -= 1
        else:
            new.x += 1
        
        if self.validatePosition(new):
            return new
        else:
            return start

    def validatePosition(self, position):
        if ((position.x < self.minX) or (position.y < self.minY) or (position.x > self.maxX) or (position.y > self.maxY)):
            return False
        return True

