# -*- coding: utf-8 -*-
import re
import sys
from setuptools import setup, find_packages
from setuptools.command.test import test as TestCommand

# Requirements
requires = [
    'marshmallow>=2.0.0b2',
    'webargs>=0.13.0'
]

def find_version(fname):
    '''Attempts to find the version number in the file names fname.
    Raises RuntimeError if not found.
    '''
    version = ''
    with open(fname, 'r') as fp:
        reg = re.compile(r'__version__ = [\'"]([^\'"]*)[\'"]')
        for line in fp:
            m = reg.match(line)
            if m:
                version = m.group(1)
                break
    if not version:
        raise RuntimeError('Cannot find version information')
    return version

__version__ = find_version("webargs_marshmallow/__init__.py")


def read(fname):
    with open(fname) as fp:
        content = fp.read()
    return content

setup(
    name='webargs',
    version=__version__,
    description=(
        'webargs-marshmallow provides a webargs parser that understands '
        'marshmallow schemas.'),
    long_description=read("README.md"),
    author='Rory Hart',
    author_email='hartror@gmail.com',
    url='https://github.com/hartror/webargs-marshmallow',
    packages=find_packages(),
    package_dir={'webargs-marshmallow': 'webargs-marshmallow'},
    install_requires=REQUIREMENTS,
    license=read("LICENSE"),
    zip_safe=False,
    keywords=('webargs', 'http', 'flask', 'django', 'bottle', 'tornado',
      'webapp2', 'request', 'arguments', 'parameters', 'rest', 'api',
      'marshmallow'),
    classifiers=[
        'Development Status :: 1 - Planning',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        "Programming Language :: Python :: 2",
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: Implementation :: CPython',
        'Programming Language :: Python :: Implementation :: PyPy',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
        'Topic :: Internet :: WWW/HTTP :: WSGI :: Application',
    ]
)
