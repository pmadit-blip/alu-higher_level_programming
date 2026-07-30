#!/usr/bin/python3
"""Module that sends a request to a URL and handles HTTP errors."""
import urllib.request
import urllib.error
import sys


try:
    with urllib.request.urlopen(sys.argv[1]) as response:
        print(response.read().decode('utf-8'))
except urllib.error.HTTPError as e:
    print("Error code: {}".format(e.code))
