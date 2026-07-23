#!/usr/bin/python3
"""Module for Square class."""

Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Representation of a square."""

    def __init__(self, size):
        """Initialize square with size."""
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)
