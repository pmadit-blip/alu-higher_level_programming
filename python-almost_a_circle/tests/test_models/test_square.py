#!/usr/bin/python3
"""Unit tests for the Square class"""
import unittest
from models.square import Square


class TestSquare(unittest.TestCase):
    """Test cases for Square class"""

    def test_size_sets_width_height(self):
        s = Square(5)
        self.assertEqual(s.width, 5)
        self.assertEqual(s.height, 5)

    def test_full_init(self):
        s = Square(5, 1, 2, 10)
        self.assertEqual((s.size, s.x, s.y, s.id), (5, 1, 2, 10))

    def test_size_type_error(self):
        with self.assertRaises(TypeError):
            Square("5")

    def test_size_le_zero(self):
        with self.assertRaises(ValueError):
            Square(0)

    def test_area(self):
        s = Square(4)
        self.assertEqual(s.area(), 16)

    def test_str(self):
        s = Square(4, 2, 1, 12)
        self.assertEqual(str(s), "[Square] [12] 2/1 - 4/4")

    def test_update_args(self):
        s = Square(5, 5, 5, 1)
        s.update(89, 1, 2, 3)
        self.assertEqual((s.id, s.size, s.x, s.y), (89, 1, 2, 3))

    def test_update_kwargs(self):
        s = Square(5, 5, 5, 1)
        s.update(size=1, x=2, y=3, id=89)
        self.assertEqual((s.id, s.size, s.x, s.y), (89, 1, 2, 3))

    def test_to_dictionary(self):
        s = Square(10, 2, 1, 5)
        d = s.to_dictionary()
        self.assertEqual(d, {"id": 5, "size": 10, "x": 2, "y": 1})
