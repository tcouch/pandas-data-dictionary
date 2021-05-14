# pandas-data-dictionary

Pandas extension adding data dictionary accessor for describing and validating data.

## Usage
### Import pandas data dictionary
```
import pandas as pd
from pandas_data_dictionary import pd_dd
```
All pandas data frames will now have an attached data dictionary accessible via the `dd` accessor.
### Set allowed values
Allowed values for each data frame column can be set including:
* minimum value: min_value
* maximum value: max_value
* minimum length: min_length
* maximum length: max_length
* categories: categories
For example:
```
# set the minimum value for column1 to 10
df.dd.set_min_value('column1',10)
```
### Validate data
Use `df.dd.validate_all()` to check data in all columns is valid.
If invalid data is found, validate_all will print those column names.

Use `df.dd.validate('column')` to validate a specific column.
This will return a True/False series representing each data point in that column.


## Installation
`python setup.py install`
### Requirements
* pandas
* numpy

## Compatibility

## Licence
MIT
## Authors

`pandas-data-dictionary` was written by `Tom Couch <t.couch@ucl.ac.uk>`_.
