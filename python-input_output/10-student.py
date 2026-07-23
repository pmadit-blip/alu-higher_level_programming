#!/usr/bin/python3
"""Module for Student class."""


class Student:
    """Defines a student."""

    def __init__(self, first_name, last_name, age):
        """Initialize student attributes."""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Return dictionary representation of Student.

        If attrs is a list of strings, only return those attributes.
        Otherwise, return all attributes.
        """
        if isinstance(attrs, list):
            dictionary = {}
            for attr in attrs:
                if attr in self.__dict__:
                    dictionary[attr] = self.__dict__[attr]
            return dictionary

        return self.__dict__
