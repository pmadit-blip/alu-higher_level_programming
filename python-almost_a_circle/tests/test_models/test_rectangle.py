#!/usr/bin/python3
"""Unittests for Rectangle class."""
import unittest
import os
from io import StringIO
from unittest.mock import patch
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

    def test_width_negative(self):
        with self.assertRaises(ValueError):
            Rectangle(-1, 2)

    def test_height_negative(self):
        with self.assertRaises(ValueError):
            Rectangle(1, -2)

    def test_width_zero(self):
        with self.assertRaises(ValueError):
            Rectangle(0, 2)

    def test_height_zero(self):
        with self.assertRaises(ValueError):
            Rectangle(1, 0)

    def test_x_negative(self):
        with self.assertRaises(ValueError):
            Rectangle(1, 2, -1)

    def test_y_negative(self):
        with self.assertRaises(ValueError):
            Rectangle(1, 2, 3, -1)

    def test_area(self):
        self.assertEqual(Rectangle(3, 4).area(), 12)

    def test_str(self):
        r = Rectangle(4, 6, 2, 1, 12)
        self.assertEqual(str(r), "[Rectangle] (12) 2/1 - 4/6")

    def test_display_without_x_and_y(self):
        r = Rectangle(2, 2)
        with patch('sys.stdout', new=StringIO()) as fake_out:
            r.display()
            self.assertEqual(fake_out.getvalue(), "##\n##\n")

    def test_display_without_y(self):
        r = Rectangle(2, 2, 1)
        with patch('sys.stdout', new=StringIO()) as fake_out:
            r.display()
            self.assertEqual(fake_out.getvalue(), " ##\n ##\n")

    def test_display(self):
        r = Rectangle(2, 2, 1, 1)
        with patch('sys.stdout', new=StringIO()) as fake_out:
            r.display()
            self.assertEqual(fake_out.getvalue(), "\n ##\n ##\n")

    def test_to_dictionary(self):
        r = Rectangle(1, 2, 3, 4, 5)
        d = r.to_dictionary()
        self.assertEqual(d, {'id': 5, 'width': 1,
                             'height': 2, 'x': 3, 'y': 4})

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

    def test_create_id(self):
        r = Rectangle.create(**{'id': 89})
        self.assertEqual(r.id, 89)

    def test_create_id_width(self):
        r = Rectangle.create(**{'id': 89, 'width': 1})
        self.assertEqual(r.width, 1)

    def test_create_id_width_height(self):
        r = Rectangle.create(**{'id': 89, 'width': 1, 'height': 2})
        self.assertEqual(r.height, 2)

    def test_create_id_width_height_x(self):
        r = Rectangle.create(**{'id': 89, 'width': 1, 'height': 2, 'x': 3})
        self.assertEqual(r.x, 3)

    def test_create_id_width_height_x_y(self):
        r = Rectangle.create(
            **{'id': 89, 'width': 1, 'height': 2, 'x': 3, 'y': 4})
        self.assertEqual(r.y, 4)

    def test_save_to_file_None(self):
        Rectangle.save_to_file(None)
        with open("Rectangle.json", "r") as f:
            self.assertEqual(f.read(), "[]")

    def test_save_to_file_list_empty(self):
        Rectangle.save_to_file([])
        with open("Rectangle.json", "r") as f:
            self.assertEqual(f.read(), "[]")

    def test_save_to_file_empty_list(self):
        Rectangle.save_to_file([])
        with open("Rectangle.json", "r") as f:
            self.assertEqual(f.read(), "[]")

    def test_save_to_file(self):
        Rectangle.save_to_file([Rectangle(1, 2)])
        with open("Rectangle.json", "r") as f:
            self.assertIn("width", f.read())

    def test_load_from_file_no_file(self):
        if os.path.exists("Rectangle.json"):
            os.remove("Rectangle.json")
        self.assertEqual(Rectangle.load_from_file(), [])

    def test_load_from_file(self):
        Rectangle.save_to_file([Rectangle(1, 2)])
        rects = Rectangle.load_from_file()
        self.assertIsInstance(rects[0], Rectangle)


if __name__ == '__main__':
    unittest.main()

