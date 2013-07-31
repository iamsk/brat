#-*- coding: utf-8 -*-

from brat.macro import HTTP_CODE


class APIException(Exception):
    """
    API Base Exception
    """

    def __init__(self, code=None, message=None):
        super(APIException, self).__init__()
        self._code = code
        self._message = message

    def __str__(self):
        _str = u"Exception: code=%d, message='%s'" % (self._code, self._message)
        return _str.encode('utf-8')

    def __repr__(self):
        return self.__str__()

    def __unicode__(self):
        return u"Exception: code=%d, message='%s'" % (self._code, self._message)

    @property
    def code(self):
        return self._code

    @property
    def msg(self):
        return self._message

    @property
    def info(self):
        return {'error': {'code': self._code, 'message': self._message}}


class BadRequest(APIException):
    def __init__(self, code=HTTP_CODE.BAD_REQUEST, message=u'请求参数错误'):
        super(BadRequest, self).__init__(code=code, message=message)


class Unauthorized(APIException):
    def __init__(self, code=HTTP_CODE.UNAUTHORIZED, message=u'用户未验证'):
        super(Unauthorized, self).__init__(code=code, message=message)


class Forbidden(APIException):
    def __init__(self, code=HTTP_CODE.FORBIDDEN, message=u'操作不允许'):
        super(Forbidden, self).__init__(code=code, message=message)


class NotFound(APIException):
    def __init__(self, code=HTTP_CODE.NOT_FOUND, message=u'请求资源不存在'):
        super(NotFound, self).__init__(code=code, message=message)


class MethodNotAllowed(APIException):
    def __init__(self, code=HTTP_CODE.METHOD_NOT_ALLOWED, message=u'不支持的HTTP方法'):
        super(MethodNotAllowed, self).__init__(code=code, message=message)


class InternalServerError(APIException):
    def __init__(self, code=HTTP_CODE.INTERNAL_SERVER_ERROR, message=u'服务器响应错误'):
        super(InternalServerError, self).__init__(code=code, message=message)


class OAuth2Exception(Exception):
    """
    OAuth 2.0 Base Exception
    """

    def __init__(self, code=None, message=None):
        super(OAuth2Exception, self).__init__()
        self._code = code
        self._message = message

    def __str__(self):
        _str = u"Exception: code=%d, message='%s'" % (self._code, self._message)
        return _str.encode('utf-8')

    def __repr__(self):
        return self.__str__()

    def __unicode__(self):
        return u"Exception: code=%d, message='%s'" % (self._code, self._message)

    @property
    def code(self):
        return self._code

    @property
    def msg(self):
        return self._message

    @property
    def info(self):
        return {'error': {'code': self._code, 'message': self._message}}


class InvalidRequest(OAuth2Exception):
    def __init__(self, code=HTTP_CODE.BAD_REQUEST, message=u'请求验证失败，参数不完整、用户名密码错误等！'):
        super(InvalidRequest, self).__init__(code=code, message=message)


class InvalidClient(OAuth2Exception):
    def __init__(self, code=HTTP_CODE.UNAUTHORIZED, message=u'客户端验证失败，参数不完整、不存在、不匹配等！'):
        super(InvalidClient, self).__init__(code=code, message=message)


class InvalidGrant(OAuth2Exception):
    def __init__(self, code=HTTP_CODE.UNAUTHORIZED, message=u'未验证通过的授权！'):
        super(InvalidGrant, self).__init__(code=code, message=message)


class UnsupportedGrantType(OAuth2Exception):
    def __init__(self, code=HTTP_CODE.UNAUTHORIZED, message=u'不支持的授权类型！'):
        super(UnsupportedGrantType, self).__init__(code=code, message=message)

if __name__ == '__main__':
    print BadRequest().info
    print str(BadRequest())
    print unicode(BadRequest())
