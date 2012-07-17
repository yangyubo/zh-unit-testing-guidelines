# -*- coding: utf-8 -*-



import sys, os
project = u'单元测试准则'
copyright = u''
version = u''
release = u''

source_suffix = '.rst'
master_doc = 'index'
language = 'en_US'
exclude_patterns = ['_build']
extensions = ['sphinx.ext.pngmath']
pygments_style = 'sphinx'

html_title = u'单元测试准则'
html_theme = 'haiku'
html_theme_path = ['../../../templates/sphinx', ]
htmlhelp_basename = 'unit-testing-guidelines'
html_add_permalinks = None

file_insertion_enabled = False
latex_documents = [
  ('index', 'unit-testing-guidelines.tex', u'单元测试准则',
   u'', 'manual'),
]

exclude_patterns = ['README.rst']


#Add sponsorship and project information to the template context.
context = {
    'MEDIA_URL': "/media/",
    'slug': 'unit-testing-guidelines',
    'name': u'单元测试准则',
    'analytics_code': '',
}

html_context = context
