#!/usr/bin/env python
# -*- coding: utf-8 -*-

DEBUG = False
PORT = 10010
HOST = 'http://127.0.0.1'
COOKIE_SECRET = '0532ba8942499cdef558f8da355093ce'
APP = 'test'

try:
    from local_config import *  # noqa
except:
    pass
