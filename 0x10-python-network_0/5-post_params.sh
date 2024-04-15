#!/bin/bash
# Script that takes a url sends a post request to the url and displays the body of the response
curl -s -X POST -d "email=test@gmail.com&subject=I will always be here for PLD" "$1"
