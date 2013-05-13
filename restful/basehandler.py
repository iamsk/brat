#!/usr/bin/env python
#-*- coding: utf-8 -*-

import tornado
from tornado.options import options

from restful.macro import HTTP_CODE
from restful.exception import exceptions
from restful.exception.handler import ExceptionHandler
from restful.authenticate import Authenticator
from restful.serializers import JsonEncoder, XmlEncoder


class BaseHandler(Authenticator, tornado.web.RequestHandler):
    def __init__(self, application, request, **kwargs):
        tornado.web.RequestHandler.__init__(self, application, request, **kwargs)

    def prepare(self):
        try:
            support_accept_headers = ['application/json', 'application/xml']
            accept_header = self.request.headers.get('Accept', 'application/json')
            self.media_type = accept_header if accept_header in support_accept_headers else 'application/json'
            if self.media_type == 'application/json':
                self.encoder = JsonEncoder
            else:
                self.encoder = XmlEncoder
            if not getattr(options, 'need_auth', False):
                return
            if self.request.method.upper() == 'OPTIONS':
                return
            self.auth = self.validate()
            if self.auth['type'] == 'oauth':
                allow_client_methods = getattr(self, 'allow_client_methods', [])
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
    def get(self, *args, **kwargs):
        return self.real_get(*args, **kwargs)

    def real_get(self, *args, **kwargs):
        raise exceptions.MethodNotAllowed

    @ExceptionHandler
    def post(self, *args, **kwargs):
        self.set_status(HTTP_CODE.CREATED)
        return self.real_post(*args, **kwargs)

    def real_post(self, *args, **kwargs):
        raise exceptions.MethodNotAllowed

    @ExceptionHandler
    def put(self, *args, **kwargs):
        self.set_status(HTTP_CODE.ACCEPTED)
        return self.real_put(*args, **kwargs)

    def real_put(self, *args, **kwargs):
        raise exceptions.MethodNotAllowed

    @ExceptionHandler
    def delete(self, *args, **kwargs):
        return self.real_delete(*args, **kwargs)

    def real_delete(self, *args, **kwargs):
        raise exceptions.MethodNotAllowed

    @ExceptionHandler
    def options(self, *args, **kwargs):
        return self.real_options(*args, **kwargs)

    def real_options(self, *args, **kwargs):
        raise exceptions.MethodNotAllowed

    def finish(self, chunk=None):
        self._chunk = chunk
        self.set_header("Content-Type", self.media_type)
        tornado.web.RequestHandler.finish(self, self._chunk)


class NotFoundHandler(BaseHandler):
    def real_get(self, *args, **kwargs):
        raise exceptions.NotFound

    def real_put(self, *args, **kwargs):
        raise exceptions.NotFound

    def real_post(self, *args, **kwargs):
        raise exceptions.NotFound

    def real_delete(self, *args, **kwargs):
        raise exceptions.NotFound

    def real_options(self, *args, **kwargs):
        raise exceptions.NotFound
