#!/bin/bash
# Script that sends a GET request and displays body only if status code is 200
curl -s -L -o /dev/null -w "%{http_code}" "$1" | grep -q "200" && curl -s -L "$1"
