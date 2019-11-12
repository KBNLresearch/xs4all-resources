#! /usr/bin/env python3

"""
Check value of last-modified date header for list of URLs
Johan van der Knijff
"""

import sys
import csv
import argparse
import validators
import requests

def parseCommandLine(parser):
    """Command line parser"""

    parser.add_argument('fileIn',
                        action='store',
                        type=str,
                        help='input file')
    parser.add_argument('fileOut',
                        action='store',
                        type=str,
                        help='output file')
    # Parse arguments
    arguments = parser.parse_args()
    return arguments


def errorExit(msg):
    """Print error to stderr and exit"""
    msgString = ('ERROR: ' + msg + '\n')
    sys.stderr.write(msgString)
    sys.exit(1)


def main():
    """Main function"""

    # Parse arguments from command line
    parser = argparse.ArgumentParser(description='Check value of last-modified date header for list of URLs')
    args = parseCommandLine(parser)
    fileIn = args.fileIn
    fileOut = args.fileOut
    separator = ","

    # Read input file
    try:
        fIn = open(fileIn, "r", encoding="utf-8")
    except IOError:
        msg = 'could not read file ' + fileIn
        errorExit(msg)

    # Parse input file as comma-delimited data
    try:
        inCSV = csv.reader(fIn, delimiter=',')
        # No header so commented this out
        #inHeader = next(inCSV)
        inRows = [row for row in inCSV]
        fIn.close()
    except csv.Error:
        fIn.close()
        msg = 'could not parse ' + fileIn
        errorExit(msg)

    # Empty list for storing output records
    outRows = []

    # Header for output file as list
    outHeader = ['url', 'isValidUrl', 'http-status', 'last-modified']

    # Append header to outRows list
    outRows.append(outHeader)

    for inRow in inRows:
        url = inRow[0]

        # Validate url
        urlIsValid = validators.url(url)

        if urlIsValid:
            isValidUrl = True
            res = requests.get(url)
            httpStatus = res.status_code

            try:
                lastModified = res.headers['last-modified']
            except KeyError:
                lastModified = ""

        else:
            isValidUrl = False
            httpStatus = ""
            lastModified = ""

        # Add items to output row
        outRow = [url, isValidUrl, httpStatus, lastModified]

        # Add output row to outRows list
        outRows.append(outRow)

    # Open output file
    try:
        fOut = open(fileOut, "w", encoding="utf-8")
    except IOError:
        msg = 'could not read file ' + fileIn
        errorExit(msg)

    # Write CSV
    try:
        outCSV = csv.writer(fOut, delimiter=separator, lineterminator='\n')
        for row in outRows:
            outCSV.writerow(row)

        fOut.close()

    except IOError:
        msg = 'could not write file ' + fileOut
        errorExit(msg)

if __name__ == "__main__":
    main()