import pandas as pd

class Standard:
    def __init__(self, df):
        self.df = df
    
    def sum(self, column_name):
        result = self.df.loc[:,column_name].sum()
        return result
    
    def multiply(self, column_name, factor):
        result = self.df.loc[:, column_name] * factor
        return result
    
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
    
