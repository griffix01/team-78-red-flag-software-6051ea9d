from levelup.map import Map
from levelup.position import Position
class fakeMap(Map):
    position: Position

    def __init__(self, minX, minY, maxX, maxY):
        super().__init__()
        position = Position(1, 1)