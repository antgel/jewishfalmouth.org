#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'Antony Gelberg'
SITENAME = u'Jewish Falmouth'
SITEURL = ''

PATH = 'content'

TIMEZONE = 'Europe/London'

DEFAULT_LANG = u'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
#  LINKS = (('Pelican', 'http://getpelican.com/'),
         #  ('Python.org', 'http://python.org/'),
         #  ('Jinja2', 'http://jinja.pocoo.org/'),
         #  ('You can modify those links in your config file', '#'),)

# Social widget
#  SOCIAL = (('You can add links in your config file', '#'),
          #  ('Another social link', '#'),)

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
# RELATIVE_URLS = True

PLUGIN_PATHS = ['../pelican-plugins']
PLUGINS = ['pelican_dynamic', 'photos']

DISPLAY_PAGES_ON_MENU = False

# https://github.com/getpelican/pelican-plugins/tree/master/photos
PHOTO_LIBRARY = "pictures"
PHOTO_RESIZE_JOBS = 4
PHOTO_EXIF_KEEP = True
PHOTO_EXIF_REMOVE_GPS = False

THEME = 'themes/notmyidea'
