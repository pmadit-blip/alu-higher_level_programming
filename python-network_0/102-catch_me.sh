#!/bin/bash
# Script that makes a request to catch_me and displays You got me!
curl -s -L -X PUT -H "Content-Type: application/json" -H "X-School-User-Id: 98" 0.0.0.0:5000/catch_me
