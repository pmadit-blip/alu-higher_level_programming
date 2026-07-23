#!/usr/bin/python3
"""Module that defines a Square class with area method"""


class Square:
    """Class that defines a square with area method"""

    def __init__(self, size=0):
        """Instantiation with optional size and validation"""
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """Returns the current square area"""
        return self.__size * self.__size
