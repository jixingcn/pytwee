'''
Sphinx docs configuration
'''
#!/usr/bin/python
# -*- coding: utf-8 -*-

# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

import datetime


project   = 'pytwine' # pylint: disable=invalid-name
copyright = f'{datetime.datetime.now().year}, Xing Ji (me@xingji.me).' # pylint: disable=redefined-builtin, invalid-name
author    = 'Xing Ji (me@xingji.me)' # pylint: disable=invalid-name
version   = '0.1.0' # pylint: disable=invalid-name


# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.autosummary',
    'sphinx.ext.autosectionlabel',
    'sphinx.ext.mathjax',
    'sphinx.ext.graphviz',
    'sphinx_rtd_theme',
    'sphinx_rtd_dark_mode',
]

html_theme           = 'sphinx_rtd_theme' # pylint: disable=invalid-name
#html_static_path     = ['_static']
html_extra_path      = []
#html_favicon         = '_static/favicon.png'
#html_logo            = '_static/favicon.png'
html_copy_source     = False # pylint: disable=invalid-name
html_show_sourcelink = False # pylint: disable=invalid-name
html_css_files       = []
html_js_files        = []

exclude_patterns = []
source_suffix    = {'.rst': 'restructuredtext'}
master_doc       = 'index' # pylint: disable=invalid-name

gettext_compact = False # pylint: disable=invalid-name
pygments_style  = 'default' # pylint: disable=invalid-name
