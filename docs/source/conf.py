import os
import sys
import django

sys.path.insert(0, os.path.abspath('../..'))
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'oc_lettings_site.settings')
os.environ.setdefault('SECRET_KEY', 'sphinx-docs-build-only')
django.setup()

project = 'OC Lettings'
copyright = '2026, Franco-Dev'
author = 'Franco-Dev'
release = '1.0'

extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.viewcode',
    'sphinx.ext.napoleon',
]

templates_path = ['_templates']
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']

html_theme = 'sphinx_rtd_theme'
html_static_path = ['_static']
