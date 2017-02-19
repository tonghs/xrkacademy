#!/usr/bin/env python
# -*- coding: utf-8 -*-

import _env  # noqa
import os

from mako.lookup import TemplateLookup
import tornado.web
from config import APP
# from raven.contrib.tornado import SentryMixin


class Singleton(object):
    def __new__(cls, *args, **kw):
        if not hasattr(cls, '_instance'):
            orig = super(Singleton, cls)
            cls._instance = orig.__new__(cls, *args, **kw)
        return cls._instance


class Route(Singleton):
    def __init__(self):
        self.url_list = list()

    def __call__(self, url):
        def _(cls):
            self.url_list.append((url, cls))

            return cls
        return _


route = Route()


class Static(object):
    def __getattr__(self, name):
        def load(src):
            return '/static/{type_}/{src}'.format(type_=name, src=src)
        return load


# class BaseHandler(SentryMixin, tornado.web.RequestHandler):
class BaseHandler(tornado.web.RequestHandler):
    def prepare(self):
        if not self.current_user:
            self.redirect('/login')

    def initialize(self):
        template_path = os.path.join(os.path.dirname(__file__), '..', 'template')
        self.lookup = TemplateLookup(directories=template_path,
                                     input_encoding='utf-8',
                                     output_encoding='utf-8')

    def render_string(self, filename, **kwargs):
        kwargs["current_user"] = self.current_user
        template = self.lookup.get_template(filename)
        namespace = self.get_template_namespace()
        namespace.update(kwargs)

        return template.render(**namespace)

    def render(self, **kwargs):
        filename = "{0}.html".format(self._camel_to_underline(self.__class__.__name__))
        filename = "{0}{1}".format(filename[0].lower(), filename[1:])
        path = '/'.join(self.__module__.split('.')[2: -2])
        filename = os.path.join(path, filename)

        if isinstance(kwargs, dict):
            kwargs.update(STATIC=Static())
            kwargs.update(APP=APP)

        self.finish(self.render_string(filename, **kwargs))

    def get_current_user(self):
        return {'name': 'test'}

    def _camel_to_underline(self, camel_format):
        ''' 驼峰命名格式转下划线命名格式
        '''
        underline_format = ''
        if isinstance(camel_format, str):
            for i, _s_ in enumerate(camel_format):
                if i == 0:
                    underline_format += _s_ if _s_.islower() else _s_.lower()
                else:
                    underline_format += _s_ if _s_.islower() else '_' + _s_.lower()

        return underline_format

    @property
    def arguments(self):
        return {k: self.get_argument(k) for k, v in self.request.arguments.iteritems()}
