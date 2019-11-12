#! /usr/bin/env python3

"""
Generate cleaned-up selection list from tab-delimited WebCurator dump
Johan van der Knijff
"""

import sys
import csv
import argparse


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
    parser.add_argument('--separator', '-s',
                        action='store',
                        default=',',
                        dest='separator',
                        help='output separator (default: comma)')

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
    parser = argparse.ArgumentParser(description='Extract year from last-modified date')
    args = parseCommandLine(parser)
    fileIn = args.fileIn
    fileOut = args.fileOut
    separator = args.separator

    # Read input file
    try:
        fIn = open(fileIn, "r", encoding="utf-8")
    except IOError:
        msg = 'could not read file ' + fileIn
        errorExit(msg)

    # Parse input file as comma-delimited data
    try:
        inCSV = csv.reader(fIn, delimiter=',')
        inHeader = next(inCSV)
        inRows = [row for row in inCSV]
        fIn.close()
    except csv.Error:
        fIn.close()
        msg = 'could not parse ' + fileIn
        errorExit(msg)

    # Remove trailing and leading whitespace characters from all cells
    for row in inRows:
        for j in range(len(row)):
            row[j] = row[j].strip()

    # Empty list for storing output records
    outRows = []

    # Header for output file as list
    outHeader = ['url', 'year']

    # Append header to outRows list
    outRows.append(outHeader)

    for inRow in inRows:
        url = inRow[0]
        lastModified = inRow[1]

        try:
            year = lastModified.split()[4]
        except IndexError:
            year = ""

        # Add items to output row
        outRow = [url, year]

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