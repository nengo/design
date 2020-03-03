#!/usr/bin/env python3

from datetime import datetime
import os

extensions = [
    "sphinx.ext.autosectionlabel",
    "sphinx.ext.githubpages",
    "sphinx.ext.intersphinx",
    "sphinx.ext.mathjax",
    "sphinx.ext.todo",
    "nengo_sphinx_theme",
]

# -- sphinx
nitpicky = True
exclude_patterns = [
    "_build", "Thumbs.db", ".DS_Store", "README.rst", "fonts/README.rst"
]
source_suffix = ".rst"
source_encoding = "utf-8"
master_doc = "index"
project = "Nengo design"
copyright = "2017-2020, Applied Brain Research"
author = "Applied Brain Research"
version = release = datetime.now().strftime("%Y-%m-%d")

# -- sphinx.ext.todo
todo_include_todos = True

intersphinx_mapping = {
    "nengo": ("https://www.nengo.ai/nengo", None)
}

# -- nengo_sphinx_theme
html_theme = "nengo_sphinx_theme"
pygments_style = "friendly"
templates_path = []
html_favicon = "general/favicon.ico"
html_static_path = ["_static"]
html_logo = os.path.join("_static", "logo.svg")

# -- other
htmlhelp_basename = "Nengo design"

latex_elements = {
    # "papersize": "letterpaper",
    # "pointsize": "11pt",
    # "preamble": "",
    # "figure_align": "htbp",
}

latex_documents = [
    (master_doc,  # source start file
     "nengo.tex",  # target name
     "Nengo Design",  # title
     "Applied Brain Research",  # author
     "manual"),  # documentclass
]

man_pages = [
    # (source start file, name, description, authors, manual section).
    (master_doc, "nengo", "Nengo Design", [author], 1)
]

texinfo_documents = [
    (master_doc,  # source start file
     "Nengo",  # target name
     "Nengo Design",  # title
     author,  # author
     "Nengo",  # dir menu entry
     "Design assets for Nengo",  # description
     "Miscellaneous"),  # category
]


def setup(app):
    def modify_filenames(_, env):
        for source, (parents, _) in env.images.items():
            env.images[source] = (parents, "-".join(os.path.split(source)))

    app.connect("env-updated", modify_filenames)
    app.add_stylesheet("custom.css")
