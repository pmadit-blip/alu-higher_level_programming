#!/usr/bin/python3
"""Unit tests for the Square class"""
import unittest
import os
from models.square import Square


class TestSquare(unittest.TestCase):
    """Test cases for Square class"""

    def test_size(self):
        s = Square(3)
        self.assertEqual(s.width, 3)
        self.assertEqual(s.height, 3)

    def test_size_x(self):
        s = Square(3, 2)
        self.assertEqual(s.x, 2)

    def test_size_x_y(self):
        s = Square(3, 2, 4)
        self.assertEqual(s.y, 4)

    def test_size_x_y_id(self):
        s = Square(3, 2, 4, 10)
        self.assertEqual(s.id, 10)

    def test_size_type_error(self):
        with self.assertRaises(TypeError):
            Square("3")

    def test_size_negative(self):
        with self.assertRaises(ValueError):
            Square(-3)

    def test_size_zero(self):
        with self.assertRaises(ValueError):
            Square(0)

    def test_x_type_error(self):
        with self.assertRaises(TypeError):
            Square(1, "2")

    def test_y_type_error(self):
        with self.assertRaises(TypeError):
            Square(1, 2, "3")

    def test_x_negative(self):
        with self.assertRaises(ValueError):
            Square(1, -2)

    def test_y_negative(self):
        with self.assertRaises(ValueError):
            Square(1, 2, -3)

    def test_area(self):
        s = Square(4)
        self.assertEqual(s.area(), 16)

    def test_str(self):
        s = Square(4, 2, 1, 12)
        self.assertEqual(str(s), "[Square] (12) 2/1 - 4")

    def test_update_args(self):
        s = Square(5)
        s.update(89, 1, 2, 3)
        self.assertEqual((s.id, s.size, s.x, s.y), (89, 1, 2, 3))

    def test_update_kwargs(self):
        s = Square(5)
        s.update(size=1, x=2, y=3, id=89)
        self.assertEqual((s.id, s.size, s.x, s.y), (89, 1, 2, 3))

    def test_to_dictionary(self):
        s = Square(10, 2, 1, 5)
        d = s.to_dictionary()
        self.assertEqual(d, {"id": 5, "size": 10, "x": 2, "y": 1})

    def test_create_id(self):
        s = Square.create(**{'id': 89})
        self.assertEqual(s.id, 89)

    def test_create_id_size(self):
        s = Square.create(**{'id': 89, 'size': 1})
        self.assertEqual((s.id, s.size), (89, 1))

    def test_create_id_size_x(self):
        s = Square.create(**{'id': 89, 'size': 1, 'x': 2})
        self.assertEqual((s.id, s.size, s.x), (89, 1, 2))

    def test_create_id_size_x_y(self):
        s = Square.create(**{'id': 89, 'size': 1, 'x': 2, 'y': 3})
        self.assertEqual((s.id, s.size, s.x, s.y), (89, 1, 2, 3))

    def test_save_to_file_none(self):
        Square.save_to_file(None)
        with open("Square.json", "r") as f:
            self.assertEqual(f.read(), "[]")

    def test_save_to_file_empty_list(self):
        Square.save_to_file([])
        with open("Square.json", "r") as f:
            self.assertEqual(f.read(), "[]")

    def test_save_to_file_list(self):
        s = Square(1)
        Square.save_to_file([s])
        with open("Square.json", "r") as f:
            content = f.read()
        self.assertIn('"id"', content)

    def test_load_from_file_no_file(self):
        if os.path.exists("Square.json"):
            os.remove("Square.json")
        result = Square.load_from_file()
        self.assertEqual(result, [])

    def test_load_from_file_with_file(self):
        s = Square(1)
        Square.save_to_file([s])
        result = Square.load_from_file()
        self.assertEqual(len(result), 1)
        self.assertIsInstance(result[0], Square)

    def tearDown(self):
        """Clean up any file created during tests"""
        if os.path.exists("Square.json"):
            os.remove("Square.json")#!/usr/bin/python3
"""Unit tests for the Square class"""
import unittest
import os
from models.square import Square


class TestSquare(unittest.TestCase):
    """Test cases for Square class"""

    def test_size(self):
        s = Square(3)
        self.assertEqual(s.width, 3)
        self.assertEqual(s.height, 3)

    def test_size_x(self):
        s = Square(3, 2)
        self.assertEqual(s.x, 2)

    def test_size_x_y(self):
        s = Square(3, 2, 4)
        self.assertEqual(s.y, 4)

    def test_size_x_y_id(self):
        s = Square(3, 2, 4, 10)
        self.assertEqual(s.id, 10)

    def test_size_type_error(self):
        with self.assertRaises(TypeError):
            Square("3")

    def test_size_negative(self):
        with self.assertRaises(ValueError):
            Square(-3)

    def test_size_zero(self):
        with self.assertRaises(ValueError):
            Square(0)

    def test_x_type_error(self):
        with self.assertRaises(TypeError):
            Square(1, "2")

    def test_y_type_error(self):
        with self.assertRaises(TypeError):
            Square(1, 2, "3")

    def test_x_negative(self):
        with self.assertRaises(ValueError):
            Square(1, -2)

    def test_y_negative(self):
        with self.assertRaises(ValueError):
            Square(1, 2, -3)

    def test_area(self):
        s = Square(4)
        self.assertEqual(s.area(), 16)

    def test_str(self):
        s = Square(4, 2, 1, 12)
        self.assertEqual(str(s), "[Square] (12) 2/1 - 4")

    def test_update_args(self):
        s = Square(5)
        s.update(89, 1, 2, 3)
        self.assertEqual((s.id, s.size, s.x, s.y), (89, 1, 2, 3))

    def test_update_kwargs(self):
        s = Square(5)
        s.update(size=1, x=2, y=3, id=89)
        self.assertEqual((s.id, s.size, s.x, s.y), (89, 1, 2, 3))

    def test_to_dictionary(self):
        s = Square(10, 2, 1, 5)
        d = s.to_dictionary()
        self.assertEqual(d, {"id": 5, "size": 10, "x": 2, "y": 1})

    def test_create_id(self):
        s = Square.create(**{'id': 89})
        self.assertEqual(s.id, 89)

    def test_create_id_size(self):
        s = Square.create(**{'id': 89, 'size': 1})
        self.assertEqual((s.id, s.size), (89, 1))

    def test_create_id_size_x(self):
        s = Square.create(**{'id': 89, 'size': 1, 'x': 2})
        self.assertEqual((s.id, s.size, s.x), (89, 1, 2))

    def test_create_id_size_x_y(self):
        s = Square.create(**{'id': 89, 'size': 1, 'x': 2, 'y': 3})
        self.assertEqual((s.id, s.size, s.x, s.y), (89, 1, 2, 3))

    def test_save_to_file_none(self):
        Square.save_to_file(None)
        with open("Square.json", "r") as f:
            self.assertEqual(f.read(), "[]")

    def test_save_to_file_empty_list(self):
        Square.save_to_file([])
        with open("Square.json", "r") as f:
            self.assertEqual(f.read(), "[]")

    def test_save_to_file_list(self):
        s = Square(1)
        Square.save_to_file([s])
        with open("Square.json", "r") as f:
            content = f.read()
        self.assertIn('"id"', content)

    def test_load_from_file_no_file(self):
        if os.path.exists("Square.json"):
            os.remove("Square.json")
        result = Square.load_from_file()
        self.assertEqual(result, [])

    def test_load_from_file_with_file(self):
        s = Square(1)
        Square.save_to_file([s])
        result = Square.load_from_file()
        self.assertEqual(len(result), 1)
        self.assertIsInstance(result[0], Square)

    def tearDown(self):
        """Clean up any file created during tests"""
        if os.path.exists("Square.json"):
            os.remove("Square.json")
