import pandas as pd
import numpy as np
import math

class Scientific:
    def __init__(self, df):
        self.df = df
    
    def absolute_value(self, column_name):
        valores = self.df.loc[:, column_name].tolist()
        result = []
        for x in valores:
            y = abs(x)
            result.append(y)
        return result
    
    def power(self, column_name, exponent):
        result = self.df.loc[:, column_name] ** exponent
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
        result = self.df.loc[:, column_name].apply(lambda x: math.factorial(x) if isinstance(x, int) and x > 0 else 'Error')
        return result
    