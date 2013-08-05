#!/usr/bin/env python
#-*- coding: utf-8 -*-

import base64
from brat.exception import exceptions


class Authenticator(object):
    """
    Tornado Request authenticator.
    以 mixin 方式提供
    """

    def validate(self):
        """
        验证请求合法性
        """
        info = {}
        if "Authorization" not in self.request.headers:
            raise exceptions.BadRequest(message=u'未设置验证方式')
        auth = self.request.headers['Authorization'].split()
        self.auth_type = auth[0].lower()
        self.auth_value = " ".join(auth[1:]).strip()
        kv = base64.decodestring(self.auth_value)
        if self.auth_type == "basic":
            kv = kv.split(':')
            user_id = self.validate_basic(kv[0], kv[1])
            info = {'type': 'basic', 'user_id': user_id}
        elif self.auth_type == 'bearer':
            user_id = self.validate_bearer(kv)
            info = {'type': 'bearer', 'user_id': user_id}
        elif self.auth_type == 'client':
            kv = kv.split(':')
            client_id = self.validate_client(kv[0], kv[1])
            info = {'type': 'client', 'client_id': client_id}
        else:
            raise exceptions.BadRequest(message=u"不支持的验证方式")
        return info

    def validate_basic(self, username, password):
        """
        Validate Basic Auth.
        """
        raise exceptions.InternalServerError(message=u'Basic Auth 未实现')

    def validate_client(self, client_key, client_secret):
        """
        Validate client request
        """
        raise exceptions.InternalServerError(message=u'Two legged Auth 未实现')

    def validate_bearer(self, token):
        """
        Validate bearer Auth.
        """
        raise exceptions.InternalServerError(message=u'bearer 未实现')
