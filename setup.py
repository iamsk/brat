#!/usr/bin/env python

import os
from setuptools import setup, find_packages


def read(*rnames):
    return open(os.path.join(os.path.dirname(__file__), *rnames)).read()

setup(
    name='Tornado-RESTful',
    version='0.0.1',
    url='https://www.bitbucket.org/iamsk/tornado-restful/',
    author='iamsk',
    author_email='iamsk.info@gmail.com',
    description='Simple framework for creating REST APIs',
    long_description=read('README.md'),
    packages=find_packages(),
    zip_safe=False,
    include_package_data=True,
    platforms='any',
    install_requires=[
        'tornado',
        'ujson',
        'requests',
    ],
    entry_points="""
    [console_scripts]
    doc_gen = doc_generator.doc:gen
    """,
)
