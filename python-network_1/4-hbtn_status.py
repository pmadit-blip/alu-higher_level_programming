#!/usr/bin/python3
"""Module that fetches https://alu-intranet.hbtn.io/status using requests."""
import requests


response = requests.get('https://alu-intranet.hbtn.io/status')
print("Body response:")
print("	- type: {}".format(type(response.text)))
print("	- content: {}".format(response.text))
