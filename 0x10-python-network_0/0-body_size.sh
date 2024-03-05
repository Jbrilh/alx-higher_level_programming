#!/usr/bin/bash
# send a request to an URL with curl and displays it in bytes
curl -s "$1" | wc -c
