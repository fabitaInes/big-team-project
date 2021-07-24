import pandas as pd

class Statics:
    def __init__(self, df):
        self.df = df
    
    def sum(self, column_name):
        valores = self.df.loc[:, column_name].tolist()
        suma = 0
        for x in valores:
            suma = suma + x
        return suma

    def min(self, column_name):
        result = self.df.loc[:,column_name].min()
        return result
    
    def max(self, column_name):
        result = self.df.loc[:, column_name].max()
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
    
    def average(self, column_name):
        result = self.df.loc[:, column_name].mean()
        return result
    
    def standard_deviation(self, column_name):
        result = self.df.loc[:, column_name].std()
        return result
    
    def count_values(self, column_name):
        result = self.df.loc[:, column_name].count()
        return result

    def count_distinct_values(self, column_name):
        result = pd.unique(self.df.loc[:, column_name])
        n = len(result)
        return n