#!/usr/bin/env python
#-*- coding: utf-8 -*-

from restful.exception import exceptions


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
        if self.auth_type == 'client':
            client_key = self.validate_client(self.auth_value)
            info = {'type': 'client', 'client_key': client_key}
        elif self.auth_type == "basic":
            import base64
            kv = base64.decodestring(self.auth_value)
            kv = kv.split(':')
            user_id = self.validate_basic(kv[0], kv[1])
            info = {'type': 'Basic', 'user_id': user_id}
        else:
            raise exceptions.BadRequest(message=u"不支持的验证方式")
        return info

    def validate_basic(self, username, password):
        """
        Validate Basic Auth.
        """
        raise exceptions.InternalServerError(message=u'Basic Auth 未实现')

    def validate_client(self, client_key):
        """
        Validate client request
        """
        from tornado.options import options

        if client_key not in options.clients:
            error_message = u"应用（client_key: %s）不存在" % client_key
            raise exceptions.BadRequest(message=error_message)
        return client_key
