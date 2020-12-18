#!/bin/bash
# Size of the body
curl -sI "$1" | grep "Content-Length" | cut -d' ' -f 2
