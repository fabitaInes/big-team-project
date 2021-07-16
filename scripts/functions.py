import pandas as pd
import numpy as np
import math


class PowerBiFunctions:
    df = None

    def __init__(self, excel_path):
        self.df = pd.read_excel(excel_path)

    def get_df(self):
        return self.df

    def sum(self, column_name):
        result = self.df.loc[:,column_name].sum()
        return result

    def multiply(self, column_name, factor):
        result = self.df.loc[:, column_name] * factor
        return result
    
    def get_head(self):
        return self.df.head()
    
    def get_column_names(self):
        return self.df.columns
    
    def subtract(self, column_name, value):
        result = self.df.loc[:, column_name] - value
        return result    
    
    def division(self, column_name, value):
        result = self.df.loc[:, column_name] / value
        return result
    
    def modulo(self, column_name, value):
        result = self.df.loc[:, column_name] % value
        return result
    
    def percentage(self, column_name, value):
        result = self.df.loc[:, column_name] * (value / 100.0)
        return result
    
    def square_root(self, column_name):
        result = self.df.loc[:, column_name] ** 0.5
        return result
    
    def exponent(self, column_name):
        result = np.exp(self.df.loc[:, column_name])
        return result
    
    def logarithm_base10(self, column_name):
        result = np.log10(self.df.loc[:, column_name])
        return result
    
    def logarithm_natural(self, column_name):
        result = np.log(self.df.loc[:, column_name])
        return result
    
    def factorial(self, column_name):
        col = self.df.loc[:, column_name]
        result = [math.factorial(x) if isinstance(x, int)  else 'Error' for x in col]
        return result
    
    def sine(self, column_name):
        result = np.sin(self.df.loc[:, column_name])
        return result
    
    def cosine(self, column_name):
        result = np.cos(self.df.loc[:, column_name])
        return result
    
    def tangent(self, column_name):
        result = np.tan(self.df.loc[:, column_name])
        return result
    
    def arcsine(self, column_name):
        result = np.arcsin(self.df.loc[:, column_name])
        return result

    def arccosine(self, column_name):
        result = np.arccos(self.df.loc[:, column_name])
        return result
    
    def arctangent(self, column_name):
        result = np.arctan(self.df.loc[:, column_name])
        return result
    
    def max(self, column_name):
        result = self.df.loc[:, column_name].max()
        return result
    
    def average(self, column_name):
        result = self.df.loc[:, column_name].mean()
        return result
    
    def media(self, column_name):
        values = list(self.df.loc[:, column_name])
        values.sort()
        n = len(values)
        media = 0
        if n % 2 == 0:
            media = values[int(n / 2)] + values[int(n / 2) - 1]
        else:
            media = values[int(n / 2)]
        return media
    
    def standard_deviation(self, column_name):
        result = self.df.loc[:, column_name].std()
        return result
    
    def count(self, column_name):
        result = self.df.loc[:, column_name].count()
        return result

    def count_distinct_values(self, column_name):
        result = pd.unique(self.df.loc[:, column_name])
        n = len(result)
        return n

    def choose_columns(self, column_names):
        result = self.df.loc[:, column_names]
        return result
    
    def remove_top_rows(self):
        result = self.df.iloc[3:]
        
    def remove_blank_rows(self, column_name):
        unq_df_clean = unq_df.dropna(subset=unq_df.columns.difference(pd.Index([column_name])),how="any")
        return unq_df_clean.head(10)
        
        
    def remove_bottom_rows(self):
        unq_df = self.df.drop_duplicates() 
        return unq_df.shape
    
    def lowercase_to_uppercase(self,column_name):
        valores = self.df.loc[:,column_name].tolist()
        for x in valores:
            x.upper()
        return valores
    
    def data_type(self, column_name):
        result = self.df.loc[:, column_name].dtypes
        return result
    
    def count_rows(self, column_name):
        rows = self.df.loc[:, column_name]
        result = len(rows)
        return result
    
    def rename(self, column_name, renombrado):
        column = self.df.loc[:, column_name]
        result = self.df.rename(columns={column: renombrado})
        return result
    
    def convert_to_list(self, column_name):
        result = self.df.loc[: column_name]
        return result.tolist()
    
    
    def length(self,column_name):
        valores = self.df.loc[:,column_name].tolist()
        for x in valores:
            y = len(x)
            result.append(x)
        return result
    
    def json(self):
        result = self.df.to_json('C:\Users\export.json')
        return result
    
    def sumar_valores_columna(self, column_name):
        valores = self.df.loc[:, column_name].tolist()
        suma = 0
        for x in valores:
            suma = suma + x
        return suma
    
    def valor_absoluto(self, column_name):
        valores = self.df.loc[:, column_name].tolist()
        result = []
        for x in valores:
            y = abs(x)
            result.append(y)
        return result