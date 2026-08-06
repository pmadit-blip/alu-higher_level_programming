#!/usr/bin/python3
"""Lists the 10 most recent commits of a GitHub repository."""

import requests
import sys


if __name__ == "__main__":
    repo = sys.argv[1]
    owner = sys.argv[2]

    url = "https://api.github.com/repos/{}/{}/commits".format(owner, repo)

    response = requests.get(url)

    for commit in response.json()[:10]:
        print("{}: {}".format(
            commit.get("sha"),
            commit.get("commit").get("author").get("name")
        ))
