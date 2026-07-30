#!/usr/bin/python3
"""
Module that sends a request to a URL and displays the body
of the response. Handles urllib.error.HTTPError exceptions
and prints the HTTP status code.
"""
import urllib.request
import urllib.error
import sys

url = sys.argv[1]
try:
    with urllib.request.urlopen(url) as response:
        print(response.read().decode('utf-8'))
except urllib.error.HTTPError as e:
    print("Error code: {}".format(e.code))
