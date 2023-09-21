from unittest import TestCase
from levelup.position import Position
from levelup.map import Map

class TestCalculatePositionUp(TestCase):
    def test_init(self):
        testObj = Map()
        testPosition = Position(2,2)
        self.assertEqual(testPosition.x, testObj.calculatePosition(Position(2, 1), "w").x)
        self.assertEqual(testPosition.y, testObj.calculatePosition(Position(2, 1), "w").y)

class TestCalculatePositionDown(TestCase):
    def test_init(self):
        testObj = Map()
        testPosition = Position(2,0)
        self.assertEqual(testPosition.x, testObj.calculatePosition(Position(2, 1), "s").x)
        self.assertEqual(testPosition.y, testObj.calculatePosition(Position(2, 1), "s").y)

class TestCalculatePositionLeft(TestCase):
    def test_init(self):
        testObj = Map()
        testPosition = Position(1,1)
        self.assertEqual(testPosition.x, testObj.calculatePosition(Position(2, 1), "a").x)
        self.assertEqual(testPosition.y, testObj.calculatePosition(Position(2, 1), "a").y)

class TestCalculatePositionRight(TestCase):
    def test_init(self):
        testObj = Map()
        testPosition = Position(3,1)
        self.assertEqual(testPosition.x, testObj.calculatePosition(Position(2, 1), "d").x)
        self.assertEqual(testPosition.y, testObj.calculatePosition(Position(2, 1), "d").y)

class TestValidatePositionValid(TestCase):
    def test_init(self):
        testObj = Map()
        testPosition = Position(0,0)
        self.assertTrue(testObj.validatePosition(testPosition))

class TestValidatePositionInvalid(TestCase):
    def test_init(self):
        testObj = Map()
        testPosition = Position(-1,0)
        self.assertFalse(testObj.validatePosition(testPosition))

class TestValidateBouncyWall(TestCase):
    def test_init(self):
        testObj = Map()
        testPosition = Position(0,0)
        self.assertEqual(testPosition.x, testObj.calculatePosition(Position(0, 0), "s").x)
        self.assertEqual(testPosition.y, testObj.calculatePosition(Position(0, 0), "s").y)
