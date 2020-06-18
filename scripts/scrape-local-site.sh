#!/bin/bash

site="ziklies.home.xs4all.nl"

# First add domain root
echo "http://"$site"/" > urls.txt

# Add remaining files (and rewrite file paths as URLs)
find "/var/www/"$site -type f | sed -e 's/\/var\/www\//http:\/\//g' >> urls.txt

# Run wget using list as input
wget --page-requisites \
    --warc-file=$site \
    --warc-cdx \
    --output-file=$site".log" \
    --input-file=urls.txt 