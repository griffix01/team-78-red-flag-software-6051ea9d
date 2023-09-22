import logging
from dataclasses import dataclass
from enum import Enum
from levelup.gameStatus import GameStatus
from levelup.character import Character
from levelup.map import Map


DEFAULT_CHARACTER_NAME = "Character"

class Direction(Enum):
    UP = "w"
    LEFT = "a"
    DOWN = "s"
    RIGHT = "d"

class CharacterNotFoundException(Exception):
    pass

class InvalidMoveException(Exception):
    pass

class GameController:
    status: GameStatus
    character: Character
    
    def __init__(self):
        self.status = GameStatus()

    def create_character(self, character_name: str) -> None:
        if character_name is not None and character_name != "":
            self.status.character_name = character_name
        else:
            self.status.character_name = DEFAULT_CHARACTER_NAME
        self.character = Character(character_name)

    def start_game(self):
        self.character.enterMap(Map())
        self.status.currentPosition = self.character.position

    def move(self, direction: Direction) -> None:
        self.character.move(direction)
        self.status.currentPosition = self.character.position
        self.status.moveCount += 1

    def set_character_position(self, xycoordinates: tuple) -> None:
        self.status.currentPosition.x = xycoordinates[0]
        self.status.currentPosition.y = xycoordinates[1]

    def set_current_move_count(self, move_count: int) -> None:
        self.status.moveCount = move_count

    def get_total_positions(self) -> int:
        return 100

    
