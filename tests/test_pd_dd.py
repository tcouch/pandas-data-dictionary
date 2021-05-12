import io
import pytest
import sys

import pandas as pd
from pandas_data_dictionary import pd_dd

@pytest.fixture
def simple_df():
    df = pd.read_csv('tests/simple-test-data.csv')
    return df

def test_access_dd_extension(simple_df):
    simple_df.dd

def test_datatypes_property(simple_df):
    simple_df.dd.datatypes

def test_print_dd(simple_df):
    capturedOutput = io.StringIO()
    sys.stdout = capturedOutput
    print(simple_df.dd)
    sys.stdout = sys.__stdout__
    assert 'aardvark' in capturedOutput.getvalue()

