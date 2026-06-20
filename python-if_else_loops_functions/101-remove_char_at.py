#!/usr/bin/python3
def remove_char_at(str, n):
    """Removes the character at position n from str"""
    if n < 0 or n >= len(str):
        return str
    return str[:n] + str[n + 1:]
