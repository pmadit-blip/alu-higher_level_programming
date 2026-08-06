#!/usr/bin/python3
"""Script that uses GitHub API to display user id."""
import requests
import sys

response = requests.get("https://api.github.com/user",
                        auth=(sys.argv[1], sys.argv[2]))
print(response.json().get("id"))

