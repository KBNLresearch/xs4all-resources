#!/bin/bash

# Recursively rename al files and folders in directory tree
# to lowercase.
# Adapted from: https://stackoverflow.com/a/152741/1209004

my_root_dir=$1

for SRC in `find ${my_root_dir} -depth`
do
    DST=`dirname "${SRC}"`/`basename "${SRC}" | tr '[A-Z]' '[a-z]'`
    if [ "${SRC}" != "${DST}" ]
    then
        #echo ${SRC}, ${DST}
        [ ! -e "${DST}" ] && mv -T "${SRC}" "${DST}" || echo "${SRC} was not renamed"
    fi
done