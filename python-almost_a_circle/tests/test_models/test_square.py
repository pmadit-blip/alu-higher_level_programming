#!/usr/bin/python3
"""Unittests for Square class."""
import unittest
from models.base import Base
from models.square import Square


class TestSquare(unittest.TestCase):
    """Test cases for Square class."""

    def setUp(self):
        """Reset __nb_objects before each test."""
        Base._Base__nb_objects = 0

    def test_basic(self):
        s = Square(5)
        self.assertEqual(s.width, 5)
        self.assertEqual(s.height, 5)

    def test_all_args(self):
        s = Square(5, 1, 2, 3)
        self.assertEqual(s.id, 3)

    def test_size_type(self):
        with self.assertRaises(TypeError):
            Square("1")

    def test_size_value(self):
        with self.assertRaises(ValueError):
            Square(0)

    def test_x_value(self):
        with self.assertRaises(ValueError):
            Square(1, -1)

    def test_y_value(self):
        with self.assertRaises(ValueError):
            Square(1, 0, -1)

    def test_area(self):
        self.assertEqual(Square(5).area(), 25)

    def test_str(self):
        s = Square(5, 1, 2, 3)
        self.assertEqual(str(s), "[Square] (3) 1/2 - 5")

    def test_size_setter(self):
        s = Square(5)
        s.size = 10
        self.assertEqual(s.width, 10)
        self.assertEqual(s.height, 10)

    def test_update_args(self):
        s = Square(5)
        s.update(10, 20, 3, 4)
        self.assertEqual(s.id, 10)
        self.assertEqual(s.size, 20)

    def test_update_kwargs(self):
        s = Square(5)
        s.update(size=10, x=3)
        self.assertEqual(s.size, 10)
        self.assertEqual(s.x, 3)

    def test_to_dictionary(self):
        s = Square(5, 1, 2, 3)
        d = s.to_dictionary()
        self.assertEqual(d['size'], 5)
        self.assertEqual(d['x'], 1)


if __name__ == '__main__':
    unittest.main()

