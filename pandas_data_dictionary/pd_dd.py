import pandas as pd

@pd.api.extensions.register_dataframe_accessor("dd")
class DataDictionaryAccessor():
    def __init__(self, pandas_obj):
        self._df = pandas_obj