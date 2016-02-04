# -*- coding: utf-8 -*-

from distutils.core import setup
from Cython.Build import cythonize

setup(
  name = 'generate_cythoned',
  ext_modules = cythonize("generate_source.pyx"),
)