#!/usr/bin/env python
from setuptools import setup, find_packages
setup(
    name='ar_markers',
    version='1.0',
    packages=find_packages(),
    install_requires=['numpy', 'scipy'],
    setup_requires=[],
    author='Max Brauer',
    author_email='max@max-brauer.com',
    description='Detection of hamming markers for OpenCV written in python',
    url='https://github.com/DebVortex/python-ar-markers',
    license='GNU GENERAL PUBLIC LICENSE Version 3',
)