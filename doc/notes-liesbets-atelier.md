# Notes Liesbet's atelier

Live site still here:

<https://ziklies.home.xs4all.nl/>

## Scrape site

Wget version: GNU Wget 1.19.4 built on linux-gnu.

Script:

[scrapesite.sh](../scripts/scrapesite.sh)

- Toilet missing, bc wrong link! But is on live site:

<https://ziklies.home.xs4all.nl/toilet.html>
<https://ziklies.home.xs4all.nl/e-toilet.html>

So scraped again using those pages as seeds:

[scrape-toilet.sh](../scripts/scrape-toilet.sh)

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

## Replace links to website root

For internal links site uses a mixture of relative URLs (which work fine) and absolute ones that use the website root `http://www.xs4all.nl/~ziklies/`, which is forwarded by X4ALL to `https://ziklies.home.xs4all.nl/`. This causes some issues, so I've rewritten these absolute internal URLs as relative links. Script:

<https://github.com/KBNLresearch/xs4all-resources/blob/master/scripts/rewriteurls.sh>

BUT note that this affects the appearance of the statistics page:

<http://127.0.0.1:8000/statistics.html>

Fixed this by undoing commit for this one single file using:

```
git checkout HEAD^ -- ziklies.home.xs4all.nl/statistics.html
```

## Mail form, toilet page

Page:

<https://ziklies.home.xs4all.nl/toilet.html>

Form:

```
<FORM METHOD="POST" ACTION="/cgi-bin/mail-a-form">
<INPUT TYPE="hidden" name="to" value="ziklies">
<INPUT TYPE="hidden" name="nextpage" value="/toilet.html">
<INPUT TYPE="hidden"  NAME="signature" VALUE="toilet@message" >
<INPUT TYPE="text"  NAME="toiletmessage" VALUE="kras hier"SIZE=60>

<!TEXTAREA NAME="message_body" Rows=1 Cols=60 ></TEXTAREA><br>
<p>

<INPUT TYPE="submit" VALUE="verstuur tekst"> . . . . 
<INPUT TYPE="reset" VALUE="wis boodschap"><br>
of een emailtje te sturen met gif-plaatje.
</FORM><br>
```

The `ACTION` attribute of the form defines form handler (page with script that handles the submitted form data) `http://www.xs4all.nl/cgi-bin/mail-a-form`. It is documented here:

<https://www.xs4all.nl/service/installeren/hosting/mail-a-form-toevoegen/>


Moreover the ZIP file contains an old Python script that appears to read a message submitted through the form, and then adds it to the image:

```
~/kb/liesbets-atelier/liesbets-atelier-zip/Homepage-html/HOMEPAGE/TOILET/WCMUUR.PY`
```

BUT this is an old Python version (1.4), and not clear how I/O works exactly (besides the submit form doesn't do)

Also, as per site's author (email to Kees, October 2019):

> Het scriptje voor de toiletdeur is er misschien niet meer.
> Was door een Delftse student gemaakt en misschien direct in de juiste map
> gezet.
> Zou het niet meer precies weten.
> In eerste instantie maakte ik zelf met de hand een update van de
> toiletdeur. Pas later kwam er dat scriptje.

**Action:** leave as-is.

## Find more forms

```
grep -r "<FORM" ~/kb/liesbets-atelier/liesbets-atelier/ > grep.txt
```

Result:

```
/home/johan/kb/liesbets-atelier/liesbets-atelier/ziklies.home.xs4all.nl/toilet.html:<FORM METHOD="POST" ACTION="/cgi-bin/mail-a-form">
/home/johan/kb/liesbets-atelier/liesbets-atelier/ziklies.home.xs4all.nl/slaapk/e-slaap1.html:<FORM METHOD="POST"
/home/johan/kb/liesbets-atelier/liesbets-atelier/ziklies.home.xs4all.nl/slaapk/slaap01.html:<FORM METHOD="POST"
/home/johan/kb/liesbets-atelier/liesbets-atelier/ziklies.home.xs4all.nl/e-toilet.html:<FORM METHOD="POST" ACTION="/cgi-bin/mail-a-form">
```

## Slaapkamer form

```
<FORM METHOD="POST"
ACTION="/cgi-bin/barbie.cgi">

<DL>
<DD><b>Als eerste: welke broek of rok moet ze aandoen? </b><br>
<INPUT TYPE="radio" NAME="onder" VALUE="1a" > A1
<INPUT TYPE="radio" NAME="onder" VALUE="2a" > A2
<INPUT TYPE="radio" NAME="onder" VALUE="3a" > A3
<INPUT TYPE="radio" NAME="onder" VALUE="4a" > A4
<INPUT TYPE="radio" NAME="onder" VALUE="5a" > A5
<INPUT TYPE="radio" NAME="onder" VALUE="6a" > A6
<INPUT TYPE="radio" NAME="onder" VALUE="7a" > A7<br>
</DL>
<br>
<DL>
<DD><b>En dan: welk topje, trui, blouze of jasje past daarbij? </b><br>
<INPUT TYPE="radio" NAME="midden" VALUE="1b" > B1
<INPUT TYPE="radio" NAME="midden" VALUE="2b" > B2
<INPUT TYPE="radio" NAME="midden" VALUE="3b" > B3
<INPUT TYPE="radio" NAME="midden" VALUE="4b" > B4
<INPUT TYPE="radio" NAME="midden" VALUE="5b" > B5
<INPUT TYPE="radio" NAME="midden" VALUE="6b" > B6
<INPUT TYPE="radio" NAME="midden" VALUE="7b" > B7<br>
</DL>
<br>
<DL>
<DD><b>En als laatste: welke oorbellen en wat moet ze met haar haar? </b><br>
<INPUT TYPE="radio" NAME="top" VALUE="1c" > C1
<INPUT TYPE="radio" NAME="top" VALUE="2c" > C2
<INPUT TYPE="radio" NAME="top" VALUE="3c" > C3
<INPUT TYPE="radio" NAME="top" VALUE="4c" > C4
<INPUT TYPE="radio" NAME="top" VALUE="5c" > C5
<INPUT TYPE="radio" NAME="top" VALUE="6c" > C6
<INPUT TYPE="radio" NAME="top" VALUE="7c" > C7<br>
</DL><br>
<center>
<INPUT TYPE="submit" VALUE="kijk in de spiegel voor het resultaat">
<br></center>
</FORM>
```

Script `barbie.cgi` (and `barbie1.cgi` for English version) included in ZIP file. Steps:

1. Create `cgi-bin` directory at website root
2. Copy `barbie.cgi` and `barbie.cgi` over to this dir
3. Make it executable using `chmod 755 barbie.cgi`
4. Start server with `--cgi` flag, i.e. `python3 -m http.server --cgi`
5. Inside scripts, replace `http://www.xs4all.nl/~ziklies/` with `/`.
6. Copy the 21 1A.GIF ... 7C.GIF files to `slaapk`, and change name + extension to lowercase (see also <https://ziklies.home.xs4all.nl/slaapk/>). 

BUT submitting the form then results in this:

```
FileNotFoundError: [Errno 2] No such file or directory: '/home/johan/kb/liesbets-atelier/liesbets-atelier/ziklies.home.xs4all.nl/cgi-bin/barbie.cgi'
```
Not clear why this happens, as neither the form nor the script refer to the `ziklies.home.xs4all.nl` subdomain.

From:

<https://stackoverflow.com/questions/13490311/cgi-scripts-with-python/14739973>

Problem is actually this line in `barbie.cgi` and `barbie1.cgi`:

```
#!/usr/local/bin/perl
```

This doesn't exist, so changed to:

```
#!/usr/bin/perl
```

After this change the script executes without errors, but it doesn't seem to have any effect.

## Missing gspot directory + files

This directory is missing from scraped site (and ZIP as well) because it is only referenced through JavaScript:

<https://ziklies.home.xs4all.nl/slaapk/gspot/>

Javascript reference (in `slaap01.html` + English version)

```
<A HREF="javascript:openit('gspot/index.html')">
```

File source:

```
<HTML>
<HEAD>
<TITLE>G_spot</TITLE>
</HEAD>
<BODY BGCOLOR="#000000" LINK="#E7E801" VLINK="#E7E801">
<TABLE BORDER="0" CELLSPACING="0" WIDTH=100% HEIGHT=100%>
<TR >
<TD ALIGN=CENTER VALIGN=MIDDLE>
<FONT FACE="arial,helvetica" SIZE=3 COLOR="#E7E801">
<embed SRC="gspot.dcr" BGCOLOR=#000000 WIDTH=512 HEIGHT=320>       
</font>
</td>
</tr>
</table>
</body>
</html>
```


Note referenced file `gspot.dcr`. These files are also missing from the ZIP file. 


Fix:

1. Manually create `gspot` directory
2. Add files using `wget`:
   - `wget https://ziklies.home.xs4all.nl/slaapk/gspot/index.html`
   - `wget https://ziklies.home.xs4all.nl/slaapk/gspot/gspot.dcr`

But what is a .dcr file?

- Caja file manager: Kodak DCR Raw image
- File: RIFF (big-endian) data
- Siegfried: 'Macromedia (Adobe) Director Compressed Resource file' ('extension match dcr; byte match at 0, 12 (signature 1/2)')
- Apache Tika: application/x-director

More info here:

<http://fileformats.archiveteam.org/wiki/Shockwave_(Director)>

<https://en.wikipedia.org/wiki/Adobe_Shockwave>

<https://medium.com/@nosamu/a-tour-of-the-adobe-director-file-format-e375d1e063c0>

How to play these files:

<https://gaming.stackexchange.com/questions/339173/how-can-i-play-dcr-shockwave-games>

Internet Explorer 11: won't install in Wine!

## Find more scripting

```
grep -r "/cgi-bin" ~/kb/liesbets-atelier/liesbets-atelier/ > grep.txt
```

Result:

```
/home/johan/kb/liesbets-atelier/liesbets-atelier/ziklies.home.xs4all.nl/index.html:<a href="http://www.nedstat.nl/cgi-bin/viewstat?name=at1tel">
/home/johan/kb/liesbets-atelier/liesbets-atelier/ziklies.home.xs4all.nl/index.html:<img src="http://www.nedstat.nl/cgi-bin/nedstat.gif?name=at1tel" 
/home/johan/kb/liesbets-atelier/liesbets-atelier/ziklies.home.xs4all.nl/slaapk/e-slaap1.html:document.write("<img src=\"http://www.nedstat.nl/cgi-bin/referstat.gif?name=slptel&refer="+escape(document.referrer)+"\" width=1 height=1 alt=\"\">");
/home/johan/kb/liesbets-atelier/liesbets-atelier/ziklies.home.xs4all.nl/slaapk/e-slaap1.html:ACTION="/cgi-bin/barbie1.cgi">
/home/johan/kb/liesbets-atelier/liesbets-atelier/ziklies.home.xs4all.nl/slaapk/e-slaap1.html:<a href="http://www.nedstat.nl/cgi-bin/viewstat?name=slptel">
/home/johan/kb/liesbets-atelier/liesbets-atelier/ziklies.home.xs4all.nl/slaapk/e-slaap1.html:<img src="http://www.nedstat.nl/cgi-bin/nedstat.gif?name=slptel" 
/home/johan/kb/liesbets-atelier/liesbets-atelier/ziklies.home.xs4all.nl/slaapk/e-slaap0.html:document.write("<img src=\"http://www.nedstat.nl/cgi-bin/referstat.gif?name=slptel&refer="+escape(document.referrer)+"\" width=1 height=1 alt=\"\">");
/home/johan/kb/liesbets-atelier/liesbets-atelier/ziklies.home.xs4all.nl/slaapk/e-slaap0.html:<a href="http://www.nedstat.nl/cgi-bin/viewstat?name=slptel">
/home/johan/kb/liesbets-atelier/liesbets-atelier/ziklies.home.xs4all.nl/slaapk/e-slaap0.html:<img src="http://www.nedstat.nl/cgi-bin/nedstat.gif?name=slptel" 
/home/johan/kb/liesbets-atelier/liesbets-atelier/ziklies.home.xs4all.nl/slaapk/slaap00.html:document.write("<img src=\"http://www.nedstat.nl/cgi-bin/referstat.gif?name=slptel&refer="+escape(document.referrer)+"\" width=1 height=1 alt=\"\">");
/home/johan/kb/liesbets-atelier/liesbets-atelier/ziklies.home.xs4all.nl/slaapk/slaap00.html:<a href="http://www.nedstat.nl/cgi-bin/viewstat?name=slptel">
/home/johan/kb/liesbets-atelier/liesbets-atelier/ziklies.home.xs4all.nl/slaapk/slaap00.html:<img src="http://www.nedstat.nl/cgi-bin/nedstat.gif?name=slptel" 
/home/johan/kb/liesbets-atelier/liesbets-atelier/ziklies.home.xs4all.nl/slaapk/slaap01.html:document.write("<img src=\"http://www.nedstat.nl/cgi-bin/referstat.gif?name=slptel&refer="+escape(document.referrer)+"\" width=1 height=1 alt=\"\">");
/home/johan/kb/liesbets-atelier/liesbets-atelier/ziklies.home.xs4all.nl/slaapk/slaap01.html:ACTION="/cgi-bin/barbie.cgi">
/home/johan/kb/liesbets-atelier/liesbets-atelier/ziklies.home.xs4all.nl/slaapk/slaap01.html:<a href="http://www.nedstat.nl/cgi-bin/viewstat?name=slptel">
/home/johan/kb/liesbets-atelier/liesbets-atelier/ziklies.home.xs4all.nl/slaapk/slaap01.html:<img src="http://www.nedstat.nl/cgi-bin/nedstat.gif?name=slptel" 
/home/johan/kb/liesbets-atelier/liesbets-atelier/ziklies.home.xs4all.nl/start.html:document.write("<img src=\"http://www.nedstat.nl/cgi-bin/referstat.gif?name=attel&refer="+escape(document.referrer)+"\" width=1 height=1 alt=\"\">");
/home/johan/kb/liesbets-atelier/liesbets-atelier/ziklies.home.xs4all.nl/start.html:<a href="http://www.xs4all.nl/cgi-bin/vote/vote.cgi?ziklies">
/home/johan/kb/liesbets-atelier/liesbets-atelier/ziklies.home.xs4all.nl/start.html:<a href="http://www.nedstat.nl/cgi-bin/viewstat?name=attel">
/home/johan/kb/liesbets-atelier/liesbets-atelier/ziklies.home.xs4all.nl/start.html:<img src="http://www.nedstat.nl/cgi-bin/nedstat.gif?name=attel"
/home/johan/kb/liesbets-atelier/liesbets-atelier/ziklies.home.xs4all.nl/bad/zeil01.htm:<a href="http://www.nedstat.nl/cgi-bin/viewstat?name=malta">
/home/johan/kb/liesbets-atelier/liesbets-atelier/ziklies.home.xs4all.nl/bad/zeil01.htm:<img src="http://www.nedstat.nl/cgi-bin/nedstat.gif?name=malta" 
/home/johan/kb/liesbets-atelier/liesbets-atelier/ziklies.home.xs4all.nl/bad/kaart00.htm:<a href="http://www.nedstat.nl/cgi-bin/viewstat?name=gam">
/home/johan/kb/liesbets-atelier/liesbets-atelier/ziklies.home.xs4all.nl/bad/kaart00.htm:<img src="http://www.nedstat.nl/cgi-bin/nedstat.gif?name=gam" 
/home/johan/kb/liesbets-atelier/liesbets-atelier/ziklies.home.xs4all.nl/bad/zeil00.htm:<!a href="http://www.nedstat.nl/cgi-bin/viewstat?name=gam">
/home/johan/kb/liesbets-atelier/liesbets-atelier/ziklies.home.xs4all.nl/bad/zeil00.htm:<!img src="http://www.nedstat.nl/cgi-bin/nedstat.gif?name=gam" 
/home/johan/kb/liesbets-atelier/liesbets-atelier/ziklies.home.xs4all.nl/new.html:<a href="http://www.xs4all.nl/cgi-bin/vote/vote.cgi?ziklies>
/home/johan/kb/liesbets-atelier/liesbets-atelier/ziklies.home.xs4all.nl/new.html:<a href="http://www.xs4all.nl/cgi-bin/vote/vote.cgi?ziklies>
/home/johan/kb/liesbets-atelier/liesbets-atelier/ziklies.home.xs4all.nl/e-toilet.html:<FORM METHOD="POST" ACTION="/cgi-bin/mail-a-form">
```

- Most are refs to scripts at nedstat.nl (offline; actually slows things down a bit)
- On start.html, new.html: link to voting script http://www.xs4all.nl/cgi-bin/vote/vote.cgi

## Keep track of changes

Site data in Git repo, commit for each modification:

![](./images/liesbet-gitk.png)

## Serve with Apache

See:

<https://github.com/KBNLresearch/nl-menu-resources/blob/master/doc/serving-static-website-with-Apache.md>

Create directory `ziklies.home.xs4all.nl` in `/var/www`. Then from that directory:

```
sudo rsync -avhl /home/johan//kb/liesbets-atelier/liesbets-atelier/ziklies.home.xs4all.nl/ ./
```

Then fix permissions:

```
sudo find . -type d -exec chmod 755 {} \;
sudo find . -type f -exec chmod 644 {} \;
```

Create config file:

```
sudo cp /etc/apache2/sites-available/000-default.conf /etc/apache2/sites-available/ziklies.conf
```

Then edit (as sudo), and adjust DocumentRoot:

```
DocumentRoot /var/www/ziklies.home.xs4all.nl
```

And also set server name (needed to make redirects work):

```
ServerName ziklies.home.xs4all.nl
```

Activate new config:

```
sudo a2dissite 000-default.conf
sudo a2ensite ziklies.conf
```

Add line to hosts file:

```
127.0.0.1	ziklies.home.xs4all.nl
```

Restart server:

```
sudo systemctl restart apache2
```

## Enable cgi scripts

Info from [Apache docs](https://httpd.apache.org/docs/2.4/howto/cgi.html) doesn't  seem to work, so followed [this tutorial](https://code-maven.com/set-up-cgi-with-apache) instead.

First copy default cgi config file to custom one:

```
sudo cp /etc/apache2/conf-available/serve-cgi-bin.conf /etc/apache2/conf-available/serve-cgi-bin-custom.conf
```

Then edit:

```
sudo xed /etc/apache2/conf-available/serve-cgi-bin-custom.conf
```
Change "Directory" to:

```
<Directory "/var/www/ziklies.home.xs4all.nl/cgi-bin">
```

Disable default config:

```
sudo a2disconf serve-cgi-bin.conf
```

Enable custom one:

```
sudo a2enconf serve-cgi-bin-custom.conf
```

Enable cgi:

```
sudo a2enmod cgi.load
```

Restart server:

```
sudo systemctl reload apache2
```

Calling script results in "403 Forbidden". Check error log:

```
xed /var/log/apache2/error.log
```

Which contains:

```
[Fri Jun 19 14:40:27.083544 2020] [authz_core:error] [pid 9144:tid 140374009665280] [client 127.0.0.1:39262] AH01630: client denied by server configuration: /usr/lib/cgi-bin/barbie.cgi, referer: http://ziklies.home.xs4all.nl/slaapk/slaap01.html
```

So it seems server looks for script at wrong location. Changed in "serve-cgi-bin-custom.conf":

```
ScriptAlias /cgi-bin/ /usr/lib/cgi-bin/
```

Into:

```
ScriptAlias /cgi-bin/ /var/www/ziklies.home.xs4all.nl/cgi-bin/
```

Then:

```
sudo a2disconf serve-cgi-bin-custom.conf
sudo a2enconf serve-cgi-bin-custom.conf
sudo systemctl reload apache2
```

After these changes it works!

## More generic method

The ScriptAlias method assumes all scripts are in same dir, which is unpractical if we use the server setup for multiple sites later on. Below configuration (adapted from "User Directories" example [here](https://httpd.apache.org/docs/2.4/howto/cgi.html)) will work for cgi scripts located in any `cgi-bin` folder under `/var/www`:

```
<IfModule mod_alias.c>
	<IfModule mod_cgi.c>
		Define ENABLE_USR_LIB_CGI_BIN
	</IfModule>

	<IfModule mod_cgid.c>
		Define ENABLE_USR_LIB_CGI_BIN
	</IfModule>

	<IfDefine ENABLE_USR_LIB_CGI_BIN>
		<Directory "/var/www/*/cgi-bin">
			Options +ExecCGI
			AddHandler cgi-script .cgi
		</Directory>
	</IfDefine>
</IfModule>

# vim: syntax=apache ts=4 sw=4 sts=4 sr noet
```

## Scrape local site to warc

Used script [scrape-local-site.sh](../scripts/scrape-local-site.sh) (adapted from earlier NL-menu work).


## Render warc

Install pywb:

```
python3 -m install --user pywb
```

(BTW installation process reports `Segmentation fault (core dumped)` at end of install!)

Create web archives directory and then enter it:

```
mkdir web-archives
cd web-archives
```

Create new archive:

```
wb-manager init ziklies
```

Add warc file to archive:

```
wb-manager add ziklies /home/johan/kb/liesbets-atelier/warc/ziklies.home.xs4all.nl.warc
```

Start pywb:

```
wayback
```

Archived website now accessible from browser at below link:

<http://localhost:8080/ziklies/20200618150835/http://ziklies.home.xs4all.nl/>
- 

## AV formats on toilet page

- Page "toilet.html" links to 3 QuickTime movie files, but this format is not supported by modern web browsers.

- It also links to a Sun Audio (<https://en.wikipedia.org/wiki/Au_file_format>) file.

Likewise for "e-toilet.html".

## Misc

Bio of creator Liesbet Zikkenheimer:

<http://zicnet.nl/>

Interview:

<https://www.netkwesties.nl/documenten/Interview%20Liesbet%20Zikkenheimer.pdf>
