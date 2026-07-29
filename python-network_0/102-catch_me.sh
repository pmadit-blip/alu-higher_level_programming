#!/bin/bash
# Script that makes a request to catch_me and displays You got me!
curl -s -X PUT -H "Content-Type: application/json" 0.0.0.0:5000/catch_me
