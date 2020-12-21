#!/bin/bash
# a JSON POST request to a URL as the first arg and displays the body
curl -sX POST -H "Content-Type: application/json" -d @"$2" "$1"
