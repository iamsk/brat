#!/usr/bin/env python
#-*- coding: utf-8 -*-

from restful import Api
from view import UsersHandler, UserHandler

api = Api()

api.define('port', default=5000, help="Run on the given port", type=int)
api.define('clients', default=['1234567890'])

api.add_handler('/users', UsersHandler)
api.add_handler('/users/(\d+)', UserHandler)


def run():
    api.run()

if __name__ == '__main__':
    run()
