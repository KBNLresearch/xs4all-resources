# Liesbet's Atelier Apache setup notes

These notes describe the steps I followed for serving a local copy of the Liesbet's Atelier site.

The general procedure is described here (this also explains how to installation Apache):

<https://github.com/KBNLresearch/nl-menu-resources/blob/master/doc/serving-static-website-with-Apache.md>

## Copy the files

Create directory `ziklies.home.xs4all.nl` in `/var/www`. Then from that directory:

```
sudo rsync -avhl /home/johan//kb/liesbets-atelier/liesbets-atelier/ziklies.home.xs4all.nl/ ./
```

Then fix file and directory permissions:

```
sudo find . -type d -exec chmod 755 {} \;
sudo find . -type f -exec chmod 644 {} \;
```

**NOTE**: scripts in cgi-bin directory also need 755! 

## General site configuration

Copy default config file to a new one for this site:

```
sudo cp /etc/apache2/sites-available/000-default.conf /etc/apache2/sites-available/ziklies.conf
```

Then edit (as sudo), and adjust DocumentRoot:

```
DocumentRoot /var/www/ziklies.home.xs4all.nl
```

Set the server name (needed to make redirects work):

```
ServerName ziklies.home.xs4all.nl
```

## Add site domain to hosts file

Add this line to the hosts file /etc/hosts (mind the TAB character!):

```
127.0.0.1	ziklies.home.xs4all.nl
```

## Activate configuration

Disable default config, then enable new one: 

```
sudo a2dissite 000-default.conf
sudo a2ensite ziklies.conf
```

## Cgi script configuration

Largely adapted from  [this tutorial](https://code-maven.com/set-up-cgi-with-apache) (after getting stuck with the [official Apache documentation](https://httpd.apache.org/docs/2.4/howto/cgi.html), apparently the configuration is slightly different for Ubuntu/Debian based packages)

First copy default cgi config file to custom one:

```
sudo cp /etc/apache2/conf-available/serve-cgi-bin.conf /etc/apache2/conf-available/serve-cgi-bin-custom.conf
```

Then edit:

```
sudo xed /etc/apache2/conf-available/serve-cgi-bin-custom.conf
```

Then 2 options to link `/cgi-bin` to actual directory location::

1. Use ScriptAlias

    ```
    ScriptAlias /cgi-bin/ /var/www/ziklies.home.xs4all.nl/cgi-bin/
    ```

    This works, but the ScriptAlias method assumes all scripts are in same dir, which is unpractical if we use the server setup for multiple sites later on.

2. Use below configuration (adapted from "User Directories" example [here](https://httpd.apache.org/docs/2.4/howto/cgi.html)). This will work for cgi scripts located in *any* `cgi-bin` folder under `/var/www`:

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

For the Liesbet's Atelier project I went for option 2.

## Activate Cgi script configuration

Disable default, then enable custom config:

```
sudo a2disconf serve-cgi-bin.conf
sudo a2enconf serve-cgi-bin-custom.conf
```

Enable cgi:

```
sudo a2enmod cgi.load
```

Restart server:

```
sudo systemctl restart apache2
```

All done!
