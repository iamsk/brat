#!/usr/bin/env python
#-*- coding: utf-8 -*-

from urlparse import urlparse

from brat.macro import MACRO


def format_url(url):
    """
    去掉参数，并格式化 URL
    """
    url = url.split('?')[0]
    if not url.startswith('http://'):
        url = 'http://' + url
    url = urlparse(url)
    return url


def utf8_param(v):
    """
    将参数中的 unicode 及 int 转为 utf8 的 str
    """
    return v.encode('utf-8') if isinstance(v, unicode) else str(v)


def urlencode(params):
    """
    自定义 urlencode，仅做字符串拼接
    """
    if hasattr(params, "items"):
        # mapping objects
        params = params.items()
    else:
        # tuple list
        pass
    l = []
    for k, v in params:
        l.append(k + '=' + utf8_param(v))
    param = '&'.join(l)
    return param.decode('utf-8')


def get_limit(limit, max_count=MACRO.DEFAULT_MAX_COUNT):
    """
    限制 list 请求数
    """
    if MACRO.DEFAULT_MIN_COUNT > limit:
        return MACRO.DEFAULT_MIN_COUNT
    if max_count < limit:
        return max_count
    return limit
