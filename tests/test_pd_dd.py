import pytest

import pandas as pd
from pandas_data_dictionary import pd_dd

def setup_function(function):
    df = pd.read_csv('tests/simple-test-data.csv')
    return df

def test_access_dd_extension():
    df.dd

