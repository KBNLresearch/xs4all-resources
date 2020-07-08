
```
python WCMUUR.PY
```

Result:

```
ImportError: No module named gd
```
Looks like  gd refers to this module:

<http://newcenturycomputers.net/projects/gdmodule.html>

Github:

<https://github.com/Solomoriah/gdmodule>

Require install of Thomas Boutell's GD library, but provided link (<http://www.boutell.com/gd/>) now resolves to "short-term loan" site.

Current site:

<https://libgd.github.io/>

Install libgd:

```
sudo apt-get update -y
sudo apt-get install -y libgd-dev
```

Install gdmodule - first install libpython2.7-dev:


```
sudo apt install libpython2.7-dev
```

Then (note: needs global install, as user install won't work when running from Apache!!):

```
git clone https://github.com/Solomoriah/gdmodule
cd gdmodule
sudo python setup.py install
```

BUT installation gives errors:

```
collect2: error: ld returned 1 exit status
error: command 'x86_64-linux-gnu-gcc' failed with exit status 1
```

Looking into detail seems to be about missing format libraries for JPEG, PNG or GIF:

```
gdlib-config: not found -lgd -ljpeg -lX11 -lXpm -lfreetype -lpng -lgif -lz -o build/lib.linux-x86_64-2.7/_gd.so
/usr/bin/ld: cannot find -lgif
```

Turns out GIF library is culprit, so:

```
sudo apt install libgif-dev
```

After this install  works. So try again:

```
python WCMUUR.PY
```

Result:

```
ImportError: No module named rand
```

Python 1.x had [standard module rand](https://docs.python.org/release/1.4/lib/node57.html#SECTION00620000000000000000); function rand "Returns an integer random number in the range [0 ... 32768). So rewrote that using current random function.


Script refers to location at prima12.xs4all.nl. Internet Archive search turns up this:

<https://web.archive.org/web/19981205234146/http://prima12.xs4all.nl/liesbet/toilet.html>

```html
<form method="POST" action="/web/19981205234146/http://prima12.xs4all.nl/cgi-bin/Liesbet/wcmuur.py">

<input type="text" name="toiletmessage" value="kras hier" size="60">
```

Image also there:

```html
<img src="http://prima12.xs4all.nl/liesbet/wctxt.gif?XXX">
```

## Server

Script needs write access to dir where "wctxt.gif" is stored! See:

<https://stackoverflow.com/a/33622448/1209004>

So:

```
sudo chgrp www-data /var/www/ziklies.home.xs4all.nl/toilet
sudo chmod g+rwx /var/www/ziklies.home.xs4all.nl/toilet
```

Make existing files in directory writable:

```
sudo chgrp www-data /var/www/ziklies.home.xs4all.nl/toilet/*
sudo chmod g+rw /var/www/ziklies.home.xs4all.nl/toilet/*
```

## Python 3

No Python 3 support for gdmodule, and developer closed feature request on this:

<https://github.com/Solomoriah/gdmodule/issues/3>

Forked the repo and made some changes trying to update the code here:

<https://github.com/KBNLresearch/gdmodule>

Use this for C-extension changes:

<http://python3porting.com/cextensions.html>

Got stuck on this error:

```
python3 setup.py install --user
```

```
_gdmodule.c: In function ‘write_file’:
_gdmodule.c:209:41: error: ‘PyFile_Type’ undeclared (first use in this function); did you mean ‘PyFilter_Type’?
```

More info here:

<https://stackoverflow.com/questions/8195383/pyfile-type-replaced-by>

So no obvious solution.