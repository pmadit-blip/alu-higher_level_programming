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

        If attrs is a list of strings, return only those attributes.
        Otherwise return all attributes.
        """
        if isinstance(attrs, list):
            dictionary = {}
            for attr in attrs:
                if attr in self.__dict__:
                    dictionary[attr] = self.__dict__[attr]
            return dictionary

        return self.__dict__

    def reload_from_json(self, json):
        """Replace attributes using a dictionary."""
        for key, value in json.items():
            setattr(self, key, value)
