#!/usr/bin/python3
"""8-json_api"""
import requests
import sys


q = sys.argv[1] if len(sys.argv) > 1 else ""
r = requests.post("http://0.0.0.0:5000/search_user", data={"q": q})
try:
    j = r.json()
    if j:
        print("[{}] {}".format(j.get("id"), j.get("name")))
    else:
        print("No result")
except ValueError:
    print("Not a valid JSON")
