#!/usr/bin/python3
"""Module for looking up object attributes."""


def lookup(obj):
    """Return a list of available attributes and methods of an object."""
    return dir(obj)
