import pandas as pd

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
    def datatypes(self):
        return self._data_dict['datatype']