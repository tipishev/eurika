#!/usr/bin/env python
# -*- coding: utf-8 -*- #

AUTHOR = 'admin'
SITENAME = 'Eurika.se'
SITEURL = ''
PATH = 'content'
TIMEZONE = 'Europe/Stockholm'
DEFAULT_LANG = 'ru'
DEFAULT_PAGINATION = False
TYPOGRIFY = True
THEME = 'theme'

PLUGINS = ['photos']

PAGE_ORDER = ['home', 'about', 'schedule', 'rules', 'contacts']

# Photos Plugin
PHOTO_LIBRARY = 'content/photos'
PHOTO_ARTICLE = (760, 506, 80)
PHOTO_THUMB = (300, 200, 100)
