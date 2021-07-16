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