#!/bin/bash
# script that takes in a URL and displays all HTTP methods
curl -sI "$1" | cut -d' ' -f 2-
