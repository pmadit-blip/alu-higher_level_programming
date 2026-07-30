#!/usr/bin/python3
"""
Module that sends a request to a URL and displays
the value of the X-Request-Id variable in the response header.
"""
import urllib.request
import sys


def main():
    """Main function that fetches URL and prints X-Request-Id header."""
    url = sys.argv[1]
    with urllib.request.urlopen(url) as response:
        print(response.getheader('X-Request-Id'))


if __name__ == "__main__":
    main()
