#!/usr/bin/python3
"""Unit tests for the Base class"""
import unittest
from models.base import Base


class TestBase(unittest.TestCase):
    """Test cases for Base class"""

    def setUp(self):
        """Reset the id counter before each test"""
        Base._Base__nb_objects = 0

    def test_id_none_assigns_incrementing_id(self):
        b1 = Base()
        b2 = Base()
        self.assertEqual(b1.id, 1)
        self.assertEqual(b2.id, 2)

    def test_id_given_value(self):
        b = Base(89)
        self.assertEqual(b.id, 89)

    def test_id_negative_value(self):
        b = Base(-5)
        self.assertEqual(b.id, -5)

    def test_id_is_public(self):
        b = Base(12)
        self.assertTrue(hasattr(b, "id"))
