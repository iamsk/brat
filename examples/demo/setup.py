#!/usr/bin/env python
#-*- coding: utf-8 -*-

from setuptools import setup, find_packages

name = "demo"
version = "0.1"

setup(
    name=name,
    version=version,
    description="demo",
    long_description='README.md',
    keywords="",
    author="iamsk",
    author_email='iamsk.info@gmail.com',
    packages=find_packages('src'),
    package_dir={'': 'src'},
    include_package_data=True,
    zip_safe=False,
    install_requires=[
        'setuptools',
        'brat',
        'pony',
        'rxpy',
    ],
    entry_points="""
    [console_scripts]
    run = app:run
    """,
)
