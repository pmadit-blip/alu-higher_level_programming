#!/usr/bin/python3
"""
Module that sends a POST request to a URL with an email parameter
and displays the body of the response decoded in utf-8.
"""
import urllib.request
import urllib.parse
import sys


def main():
    """Main function that sends POST request with email and prints response."""
    url = sys.argv[1]
    email = sys.argv[2]
    data = urllib.parse.urlencode({'email': email}).encode('utf-8')
    with urllib.request.urlopen(url, data) as response:
        print(response.read().decode('utf-8'))


if __name__ == "__main__":
    main()
