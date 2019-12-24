# -*- coding: utf-8 -*-
"""Project configuration."""

import os

__author__ = 'deepVector'
__copyright__ = 'Copyright 2019-present, deepVector'
__credits__ = ['os: https://docs.python.org/3/']
__license__ = 'CC-BY-NC-ND-4.0'
__version__ = '1.0.2'
__maintainer__ = 'deepVector'
__email__ = 'd33pv3ct0r@gmail.com'
__status__ = 'Dev'

# Specify path(s): Root data dir
DATA_ROOT_DIR = os.path.join(
    r'D:\dtHome', 'deepVector_19_dataPhD_Rx09-11_repo01_data')

# Setup path(s): Input, working, output dirs
DATA_INPUT_DIR = os.path.join(DATA_ROOT_DIR, 'data01_input')
DATA_WORKING_DIR = os.path.join(DATA_ROOT_DIR, 'data02_working')
DATA_OUTPUT_DIR = os.path.join(DATA_ROOT_DIR, 'data03_output')
