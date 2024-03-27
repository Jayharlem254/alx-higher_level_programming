#!/bin/bash

if [ $# -ne 1 ]; then
    echo "Usage: $0 <URL>"
    exit 1
fi

URL=$1
TEMP_FILE=$(mktemp)

curl -s $URL -o $TEMP_FILE
SIZE=$(wc -c < $TEMP_FILE)

echo $SIZE

rm $TEMP_FILE

