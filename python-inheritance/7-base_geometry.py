#!/usr/bin/python3
"""Module that defines a BaseGeometry class"""


class BaseGeometry:
    """Class that serves as a base for other geometry classes"""

    def area(self):
        """Raises an exception since area is not implemented here"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Validates that value is an integer greater than 0"""
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
