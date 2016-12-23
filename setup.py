# -*- coding: utf-8 -*-
from setuptools import setup, find_packages

setup(
    name='django-weightedcase',
    packages=find_packages(),
    version='0.1',
    description='Method and models to ponderate a queryset using weighted cases.',
    author='Commite',
    author_email='hola@commite.co',
    url='https://github.com/commite/django-weightedcase',
    keywords=['django', 'ponderate', 'queryset', 'weight', 'weighted', 'case', 'when'],
    include_package_data=True,
    classifiers=[
        "Programming Language :: Python",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "License :: OSI Approved :: MIT License",
        "Environment :: Web Environment",
        "Development Status :: 3 - Alpha",
        "Programming Language :: Python :: 2.6",
        "Programming Language :: Python :: 2.7",
        "Framework :: Django",
        "Framework :: Django :: 1.7",
        "Framework :: Django :: 1.8"
    ],
)
