#!/usr/bin/python3
"""Module that fetches https://intranet.hbtn.io/status using requests."""
import requests


r = requests.get('https://intranet.hbtn.io/status')
print("Body response:")
print("	- type: {}".format(type(r.text)))
print("	- content: {}".format(r.text))
