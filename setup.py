# Copyright (c) 2023, mivallion
# Copyright (c) 2015, Nir Soffer
# Copyright (c) 2013, Stavros Korokithakis
# All rights reserved.
#
# Licensed under BSD licnese, see LICENSE.

from distutils.core import setup

setup(
    author="mivallion",
    author_email="mivallion@gmail.com",
    description=("A very slow file sysem for simulating overloded storage with HTTP API control"),
    license="BSD",
    name="slowfs",
    scripts=["slowfsctl", "slowfs", "slowfs_api"],
    url="https://github.com/nirs/slowfs",
    version="0.2",
)
