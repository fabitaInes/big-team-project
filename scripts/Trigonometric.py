import pandas as pd
import numpy as np

class Trigonometric:
    def __init__(self, df):
        self.df = df
    
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