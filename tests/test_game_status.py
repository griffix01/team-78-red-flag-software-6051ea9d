from unittest import TestCase
from levelup.character import Character
from levelup.gameStatus import GameStatus
from levelup.map import Map

class TestCharacterName(TestCase):
    def test_init(self):
        ARBITRARY_NAME = "MyName"
        testChar = Character(ARBITRARY_NAME)
        testMap = Map()
        testChar.enterMap(testMap)
        testGameStatus = GameStatus(testChar)
        self.assertEqual(testGameStatus.characterName, testChar.name)