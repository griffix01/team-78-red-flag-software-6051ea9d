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

    def welcome(self):
        print("""
 _       __     __                        
| |     / /__  / /________  ____ ___  ___ 
| | /| / / _ \/ / ___/ __ \/ __ `__ \/ _ |
| |/ |/ /  __/ / /__/ /_/ / / / / / /  __/
|__/|__/\___/_/\___/\____/_/ /_/ /_/\___/ 

You awaken to a land unknown. The Kingdom of Red Flag dares you to escape the dragon
and travel through the land.

Be wary traveler, Milo the cat and Creey the Clown wait! Adventure begins and enemies lurk. 
Will you benefit from treasure or die?

Keyboard Guide:
Movement (W - UP, A - LEFT, S - DOWN, D - RIGHT)
Exit Game - Ctrl-C

        """)

    def create_character(self):
        character = self.prompt("Enter character name", lambda x: len(x) > 0)
        self.controller.create_character(character)
        print("Welcome, " + self.controller.status.character_name + "!\n")

    def move_loop(self):
        while True:
            print("You are at position (" + str(self.controller.status.currentPosition.x) + ", " + str(self.controller.status.currentPosition.y) + ").")
            
            if ((self.controller.status.currentPosition.x == 4) and (self.controller.status.currentPosition.x == 6)):
                print("")
            elif ((self.controller.status.currentPosition.x == 4) and (self.controller.status.currentPosition.x == 6)):
                print("")

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
        self.welcome()
        self.create_character()
        self.controller.start_game()
        self.move_loop()

    def quit(self):
        #print(f"\n\n{self.controller.status.currentPosition}")
        print("You started the game at position (0,0).")
        print("You are currently at position (" + str(self.controller.status.currentPosition.x) + ", " + str(self.controller.status.currentPosition.y) + ").")
        print("You have made " + str(self.controller.status.moveCount) + " moves in the game.")