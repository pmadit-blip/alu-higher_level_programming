#!/usr/bin/python3
import sys


def safe_print_integer_err(value):
    """Prints an integer and handles errors."""
    try:
        print("{:d}".format(value))
        return True
    except (TypeError, ValueError) as err:
        print("Exception: {}".format(err), file=sys.stderr)
        return False
