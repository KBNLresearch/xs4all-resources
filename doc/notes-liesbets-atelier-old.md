# Notes Liesbets atelier

Live site still here:

<https://ziklies.home.xs4all.nl/>

## Contents of ZIP file

- Directory tree "Homepage-html". Contains 1442 items, totalling 37.0 MB.

- Another ZIP file "Homepage-html.zip"; contents look identical to directory "Homepage-html"

## Comparison directory tree and ZIP file

Extract ZIP file to dir "Homepage-html-2". Then compare using:

```
diff --brief --recursive Homepage-html/ Homepage-html-2/
``` 

Result:

```
Only in Homepage-html-2/BEHANG: Thumbs.db
Only in Homepage-html-2/Claude: Thumbs.db
Only in Homepage-html-2/DOOLHOF: Thumbs.db
Only in Homepage-html-2/FILM: Thumbs.db
Only in Homepage-html-2/FOTO'S: Thumbs.db
Only in Homepage-html-2/HOMEPAGE/BAD: Thumbs.db
Only in Homepage-html-2/HOMEPAGE/Gambia: Shortcut to afritm5.mid.lnk
Only in Homepage-html-2/HOMEPAGE: Thumbs.db
Only in Homepage-html-2/Homepage DDS: Thumbs.db
Only in Homepage-html-2/JPG-GIF: Thumbs.db
Only in Homepage-html-2/PAINTBMP: Thumbs.db
Only in Homepage-html-2/PARK: Thumbs.db
Only in Homepage-html-2/SCHILDER: Thumbs.db
Only in Homepage-html-2/TEMP: Thumbs.db
Only in Homepage-html-2/: Thumbs.db
Only in Homepage-html-2/TOILET: Thumbs.db
Only in Homepage-html-2/VIRTSCHL: Thumbs.db
```

So apart from thumbnail files both are identical. For remaining analysis used ""Homepage-html" directory (without the thumbnails).

## Serving the files

Using Python's built-in server. Open directory in terminal, then:

```
python3 -m http.server
```

Then local site available at:

<http://127.0.0.1:8000/> 


## Problems

This page:


<http://127.0.0.1:8000/HOMEPAGE/start.html>

Contains hyperlink to:

<http://127.0.0.1:8000/HOMEPAGE/gambia/africa00.htm>

But this results in a 404. Looking inside the "HOMEPAGE" directory we see:

- folder "Gambia" (not 1st character is capitalized, unlike the link!)

- inside this is a file named "AFRICA00.HTM" (note uppercase!).

We can open this location (although inside it are other references that throw a 404): 

<http://127.0.0.1:8000/HOMEPAGE/Gambia/AFRICA00.HTM>

So we might be able to make (some of) the site work by renaming folders/files to their (supposedly) original names.

## List all files in direcory tree

Script:

```
#!/bin/bash
dirIn=$1

while IFS= read -d $'\0' -r file ; do
    echo $file
done < <(find $dirIn -type f -print0)
```

Then run as:

```
./list-files.sh ./Homepage-html/ > files.txt
```

- 1399 files

- 231 with .htm or .html file extension

## Extract all hyperlinks from HTML files

Following [instructions here](https://superuser.com/a/1224547/681049).

First install [Lynx](https://lynx.invisible-island.net/):

```
sudo apt install lynx
```

Then extract links from all HTML files using this script:

```
#!/bin/bash
fileIn=$1
fileOut=$2

if [ -f "$fileOut" ] ; then
    rm $fileOut
fi

while read -r file; do
    # Only process lines with .htm or .html extension (upper + lower case)
    case ${file^^} in *.HTM*)
        lynx -listonly -nonumbers -dump "$file" >> "$fileOut"
    esac
done < $fileIn
```

Command:

```
./extract-links.sh files.txt links.txt
```

Script iterates over all files that are part of the site (using output file of previous step, then for each file with HTM(L) extension extracts all hyperlinks, which are written to  output file (links.txt).

## Make subselection of links to local files


Script:

```
#!/bin/bash
fileIn=$1
fileOut=$2

if [ -f "$fileOut" ] ; then
    rm $fileOut
fi

prefixLocal="file:///home/johan/kb/liesbets-atelier/liesbets-atelier/Homepage-html/"

while read -r line; do
    # Line starts with prefixLocal, so local file
    case $line in $prefixLocal*)
        echo $line >> "$fileOut"
    esac
done < $fileIn
```

Command:

```
./local-links.sh links.txt links-local.txt
```

Result: file with 966 local links.

## Additional notes

Following HTML files contain invalid characters and cannot be parsed:

- /home/johan/kb/liesbets-atelier/liesbets-atelier/Homepage-html/HOMEPAGE/GASTEN.HTM
- /home/johan/kb/liesbets-atelier/liesbets-atelier/Homepage-html/HOMEPAGE/WOONK/KRANT3.HTM
- /home/johan/kb/liesbets-atelier/liesbets-atelier/Homepage-html/HOMEPAGE/WOONK/POEM.HTM
- /home/johan/kb/liesbets-atelier/liesbets-atelier/Homepage-html/HOMEPAGE/BAD/ZEIL02.HTM
- /home/johan/kb/liesbets-atelier/liesbets-atelier/Homepage-html/HOMEPAGE/BAD/ZEIL03.HTM
- /home/johan/kb/liesbets-atelier/liesbets-atelier/Homepage-html/HOMEPAGE/BAD/ZEIL05.HTM
- /home/johan/kb/liesbets-atelier/liesbets-atelier/Homepage-html/HOMEPAGE/BAD/ZEIL06.HTM
- /home/johan/kb/liesbets-atelier/liesbets-atelier/Homepage-html/HOMEPAGE/BAD/ZEIL04.HTM
- /home/johan/kb/liesbets-atelier/liesbets-atelier/Homepage-html/HOMEPAGE/Gambia/LUNCH.HTM
- /home/johan/kb/liesbets-atelier/liesbets-atelier/Homepage-html/HOMEPAGE/Gambia/TOERIST.HTM
- /home/johan/kb/liesbets-atelier/liesbets-atelier/Homepage-html/HOMEPAGE/Gambia/AFRICA03.HTM
- /home/johan/kb/liesbets-atelier/liesbets-atelier/Homepage-html/HOMEPAGE/Gambia/PAPIER.HTM

Dir `/home/johan/kb/liesbets-atelier/liesbets-atelier/Homepage-html/Claude/logeerk-kl/SIMGRANDES/` (+ underlying files) does not exist.

HTML contains references to following locations that are not part of the ZIP file:

```
/ikon/finaux/0-home
/ikon/finaux/autre
/ikon/finaux/8-imaque
/users/bex/www/personal
/
/~marcush
/misc
/cgi-bin/imagemap/~ziklies
```
HTML hasc refs to both upper- and lowercase versions of same dirs, e.g.:

`file:///home/johan/kb/liesbets-atelier/liesbets-atelier/Homepage-html/HOMEPAGE/woonk/woon01.html`

and

`file:///home/johan/kb/liesbets-atelier/liesbets-atelier/Homepage-html/HOMEPAGE/WOONK/krant.html`

BUT refs in html don't contain full path so maybe sth goes wrong in script?


## Image maps

Original site: server-side [image maps](https://en.wikipedia.org/wiki/Image_map). in HTML:

```
<A HREF="/cgi-bin/imagemap/~ziklies/deurtje1.map"><img src="deurtje1.gif" Border=0 ISMAP></A>
```

Contents of `deurtje1.map` file:

```
default http://www.xs4all.nl/~ziklies/start.html
poly http://www.xs4all.nl/~ziklies/start.html 0,56 76,40 91,43 89,67 76,62 6,77 0,60 1,55 
poly http://www.xs4all.nl/~ziklies/e-start.html 53,72 80,76 81,81 91,85 89,107 76,106 69,137 42,130 51,77
```

Server-side image maps are obsolete and don't work in modern browsers (source), but it is possible to convert the image map into a client-side image map. This can be done by replacing the *A* element in the HTML by this: 

```
<map name="mapname">
  <area shape="default" href="http://www.xs4all.nl/~ziklies/start.html">
  <area shape="poly" coords="0,56 76,40 91,43 89,67 76,62 6,77 0,60 1,55" href="http://www.xs4all.nl/~ziklies/start.html">
  <area shape="poly" coords="53,72 80,76 81,81 91,85 89,107 76,106 69,137 42,130 51,77" href="http://www.xs4all.nl/~ziklies/e-start.html">
</map>
```

Which works in a modern browser.

## Missing CGI scripts

<https://ziklies.home.xs4all.nl/slaapk/slaap01.html>

```
<FORM METHOD="POST"
ACTION="http://www.xs4all.nl/~ziklies/cgi-bin/barbie.cgi"
```

Uses barbie.cgi script under `~ziklies/cgi-bin/barbie.cgi`. Maar dit script staat onder
`Homepage-html/HOMEPAGE/SLAAPK`!

BUT that contains internal references to `http://www.xs4all.nl/~ziklies/`, probably possible to make this work by editing the hosts file.

Apparently Python http server supports CGI scripts:

<https://docs.python.org/3/library/http.server.html>

## Reconstruct using wget

### Scrape live site

Wget version: GNU Wget 1.19.4 built on linux-gnu.

Script:

<https://github.com/KBNLresearch/xs4all-resources/blob/master/scripts/scrapesite.sh>


- Toilet missing, bc wrong link! But is on live site:

<https://ziklies.home.xs4all.nl/toilet.html>
<https://ziklies.home.xs4all.nl/e-toilet.html>

So scraped again using those pages as seeds:

<https://github.com/KBNLresearch/xs4all-resources/blob/master/scripts/scrape-toilet.sh>

Here "$1" is a reference to a text file with 2 seeds URLs of the  'toilet' pages that are missing from the original capture:  

```
https://ziklies.home.xs4all.nl/toilet.html
https://ziklies.home.xs4all.nl/e-toilet.html
```

Diff on both captures:

```
diff -r ./wget-site/ziklies.home.xs4all.nl/ ./wget-toilet/ziklies.home.xs4all.nl/ > diff-site-toilet.txt
```

Result: "toilet" capture contains everything that is also in the "regular" capture.

