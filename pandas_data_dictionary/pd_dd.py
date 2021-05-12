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
        data_dict = pd.DataFrame()
        data_dict.reindex(self._df.columns)
        data_dict['datatype'] = self._df.dtypes.astype(str)
        data_dict['min_value'] = np.NaN
        data_dict['max_value'] = np.NaN
        self._data_dict = data_dict


    @property
    def datatype(self):
        return self._data_dict['datatype']

    def set_var_property(self,var:str,property_column:str,value,dtype=str):
        # Check if column exists. If not create it with empty value of appropriate type
        if property_column not in self._data_dict:
            # Hopefully this type checking is sufficient for all use cases
            empty_value = "" if dtype==str else np.NaN 
            self._data_dict[property_column] = empty_value
        self._data_dict.at[var,property_column] = value

    @property
    def description(self):
        if 'description' not in self._data_dict:
            raise KeyError('No descriptions have been set yet')
        return self._data_dict['description']

    def set_desc(self,var:str,desc:str):
        self.set_var_property(var,'description',desc)

    @property
    def title(self):
        if 'title' not in self._data_dict:
            raise KeyError('No titles have been set yet')
        return self._data_dict['title']

    def set_title(self,var:str,title:str):
        self.set_var_property(var,'title',title)

    @property
    def units(self):
        if 'units' not in self._data_dict:
            raise KeyError('No units have been set yet')
        return self._data_dict['units']

    def set_units(self,var:str,units:str):
        self.set_var_property(var,'units',units)

    def series_with_units(self,var):
        return self._df[var].astype(str) + ' ' + self._data_dict['units'][var]

    @property
    def validation(self):
        validation_columns = ['min_value','max_value']
        return self._data_dict[validation_columns]

    def set_min_value(self,var:str,value):
        self.set_var_property(var,'min_value',float(value),dtype=float)

    def set_max_value(self,var:str,value):
        self.set_var_property(var,'max_value',float(value),dtype=float)