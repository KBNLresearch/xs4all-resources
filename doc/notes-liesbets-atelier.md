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

## Image map index page

Original site: server-side [image maps](https://en.wikipedia.org/wiki/Image_map). in HTML:

```
<A HREF="/cgi-bin/imagemap/~ziklies/deurtje1.map"><img src="deurtje1.gif" Border=0 ISMAP></A>
```

Contents of `DEURTJE1.MAP` file (from ZIP file provided by site creator):

```
default http://www.xs4all.nl/~ziklies/start.html
poly http://www.xs4all.nl/~ziklies/start.html 0,56 76,40 91,43 89,67 76,62 6,77 0,60 1,55 
poly http://www.xs4all.nl/~ziklies/e-start.html 53,72 80,76 81,81 91,85 89,107 76,106 69,137 42,130 51,77
```

Server-side image maps are obsolete and don't work in modern browsers (source), but it is possible to convert the image map into a client-side image map. This can be done by replacing the *A* element in the HTML by this: 

```
<img src="deurtje1.gif" usemap="#deurtje1Map" alt="deurtje 1" border="0">
<map name="deurtje1Map">
    <area shape="poly" coords="0,56 76,40 91,43 89,67 76,62 6,77 0,60 1,55" href="http://www.xs4all.nl/~ziklies/start.html">
    <area shape="poly" coords="53,72 80,76 81,81 91,85 89,107 76,106 69,137 42,130 51,77" href="http://www.xs4all.nl/~ziklies/e-start.html">
    <area shape="default" href="http://www.xs4all.nl/~ziklies/start.html">
</map>
```

Which works in a modern browser.

## Image map start.html

Same as above:

```
<A HREF="/cgi-bin/imagemap/~ziklies/hal.map">
<img src="hal.gif" Align="right" Border=0 ISMAP></A>
```

Server-side image map `HAL.MAP`(from ZIP file provided by site creator):

```
default http://www.xs4all.nl/~ziklies/woonk/woon01.html
rect http://www.xs4all.nl/~ziklies/prikbord.html 69,7 153,57
rect http://www.xs4all.nl/~ziklies/woonk/woon01.html 5,59 63,139
rect http://imagine.xs4all.nl/ziklies/ 5,162 62,242
rect http://www.xs4all.nl/~ziklies/logeer1.html 246,57 307,142
rect http://imagine.xs4all.nl/ziklies/ 247,162 307,244
poly http://www.xs4all.nl/~ziklies/trap.html 170,51 214,4 244,3 246,31 186,72 169,55
rect http://imagine.xs4all.nl/ziklies/ 5,160 62,243
rect http://www.xs4all.nl/~ziklies/keuken/keuken1.html 245,58 306,141
rect http://www.xs4all.nl/~ziklies/logeer1.html 244,161 308,246
```

So convert to:

```
<img src="hal.gif" usemap="#halMap" align="right" alt="hal" border="0">
<map name="halMap">
    <area shape="rect" coords="69,7 153,57" href="http://www.xs4all.nl/~ziklies/prikbord.html">
    <area shape="rect" coords="5,59 63,139" href="http://www.xs4all.nl/~ziklies/woonk/woon01.html">
    <area shape="rect" coords="5,162 62,242" href="http://imagine.xs4all.nl/ziklies/">
    <area shape="rect" coords="246,57 307,142" href="http://www.xs4all.nl/~ziklies/logeer1.html">
    <area shape="rect" coords="247,162 307,244" href="http://imagine.xs4all.nl/ziklies">
    <area shape="poly" coords="170,51 214,4 244,3 246,31 186,72 169,55" href="http://www.xs4all.nl/~ziklies/trap.html">
    <area shape="rect" coords="5,160 62,243" href="http://imagine.xs4all.nl/ziklies/">
    <area shape="rect" coords="245,58 306,141" href="http://www.xs4all.nl/~ziklies/keuken/keuken1.html">
    <area shape="rect" coords="244,161 308,246" href="http://www.xs4all.nl/~ziklies/logeer1.html">
    <area shape="default" href="http://www.xs4all.nl/~ziklies/woonk/woon01.html">
</map>
```
## Image map e-start.html

Same as above:

```
<A HREF="/cgi-bin/imagemap/~ziklies/e-hal.map">
<img src="e-hal.gif" Align="right" Border=0 ISMAP></A>
```

Server-side image map `E-HAL.MAP`(from ZIP file provided by site creator):

```
default http://www.xs4all.nl/~ziklies/woonk/e-woon01.html
rect http://www.xs4all.nl/~ziklies/keuken/e-keuk1.html 0,159 66,245 
rect http://www.xs4all.nl/~ziklies/e-logr1.html 246,59 307,142 
rect http://imagine.xs4all.nl/ziklies/ 245,161 308,244 
rect http://www.xs4all.nl/~ziklies/e-prikb.html 69,5 155,57 
poly http://www.xs4all.nl/~ziklies/e-trap.html 167,54 213,1 260,0 255,38 189,82 167,55 
rect http://www.xs4all.nl/~ziklies/woonk/e-woon01.html 2,55 65,140 
```

Convert to:

```
<img src="e-hal.gif" usemap="#ehalMap" align="right" alt="e-hal" border="0">
<map name="ehalMap">
    <area shape="rect" coords="0,159 66,245" href="http://www.xs4all.nl/~ziklies/keuken/e-keuk1.html">
    <area shape="rect" coords="246,59 307,142" href="http://www.xs4all.nl/~ziklies/e-logr1.html">
    <area shape="rect" coords="245,161 308,244" href="http://imagine.xs4all.nl/ziklies/">
    <area shape="rect" coords="69,5 155,57" href="http://www.xs4all.nl/~ziklies/e-prikb.html">
    <area shape="poly" coords="167,54 213,1 260,0 255,38 189,82 167,55" href="http://www.xs4all.nl/~ziklies/e-trap.html">
    <area shape="rect" coords="2,55 65,140" href="http://www.xs4all.nl/~ziklies/woonk/e-woon01.html">
    <area shape="default" href="http://www.xs4all.nl/~ziklies/woonk/e-woon01.html">
</map>
```

## Image map overloop.html

Same as above:

```
<A HREF="/cgi-bin/imagemap/~ziklies/overloop.map">
<img src="overloop.gif" Align="right" Border=0 ISMAP></A>
```

Server-side image map `OVERLOOP.MAP`(from ZIP file provided by site creator):

```
default http://www.xs4all.nl/~ziklies/badkamer.html
rect http://www.xs4all.nl/~ziklies/atelier/atelier1.html 1,1 64,98 
rect http://www.xs4all.nl/~ziklies/doka.html 0,102 66,203 
rect http://www.xs4all.nl/~ziklies/slaapk/slaap00.html 195,1 278,102 
rect http://www.xs4all.nl/~ziklies/zolder/zolder1.html 195,104 258,202 
rect http://www.xs4all.nl/~ziklies/trapaf.html 112,176 187,237 
```

Convert to:

```
<img src="overloop.gif" usemap="#overloopMap" align="right" alt="overloop" border="0">
<map name="overloopMap">
    <area shape="rect" coords="1,1 64,98" href="http://www.xs4all.nl/~ziklies/atelier/atelier1.html">
    <area shape="rect" coords="0,102 66,203" href="http://www.xs4all.nl/~ziklies/doka.html">
    <area shape="rect" coords="195,1 278,102" href="http://www.xs4all.nl/~ziklies/slaapk/slaap00.html">
    <area shape="rect" coords="195,104 258,202" href="http://www.xs4all.nl/~ziklies/zolder/zolder1.html">
    <area shape="rect" coords="112,176 187,237" href="http://www.xs4all.nl/~ziklies/trapaf.html">
    <area shape="default" href="http://www.xs4all.nl/~ziklies/badkamer.html">
</map>
```

## Image map e-overloop.html

Same as above:

```
<A HREF="/cgi-bin/imagemap/~ziklies/e-overl.map">
<img src="e-overl.gif" Align="right" Border=0 ISMAP></A>
```

Server-side image map `E-OVERL.MAP`(from ZIP file provided by site creator):

```
default http://www.xs4all.nl/~ziklies/trapaf.html
rect http://www.xs4all.nl/~ziklies/atelier/e-atelr1.html 1,0 63,99 
rect http://www.xs4all.nl/~ziklies/doka.html 0,104 64,204 
rect http://www.xs4all.nl/~ziklies/slaapk/e-slaap0.html 195,1 278,101 
rect http://www.xs4all.nl/~ziklies/zolder/zolder1.html 195,103 258,210 
rect http://www.xs4all.nl/~ziklies/e-trapaf.html 116,176 188,237 
```

Convert to:

```
<img src="e-overl.gif" usemap="#eOverloopMap" align="right" alt="e-overloop" border="0">
<map name="eOverloopMap">
    <area shape="rect" coords="1,0 63,99" href="http://www.xs4all.nl/~ziklies/atelier/e-atelr1.html">
    <area shape="rect" coords="0,104 64,204" href="http://www.xs4all.nl/~ziklies/doka.html">
    <area shape="rect" coords="195,1 278,101" href="http://www.xs4all.nl/~ziklies/slaapk/e-slaap0.html">
    <area shape="rect" coords="195,103 258,210" href="http://www.xs4all.nl/~ziklies/zolder/zolder1.html">
    <area shape="rect" coords="116,176 188,237" href="http://www.xs4all.nl/~ziklies/e-trapaf.html">
    <area shape="default" href="http://www.xs4all.nl/~ziklies/trapaf.html">
</map>
```

## AV formats on toilet page

- Page "toilet.html" links to 3 QuickTime movie files, but this format is not supported by modern web browsers.

- It also links to a Sun Audio (<https://en.wikipedia.org/wiki/Au_file_format>) file.

Likewise for "e-toilet.html".
