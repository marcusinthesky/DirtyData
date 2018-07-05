#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'Marcus Gawronsky'
SITENAME = 'DirtyData'
SITEURL = ''

PATH = 'content'

TIMEZONE = 'Africa/Johannesburg'

DEFAULT_LANG = 'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (('Pelican', 'http://getpelican.com/'),
         ('Python.org', 'http://python.org/'),)

# Social widget
SOCIAL = (('Twitter', 'https://twitter.com/marcusinthesky'),
         ('GitHub', 'https://github.com/marcusinthesky'),
         ('LinkedIn', 'https://za.linkedin.com/in/marcussky'),
          ('Kaggle', 'https://www.kaggle.com/marcusgawronsky'),
         )

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
RELATIVE_URLS = False

MARKUP = ('md', 'ipynb')

PLUGIN_PATHS = ['./plugins']
PLUGINS = ['ipynb.markup','assets']
OUTPUT_PATH = 'docs/'

# for my themes
## https://github.com/textbook/bulrush/tree/19b2fc4d79e7c060218172ae5484a4a216b40921
import bulrush

THEME = bulrush.PATH
JINJA_ENVIRONMENT = bulrush.ENVIRONMENT
JINJA_FILTERS = bulrush.FILTERS
