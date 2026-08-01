#!/usr/bin/python3
"""Unittests for Base class."""
import unittest
from models.base import Base


class TestBase(unittest.TestCase):
    """Test cases for Base class."""

    def setUp(self):
        """Reset __nb_objects before each test."""
        Base._Base__nb_objects = 0

    def test_id_assigned(self):
        self.assertEqual(Base(10).id, 10)

    def test_id_auto(self):
        b1 = Base()
        b2 = Base()
        self.assertEqual(b1.id, 1)
        self.assertEqual(b2.id, 2)

    def test_id_none(self):
        self.assertEqual(Base(None).id, 1)

    def test_id_zero(self):
        self.assertEqual(Base(0).id, 0)

    def test_id_negative(self):
        self.assertEqual(Base(-5).id, -5)


if __name__ == '__main__':
    unittest.main()
