###############################################################################
# Copyright 2015-2016 University of Florida. All rights reserved.
# This file is part of UF CTS-IT's NACCulator project.
# Use of this source code is governed by the license found in the LICENSE file.
###############################################################################

from setuptools import setup, find_packages

VERSION = "0.1.0"
GITHUB_URL = "https://github.com/ctsit/nacculator_utils"

setup(
    name="nacculator",
    version=VERSION,
    maintainer="UF CTS-IT",
    maintainer_email="ctsit@ctsi.ufl.edu",
    url="https://github.com/ctsit/nacculator_utils",
    license="Apache2",
    description="Tools for the NACCulator",
    keywords=["REDCap", "NACC", "UDS", "Clinical data"],
    download_url=GITHUB_URL + "/releases/tag/" + VERSION,
    package_dir={'nacc': 'nacc'},
    packages=find_packages(),
    entry_points={
        "console_scripts": [
            "redcap2nacc = nacc.redcap2nacc:main"
        ]
    }
)
