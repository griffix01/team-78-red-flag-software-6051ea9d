from unittest import TestCase
from levelup.character import Character
from levelup.fakeMap import fakeMap

class TestCharacterInitWithName(TestCase):
    def test_init(self):
        ARBITRARY_NAME = "MyName"
        testobj = Character(ARBITRARY_NAME)
        self.assertEqual(ARBITRARY_NAME, testobj.name)

class TestEnterMap(TestCase):
    def test_init(self):
        testobj = Character("name")
        testmap = fakeMap()
        testobj.enterMap(testmap)
        self.assertNotEquals(testobj.position, [])
class TestCharacterPositionUpdates(TestCase):
    def test_init(self):
        testobj = Character("name")
        testmap = fakeMap()
        testobj.move()
        self.assertEqual(testobj.position, testmap.calculatePosition([0,0], "w"))