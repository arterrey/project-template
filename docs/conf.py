"""Sphinx Documentation Configuration
"""

from datetime import datetime

import pkg_resources

project = "My Project"
author = "Author"

extensions = [
    "sphinx.ext.autodoc",
    "sphinx.ext.viewcode",
    "sphinxcontrib.programoutput",
]
templates_path = ["_templates"]
source_suffix = ".rst"
master_doc = "index"
copyright = "{}, {}".format(datetime.now().year, author)
version = pkg_resources.get_distribution("app").version
release = version
language = "en"
exclude_patterns = ["_build"]
pygments_style = "sphinx"
todo_include_todos = False
html_theme = "furo"
html_title = "Market Stats"
html_static_path = ["_static"]
htmlhelp_basename = project
autodoc_member_order = "bysource"
autoclass_content = "class"


def setup(app):
    app.add_css_file("css/custom.css")
