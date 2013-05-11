#!/usr/bin/env python
#-*- coding: utf-8 -*-

from ujson import dumps


class JsonEncoder(object):
    def __init__(self, data):
        self.mimetype = 'application/json'
        self.extension = 'json'

    def encode(self):
        return dumps(self.data)

    def __unicode__(self):
        return self.encode(self.data)
