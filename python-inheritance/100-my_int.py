#!/usr/bin/python3
"""Module for MyInt class."""


class MyInt(int):
    """A rebel integer class with inverted == and !=."""

    def __eq__(self, other):
        """Invert the == operator."""
        return int(self) != other

    def __ne__(self, other):
        """Invert the != operator."""
        return int(self) == other
