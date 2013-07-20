#!/usr/bin/env python
#-*- coding: utf-8 -*-

from brat import Brat
from views import UsersHandler, UserHandler

brat = Brat()

brat.define('port', default=7778, help="Run on the given port", type=int)
brat.define('need_auth', default=True)
brat.define('api_url', default='http://localhost:7778')

brat.add_handler('/users', UsersHandler)
brat.add_handler('/users/(\d+)', UserHandler)


def run():
    brat.run()

if __name__ == '__main__':
    run()
