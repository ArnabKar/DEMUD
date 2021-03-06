#!/usr/bin/env python

from setuptools import setup

execfile('demud/version.py')  # brings in a "version" variable

description = ''
with open('README.md') as f:
    long_description = f.read()

setup(name='DEMUD',
      version=version,
      description=description,
      long_description=long_description,
      author='Kiri Wagstaff',
      author_email='kiri.wagstaff@jpl.nasa.gov',
      url='https://github.com/wkiri/DEMUD',
      packages=['demud'],
      install_requires=['matplotlib', 'numpy', 'pillow'],
      entry_points={'console_scripts': ['demud=demud.demud:main']}
     )
