# -*- coding: utf-8 -*-
"""Data preparation."""

import os

import pandas as pd

from config import DATA_WORKING_DIR

__author__ = 'deepVector'
__copyright__ = 'Copyright 2019-present, deepVector'
__credits__ = ['os: https://docs.python.org/3/']
__license__ = 'CC-BY-NC-ND-4.0'
__version__ = '1.0.1'
__maintainer__ = 'deepVector'
__email__ = 'd33pv3ct0r@gmail.com'
__status__ = 'Dev'

# Specify the input file
data_input_csv = os.path.join(DATA_WORKING_DIR,
                              'Witold_samples_no_info.csv')

# Read the input file to a data frame
df = pd.read_csv(data_input_csv)

# Check for duplicate rows, based on the column 'Sample ID'
# duplicateRowDF = df[df.duplicated(['Sample ID'])]

# Drop duplicate rows, except for the first occurrence,
# based on the column 'Sample ID' and save to a new dataframe
dfNoDup = df.drop_duplicates(subset='Sample ID',
                             keep='first',
                             inplace=False)

# Save to a csv file
dataNoDup_csv = os.path.join(DATA_WORKING_DIR,
                             'Witold_samples_no_info_noDup.csv')

dfNoDup.to_csv(dataNoDup_csv,
               index=False)
