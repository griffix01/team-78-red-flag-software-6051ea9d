from unittest import TestCase
from levelup.position import Position
from levelup.map import Map


class TestCalculatePositionUp(TestCase):
    def test_init(self):
        testObj = Map()
        testPosition = Position(2,2)
        self.assertEqual(testPosition.x, testObj.calculatePosition(Position(2, 1), "w").x)
        self.assertEqual(testPosition.y, testObj.calculatePosition(Position(2, 1), "w").y)