import pandas as pd


class Time:
    def __init__(self, df):
        self.df = df

    def extract_hour(self, column_name):
        self.__convert_to_datetime(column_name)
        result = self.df[column_name].dt.hour
        return result
        
    def extract_minute (self, column_name):
        self.__convert_to_datetime(column_name)
        result = self.df[column_name].dt.minute
        return result

    def extract_second(self, column_name):
        self.__convert_to_datetime(column_name)
        result = self.df[column_name].dt.second
        return result
    
    def __convert_to_datetime(self, column_name):
        try:
            self.df[column_name] = pd.to_datetime(self.df[column_name])
        except Exception as e:
            print('Cannot convert ' + column_name + ' column to Datetime')
