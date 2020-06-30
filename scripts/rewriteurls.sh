#!/bin/bash

# This script replaces all references to website root http://www.xs4all.nl/~ziklies/
# by an empty string so references become relative

# Location on file system
rootDir=/home/johan/kb/liesbets-atelier/liesbets-atelier-new/ziklies.home.xs4all.nl

# Old and new root domain (used for updating redirects)
rootOld=http://www.xs4all.nl/~ziklies/
rootNew="/"

while IFS= read -d $'\0' -r file ; do
    # Update references to root domain
    #echo $file    
    sed -i "s|$rootOld|$rootNew|g" $file
done < <(find $rootDir -type f -regex '.*\.\(html\|htm\)' -print0)

