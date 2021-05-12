import pytest

import pandas as pd
from pandas_data_dictionary import pd_dd

@pytest.fixture
def simple_df():
    df = pd.read_csv('tests/simple-test-data.csv')
    return df

def test_access_dd_extension(simple_df):
    simple_df.dd

