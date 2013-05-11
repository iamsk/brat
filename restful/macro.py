#!/usr/bin/env python
#-*- coding: utf-8 -*-

class HTTP_CODE:
    """
    HTTP Status Code
    """
    OK = 200
    CREATED = 201
    ACCEPTED = 202
    BAD_REQUEST = 400
    UNAUTHORIZED = 401
    FORBIDDEN = 403
    NOT_FOUND = 404
    METHOD_NOT_ALLOWED = 405
    INTERNAL_SERVER_ERROR = 500


class MACRO:
    """
    常量
    """
    ZERO = 0
    DEFAULT_MIN_COUNT = 1
    DEFAULT_COUNT = 10
    DEFAULT_MAX_COUNT = 20
