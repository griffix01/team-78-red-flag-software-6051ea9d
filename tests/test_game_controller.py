from unittest import TestCase
from levelup.controller import GameController
from levelup.character import Character

class TestGameController(TestCase):
    def test_init(self):
        testObj = GameController()
        assert testObj.status != None
        
class TestMove(TestCase):
    def test_init(self):
        pass

class TestCreateCharacter(TestCase):
    def test_init(self):
        pass

class TestStartGame(TestCase):
    def test_init(self):
        pass

class TestSetCharacterPosition(TestCase):
    def test_init(self):
        pass