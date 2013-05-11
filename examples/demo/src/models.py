#!/usr/bin/env python
#-*- coding: utf-8 -*-

from pony.orm import Database, Required


db = Database('sqlite', ':memory:')


class User(db.Entity):
    email = Required(unicode)
    password = Required(unicode)

db.generate_mapping(create_tables=True)
