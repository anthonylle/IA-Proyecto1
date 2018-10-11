#------ librerias 
import numpy as np
import pandas as pd
#funcion para pasar valores numericos
from scipy.stats import zscore


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
    
    # ------------------------------------------------------------
    # input: none
    # function: 
    # output:         
    def normalizer_column(self, column_value, current_column, column_name):
        
        _type = self.checker_type(column_value)
        
        if( _type == 1 ):
            return self.normalizer_categorical_values(current_column, column_name)
        
        elif( _type == 2 ):
            return current_column.apply(zscore)  
        
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
    def normalizer_data(self,data_frame):
        
        first_row = self.get_first_row(data_frame)
        temp_df= self.temporal_data_frame(data_frame)
        columns_names = data_frame.columns
        
        for i in range( len( first_row ) ):
            current_col = self.get_current_column(data_frame,i)

            current_col = self.normalizer_column(first_row[i], current_col, columns_names[i])

            temp_df= self.join_data(temp_df, current_col)
        return temp_df


        
        
        