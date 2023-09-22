from unittest import TestCase
from levelup.controller import GameController
from levelup.character import Character
from levelup.fakeMap import fakeMap

class TestGameController(TestCase):
    def test_init(self):
        testObj = GameController()
        assert testObj.status != None
        
class TestMove(TestCase):
    def test_init(self):
        testController = GameController()
        testController.create_character("name")
        testmap = fakeMap(0,0,9,9)
        testController.character.enterMap(testmap)
        testController.move("w")
        self.assertEqual(testController.character.position.x, 0)
        self.assertEqual(testController.character.position.y, 1)
        self.assertEqual(testController.status.moveCount, 1)

class TestCreateCharacter(TestCase):
    def test_init(self):
        testController = GameController()
        testController.create_character("name")
        self.assertEqual(testController.status.characterName, "name")

class TestStartGame(TestCase):
    def test_init(self):
        testController = GameController()
        testController.create_character("bob")
        testController.start_game()
        self.assertEqual(testController.status.characterName, "bob")
        self.assertEqual(testController.status.currentPosition.x, 0)
        self.assertEqual(testController.status.currentPosition.y, 0)