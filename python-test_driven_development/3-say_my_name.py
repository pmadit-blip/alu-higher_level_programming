#!/usr/bin/python3
"""
This module contains a function that prints a name.

>>> say_my_name("John", "Smith")
My name is John Smith
"""


def say_my_name(first_name, last_name=""):
    """
    Prints My name is <first_name> <last_name>.

    >>> say_my_name("Walter", "White")
    My name is Walter White
    """
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")
    print("My name is {} {}".format(first_name, last_name))

