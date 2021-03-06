import pandas as pd
import numpy as np
import math
import datetime


class PowerBiFunctions:
    df = None

    def __init__(self, excel_path):
        self.df = pd.read_excel(excel_path)

    def get_df(self):
        return self.df

    def get_head(self):
        return self.df.head()
    
    def get_column_names(self):
        return self.df.columns
    
    def choose_columns(self, column_names):
        result = self.df.loc[:, column_names]
        return result
    
    def remove_top_rows(self):
        result = self.df.iloc[3:]
        
    def remove_blank_rows(self, column_name):
        unq_df_clean = unq_df.dropna(subset=unq_df.columns.difference(pd.Index([column_name])),how="any")
        return unq_df_clean.head(10)
        
        
    def remove_bottom_rows(self):
        unq_df = self.df.drop_duplicates() 
        return unq_df.shape
    
    def lowercase_to_uppercase(self,column_name):
        valores = self.df.loc[:,column_name].tolist()
        for x in valores:
            x.upper()
        return valores
    
    def data_type(self, column_name):
        result = self.df.loc[:, column_name].dtypes
        return result
    
    def count_rows(self, column_name):
        rows = self.df.loc[:, column_name]
        result = len(rows)
        return result
    
    def rename(self, column_name, renombrado):
        column = self.df.loc[:, column_name]
        result = self.df.rename(columns={column: renombrado})
        return result
    
    def convert_to_list(self, column_name):
        result = self.df.loc[: column_name]
        return result.tolist()
    
    
    def length(self,column_name):
        valores = self.df.loc[:,column_name].tolist()
        for x in valores:
            y = len(x)
            result.append(x)
        return result
    
    def json(self):
        result = self.df.to_json('export.json')
        return result
    

    def remove_columns(self, column_names):
        result = self.df.drop(column_names, axis=1)
        return result

    def keep_top_rows(self, number_rows):
        result = self.df.head(number_rows)
        return result

    def keep_tail_rows(self, number_rows):
        result = self.df.tail(number_rows)
        return result

    def keep_range_rows(self, initial_row_number, final_row_number):
        result = self.df.iloc[initial_row_number:final_row_number]
        return result

    def split_column_delimiter(self, column_name, new_column_names, delimiter):
        aux = self.df[column_name].str.split(delimiter, expand=True)
        aux.columns = new_column_names
        result = pd.concat([self.df, aux], axis=1)
        return result

    def custom_colum(self, new_column_name, condition_column, condition_operator, condition_value, output_column):
        self.df[new_column_name] = self.df[condition_column].where(
            eval(condition_column + condition_operator + condition_value), self.df[output_column])
        result = self.df.loc[:, new_column_name]
        return result

    # def conditional_column(self, *conditions):
    #     result = None
    #     return result

    def __convert_to_datetime(self, column_name):
        try:
            self.df[column_name] = pd.to_datetime(self.df[column_name])
        except Exception as e:
            print('Cannot convert ' + column_name + ' column to Datetime')


    def extract_minute (self, column_name):
        self.__convert_to_datetime(column_name)
        result = self.df[column_name].dt.minute
        return result

    def extract_hour(self, column_name):
        self.__convert_to_datetime(column_name)
        result = self.df[column_name].dt.hour
        return result

    def extract_second(self, column_name):
        self.__convert_to_datetime(column_name)
        result = self.df[column_name].dt.second
        return result

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

    def last_char(self, column_name):
        result = self.df[column_name].str.strip().str[-1]
        return result

    def first_char(self, column_name):
        result = self.df[column_name].str.strip().str[0]
        return result

    def merge_columns (self, new_column_name, columns, separator):
        self.df[new_column_name] = self.df[columns].apply(lambda row: separator.join(row.values.astype(str)), axis=1)
        result = self.choose_columns(new_column_name)
        return result

    def round_even(self, column_name):
        self.df[column_name] = self.df[column_name].apply(lambda x: np.ceil(x) if int(x) % 2 == 0 else np.floor(x))
        result = self.choose_columns(column_name)
        return result

    def round_odd(self, column_name):
        self.df[column_name] = self.df[column_name].apply(lambda x: np.ceil(x) if int(x) % 2 > 0 else np.floor(x))
        result = self.choose_columns(column_name)
        return result