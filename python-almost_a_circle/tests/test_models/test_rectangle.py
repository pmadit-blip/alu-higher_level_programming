#!/usr/bin/python3
"""Unit tests for the Rectangle class"""
import unittest
from models.rectangle import Rectangle


class TestRectangle(unittest.TestCase):
    """Test cases for Rectangle class"""

    def test_width_height_x_y_default(self):
        r = Rectangle(10, 2)
        self.assertEqual(r.width, 10)
        self.assertEqual(r.height, 2)
        self.assertEqual(r.x, 0)
        self.assertEqual(r.y, 0)

    def test_full_init(self):
        r = Rectangle(3, 4, 5, 6, 7)
        self.assertEqual((r.width, r.height, r.x, r.y, r.id), (3, 4, 5, 6, 7))

    def test_width_type_error(self):
        with self.assertRaises(TypeError):
            Rectangle("3", 4)

    def test_width_le_zero(self):
        with self.assertRaises(ValueError):
            Rectangle(0, 4)

    def test_height_type_error(self):
        with self.assertRaises(TypeError):
            Rectangle(3, "4")

    def test_height_le_zero(self):
        with self.assertRaises(ValueError):
            Rectangle(3, -1)

    def test_x_type_error(self):
        with self.assertRaises(TypeError):
            Rectangle(3, 4, "5")

    def test_x_negative(self):
        with self.assertRaises(ValueError):
            Rectangle(3, 4, -5)

    def test_y_type_error(self):
        with self.assertRaises(TypeError):
            Rectangle(3, 4, 5, "6")

    def test_y_negative(self):
        with self.assertRaises(ValueError):
            Rectangle(3, 4, 5, -6)

    def test_area(self):
        r = Rectangle(3, 5)
        self.assertEqual(r.area(), 15)

    def test_display_no_offset(self):
        r = Rectangle(2, 2)
        r.display()

    def test_str(self):
        r = Rectangle(4, 6, 2, 1, 12)
        self.assertEqual(str(r), "[Rectangle] [12] 2/1 - 4/6")

    def test_update_args(self):
        r = Rectangle(10, 10, 10, 10, 1)
        r.update(89, 1, 2, 3, 4)
        self.assertEqual((r.id, r.width, r.height, r.x, r.y), (89, 1, 2, 3, 4))

    def test_update_kwargs(self):
        r = Rectangle(10, 10, 10, 10, 1)
        r.update(width=1, height=2, x=3, y=4, id=89)
        self.assertEqual((r.id, r.width, r.height, r.x, r.y), (89, 1, 2, 3, 4))

    def test_to_dictionary(self):
        r = Rectangle(10, 2, 1, 9, 5)
        d = r.to_dictionary()
        self.assertEqual(d, {"id": 5, "width": 10, "height": 2, "x": 1, "y": 9})
