import pandas as pd
from pandas.api.types import CategoricalDtype
import numpy as np

@pd.api.extensions.register_dataframe_accessor("dd")
class DataDictionaryAccessor():

    validation_columns = {
            'min_value':np.NaN,
            'max_value':np.NaN,
            'categories':"",
            'ordered':False,
            'min_length':np.NaN,
            'max_length':np.NaN
        }

    def __init__(self, pandas_obj):
        self._df = pandas_obj
        self.reset_data_dict()

    def __repr__(self):
        return self._data_dict.__repr__()

    def reset_data_dict(self):
        data_dict = pd.DataFrame()
        data_dict.reindex(self._df.columns)
        data_dict['datatype'] = self._df.dtypes.astype(str)

        # Create validation columns (name, default value)
        for column, default_value in DataDictionaryAccessor.validation_columns.items():
            data_dict[column] = default_value

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
        return self._data_dict[self.validation_columns.keys()]

    def set_min_value(self,var:str,value):
        self.set_var_property(var,'min_value',float(value),dtype=float)

    def validate_min_value(self,var,value):
        return self._df[var] >= float(value)

    def set_max_value(self,var:str,value):
        self.set_var_property(var,'max_value',float(value),dtype=float)

    def validate_max_value(self,var,value):
        return self._df[var] <= float(value)

    def set_min_length(self,var:str,value):
        self.set_var_property(var,'min_length',int(value),dtype=int)

    def validate_min_length(self,var,value):
        return self._df[var].str.len() >= float(value)

    def set_max_length(self,var:str,value):
        self.set_var_property(var,'max_length',int(value),dtype=int)

    def validate_max_length(self,var,value):
        return self._df[var].str.len() <= float(value)

    def set_categories(self,var:str,category_list=None,ordered=False):
        if not category_list:
            # get a list from existing data column
            category_list = list(self._df[var].unique())
        cat_type = CategoricalDtype(categories=category_list,ordered=ordered)
        self._df[var] = self._df[var].astype(cat_type)
        self.set_var_property(var,'datatype','category')
        category_list = [str(x) for x in self._df[var].dtype.categories]
        category_list_string = '|'.join(category_list)
        self.set_var_property(var,'categories',category_list_string)
        self.set_var_property(var,'ordered',ordered)
        
    def validate_categories(self,var,value):
        return self._df[var].str.contains(value,na=False)

    def validate(self,var:str=None):
        # Get validation parameters for var
        validation_params = self.validation.loc[var].astype(str).to_dict()
        # Remove those with default values
        defaults = ['nan','','False']
        validation_params = {k:v for k,v in validation_params.items() if v not in defaults}
        # Call validation function for each validation parameter
        series_collection = []
        for parameter, value in validation_params.items():
            valid_series = getattr(self,'validate_' + parameter)(var,value)
            # Append series to df
            series_collection.append(valid_series)
        # Finally use all to create new series representing each row
        return pd.concat(series_collection,axis=1).all(axis=1)