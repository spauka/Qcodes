#!/usr/bin/env python3
#
# QCoDeS documentation build configuration file, created by
# sphinx-quickstart on Thu Jun  2 10:41:37 2016.
#
# This file is execfile()d with the current directory set to its
# containing dir.
#
# Note that not all possible configuration values are present in this
# autogenerated file.
#
# All configuration values have a default; values that are commented out
# serve to show the default.

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#
import os
import sys

# Import matplotlib and set the backend
# before qcodes imports pyplot and automatically
# sets the backend
import matplotlib
import sphinx_rtd_theme
from packaging.version import parse

import qcodes

matplotlib.use('Agg')

sys.path.insert(0, os.path.abspath('..'))

# -- General configuration ------------------------------------------------

# If your documentation needs a minimal Sphinx version, state it here.
#
# needs_sphinx = '1.0'

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
    "nbsphinx",
    "sphinx.ext.autodoc",
    "sphinx.ext.autosummary",
    "sphinx.ext.napoleon",
    "sphinx-jsonschema",
    "sphinx.ext.doctest",
    "sphinx.ext.intersphinx",
    "sphinx.ext.todo",
    "sphinx.ext.coverage",
    "sphinx.ext.mathjax",
    "sphinx.ext.viewcode",
    "sphinx.ext.githubpages",
    "sphinx.ext.todo",
    "qcodes.sphinx_extensions.parse_parameter_attr",
    "sphinxcontrib.towncrier",
    "autodocsumm",
    "sphinx_issues",
    "sphinx-favicon",
]

# include special __xxx__ that DO have a docstring
# it probably means something important
napoleon_include_special_with_doc = True

# The suffix(es) of source filenames.
# You can specify multiple suffix as a list of string:
#
# source_suffix = ['.rst', '.md']
source_suffix = '.rst'

# The encoding of source files.
#
# source_encoding = 'utf-8-sig'

# Add link to Binder in Prolog of the notebooks
# -- Get version information  ----------------------------

version = qcodes.__version__
release = parse(qcodes.__version__).public

# Add link to Binder in Prolog (WRITE MORE DETAILS ONCE FIXED)
nbsphinx_prolog = r"""
{% set docname = 'docs/' + env.doc2path(env.docname, base=None) %}

.. raw:: html

    <div class="admonition note">
      <p>This page was generated from
        <a class="reference external"
        href="https://github.com/qcodes/qcodes/blob/master/{{docname|e}}">{{ docname|replace("\\","/") }}</a>.
        Interactive online version:
        <a href="https://mybinder.org/v2/gh/qcodes/qcodes/master?filepath={{
        docname|replace("\\","/") }}"><img
    alt="Binder badge"
        src="https://mybinder.org/badge_logo.svg"
        style="vertical-align:text-bottom"></a>.
      </p>
      <script>
        if (document.location.host) {
          var p = document.currentScript.previousSibling.previousSibling;
          var a = document.createElement('a');
          a.innerHTML = 'View in <em>nbviewer</em>';
          a.href = `https://nbviewer.jupyter.org/url${
            (window.location.protocol == 'https:' ? 's/' : '/') +
            window.location.host +
            window.location.pathname.slice(0, -4) }ipynb`;
          a.classList.add('reference');
          a.classList.add('external');
          p.appendChild(a);
          p.appendChild(document.createTextNode('.'));
        }
      </script>
    </div>
"""

# The master toctree document.
master_doc = 'index'

# General information about the project.
project = 'QCoDeS'
copyright = '2016, Giulio Ungaretti, Alex Johnson'
author = 'Giulio Ungaretti, Alex Johnson'


# The language for content autogenerated by Sphinx. Refer to documentation
# for a list of supported languages.
#
# This is also used if you do content translation via gettext catalogs.
# Usually you set "language" from the command line for these cases.
language = "en"

# There are two options for replacing |today|: either, you set today to some
# non-false value, then it is used:
#
# today = ''
#
# Else, today_fmt is used as the format for a strftime call.
#
# today_fmt = '%B %d, %Y'

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This patterns also effect to html_static_path and html_extra_path
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store', '_templates', '_auto',
                    '**.ipynb_checkpoints']

# The reST default role (used for this markup: `text`) to use for all
# documents.
#
# default_role = None

# If true, '()' will be appended to :func: etc. cross-reference text.
#
# add_function_parentheses = True

# If true, the current module name will be prepended to all description
# unit titles (such as .. function::).
#
# add_module_names = True

# If true, sectionauthor and moduleauthor directives will be shown in the
# output. They are ignored by default.
#
# show_authors = False

# The name of the Pygments (syntax highlighting) style to use.
pygments_style = 'sphinx'

# A list of ignored prefixes for module index sorting.
# modindex_common_prefix = []

# If true, keep warnings as "system message" paragraphs in the built documents.
# keep_warnings = False

# If true, `todo` and `todoList` produce output, else they produce nothing.
todo_include_todos = True

# -- Options for HTML output ----------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
html_theme = "sphinx_rtd_theme"

# Theme options are theme-specific and customize the look and feel of a theme
# further.  For a list of options available for each theme, see the
# documentation.
#
# html_theme_options = {}

# Add any paths that contain custom themes here, relative to this directory.
# html_theme_path = []

# The name for this set of Sphinx documents.
# "<project> v<release> documentation" by default.
#
# html_title = 'QCoDeS v1'

# A shorter title for the navigation bar.  Default is the same as html_title.
#
# html_short_title = None

# The name of an image file (relative to this directory) to place at the top
# of the sidebar.
#
# html_logo = None

# The name of an image file (relative to this directory) to use as a favicon of
# the docs.  This file should be a Windows icon file (.ico) being 16x16 or 32x32
# pixels large.
#
# html_favicon = None

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['_static']

# Add custom favicon to the sphinx html documentation.
# Can be an absolute url or a local static file.
favicons = {"rel": "icon", "static-file": "qcodes_favicon.png", "type": "image/png"}

# Add any extra paths that contain custom files (such as robots.txt or
# .htaccess) here, relative to this directory. These files are copied
# directly to the root of the documentation.
#
# html_extra_path = []

# If not None, a 'Last updated on:' timestamp is inserted at every page
# bottom, using the given strftime format.
# The empty string is equivalent to '%b %d, %Y'.
#
# html_last_updated_fmt = None

# If true, SmartyPants will be used to convert quotes and dashes to
# typographically correct entities.
#
# html_use_smartypants = True

# Custom sidebar templates, maps document names to template names.
#
# html_sidebars = {}

# Additional templates that should be rendered to pages, maps page names to
# template names.
#
# html_additional_pages = {}

# If false, no module index is generated.
#
# html_domain_indices = True

# If false, no index is generated.
#
html_use_index = True

# If true, the index is split into individual pages for each letter.
#
# html_split_index = False

# If true, links to the reST sources are added to the pages.
#
# html_show_sourcelink = True

# If true, "Created using Sphinx" is shown in the HTML footer. Default is True.
#
# html_show_sphinx = True

# If true, "(C) Copyright ..." is shown in the HTML footer. Default is True.
#
html_show_copyright = False

# If true, an OpenSearch description file will be output, and all pages will
# contain a <link> tag referring to it.  The value of this option must be the
# base URL from which the finished HTML is served.
#
# html_use_opensearch = ''

# This is the file name suffix for HTML files (e.g. ".xhtml").
# html_file_suffix = None

# Language to be used for generating the HTML full-text search index.
# Sphinx supports the following languages:
#   'da', 'de', 'en', 'es', 'fi', 'fr', 'h', 'it', 'ja'
#   'nl', 'no', 'pt', 'ro', 'r', 'sv', 'tr', 'zh'
#
# html_search_language = 'en'

# A dictionary with options for the search language support, empty by default.
# 'ja' uses this config value.
# 'zh' user can custom change `jieba` dictionary path.
#
# html_search_options = {'type': 'default'}

# The name of a javascript file (relative to the configuration directory) that
# implements a search results scorer. If empty, the default will be used.
#
# html_search_scorer = 'scorer.js'

# Output file base name for HTML help builder.
htmlhelp_basename = 'QCoDeSdoc'

# -- Options for LaTeX output ---------------------------------------------

latex_elements = {  # The paper size ('letterpaper' or 'a4paper').
    #
    # 'papersize': 'letterpaper',

    # The font size ('10pt', '11pt' or '12pt').
    #
    # 'pointsize': '10pt',

    # Additional stuff for the LaTeX preamble.
    #
    # 'preamble': '',

    # Latex figure (float) alignment
    #
    # 'figure_align': 'htbp',
}

# Grouping the document tree into LaTeX files. List of tuples
# (source start file, target name, title,
#  author, documentclass [howto, manual, or own class]).
latex_documents = [(master_doc, 'QCoDeS.tex', 'QCoDeS Documentation',
                    'Giulio Ungaretti, Alex Johnson', 'manual'), ]

# The name of an image file (relative to this directory) to place at the top of
# the title page.
#
# latex_logo = None

# For "manual" documents, if this is true, then toplevel headings are parts,
# not chapters.
#
# latex_use_parts = False

# If true, show page references after internal links.
#
# latex_show_pagerefs = False

# If true, show URL addresses after external links.
#
# latex_show_urls = False

# Documents to append as an appendix to all manuals.
#
# latex_appendices = []

# If false, no module index is generated.
#
# latex_domain_indices = True


# -- Options for manual page output ---------------------------------------

# One entry per manual page. List of tuples
# (source start file, name, description, authors, manual section).
man_pages = [(master_doc, 'qcodes', 'QCoDeS Documentation', [author], 1)]

# If true, show URL addresses after external links.
#
# man_show_urls = False


# -- Options for Texinfo output -------------------------------------------

# Grouping the document tree into Texinfo files. List of tuples
# (source start file, target name, title, author,
#  dir menu entry, description, category)
texinfo_documents = [(
    master_doc, 'QCoDeS', 'QCoDeS Documentation', author, 'QCoDeS',
    'One line description of project.', 'Miscellaneous'), ]

# Documents to append as an appendix to all manuals.
#
# texinfo_appendices = []

# If false, no module index is generated.
#
# texinfo_domain_indices = True

# How to display URL addresses: 'footnote', 'no', or 'inline'.
#
texinfo_show_urls = 'footnote'

# If true, do not generate a @detailmenu in the "Top" node's menu.
#
# texinfo_no_detailmenu = False


# Example configuration for intersphinx: refer to the Python standard library.
intersphinx_mapping = {
    "pandas": ("https://pandas.pydata.org/pandas-docs/stable/", None),
    "matplotlib": ("https://matplotlib.org/stable", None),
    "python": ("https://docs.python.org/3.7/", None),
    "numpy": ("https://numpy.org/doc/stable/", None),
    "py": ("https://pylib.readthedocs.io/en/stable/", None),
    "pyvisa": ("https://pyvisa.readthedocs.io/en/stable/", None),
    "IPython": ("https://ipython.readthedocs.io/en/stable/", None),
}

autoclass_content = "both"
# classes should include both the
# class' and the __init__ method's docstring
autosummary_generate = True
autodoc_member_order = 'bysource'
autodoc_default_options = {'members': True, 'undoc-members': True,
                           'inherited-members': True, 'show-inheritance': True}

# we mock modules that for one reason or another is not
# there when generating the docs
autodoc_mock_imports = [
    "pyspcm",
    "zhinst",
    "zhinst.utils",
    "keysightSD1",
    "cffi",
    "spirack",
    "clr",
    "win32com",
    "win32com.client",
    "pythoncom",
    "slack-sdk",
    "hickle",
    "gclib",
]

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# we are using non local images for badges. These will change so we dont
# want to store them locally.
suppress_warnings = ['image.nonlocal_uri']

nitpicky = False

numfig = True

# Use this kernel instead of the one stored in the notebook metadata:
nbsphinx_kernel_name = 'python3'
# always execute notebooks.
nbsphinx_execute = 'always'

towncrier_draft_autoversion_mode = "draft"
towncrier_draft_include_empty = True
towncrier_draft_working_directory = ".."

issues_github_path = "QCoDeS/Qcodes"
