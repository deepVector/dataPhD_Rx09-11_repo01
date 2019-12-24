# -*- coding: utf-8 -*-
"""Merge a range of data items from multiple geospatial datasets."""

import os

import pandas as pd

from config import DATA_WORKING_DIR

__author__ = 'deepVector'
__copyright__ = 'Copyright 2019-present, deepVector'
__credits__ = [
    'os: https://docs.python.org/3/, pandas: https://pandas.pydata.org/']
__license__ = 'CC-BY-NC-ND-4.0'
__version__ = '1.0.2'
__maintainer__ = 'deepVector'
__email__ = 'd33pv3ct0r@gmail.com'
__status__ = 'Dev'

data_request_csv = os.path.join(
    DATA_WORKING_DIR,
    'Witold_samples_no_info_noDup_Select.csv')

data_EARTHMAT_csv = os.path.join(DATA_WORKING_DIR,
                                 'vData_field_CONF',
                                 'EARTHMAT_wc_LIVE_10wci_Select.csv')

data_SAMPLE_csv = os.path.join(DATA_WORKING_DIR,
                               'vData_field_CONF',
                               'SAMPLE_wc_LIVE_10wci_Select.csv')

data_STATION_csv = os.path.join(DATA_WORKING_DIR,
                                'vData_field_CONF',
                                'STATION_wc_LIVE_10wci_Select.csv')

# Read the csv into dataframes
data_request_df = pd.read_csv(data_request_csv)

data_EARTHMAT_df = pd.read_csv(data_EARTHMAT_csv)
data_SAMPLE_df = pd.read_csv(data_SAMPLE_csv)
data_STATION_df = pd.read_csv(data_STATION_csv)

# Inner joint
data_merged_inner_STATION_df = pd.merge(left=data_request_df,
                                        right=data_STATION_df,
                                        how='left',
                                        left_on='STATIONID',
                                        right_on='STATIONID')

data_merged_inner_SAMPLE_df = pd.merge(left=data_merged_inner_STATION_df,
                                       right=data_SAMPLE_df,
                                       how='left',
                                       left_on='SAMPLEID',
                                       right_on='SAMPLEID')

data_merged_inner_EARTHMAT_df = pd.merge(left=data_merged_inner_SAMPLE_df,
                                         right=data_EARTHMAT_df,
                                         how='left',
                                         left_on='EARTHMATID',
                                         right_on='EARTHMATID')


# Save to a csv file
dataSelectedInfo_csv = os.path.join(DATA_WORKING_DIR,
                                    'sampleStationEarthmat_Selected.csv')

data_merged_inner_EARTHMAT_df.to_csv(dataSelectedInfo_csv,
                                     index=False)
