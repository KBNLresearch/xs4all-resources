# Notes Liesbet's atelier

Live site still here:

<https://ziklies.home.xs4all.nl/>

## Scrape site

Wget version: GNU Wget 1.19.4 built on linux-gnu.

Script:

<../scripts/scrapesite.sh>

- Toilet missing, bc wrong link! But is on live site:

<https://ziklies.home.xs4all.nl/toilet.html>
<https://ziklies.home.xs4all.nl/e-toilet.html>

So scraped again using those pages as seeds:

<../scripts/scrape-toilet.sh>

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

## Fix links to toilet

In file "start.html":

```
<B><A HREF="http://imagine.xs4all.nl/ziklies/"> 
Ga naar de toilet</a></B>
```

Target point to external domain that doesn't exist anymore. Changed this to local file:

```
<B><A HREF="toilet.html"> 
Ga naar de toilet</a></B>
```

Likewise for "e-start.html" (with target "e-toilet.html").


## AV formats on toilet page

- Page "toilet.html" links to 3 QuickTime movie files, but this format is not supported by modern web browsers.

- It also links to a Sun Audio (<https://en.wikipedia.org/wiki/Au_file_format>) file.

Likewise for "e-toilet.html".
