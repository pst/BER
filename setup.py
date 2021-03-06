#!/usr/bin/env python

from setuptools import setup

setup(
    name='BER',
    version='0.3.1',
    description='BER content aggregation hub',
    author='Philipp Strube',
    author_email='pst@kubestack.com',
    url='',
    packages=['BER'],
    install_requires=[
        "tornado",
        "PyYAML",
        "Jinja2",
        "webassets",
        "libsass",
        "feedparser",
        "misaka",
        "prometheus-client"
    ]
)
