from unittest import TestCase
from levelup.gameStatus import GameStatus

class TestCharacterName(TestCase):
    def test_init(self):
        testGameStatus = GameStatus()
        self.assertEqual(testGameStatus.moveCount, 0)