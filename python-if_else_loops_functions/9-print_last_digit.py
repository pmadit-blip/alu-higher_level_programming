#!/usr/bin/python3
"""Function that prints the last digit of a number"""


def print_last_digit(number):
    """Prints and returns the last digit of number"""
    last = abs(number % 10)
    print("{}".format(last), end="")
    return last
