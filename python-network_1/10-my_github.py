#!/usr/bin/python3
"""Script that takes GitHub credentials and displays the user id."""
import requests
import sys

url = "https://api.github.com/user"
response = requests.get(url, auth=(sys.argv[1], sys.argv[2]))
print(response.json().get("id"))
