#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Original Copyright from Endless Key Theme - 2023 Endless OS Foundation, LLC
# SPDX-License-Identifier: MIT
# kolibri-angels4ed-theme Copyright to Angels for Education
from __future__ import absolute_import, print_function, unicode_literals

from setuptools import setup

import kolibri-angels4ed-theme

dist_name = "kolibri-angels4ed-theme"
plugin_name = "kolibri-angels4ed-theme"
repo_url = "https://github.com/judicandus/kolibri-angels4ed-theme"

# Default description of the distributed package
description = """A plugin to define a custom theme for Angels for Education for Kolibri"""

long_description = """
A plugin that defines a custom theme to customise the appearance of Kolibri for
Angels for Education. See the `Github repo <{repo_url}>`_ for more details.
""".format(
    repo_url=repo_url
)

setup(
    name=dist_name,
    version=kolibri_angels4ed_theme.__version__,
    description=description,
    long_description=long_description,
    author="Angels for Education",
    author_email="admin@vickyfoundation.org",
    url=repo_url,
    packages=[str(plugin_name)],  # https://github.com/pypa/setuptools/pull/597
    entry_points={
        "kolibri.plugins": "{plugin_name} = {plugin_name}".format(
            plugin_name=plugin_name
        ),
    },
    package_dir={plugin_name: plugin_name},
    include_package_data=True,
    license="MIT",
    zip_safe=False,
    keywords="kolibri",
    classifiers=[
        "Development Status :: 2 - Pre-Alpha",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Natural Language :: English",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.3",
        "Programming Language :: Python :: 3.4",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: Implementation :: PyPy",
    ],
)
