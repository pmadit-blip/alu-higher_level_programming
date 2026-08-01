#!/usr/bin/python3
"""Script that sends a POST request with email and displays the response body"""
import requests
import sys


r = requests.post(sys.argv[1], data={"email": sys.argv[2]})
print(r.text)
