#!/bin/bash

# Check value of last-modified date header for list of URLs
#
#  Uses curl:  https://curl.haxx.se/

# Display usage message if command line does not contain expected
# number of arguments
if [ "$#" -ne 2 ] ; then
    echo "Usage: checkLastModified.sh fileIn fileOut" >&2
    exit 1
fi

# File I/O
fileIn="$1"
fileOut="$2"

# Remove fileOut if it exists already
if [ -f $fileOut ] ; then
    rm $fileOut
fi

# Write header line
echo url,last-modified >> $fileOut

# Iterate over all URLs in fileIn
while read url; do
    # Check last-modified header
    lastModified=$(curl -sI $url | grep -i last-modified | tr -d '\r')
    # Add url, status code to output file
    echo \"$url\",\"$lastModified\" >> $fileOut
done <$fileIn