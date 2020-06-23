#! /usr/bin/env python3
from warcio.capture_http import capture_http
import requests

def main():
    # Existing warc.gz file (created with wget, then compressed using warcio's
    # 'recompress' command)
    with capture_http("ziklies.home.xs4all.nl.warc.gz"):
        for indexOnder in range(1, 8):
            for indexMidden in range(1, 8):
                for indexTop in range(1, 8):
                    vOnder = str(indexOnder) + 'a'
                    vMidden = str(indexMidden) + 'b'
                    vTop = str(indexTop) + 'c'
                    requests.post("http://ziklies.home.xs4all.nl/cgi-bin/barbie.cgi", 
                                  data={'onder':vOnder, 'midden':vMidden, 'top':vTop})
main()