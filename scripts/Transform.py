import pandas as pd


class Transform:
    def __init__(self, df):
        self.df = df
    
    
    def data_type(self, column_name):
        result = self.df.loc[:, column_name].dtypes
        return result
    
    
    def rename(self, column_name, new_columnname):
        column = self.df.loc[:, column_name]
        result = self.df.rename(columns={column: new_columnname})
        return result

    
    def convert_to_list(self, column_name):
        result = self.df.loc[: column_name]
        return result.tolist()
    
    
    def merge_columns (self, new_column_name, columns, separator):
        self.df[new_column_name] = self.df[columns].apply(lambda row: separator.join(row.values.astype(str)), axis=1)
        result = self.choose_columns(new_column_name)
        return result
    
    def use_first_row_as_header(self):
        header = self.df.iloc[0]
        result = self.df(self.df.values[1:], columns=headers)
        return result
    
    
    def replace_value(self, column_name, value, new_value):
        result = self.df[column_name].replace([value],new_value)
        return result 
    
    def transpose(self):
        result = self.df.transpose()
        return result
    
    
    def fill(self, column_name, value):
        result= self.df.fillna({column_name: value})
        return result
    
    def order_alphabetic(self, column_name):
        result = self.df.sort_values(column_name)
        return result
    
    
    
    
