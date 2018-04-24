#!/usr/bin/env python
# -*- coding: utf-8 -*-
import codecs
from setuptools import setup, find_packages

setup(
    name='luigi-credstash',
    version='0.0.1',
    description="Easily use credstash with a Luigi configuration file.",
    keywords='credstash luigi'.split(),
    author='Mike Bjerkness',
    author_email='mike.bjerkness@centriam.com',
    maintainer='Mike Bjerkness',
    maintainer_email='mike.bjerkness@centriam.com',
    url='https://github.com/centriam/luigi-credstash',
    license='MIT',
    package_dir={'luigi_credstash': 'luigi_credstash'},
    install_requires=['credstash_cache',],
    include_package_data=True,
    packages=find_packages(),
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Environment :: Console',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'Intended Audience :: System Administrators',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Topic :: Security',
        'Topic :: Utilities',
    ],
    zip_safe=False,
)
