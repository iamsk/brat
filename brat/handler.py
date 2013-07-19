#!/usr/bin/env python
#-*- coding: utf-8 -*-

import tornado
from tornado.options import options

from brat.macro import HTTP_CODE
from brat.exception import exceptions
from brat.exception.handler import ExceptionHandler
from brat.authenticate import Authenticator
from brat.serializers import JsonEncoder, XmlEncoder


class BratHandler(Authenticator, tornado.web.RequestHandler):
    def __init__(self, application, request, **kwargs):
        tornado.web.RequestHandler.__init__(self, application, request,
                                            **kwargs)

    def _execute_method(self):
        """
        hacking tornado's methods for support method's ExceptionHandler
        """
        if not self._finished:
            method = getattr(self, '_' + self.request.method.lower())
            self._when_complete(method(*self.path_args, **self.path_kwargs),
                                self._execute_finish)

    def prepare(self):
        DEFAULT_CONTENT_TYPE = 'application/json'
        support_content_types = ['application/json', 'application/xml']
        content_type = self.request.headers.get('Accept', DEFAULT_CONTENT_TYPE)
        self.content_type = content_type if content_type in \
            support_content_types else DEFAULT_CONTENT_TYPE
        if self.content_type == DEFAULT_CONTENT_TYPE:
            self.encoder = JsonEncoder
        else:
            self.encoder = XmlEncoder
        if not getattr(options, 'need_auth', False):
            return
        if self.request.method.upper() == 'OPTIONS':
            return
        try:
            self.auth = self.validate()
            if self.auth['type'] == 'oauth':
                allow_client_methods = getattr(self, 'allow_client_methods',
                                               [])
                if self.request.method.upper() not in allow_client_methods:
                    raise exceptions.Forbidden(message=u'应用独立请求时，无此操作权限')
            else:
                self.user_id = self.auth['user_id']
        except exceptions.APIException, e:
            self.set_status(HTTP_CODE.UNAUTHORIZED)
            output = self.encoder(e.info)
            return self.finish(output)

    @property
    def login_id(self):
        login_id = self.user_id or 0
        return login_id

    @ExceptionHandler
    def _get(self, *args, **kwargs):
        return self.get(*args, **kwargs)

    def get(self, *args, **kwargs):
        raise exceptions.MethodNotAllowed

    @ExceptionHandler
    def _head(self, *args, **kwargs):
        return self.head(*args, **kwargs)

    def head(self, *args, **kwargs):
        raise exceptions.MethodNotAllowed

    @ExceptionHandler
    def _post(self, *args, **kwargs):
        self.set_status(HTTP_CODE.CREATED)
        return self.post(*args, **kwargs)

    def post(self, *args, **kwargs):
        raise exceptions.MethodNotAllowed

    @ExceptionHandler
    def _delete(self, *args, **kwargs):
        return self.delete(*args, **kwargs)

    def delete(self, *args, **kwargs):
        raise exceptions.MethodNotAllowed

    @ExceptionHandler
    def _patch(self, *args, **kwargs):
        return self.patch(*args, **kwargs)

    def patch(self, *args, **kwargs):
        raise exceptions.MethodNotAllowed

    @ExceptionHandler
    def _put(self, *args, **kwargs):
        self.set_status(HTTP_CODE.ACCEPTED)
        return self.put(*args, **kwargs)

    def put(self, *args, **kwargs):
        raise exceptions.MethodNotAllowed

    @ExceptionHandler
    def _options(self, *args, **kwargs):
        return self.options(*args, **kwargs)

    def options(self, *args, **kwargs):
        raise exceptions.MethodNotAllowed

    def finish(self, chunk=None):
        self._chunk = chunk
        self.set_header("Content-Type", self.content_type)
        tornado.web.RequestHandler.finish(self, self._chunk)


class NotFoundHandler(BratHandler):
    def get(self, *args, **kwargs):
        raise exceptions.NotFound

    def head(self, *args, **kwargs):
        raise exceptions.NotFound

    def post(self, *args, **kwargs):
        raise exceptions.NotFound

    def delete(self, *args, **kwargs):
        raise exceptions.NotFound

    def patch(self, *args, **kwargs):
        raise exceptions.NotFound

    def put(self, *args, **kwargs):
        raise exceptions.NotFound

    def options(self, *args, **kwargs):
        raise exceptions.NotFound
