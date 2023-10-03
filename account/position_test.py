import unittest
from position import Position


class PositionTest(unittest.TestCase):
    def setUp(self) -> None:
        self.position = Position()

    def test_position(self):
        lists = self.position.sumAdd([5, 4, 9, 7, 2, 0], 14)
        expected = [0, 2]
        self.assertEqual(lists, expected)

    def test_sumUp(self):
        list1 = self.position.sumUp([1, 2, 3, 4, 5], [6, 7, 8, 9, 10])
        expected =[(1, 6), (2, 7), (3, 8), (4, 9), (5, 10)]
        self.assertEqual(list1,expected)