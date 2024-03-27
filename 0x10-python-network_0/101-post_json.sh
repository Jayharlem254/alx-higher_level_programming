#!/bin/bash

if [ $# -ne 2 ]; then
    echo "Usage: $0 <URL> <JSON_FILE>"
    exit 1
fi

URL=$1
JSON_FILE=$2

# Check if the JSON file is valid
jq . $JSON_FILE > /dev/null 2>&1
if [ $? -ne 0 ]; then
    echo "Not a valid JSON"
    exit 1
fi

curl -s -X POST -H "Content-Type: application/json" -d "@$JSON_FILE" $URL

