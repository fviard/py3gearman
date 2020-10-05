#!/usr/bin/env python3

from setuptools import setup

from gearman import __version__ as version

setup(
    name="py3gearman-compat",
    version=version,
    author="Florent Viard",
    author_email="florent.viard@budget-insight.com",
    description="Gearman API - Client, worker, and admin client interfaces for Python3",
    url="https://github.com/fviard/py3gearman-compat",
    packages=['gearman'],
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Developers",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Topic :: Software Development :: Libraries :: Python Modules"
    ],
)
