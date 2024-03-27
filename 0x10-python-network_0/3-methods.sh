#!/bin/bash

if [ $# -ne 1 ]; then
    echo "Usage: $0 <URL>"
    exit 1
fi

URL=$1

curl -s -I $URL | grep "Allow:" | cut -d' ' -f2-

