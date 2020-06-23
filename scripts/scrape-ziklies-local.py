#! /usr/bin/env python3
import os
from warcio.capture_http import capture_http
import requests

def main():
    """
    Scrape locally rendered version of Liesbet's Atelier to compressed WARC,
    including all outcomes of "barbie" scripts
    """

    siteName = "ziklies.home.xs4all.nl"

    # Compressed WARC file for output
    warcOut = siteName + ".warc.gz"

    siteDir = "/var/www/" + siteName

    # List of URLs to scrape
    urls = []

    # First add domain root
    urls.append("http://" + siteName)

    # Add remaining files (and rewrite file paths as URLs)
    #find "/var/www/"$site -type f | sed -e 's/\/var\/www\//http:\/\//g' >> urls.txt

    for root, dirs, files in os.walk(siteDir):
            for filename in files:
                # Full path
                file_path = os.path.join(root, filename)
                
                # Construct url and add to list
                url = file_path.replace("/var/www/", "http://")
                urls.append(url)
    
    # Iterate over URL list
    for url in urls:
        with capture_http(warcOut):
            requests.get(url)

    # Iterate over all input combinations of "barbie" scripts
    # Note that we also account for cases where 1 or more
    # fields are not set!
    # ("barbie1.cgi" is the English-language version)

    with capture_http(warcOut):
        for indexOnder in ["na", *range(1, 8)]:
            for indexMidden in ["na", *range(1, 8)]:
                for indexTop in ["na", *range(1, 8)]:
                    vOnder = str(indexOnder) + 'a'
                    vMidden = str(indexMidden) + 'b'
                    vTop = str(indexTop) + 'c'

                    scriptParams = {}
                    if indexOnder != "na":
                        scriptParams["onder"] = vOnder
                    if indexMidden != "na":
                        scriptParams["midden"] = vMidden
                    if indexTop != "na":
                        scriptParams["top"] = vTop

                    requests.post("http://ziklies.home.xs4all.nl/cgi-bin/barbie.cgi", 
                                  data=scriptParams)
                    requests.post("http://ziklies.home.xs4all.nl/cgi-bin/barbie1.cgi", 
                                  data=scriptParams)

main()