#!/usr/bin/python3
"""Module that lists 10 commits of a GitHub repository."""
import requests
import sys


repo = sys.argv[1]
owner = sys.argv[2]
url = "https://api.github.com/repos/{}/{}/commits".format(
    owner, repo)
r = requests.get(url, params={"per_page": 10})
for commit in r.json():
    sha = commit.get("sha")
    name = commit.get("commit").get("author").get("name")
    print("{}: {}".format(sha, name))
