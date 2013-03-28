#!/usr/bin/env python

from distutils.core import setup

setup(name='holycow',
      version='0.1',
      description='ESPN Baseball API library for python',
      author='Mike Guarascio',
      author_email='michael.guarascio@gmail.com',
      url='https://github.com/mguarascio/holycow',
      py_modules=['holycow'],
      requires=['requests']
     )
