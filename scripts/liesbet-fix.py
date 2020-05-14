#! /usr/bin/env python3
import os
import sys
from bs4 import BeautifulSoup
from pathlib import Path

def printWarning(msg):
    """Print warning to stderr."""
    msgString = ("WARNING: " + msg + "\n")
    sys.stderr.write(msgString)

def main():
    dirIn = "/home/johan/kb/liesbets-atelier/liesbets-atelier/Homepage-html/"
    dirOut = "/home/johan/kb/liesbets-atelier/test/Homepage-html/"

    dirsIn = []
    filesIn = []
    linksLocal = []

    # Get full paths to all files and folders in input directory
    for root, subdirs, files in os.walk(dirIn):
        for subdir in subdirs:
            subdir_path = os.path.join(root, subdir)
            dirsIn.append(subdir_path)

        for filename in files:
            file_path = os.path.join(root, filename)
            filesIn.append(file_path)

    # Extract href hyperlink targets from all HTML files
    for fileIn in filesIn:
        if fileIn.endswith(('.htm', 'html', '.HTM', '.HTML')):
            with open(fileIn) as fp:
                try:
                    soup = BeautifulSoup(fp, 'html.parser')
                    for link in soup.find_all('a'):
                        linkTarget = link.get('href')
                        if linkTarget is not None:
                            if not linkTarget.startswith(('http:', 'mailto:', 'javascript:')):
                                pathLocal = Path(fileIn).parent
                                pathParent = pathLocal.parent
                                if linkTarget.startswith('../'):
                                    # Fix links that are relative to parent dir
                                    linkTargetAbs = Path.joinpath(pathParent, linkTarget[len('../'):])
                                else:
                                    linkTargetAbs = Path.joinpath(pathLocal, linkTarget)

                                linksLocal.append(linkTargetAbs)
                except UnicodeDecodeError:
                    # Print warning and ignore this file
                    msg = "Decode error parsing file " + fileIn
                    printWarning(msg)

    """
    for dirIn in dirsIn:
        print('\t- subdirectory ' + dirIn)

    for fileIn in filesIn:
        print('\t- file ' + fileIn)
    """
    for linkLocal in linksLocal:
        print(linkLocal)


main()
