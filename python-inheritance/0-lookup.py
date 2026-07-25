#!/usr/bin/python3
"""Module for looking up attributes and methods of an object."""


def lookup(obj):
    """Return a list of attributes and methods available in an object."""
    return dir(obj)
