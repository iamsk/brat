import os
from setuptools import setup, find_packages


def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(
    name='Brat',
    version='0.0.2',
    author='iamsk',
    author_email='iamsk.info@gmail.com',
    url='https://github.com/iamsk/brat',
    description='Simple framework for creating RESTful APIs',
    long_description=read('README.md'),
    packages=find_packages(exclude=('examples', 'tests')),
    install_requires=[
        'tornado>=2.4',
        'ujson>=1.30',
        'requests>=1.2.0',
        'dicttoxml>=1.1.1',
        'argparse',
    ],
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Environment :: Web Environment',
        'Framework :: Tornado',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
    ],
    entry_points="""
    [console_scripts]
    doc_gen = doc_generator.doc:gen
    """,
    zip_safe=False,
    include_package_data=True,
)
