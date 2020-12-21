#!/bin/bash
# Script that make a request and give us a response specific
curl -sL 0:5000/catch_me -X PUT "You got me!" -H "Origin: HolbertonSchool" -d "user_id=98"
