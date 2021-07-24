import pandas as pd


class Column:
    def __init__(self, df):
        self.df = df
    
    def choose_columns(self, column_names):
        result = self.df.loc[:, column_names]
        return result
    
    def remove_top_rows(self):
        result = self.df.iloc[3:]
        return result
    
    
    def split_column_delimiter(self, column_name, new_column_names, delimiter):
        aux = self.df[column_name].str.split(delimiter, expand=True)
        aux.columns = new_column_names
        result = pd.concat([self.df, aux], axis=1)
        return result
    
    
    def number_character(self, column_name)
        result = self.df[column_name].str.len()
        return result
    
    
    def lowercase_to_uppercase(self,column_name):
        result = self.df.loc[:,column_name].tolist()
        for x in result:
            x.upper()
        return result
    
    def uppercase_to_lowercase(self,column_name):
        result = self.df.loc[:,column_name].tolist()
        for x in valores:
            x.lower()
        return result
    
    
    def position(self, column_name)
        result = self.df.get_loc(column_name)
        return result
