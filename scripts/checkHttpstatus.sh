#!/bin/bash

# Check HTTP status for list of URLs
#
#  Uses curl:  https://curl.haxx.se/

# Display usage message if command line does not contain expected
# number of arguments
if [ "$#" -ne 2 ] ; then
    echo "Usage: checkHttpStatus.sh fileIn fileOut" >&2
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
echo url,status >> $fileOut

# Iterate over all URLs in fileIn
while read url; do
    # Check status (https://superuser.com/questions/272265/getting-curl-to-output-http-status-code)
    status=$(curl -s -o /dev/null -I -L -w "%{http_code}" $url)
    # Add url, status code to output file
    echo \"$url\",$status >> $fileOut
done <$fileIn