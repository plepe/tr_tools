#!/usr/bin/python
#coding=UTF-8
from setuptools import setup, find_packages

setup(
    name = "tr-tools",
    url = 'https://github.com/plepe/tr-tools',
    author = u'Stephan Bösch-Plepelits',
    author_email = 'skunk' '@' 'xover.mud.at',
    description = 'Tools for translations using a JSON based format',
    version = '0.1-dev',
    packages = find_packages(),
    package_data = {
    },
    scripts = [ ],
)
