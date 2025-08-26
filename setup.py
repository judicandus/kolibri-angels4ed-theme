#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import absolute_import, print_function, unicode_literals

from setuptools import setup
import kolibri_angels4ed_theme  # <-- underscore

dist_name = "kolibri-angels4ed-theme"     # distribution name (may contain hyphens)
package_name = "kolibri_angels4ed_theme"  # python package name (underscores)

repo_url = "https://github.com/judicandus/kolibri-angels4ed-theme"
description = "Angels for Education custom theme for Kolibri"

long_description = (
    "A plugin that customizes Kolibri's appearance for Angels for Education. "
    "See the Github repo <{repo_url}> for details.".format(repo_url=repo_url)
)

setup(
    name=dist_name,
    version=kolibri_angels4ed_theme.__version__,
    description=description,
    long_description=long_description,
    author="Angels for Education",
    author_email="admin@vickyfoundation.org",
    url=repo_url,
    packages=[package_name],
    package_dir={package_name: package_name},
    include_package_data=True,
    entry_points={
        "kolibri.plugins": "{pkg} = {pkg}".format(pkg=package_name),
    },
    license="MIT",
    zip_safe=False,
    keywords="kolibri",
    classifiers=[
        "Development Status :: 3 - Alpha",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
    ],
)
