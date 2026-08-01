#!/usr/bin/python3
"""Sends a request to a URL and displays the body of the response."""
import urllib.request
import urllib.error
import sys

try:
    with urllib.request.urlopen(sys.argv[1]) as response:
        print(response.read().decode('utf-8'))
except urllib.error.HTTPError as e:
    print("Error code: {}".format(e.code))

