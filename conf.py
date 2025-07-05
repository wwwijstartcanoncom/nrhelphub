# Configuration file for the Sphinx documentation builder.
 
import os
import sys
 
# -- Path setup --------------------------------------------------------------
 
# If extensions or modules to document with autodoc are in another directory,
# add these directories to sys.path here.
# Example:
# sys.path.insert(0, os.path.abspath('../src'))
 
# -- Project information -----------------------------------------------------
 
project = 'Netgear Router Login Help'
copyright = '2025, Netgear Help Center'
author = 'Netgear Support'
 
# The full version, including alpha/beta/rc tags
release = '1.0.0'
 
# -- General configuration ---------------------------------------------------
 
extensions = []
 
# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']
 
# List of patterns to ignore when looking for source files.
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']
 
# -- HTML output options -----------------------------------------------------
 
# Title shown in the browser tab and top of HTML pages
html_title = "How to Log In to Your Netgear Router – Step-by-Step Guide"
 
# Optional short title (e.g., for nav bar)
html_short_title = "Netgear Router Login"
 
# Choose a theme
# Uncomment if needed. Example:
# html_theme = 'sphinx_rtd_theme'
 
# Hide "View page source"
html_show_sourcelink = False
 
# Allow raw HTML blocks in .rst files (use cautiously)
html_allow_unsafe = True
 
# Theme customization options
html_theme_options = {
    'show_powered_by': False,
}
 
# Favicon (place favicon.ico in the root or _static folder)
html_favicon = 'favicon.ico'
 
# Static assets (e.g., images, stylesheets)
# Uncomment below if you add custom styles or media:
# html_static_path = ['_static']
