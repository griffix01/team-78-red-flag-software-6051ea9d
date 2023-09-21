from levelup.character import Character
from levelup.position import Position

class GameStatus:
    characterName: str
    currentPosition: Position
    moveCount: int

    def __init__(self, character):
        self.characterName = character.name
        self.currentPosition = character.position
        self.moveCount = 0