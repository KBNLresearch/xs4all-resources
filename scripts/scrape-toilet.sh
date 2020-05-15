#!/bin/bash

wget \
    --wait=3 \
    --random-wait \
    --recursive \
    -l 10 \
    --page-requisites \
    --output-file="liesbets-toilet.log" \
    -e robots=off \
    --no-parent \
    -i "$1"

    
