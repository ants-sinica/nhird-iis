# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import sys, os

on_rtd = os.environ.get('READTHEDOCS', None) == 'True'

sys.path.append(os.path.abspath(os.pardir))

__version__ = '0.9.0'

# -- General configuration -----------------------------------------------------
templates_path = ['_templates']
source_suffix = '.rst'
master_doc = 'index'
project = 'NHIRD-IIS'
copyright = '2016, IIS, Academia Sinica'
exclude_patterns = ['_build']
release = __version__
version = '.'.join(release.split('.')[:1])
last_stable = '1.0.0'
#rst_prolog = '''
#.. |last_stable| replace:: :nhird-iis-doc:`{0}`
#'''.format(last_stable)

# The name of the Pygments (syntax highlighting) style to use.
pygments_style = 'sphinx'


# -- Options for HTML output ---------------------------------------------------

html_theme = 'default'
#if not on_rtd:
#    try:
#        import sphinx_rtd_theme
#        html_theme = 'sphinx_rtd_theme'
#        html_theme_path = [sphinx_rtd_theme.get_html_theme_path()]
#    except ImportError:
#        pass

html_static_path = ['static']

def setup(app):
    # overrides for wide tables in RTD theme
    app.add_stylesheet('theme_overrides.css')   # path relative to _static

