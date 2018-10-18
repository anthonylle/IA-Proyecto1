#------ librerias 
import numpy as np
import pandas as pd
#funcion para pasar valores numericos
from scipy.stats import zscore
import math as m

class Normalizer():
    
    # ------ functions -----------   
        
    # ------------------------------------------------------------
    # input: instance of a varible
    # function: check type of variable
    # output:- return 1 if value is a instance of string
    #        - return 2 if value is a instance of number         
    def checker_type(self,value):
        
        if(isinstance(value, np.string_)) or (isinstance(value, str)):
            return 1
        
        elif (isinstance(value, np.int64)) or (isinstance(value, int )) or (isinstance(value, float)):
            return 2
        return self.error
    
    # ------------------------------------------------------------
    # input: none
    # function: 
    # output:
    def normalizer_categorical_values(self,current_column, column_name):
        one_hot = pd.get_dummies( current_column[ column_name ])
        return one_hot  
    
    # -----------------------------------------------------------
    # input: none
    # function: 
    # output:         
    def normalizer_column(self, column_value, current_column, column_name):
        
        _type = self.checker_type(column_value)
        
        if _type == 1:
            return self.normalizer_categorical_values(current_column, column_name)
        
        elif _type == 2:
            return self.z_score(current_column, column_name)
            #return current_column.apply(zscore)
        
        else:
            print("column doesn't have valid type")
                
        return self.error     
        
    # ------------------------------------------------------------
    # input:
    # function: 
    # output: 
    def get_first_row(self, data_frame):
        row = data_frame.iloc[:,:].values
        return row[0,:]
        
    # ------------------------------------------------------------
    # input:
    # function: 
    # output: 
    def temporal_data_frame(self, data_frame):
        columns = data_frame.columns
        temp = data_frame.drop(columns,axis = 1)
        return temp

    # ------------------------------------------------------------
    # input:
    # function: 
    # output: 
    def get_current_column(self, data_frame, column_index):
        column= data_frame.iloc[:,column_index]
        column = column.to_frame()
        return column
    
    # ------------------------------------------------------------
    # input:
    # function: 
    # output: 
    def join_data(self,temp_data_frame, current_column):
        temp_data_frame = temp_data_frame.join( current_column )
        return temp_data_frame
    
    # ------------------------------------------------------------
    # input:
    # function: 
    # output:         
    def normalize_data(self, data_frame):
        
        first_row = self.get_first_row(data_frame)
        temp_df= self.temporal_data_frame(data_frame)
        columns_names = data_frame.columns
        
        for i in range(len(first_row)):
            current_col = self.get_current_column(data_frame,i)
            current_col = self.normalizer_column(first_row[i], current_col, columns_names[i])
            temp_df= self.join_data(temp_df, current_col)
        return temp_df

    #  --------------Z score-----------------------------------

    # -----------------------------------------------------------
    # input: int: media , list of x values
    # function: sum all square of  x- media
    # output: int: sum
    def square_sum(self, media, Xs):
        sum = 0
        for i in range(len(Xs)):
            sub = Xs[i][0] - media
            temp = pow(sub, 2)
            sum = sum + temp
        return sum

    # -----------------------------------------------------------
    # input: int: n, int: media, list of x values
    # function: calculate standar desviation
    # output: number with the standar desviation
    def stand_deviation(self, n, media, Xs):

        square_sum = self.square_sum(media, Xs)
        sq_div_n = square_sum / n
        sqrt = m.sqrt(sq_div_n)

        return sqrt

    # -----------------------------------------------------------
    # input: list of x values, int: media, int: standar desviation
    # function: do z score formula
    # output: list with the scores
    def z_score_formula(self, Xs, media, stand_desviation):

        scores = []

        for i in range(len(Xs)):
            result = (Xs[i][0] - media) / stand_desviation
            scores += [[result]]
        return scores

    # -----------------------------------------------------------
    # input: list of scores, string: name of column
    # function: create a dataframe column
    # output: pandas dataframe
    def zs_column(self, data, name):

        df = pd.DataFrame(data, columns=[name])
        return df
    # -----------------------------------------------------------
    # input: a pandas series
    # function: convert a pandas series in a int
    # output: a number
    def series_toInt(self, pd_series):
        ltemp = pd_series.tolist()
        return ltemp[0]

    # -----------------------------------------------------------
    # input: pandas dataframes, string: column name
    # function: do the calculate of s-score
    # output: pandas dataframe
    def z_score(self, data_set, column_name):
        sum = self.series_toInt(data_set.sum())
        n = data_set.shape[0]
        media = sum / n
        Xs = data_set.iloc[:, :].values
        Xs = Xs.tolist()
        stand_desviation = self.stand_deviation(n, media, Xs)
        data = self.z_score_formula(Xs, media, stand_desviation)
        df = self.zs_column(data, column_name)
        return df


    # ----------------------One hot---------------------------
