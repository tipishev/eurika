#!/usr/bin/env python
# -*- coding: utf-8 -*- #

#  SITEURL = 'http://eurika-se'
AUTHOR = 'admin'
SITENAME = 'Eurika.se'
TIMEZONE = 'Europe/Stockholm'
DEFAULT_LANG = 'ru'
DEFAULT_PAGINATION = False
TYPOGRIFY = True
THEME = 'theme'
STATIC_PATHS = ['images']

PLUGINS = ['photos']

# TODO custom age extractor function for courses
ARTICLE_ORDER_BY = 'date'

# Photos Plugin
PHOTO_LIBRARY = 'content/photos'
PHOTO_ARTICLE = (760, 506, 80)
PHOTO_THUMB = (150, 100, 70)
