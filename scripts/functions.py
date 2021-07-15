import pandas as pd


class PowerBiFunctions:
    df = None

    def __init__(self, excel_path):
        self.df = pd.read_excel(excel_path)

    def get_df(self):
        return self.df

    def sum(self, column_name):
        result = self.df.loc[:,column_name].sum()
        return result

    
    
    
    
    
    
    