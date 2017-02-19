#!/usr/bin/env python
# -*- coding: utf-8 -*-

import _env  # noqa

import sys
import tornado.ioloop
import tornado.web

from config import PORT, DEBUG, HOST, COOKIE_SECRET
import _url  # noqa
from handler.base import route
# from raven.contrib.tornado import AsyncSentryClient

reload(sys)
sys.setdefaultencoding('utf-8')


def write_error(self, status_code, **kwargs):
    # if status_code == 404:
    #     self.finish(dict(error_code='404', msg='url 错误'))
    # elif status_code == 500:
    #     self.finish(dict(error_code='500', msg='服务器错误'))
    pass


tornado.web.RequestHandler.write_error = write_error


def make_app():
    return tornado.web.Application(route.url_list, debug=DEBUG,
                                   cookie_secret=COOKIE_SECRET)


if __name__ == "__main__":
    port = PORT
    if len(sys.argv) > 1:
        for arg in sys.argv[1:]:
            if 'port' in arg:
                arg_port = arg.split('=')
                if len(arg_port) == 2:
                    port = arg_port[1]
                else:
                    print 'invalid port arg'

    app = make_app()
    # app.sentry_client = AsyncSentryClient(SENTRY_URL)
    app.listen(port)

    print 'Listening at {host}:{port}'.format(host=HOST, port=port)
    tornado.ioloop.IOLoop.current().start()
