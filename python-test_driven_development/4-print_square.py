#!/usr/bin/python3
"""
This module contains a function that prints a square with the character #.

>>> print_square(4)
####
####
####
####
"""


def print_square(size):
    """
    Prints a square with the character #.

    >>> print_square(1)
    #
    """
    if isinstance(size, float) and size < 0:
        raise TypeError("size must be an integer")
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    for i in range(size):
        print("#" * size)
#!/usr/bin/python3
"""
This module contains a function that prints a square with the character #.

>>> print_square(4)
####
####
####
####
"""


def print_square(size):
    """
    Prints a square with the character #.

    >>> print_square(1)
    #
    """
    if isinstance(size, float) and size < 0:
        raise TypeError("size must be an integer")
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    for i in range(size):
        print("#" * size)
