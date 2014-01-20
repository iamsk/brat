import tornado
import tornado.web
import tornado.httpserver
from tornado.options import options
from tornado.options import define as _define

from brat.handler import NotFoundHandler, BratHandler


class Brat(object):
    def __init__(self, handlers=None, settings=None):
        if handlers:
            handlers.append((r".*", NotFoundHandler))
        else:
            handlers = [(r".*", NotFoundHandler)]
        self.handlers = handlers
        default_settings = dict(
            gzip=True,
            debug=False,
        )
        self.settings = settings if settings else default_settings

    def add_handler(self, regex, obj):
        self.handlers.insert(-1, (regex, obj))

    def define(self, name, default=None, type=None, help=None):
        _define(name, default, type, help)

    def get_app(self):
        application = tornado.web.Application(self.handlers, **self.settings)
        return application

    def run(self):
        tornado.options.parse_command_line()
        application = self.get_app()
        http_server = tornado.httpserver.HTTPServer(application, xheaders=True)
        http_server.listen(getattr(options, 'port', 7777), '0.0.0.0')
        tornado.ioloop.IOLoop.instance().start()


BratHandler = BratHandler
