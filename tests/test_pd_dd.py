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
    assert simple_df.dd.description['rating'] == description

def test_if_property_not_set_raise_exception(simple_df):
    with pytest.raises(KeyError):
        simple_df.dd.description
        simple_df.dd.title

def test_set_title(simple_df):
    """test setting friendly name for use in charts etc."""
    title = "Is the item in stock?"
    simple_df.dd.set_title('in_stock',title)
    assert simple_df.dd.title['in_stock'] == title

def test_set_units(simple_df):
    """test setting units"""
    units = 'kg'
    simple_df.dd.set_units('weight',units)
    assert simple_df.dd.units['weight'] == units

def test_series_with_units(simple_df):
    """can we print a dataframe series with the associated units?"""
    simple_df.dd.set_units('weight','kg')
    capturedOutput = io.StringIO()
    sys.stdout = capturedOutput
    print(simple_df.dd.series_with_units('weight'))
    sys.stdout = sys.__stdout__
    assert '1.34 kg' in capturedOutput.getvalue()

def test_set_min_value(simple_df):
    min_val = 0.0
    simple_df.dd.set_min_value('weight',min_val)
    assert simple_df.dd.validation.min_value['weight'] == min_val

def test_set_max_value(simple_df):
    max_val = 10.0
    simple_df.dd.set_max_value('weight',max_val)
    assert simple_df.dd.validation.max_value['weight'] == max_val

def test_make_categorical(simple_df):
    """Convert variable to category type using existing data
    without ordering"""
    simple_df.dd.set_categories('continent')
    assert type(simple_df['continent'].dtype) == pd.core.dtypes.dtypes.CategoricalDtype

def test_make_categorical_with_list(simple_df):
    """Convert variable to category type and provide category list"""
    category_list = ["Asia","Europe","North America","South America", 
                     "Africa", "Australasia", "Antarctica"]
    simple_df.dd.set_categories('continent',category_list=category_list,ordered=False)
    assert list(simple_df['continent'].dtype.categories) == category_list