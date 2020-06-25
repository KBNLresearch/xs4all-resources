# Liesbet's atelier WARC capture and rendering notes

These describe the capture process of the restored Liesbet's Atelier site to WARC, and how this WARC can be played back.

## Capture local site to compressed warc

Started out with [this script](../scripts/scrape-local-site.sh) (adapted from earlier NL-menu work) which use wget. However, this doesn't capture the interactive bedroom mirror (i.e. the "barbie" scripts). Following a suggestion by Ilya Kreymer I switched to [warcio](https://github.com/webrecorder/warcio), and wrote the script [scrape-ziklies-local.py](./scripts/scripts/scrape-ziklies-local.py), which captures all possible results of this script.

## Render warc

Install pywb:

```
python3 -m install --user pywb
```

(BTW installation process reports `Segmentation fault (core dumped)` at end of install, but after this everything seems to work fine.)

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
wb-manager add ziklies /home/johan/kb/liesbets-atelier/warc/ziklies.home.xs4all.nl.warc.gz
```

Start pywb:

```
wayback
```

Archived website now accessible from browser at below link:

<http://localhost:8080/ziklies/20200618150835/http://ziklies.home.xs4all.nl/>

Seems to work perfectly, interactive bedroom mirror also fully functional.
