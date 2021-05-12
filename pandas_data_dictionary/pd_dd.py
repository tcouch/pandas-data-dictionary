import pandas as pd
import numpy as np

@pd.api.extensions.register_dataframe_accessor("dd")
class DataDictionaryAccessor():
    def __init__(self, pandas_obj):
        self._df = pandas_obj
        self.reset_data_dict()

    def __repr__(self):
        return self._data_dict.__repr__()

    def reset_data_dict(self):
        self._data_dict = pd.DataFrame()
        self._data_dict.reindex(self._df.columns)
        self._data_dict['datatype'] = self._df.dtypes.astype(str)

    @property
    def datatype(self):
        return self._data_dict['datatype']

    @property
    def description(self):
        return self._data_dict['description']

    def set_desc(self,var:'df column name',desc:'description'):
        if 'description' not in self._data_dict:
            self._data_dict['description'] = ""
        self._data_dict.at[var,'description'] = desc