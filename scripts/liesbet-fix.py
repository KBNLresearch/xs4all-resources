#! /usr/bin/env python3
import os
import sys
import shutil
from bs4 import BeautifulSoup
from pathlib import Path

def printWarning(msg):
    """Print warning to stderr."""
    msgString = ("WARNING: " + msg + "\n")
    sys.stderr.write(msgString)

def main():
    rootDirIn = "/home/johan/kb/liesbets-atelier/liesbets-atelier/Homepage-html/HOMEPAGE"
    rootDirOut = "/home/johan/kb/liesbets-atelier/test/HOMEPAGE"

    dirsIn = []
    filesIn = []
    linksLocal = []

    # Get full paths to all files and folders in input directory
    for root, subdirs, files in os.walk(rootDirIn):
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
                    for image in soup.find_all('img'):
                        imageSource = image.get('src')
                        if imageSource is not None:
                            if not imageSource.startswith(('http:')):
                                pathLocal = Path(fileIn).parent
                                pathParent = pathLocal.parent
                                if imageSource.startswith('../'):
                                    # Fix links that are relative to parent dir
                                    imageSourceAbs = Path.joinpath(pathParent, imageSource[len('../'):])
                                else:
                                    imageSourceAbs = Path.joinpath(pathLocal, imageSource)

                                linksLocal.append(imageSourceAbs)

                except UnicodeDecodeError:
                    # Print warning and ignore this file
                    msg = "Decode error parsing file " + fileIn
                    printWarning(msg)

    """
    for dirIn in dirsIn:
        print('\t- subdirectory ' + dirIn)

    for fileIn in filesIn:
        print(fileIn)
    """

    rootInLevels = len(rootDirIn.split("/"))

    # Create output directory structure, using directory names from hyperlink targets
    for linkLocal in linksLocal:
        print(linkLocal)
        parentDirIn = Path(linkLocal).parent
        fileName = Path(linkLocal).name
        if parentDirIn is not None:
            if str(parentDirIn).startswith(rootDirIn):
                dirRel = Path(*parentDirIn.parts[rootInLevels:])
                dirOut = Path.joinpath(Path(rootDirOut), dirRel)

                # Create output directory if it doesn't exist already
                if not os.path.isdir(dirOut):
                    pass
                    #Path(dirOut).mkdir(parents=True, exist_ok=True)
                
                # Lookup corresponding file in input directory tree
                for fileIn in filesIn:
                    if str(fileIn).upper() == str(linkLocal).upper():
                        from_file = fileIn
                        to_file = Path.joinpath(dirOut, fileName)
                        #print(from_file, to_file)
                        #shutil.copy(str(from_file), str(to_file))



main()
