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
    simple_df.dd.datatype

def test_print_dd(simple_df):
    capturedOutput = io.StringIO()
    sys.stdout = capturedOutput
    print(simple_df.dd)
    sys.stdout = sys.__stdout__
    assert 'rating' in capturedOutput.getvalue()

def test_set_description(simple_df):
    description = 'Rating out of 5'
    simple_df.dd.set_desc('rating',description)
    assert simple_df.dd._data_dict.at['rating','description'] == description

def test_set_title(simple_df):
    """test setting friendly name for use in charts etc."""
    title = "Is the item in stock?"
    simple_df.dd.set_title('in_stock',title)
    assert simple_df.dd._data_dict.at['in_stock','title'] == title