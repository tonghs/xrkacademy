#!/usr/bin/env python
# -*- coding: utf-8 -*-

import _env  # noqa
import tornado.web
from handler.base import BaseHandler, route


@route('/')
class Index(BaseHandler):
    def get(self):
        self.render()


@route('/login')
class Login(tornado.web.RequestHandler):
    def get(self):
        self.render('../template/login.html')


@route('/introduction')
class Introduction(BaseHandler):
    def get(self):
        self.render()
