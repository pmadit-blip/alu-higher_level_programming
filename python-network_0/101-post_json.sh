#!/bin/bash
# Script that sends a JSON POST request with file contents and displays the body
curl -s -X POST -H "Content-Type: application/json" -d "@$2" "$1"
