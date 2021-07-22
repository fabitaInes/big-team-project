import pandas as pd
import numpy as np

class Round:
    def __init__(self, df):
        self.df = df

    def round_even(self, column_name):
        self.df[column_name] = self.df[column_name].apply(lambda x: np.ceil(x) if int(x) % 2 == 0 else np.floor(x))
        result = self.choose_columns(column_name)
        return result

    def round_odd(self, column_name):
        self.df[column_name] = self.df[column_name].apply(lambda x: np.ceil(x) if int(x) % 2 > 0 else np.floor(x))
        result = self.choose_columns(column_name)
        return result
    
    def choose_columns(self, column_names):
        result = self.df.loc[:, column_names]
        return result