#!/usr/bin/env python
#-*- coding: utf-8 -*-

import tornado
import tornado.web
import tornado.httpserver
from tornado.options import options
from tornado.options import define as _define


class Api(object):
    def __init__(self, handlers=None, settings=None):
        self.handlers = handlers if handlers else []
        default_settings = dict(
            gzip=True,
            debug=True,
        )
        self.settings = settings if settings else default_settings

    def add_handler(self, regex, obj):
        self.handlers.append((regex, obj))

    def define(self, name, default=None, type=None, help=None):
        _define(name, default, type, help)

    def run(self):
        tornado.options.parse_command_line()
        application = tornado.web.Application(self.handlers, **self.settings)
        http_server = tornado.httpserver.HTTPServer(application, xheaders=True)
        http_server.listen(options.port)
        tornado.ioloop.IOLoop.instance().start()