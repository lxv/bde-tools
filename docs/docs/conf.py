# -*- coding: utf-8 -*-
#
# BDE Tools documentation build configuration file, created by
# sphinx-quickstart on Tue Apr  7 14:46:25 2015.
#
# This file is execfile()d with the current directory set to its
# containing dir.
#
# Note that not all possible configuration values are present in this
# autogenerated file.
#
# All configuration values have a default; values that are commented out
# serve to show the default.

import sys
import os

# import shlex

import sphinx
import distutils.version

sphinx_version = distutils.version.LooseVersion(sphinx.__version__)

# -- Project information -----------------------------------------------------

project = u"BDE Build Tools"
copyright = u"2022, Bloomberg Finance L.P."
author = u"BDE"

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
sys.path.insert(0, os.path.abspath("."))

# The short X.Y version.
version = ""
# The full version, including alpha/beta/rc tags.
release = ""

# -- General configuration ------------------------------------------------

# If your documentation needs a minimal Sphinx version, state it here.
# needs_sphinx = '1.0'

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
sys.path.append(os.path.abspath("helpers"))
primary_domain = "cmake"
extensions = ["sphinx.ext.extlinks",
              "sphinx.ext.githubpages",
              "myst_parser",
              "sphinxcontrib.moderncmakedomain"
              ]

# Add any paths that contain templates here, relative to this directory.
templates_path = ["_templates"]

# The suffix(es) of source filenames.
# You can specify multiple suffix as a list of string:
source_suffix = [".rst", ".md"]

# -- Options for MyST Parser (Markdown)
myst_heading_anchors = 2

# The encoding of source files.
# source_encoding = 'utf-8-sig'

# The master toctree document.
master_doc = "index"

# The exclude patterns
if tags.has("oss"):
    exclude_patterns = [
        "cmake/bde_modules.rst",
        "cmake/advanced.rst",
        "modules/*",
        "misc/docs-howto.rst",
    ]
else:
    exclude_patterns = []

# The language for content autogenerated by Sphinx. Refer to documentation
# for a list of supported languages.
#
# This is also used if you do content translation via gettext catalogs.
# Usually you set "language" from the command line for these cases.
language = None

# The name of the Pygments (syntax highlighting) style to use.
# pygments_style = 'sphinx'
pygments_style = "friendly"

# If true, `todo` and `todoList` produce output, else they produce nothing.
todo_include_todos = False

# -- Options for HTML output ----------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
html_theme = "sphinx_rtd_theme"
html_theme_path = [
    "_themes",
]

# Theme options are theme-specific and customize the look and feel of a theme
# further.  For a list of options available for each theme, see the
# documentation.
html_theme_options = {"prev_next_buttons_location": "top"}

rst_prolog = "\n.. include:: /global.inc\n"

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ["_static"]

html_context = {
    "css_files": [
        "_static/bde.css",
    ],
}

# Custom sidebar templates, must be a dictionary that maps document names
# to template names.
#
# The default sidebars (for documents that don't match any pattern) are
# defined by theme itself.  Builtin themes are using these templates by
# default: ``['localtoc.html', 'relations.html', 'sourcelink.html',
# 'searchbox.html']``.
#
# html_sidebars = {}

html_show_sourcelink = False

# -- Extension configuration -------------------------------------------------
def setup(app):
    app.add_css_file("bde.css")
