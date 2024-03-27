#!/bin/bash

if [ $# -ne 1 ]; then
    echo "Usage: $0 <URL>"
    exit 1
fi

URL=$1
TEMP_FILE=$(mktemp)

curl -s -o $TEMP_FILE -w "%{http_code}" $URL | {
    read -r response_code
    if [ "$response_code" = "200" ]; then
        cat $TEMP_FILE
    fi
}

rm $TEMP_FILE

