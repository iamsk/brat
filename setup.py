#!/usr/bin/env python

import os
from setuptools import setup, find_packages


def read(*rnames):
    return open(os.path.join(os.path.dirname(__file__), *rnames)).read()

setup(
    name='Brat',
    version='0.0.1',
    url='https://github.com/iamsk/brat',
    author='iamsk',
    author_email='iamsk.info@gmail.com',
    description='Simple framework for creating REST APIs',
    long_description=read('README.md'),
    packages=find_packages(),
    zip_safe=False,
    include_package_data=True,
    platforms='any',
    install_requires=[
        'tornado>=2.4',
        'ujson>=1.30',
        'requests>=1.2.0',
        'dicttoxml>=1.1.1',
    ],
    entry_points="""
    [console_scripts]
    doc_gen = doc_generator.doc:gen
    """,
)
