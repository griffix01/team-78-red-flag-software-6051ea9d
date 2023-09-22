from levelup.position import Position

DEFAULT_CHARACTER_NAME = "Character"

class GameStatus:
    characterName: str = DEFAULT_CHARACTER_NAME
    currentPosition: Position
    moveCount: int

    def __init__(self):
        self.moveCount = 0