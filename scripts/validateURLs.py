#! /usr/bin/env python3

"""
Validate urls in CSV file
"""

import sys
import csv
import validators

def main():
    """Main function"""

    fileIn = "2019-10-11_xs4all_actief_selectie_KT_.csv"
    fileOut = "urlvalidationresult.csv"
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
    outHeader = ['url', 'urlIsValid']

    # Append header to outRows list
    outRows.append(outHeader)

    for inRow in inRows:
        url = inRow[0]
        urlIsValid = validators.url(url)

        # Add items to output row
        outRow = [url, urlIsValid]

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