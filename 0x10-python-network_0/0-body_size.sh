#!/bin/bash
# send a request to an URL with curl, and displays size of body of response
curl -s "$1" | wc -c
