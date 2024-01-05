#!/bin/bash
# This script takes a URL as an argument, sends a silent request to that URL using curl, and displays the size of the response body.

curl -s -w "%{size_download}" -o /dev/null "$1" | { read size; echo "$size"; }