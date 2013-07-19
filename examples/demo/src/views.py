#!/usr/bin/env python
#-*- coding: utf-8 -*-

from pony.orm import commit

from brat.exception import exceptions
from brat import BratHandler
from brat.convert import get_offset_limit
from brat.paginator import Paginator

from models import User


class BaseHandler(BratHandler):
    def __init__(self, application, request, **kwargs):
        BratHandler.__init__(self, application, request, **kwargs)

    def validate_basic(self, username, password):
        return username == 'test' and password == 'test'

    def validate_client(self, client_key):
        return client_key == '112358'


class UserMixin(object):
    def __get_pagination_args(self, f, *args):
        params = {'offset': args[-2], 'limit': args[-1]}
        return {'params': params}

    @Paginator(__get_pagination_args, '/users')
    def get_users(self, offset, limit):
        users = User.select_by_sql('select * from user')[offset: offset +
                                                         limit]
        return users


class UsersHandler(UserMixin, BaseHandler):
    allow_client_methods = ['GET', 'POST']

    def get(self, *args, **kwargs):
        offset, limit = get_offset_limit(self)
        users = self.get_users(offset, limit)
        return users

    def post(self, *args, **kwargs):
        email = self.get_argument('email', None)
        password = self.get_argument('password', None)
        if not email or not password:
            raise exceptions.BadRequest
        user = User(email=email, password=password)
        commit()
        return user

    def options(self, *args, **kwargs):
        info = [{'method': 'GET', 'params': ['offset', 'limit'],
                 'description': u'用户列表'},
                {'method': 'POST', 'description': u'添加用户'}]
        return info


class UserHandler(BaseHandler):
    def get(self, id):
        user = User.get(id=id)
        if not user:
            raise exceptions.NotFound
        return user

    def delete(self, id):
        user = User.get(id=id)
        if not user:
            raise exceptions.NotFound
        user.delete()
        return {}

    def options(self, *args, **kwargs):
        info = [{'method': 'GET', 'description': u'用户详细信息'},
                {'method': 'DELETE', 'description': u'删除用户'}]
        return info
