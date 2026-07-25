#!/usr/bin/python3
"""Module for appending text to a UTF-8 file."""


def append_write(filename="", text=""):
    """Append text to a file and return the number of characters added."""
    with open(filename, mode="a", encoding="utf-8") as f:
        return f.write(text)
