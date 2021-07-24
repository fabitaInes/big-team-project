import pandas as pd


class Extract:
    def __init__(self, df):
        self.df = df
        
        
    def length(self,column_name):
        valores = self.df.loc[:,column_name].tolist()
        for x in valores:
            y = len(x)
            result.append(x)
        return result
    
    
    def first_char(self, column_name):
        result = self.df[column_name].str.strip().str[0]
        return result
    
    
    
     def last_char(self, column_name):
        result = self.df[column_name].str.strip().str[-1]
        return result
    
    def range_f(self, column_name, new_column_name, start, count):
        valores = self.df.loc[:,column_name].tolist()
        result = self.df[new_column_name]
        for x in valores:
            y = len(x)
            result.append(y)
            
        return result