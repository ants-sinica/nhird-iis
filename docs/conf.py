# -*- coding: utf-8 -*-

from __future__ import unicode_literals
import sys, os

on_rtd = os.environ.get('READTHEDOCS', None) == 'True'

sys.path.append(os.path.abspath(os.pardir))

__version__ = '1.0'

# -- General configuration -----------------------------------------------------
extensions = ['sphinx.ext.autodoc', 'sphinx.ext.ifconfig', 'sphinx.ext.extlinks']
source_suffix = '.rst'
master_doc = 'index'
project = 'nhird-iis'
copyright = '2016, IIS, Academia Sinica'
# The name of the Pygments (syntax highlighting) style to use.
pygments_style = 'sphinx'

extlinks = {}

# -- Options for HTML output ---------------------------------------------------

html_theme = 'default'

html_static_path = ['static']

# Output file base name for HTML help builder.
htmlhelp_basename = 'nhird-iis'

#html_use_smartypants = True

# If false, no module index is generated.
#html_use_modindex = False

# If false, no index is generated.
#html_use_index = False

# If true, links to the reST sources are added to the pages.
#html_show_sourcelink = False

def setup(app):
    # overrides for wide tables in RTD theme
    app.add_stylesheet('theme_overrides.css') # path relative to static
