# -*- coding: utf-8 -*-
from distutils.core import setup

setup(
    name='django-update-returning',
    version='0.3.1',
    author=u'kanu',
    packages=['update_returning'],
    url='http://github.com/kanu/django-update-returning',
    license='Public Domain',
    description='A queryset that can return the changed rows of updates on a postgresql databases',
    long_description=open('README.rst').read(),
    zip_safe=False,
)