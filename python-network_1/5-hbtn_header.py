#!/usr/bin/python3
"""Script that fetches a URL and displays the X-Request-Id header value"""
import requests
import sys


r = requests.get(sys.argv[1])
print(r.headers.get("X-Request-Id"))
