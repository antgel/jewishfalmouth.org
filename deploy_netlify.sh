#!/bin/sh -x

git clone https://github.com/getpelican/pelican-themes
pelican-themes --install pelican-themes/pelican-bootstrap3/
pelican -s publishconf.py
