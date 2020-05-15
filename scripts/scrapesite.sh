#!/bin/bash

wget -- mirror \
    --recursive
    --page-requisites \
    --output-file="liesbets-atelier.log" \
    -e robots=off \
    --no-parent \
    --domains ziklies.home.xs4all.nl
    https://ziklies.home.xs4all.nl/
    
