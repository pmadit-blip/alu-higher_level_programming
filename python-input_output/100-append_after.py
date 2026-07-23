#!/usr/bin/python3
"""Module for inserting text after matching lines."""


def append_after(filename="", search_string="", new_string=""):
    """Insert new_string after every line containing search_string."""

    with open(filename, "r", encoding="utf-8") as file:
        lines = file.readlines()

    new_lines = []

    for line in lines:
        new_lines.append(line)

        if search_string in line:
            new_lines.append(new_string)

    with open(filename, "w", encoding="utf-8") as file:
        file.writelines(new_lines)
