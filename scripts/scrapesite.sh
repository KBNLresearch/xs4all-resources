#!/bin/bash

wget \
    --wait=3 \
    --random-wait \
    --recursive \
    -l 10 \
    --page-requisites \
    --output-file="liesbets-atelier.log" \
    -e robots=off \
    --no-parent \
    https://ziklies.home.xs4all.nl/
    
