#!/bin/bash
# displays only the status code of the response
curl -sL -X HEAD -w "%{http_code}" "$1"
