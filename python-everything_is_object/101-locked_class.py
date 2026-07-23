#!/usr/bin/python3
"""LockedClass module."""


class LockedClass:
    """A class that prevents dynamic instance attributes."""

    __slots__ = ("first_name",)
