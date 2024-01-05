#!/usr/bin/env bash
# the size of the response
curl -s -w "%{size_download}" -o /dev/null "$1" | { read size; echo "$size"; }