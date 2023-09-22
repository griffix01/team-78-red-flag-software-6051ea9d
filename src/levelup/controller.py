import logging
from dataclasses import dataclass
from enum import Enum
from levelup.gameStatus import GameStatus
from levelup.character import Character
from levelup.map import Map


DEFAULT_CHARACTER_NAME = "Character"

class Direction(Enum):
    UP = "w"
    DOWN = "s"
    LEFT = "a"
    RIGHT = "d"

class CharacterNotFoundException(Exception):
    pass

class InvalidMoveException(Exception):
    pass

class GameController:
    status: GameStatus
    character: Character
    map: Map

    def __init__(self):
        self.status = GameStatus()

    def create_character(self, character_name: str) -> None:
        if character_name is not None and character_name != "":
            self.status.characterName = character_name
        else:
            self.status.characterName = DEFAULT_CHARACTER_NAME
        self.character = Character(character_name)

    def start_game(self):
        self.map = Map()
        self.character.enterMap(self.map)
        self.status.currentPosition = self.character.position

    def move(self, direction: Direction) -> None:
        # TODO: Implement move - should call something on another class
        # TODO: Should probably also update the game results
        self.character.move(direction)
        self.status.currentPosition = self.character.position
        self.status.moveCount += 1

    '''def set_character_position(self, xycoordinates: tuple) -> None:
        # TODO: IMPLEMENT THIS TO SET CHARACTERS CURRENT POSITION -- exists to be testable
        pass

    def set_current_move_count(self, move_count: int) -> None:
        # TODO: IMPLEMENT THIS TO SET CURRENT MOVE COUNT -- exists to be testable
        pass

    def get_total_positions(self) -> int:
        # TODO: IMPLEMENT THIS TO GET THE TOTAL POSITIONS FROM THE MAP - - exists to be
        # testable
        return -10
'''
    
