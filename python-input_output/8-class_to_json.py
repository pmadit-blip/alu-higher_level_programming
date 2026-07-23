#!/usr/bin/python3
"""Module for converting class objects to dictionaries."""


def class_to_json(obj):
    """Return the dictionary description of an object."""
    return obj.__dict__
