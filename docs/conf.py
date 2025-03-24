# -- Project information -----------------------------------------------------

project = 'E3Initiative'
copyright = '2025, Leonardo Gutierrez'
author = 'Leonardo Gutierrez'
release = '2024'

# -- General configuration ---------------------------------------------------

extensions = [
    'sphinx_rtd_theme',
    'myst_parser',  # Optional, only if using Markdown
]

templates_path = ['_templates']
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']

source_suffix = {
    '.rst': 'restructuredtext',
    '.md': 'markdown',
}

# -- Options for HTML output -------------------------------------------------

html_theme = 'sphinx_rtd_theme'
html_static_path = ['_static'] # Change from 'alabaster'