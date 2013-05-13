#!/usr/bin/env python
#-*- coding: utf-8 -*-

from ujson import dumps
from dicttoxml import dicttoxml


def JsonEncoder(data):
    return dumps(data)


def XmlEncoder(data):
    return dicttoxml(data)


if __name__ == '__main__':
    d = {'hello': 'world'}
    print JsonEncoder(d)
