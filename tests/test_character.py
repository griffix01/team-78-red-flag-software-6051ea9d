from unittest import TestCase
from levelup.character import Character
from levelup.fakeMap import fakeMap
from levelup.position import Position
from levelup.map import Map

class TestCharacterInitWithName(TestCase):
    def test_init(self):
        ARBITRARY_NAME = "MyName"
        testobj = Character(ARBITRARY_NAME)
        self.assertEqual(ARBITRARY_NAME, testobj.name)

class TestEnterMap(TestCase):
    def test_init(self):
        testobj = Character("name")
        testmap = fakeMap(0,0,9,9)
        testobj.enterMap(testmap)
        self.assertNotEqual(testobj.position, [])

class TestMove(TestCase):
    def test_init(self):
        testobj = Character("name")
        testmap = fakeMap(0,0,9,9)
        testobj.enterMap(testmap)
        #testGameStatus = GameStatus(testobj.name)
        testobj.move("w")
        self.assertEqual(testobj.position.x, 0)
        self.assertEqual(testobj.position.y, 1)
        #self.assertEqual(testGameStatus.moveCount, 1)


