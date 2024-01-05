#!/bin/bash
# Check if an argument is provided
if [ -z "$1" ]; then
    echo "Please provide a URL."
    exit 1
fi

# Send a GET request to the URL and capture both HTTP status code and response body
response=$(curl -s -w "%{http_code}" -o response.txt "$1")

# Check if the HTTP status code is 200 (OK)
if [[ "$response" == "200" ]]; then
    # Display the body of the response (route_2) if the status code is 200
    cat response.txt
else
    echo "HTTP status code is not 200."
fi

# Remove the temporary response file
rm response.txt
