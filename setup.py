from distutils.core import setup
import os

import py2exe

try:
    import better_exceptions
except:
    pass


target = "calc_distance.py"


option = {
    "bundle_files": 3,
    "compressed": True,
    "excludes": ["IPython", "six.moves.urllib", "jinja2.asyncsupport"],
}

setup(
    options={"py2exe": option},
    console=[target],
    zipfile=None,
)
