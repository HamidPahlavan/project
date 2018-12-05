"""Most of the configuration for a Python project is done in this setup.py file. 
we will edit this file accordingly to adapt this to our needs.
Copied and based on: https://github.com/pypa/sampleproject
"""
#!/usr/bin/env python
# -*- coding: utf-8 -*-
from setuptools import setup,find_packages
import os

with open("README", 'r') as f:
    long_description = f.read()

setup(
    name='climops',  # Required
    version='0.1.0',  # Required
    description='Python interface to get statistical relationships from Yale Climate opinion maps and Census',  # Optional
    # Often, this is the same as your README, so you can just read it in from
    # that file directly (as we have already done above)
    url='https://github.com/https://github.com/HamidPahlavan/ClimOps',  
    license = 'MIT'
    author='Robin Clancy, Rebeca de Buen, Hamid Pahlavan and Yakelyn R. Jauregui',  # Optional
    author_email='rclancy@uw.edu',  # Optional
    packages =['climops'],
    keywords='Yale Climate opinion maps, Census',  # Optional
    # Similar to `install_requires` above, these must be valid existing
    # projects.
    package_data=['data/*']
    extras_require={  # Optional
        'dev': ['check-manifest'],
        'test': ['coverage'],
    },

    project_urls={  # Optional
        'Bug Reports': 'https://github.com/https://github.com/HamidPahlavan/ClimOps/issues',
        'Source': 'https://github.com/https://github.com/HamidPahlavan/ClimOps/',
    },
)
