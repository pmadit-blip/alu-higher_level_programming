#!/usr/bin/python3
"""Unittests for Rectangle class."""
import unittest
from models.base import Base
from models.rectangle import Rectangle


class TestRectangle(unittest.TestCase):
    """Test cases for Rectangle class."""

    def setUp(self):
        """Reset __nb_objects before each test."""
        Base._Base__nb_objects = 0

    def test_basic(self):
        r = Rectangle(1, 2)
        self.assertEqual(r.width, 1)
        self.assertEqual(r.height, 2)

    def test_all_args(self):
        r = Rectangle(1, 2, 3, 4, 5)
        self.assertEqual(r.id, 5)

    def test_width_type(self):
        with self.assertRaises(TypeError):
            Rectangle("1", 2)

    def test_height_type(self):
        with self.assertRaises(TypeError):
            Rectangle(1, "2")

    def test_x_type(self):
        with self.assertRaises(TypeError):
            Rectangle(1, 2, "3")

    def test_y_type(self):
        with self.assertRaises(TypeError):
            Rectangle(1, 2, 3, "4")

    def test_width_value(self):
        with self.assertRaises(ValueError):
            Rectangle(0, 2)

    def test_height_value(self):
        with self.assertRaises(ValueError):
            Rectangle(1, 0)

    def test_x_value(self):
        with self.assertRaises(ValueError):
            Rectangle(1, 2, -1)

    def test_y_value(self):
        with self.assertRaises(ValueError):
            Rectangle(1, 2, 3, -1)

    def test_area(self):
        self.assertEqual(Rectangle(3, 4).area(), 12)

    def test_str(self):
        r = Rectangle(4, 6, 2, 1, 12)
        self.assertEqual(str(r), "[Rectangle] (12) 2/1 - 4/6")

    def test_update_args(self):
        r = Rectangle(1, 2)
        r.update(10, 5, 6, 3, 4)
        self.assertEqual(r.id, 10)
        self.assertEqual(r.width, 5)

    def test_update_kwargs(self):
        r = Rectangle(1, 2)
        r.update(width=10, height=20)
        self.assertEqual(r.width, 10)
        self.assertEqual(r.height, 20)

    def test_to_dictionary(self):
        r = Rectangle(1, 2, 3, 4, 5)
        d = r.to_dictionary()
        self.assertEqual(d['width'], 1)
        self.assertEqual(d['height'], 2)


if __name__ == '__main__':
    unittest.main()

