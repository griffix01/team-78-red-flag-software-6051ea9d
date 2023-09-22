import logging
from typing import Callable
from levelup.controller import GameController, Direction, InvalidMoveException

VALID_DIRECTIONS = [x.value for x in Direction]

class GameApp:

    controller: GameController

    def __init__(self):
        self.controller = GameController()

    def prompt(self, menu: str, validation_fn: Callable[[str], bool]) -> str:
        while True:
            response = input(f"\n{menu}\n> ")
            if validation_fn(response):
                break
        return response

    def create_character(self):
        character = self.prompt("Enter character name", lambda x: len(x) > 0)
        self.controller.create_character(character)
        print("Welcome, " + self.controller.status.character_name + "!\n")

    def move_loop(self):
        while True:
            print("You are at position (" + str(self.controller.status.currentPosition.x) + ", " + str(self.controller.status.currentPosition.y) + ").")
            response = self.prompt(
                f"Where would you like to go? {VALID_DIRECTIONS}\n(or ctrl+c to quit)",
                lambda x: x in VALID_DIRECTIONS,
            )
            try:
                self.controller.move(response)
            except InvalidMoveException:
                print(f"\nYou cannot move {Direction(response).name}.\n")
            else:
                print(f"\nYou moved {Direction(response).name}.\n")

    def start(self):
        self.create_character()
        self.controller.start_game()
        self.move_loop()

    def quit(self):
        #print(f"\n\n{self.controller.status.currentPosition}")
        print("You started the game at position (0,0).")
        print("You are currently at position (" + str(self.controller.status.currentPosition.x) + ", " + str(self.controller.status.currentPosition.y) + ").")
        print("You have made " + str(self.controller.status.moveCount) + " moves in the game.")