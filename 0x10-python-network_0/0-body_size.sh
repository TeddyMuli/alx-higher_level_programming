#!/bin/bash
# script that sends a request to a url and displays the size of the body of that request
curl -sI "$1" | grep -i Content-Length | cut -d " " -f2
