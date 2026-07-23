#!/usr/bin/python3
"""Module for reading a text file."""


def read_file(filename=""):
    """Reads a UTF-8 text file and prints its contents to stdout."""
    with open(filename, mode="r", encoding="utf-8") as f:
        print(f.read(), end="")
