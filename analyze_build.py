# -*- coding: utf-8 -*-

from distutils.core import setup
from Cython.Build import cythonize

setup(
  name = 'analyze_cythoned',
  ext_modules = cythonize("analyze_source.pyx"),
)