#!/usr/bin/python3
"""
This module contains a function that prints text with 2 new lines
after each of these characters: ., ? and :

>>> text_indentation("Hello.")
Hello.
<BLANKLINE>
"""


def text_indentation(text):
    """
    Prints text with 2 new lines after each '.', '?' and ':'.

    >>> text_indentation("Hi: how are you?")
    Hi:
    <BLANKLINE>
    how are you?
    <BLANKLINE>
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    i = 0
    while i < len(text):
        print(text[i], end="")
        if text[i] in ".?:":
            print("\n")
            i += 1
            while i < len(text) and text[i] == " ":
                i += 1
            continue
        i += 1
