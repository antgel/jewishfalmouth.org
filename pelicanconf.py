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
PLUGINS = ['i18n_subsites', 'photos']

DISPLAY_PAGES_ON_MENU = False

# https://github.com/getpelican/pelican-plugins/tree/master/photos
PHOTO_LIBRARY = "pictures"
PHOTO_RESIZE_JOBS = 4
PHOTO_EXIF_KEEP = True
PHOTO_EXIF_REMOVE_GPS = False

THEME = '../pelican-themes-antgel/pelican-bootstrap3'
JINJA_ENVIRONMENT = {'extensions': ['jinja2.ext.i18n']}
I18N_TEMPLATES_LANG = 'en'
BOOTSTRAP_THEME = 'journal'
CUSTOM_CSS = 'css/lightbox.css'
CUSTOM_JS = 'js/custom.js'
HIDE_SITENAME = True
BANNER = 'photos/town/harbour-view-1280x375a.jpg'
BANNER_ALL_PAGES = True
# BOOTSTRAP_FLUID = False
# HIDE_SIDEBAR = False
PADDED_SINGLE_COLUMN_STYLE = True
