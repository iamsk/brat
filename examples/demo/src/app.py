#!/usr/bin/env python
#-*- coding: utf-8 -*-

from restful import Api
from views import UsersHandler, UserHandler

api = Api()

api.define('port', default=7778, help="Run on the given port", type=int)
api.define('need_auth', default=True)
api.define('api_url', default='http://localhost:7778')

api.add_handler('/users', UsersHandler)
api.add_handler('/users/(\d+)', UserHandler)


def run():
    api.run()

if __name__ == '__main__':
    run()
