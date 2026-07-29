#!/bin/bash
# Script that makes a request to catch_me and displays You got me!
curl -s -L 0.0.0.0:5000/catch_me -X POST
