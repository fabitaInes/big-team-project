import pandas as pd


class Main:
    df = None

    def __init__(self, excel_path):
        self.df = pd.read_excel(excel_path)

    def get_df(self):
        return self.df
