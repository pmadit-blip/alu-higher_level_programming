#!/usr/bin/python3
"""Unittests for Square class."""
import unittest
import os
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

    def test_x_type(self):
        with self.assertRaises(TypeError):
            Square(1, "2")

    def test_y_type(self):
        with self.assertRaises(TypeError):
            Square(1, 2, "3")

    def test_size_negative(self):
        with self.assertRaises(ValueError):
            Square(-1)

    def test_size_zero(self):
        with self.assertRaises(ValueError):
            Square(0)

    def test_x_negative(self):
        with self.assertRaises(ValueError):
            Square(1, -1)

    def test_y_negative(self):
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
        self.assertEqual(d, {'id': 3, 'size': 5, 'x': 1, 'y': 2})

    def test_create_id(self):
        s = Square.create(**{'id': 89})
        self.assertEqual(s.id, 89)

    def test_create_id_size(self):
        s = Square.create(**{'id': 89, 'size': 1})
        self.assertEqual(s.size, 1)

    def test_create_id_size_x(self):
        s = Square.create(**{'id': 89, 'size': 1, 'x': 2})
        self.assertEqual(s.x, 2)

    def test_create_id_size_x_y(self):
        s = Square.create(**{'id': 89, 'size': 1, 'x': 2, 'y': 3})
        self.assertEqual(s.y, 3)

    def test_save_to_file_None(self):
        Square.save_to_file(None)
        with open("Square.json", "r") as f:
            self.assertEqual(f.read(), "[]")

    def test_save_to_file_list_empty(self):
        Square.save_to_file([])
        with open("Square.json", "r") as f:
            self.assertEqual(f.read(), "[]")

    def test_save_to_file_empty_list(self):
        Square.save_to_file([])
        with open("Square.json", "r") as f:
            self.assertEqual(f.read(), "[]")

    def test_save_to_file(self):
        Square.save_to_file([Square(1)])
        with open("Square.json", "r") as f:
            self.assertIn("size", f.read())

    def test_load_from_file_no_file(self):
        if os.path.exists("Square.json"):
            os.remove("Square.json")
        self.assertEqual(Square.load_from_file(), [])

    def test_load_from_file(self):
        Square.save_to_file([Square(1)])
        squares = Square.load_from_file()
        self.assertIsInstance(squares[0], Square)


if __name__ == '__main__':
    unittest.main()

