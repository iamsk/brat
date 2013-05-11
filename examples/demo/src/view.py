#!/usr/bin/env python
#-*- coding: utf-8 -*-

from restful.exception import exceptions
from restful.basehandler import BaseHandler
from pony.orm import commit
from models import User


class UsersHandler(BaseHandler):
    allow_client_methods = ['GET', 'POST']

    def real_get(self, *args, **kwargs):
        users = User.select_by_sql('select * from user')
        return users

    def real_post(self, *args, **kwargs):
        email = self.get_argument('email', None)
        password = self.get_argument('password', None)
        if not email or not password:
            raise exceptions.BadRequest
        user = User(email=email, password=password)
        commit()
        return user

    def real_options(self, *args, **kwargs):
        info = [{'method': 'GET', 'description': u'用户列表'},
                {'method': 'DELETE', 'params': ['email', 'password'], 'description': u'添加用户'}]
        return info


class UserHandler(BaseHandler):
    def real_get(self, id):
        user = User.get(id=id)
        if not user:
            raise exceptions.NotFound
        return user

    def real_delete(self):
        user = User.get(id=id)
        if not user:
            raise exceptions.NotFound
        user.delete()
        return {}

    def real_options(self, *args, **kwargs):
        info = [{'method': 'GET', 'description': u'用户详细信息'},
                {'method': 'DELETE', 'description': u'删除用户'}]
        return info
