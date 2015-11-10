# -*- coding: utf-8 -*-
from setuptools import setup

setup(
    name='django-pg-returning',
    version='0.3.1',
    author=u'kanu',
    packages=['pg_returning'],
    url='http://github.com/ashwoods/django-pg-returning',
    license='Public Domain',
    description='A queryset that can return the changed rows of updates on a postgresql databases',
    long_description=open('README.rst').read(),
    zip_safe=False,
    classifiers=[
        'Development Status :: 4 - Beta',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.2',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Topic :: Utilities',
    ],
)
