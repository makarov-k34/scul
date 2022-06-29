#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import setup



requirements = [

     'pyramid','colander'
]



setup(
    name='scul',
    version='1.0.0',
    description="Shared classifiers upload library",
    author="Makarov Konstantin",
    author_email='',
    url='',
    install_requires=requirements,
    license="MIT license",
    zip_safe=False,
    keywords='Shared classifiers upload',
    classifiers=[
        'Development Status :: 1 - Beta',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        "Programming Language :: Python :: 2",
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
    ]

)
