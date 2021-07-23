import pandas as pd


class Row:
    def __init__(self, df):
        self.df = df
    
    def keep_top_rows(self, number_rows):
        result = self.df.head(number_rows)
        return result
    
    def keep_bottom_rows(self, number_rows):
        result = self.df.tail(number_rows)
        return result
    
    def keep_range_rows(self, initial_row_number, final_row_number):
        result = self.df.iloc[initial_row_number:final_row_number]
        return result
    
    
    def keep_duplicates(self, column)
        result = self.df[self.df.duplicated([column])]
        return result 
    
    
    
    def remove_top_rows(self, number_rows):
        result = self.df.iloc[number_rows:]
        return result
    
    
    def remove_duplicates(self):
        unq_df = self.df.drop_duplicates() 
        return unq_df.shape
    
    
    def remove_blank_rows(self, column_name):
        unq_df_clean = unq_df.dropna(subset=unq_df.columns.difference(pd.Index([column_name])),how="any")
        return unq_df_clean.head(10)
    
    
    def count_rows(self, column_name):
        rows = self.df.loc[:, column_name]
        result = len(rows)
        return result
    
