import pandas as pd


class Date:
    def __init__(self, df):
        self.df = df

    def extract_year(self, column_name):
        self.__convert_to_datetime(column_name)
        result = self.df[column_name].dt.year
        return result

    def extract_month(self, column_name):
        self.__convert_to_datetime(column_name)
        result = self.df[column_name].dt.month
        return result

    def extract_quarter(self, column_name):
        self.__convert_to_datetime(column_name)
        result = self.df[column_name].dt.quarter
        return result

    def extract_week(self, column_name):
        self.__convert_to_datetime(column_name)
        result = self.df[column_name].dt.week
        return result

    def extract_day(self, column_name):
        self.__convert_to_datetime(column_name)
        result = self.df[column_name].dt.day
        return result

    def __convert_to_datetime(self, column_name):
        try:
            self.df[column_name] = pd.to_datetime(self.df[column_name])
        except Exception as e:
            print('Cannot convert ' + column_name + ' column to Datetime')
