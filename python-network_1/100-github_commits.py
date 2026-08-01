#!/usr/bin/python3
"""Script that lists 10 most recent commits of a GitHub repository"""
import requests
import sys


url = "https://api.github.com/repos/{}/{}/commits".format(
    sys.argv[2], sys.argv[1])
r = requests.get(url, params={"per_page": 10})
for commit in r.json():
    sha = commit.get("sha")
    name = commit.get("commit").get("author").get("name")
    print("{}: {}".format(sha, name))
