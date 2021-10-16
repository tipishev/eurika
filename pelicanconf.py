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

PAGE_ORDER = ['home', 'about', 'schedule', 'rules', 'contacts', 'home_se']

# TODO custom age extractor function for courses
ARTICLE_ORDER_BY = 'date'

# Photos Plugin
PHOTO_LIBRARY = 'content/photos'
PHOTO_ARTICLE = (760, 506, 80)
PHOTO_THUMB = (300, 200, 100)
