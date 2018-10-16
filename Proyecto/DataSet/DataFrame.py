#libraries
import pandas as pd

class DataFrame():
    
    #------ Variables -------      
    data_set = None
    
    #------- functions
    
    #-----------------------------------------------------------
    # input: -string with the name and extension of data set file
    # function: load a csv file from src/data folder 
    # output: none
    def load_data_set(self, file_name):
        self.data_set = pd.read_csv("./src/data/"+file_name)
        
    
    # ------------------------------------------------------------
    # input: - list of names columns to drop
    # function: drop columns by name in a data frame
    # output: none 
    def drop_columns_by_name(self,columns_to_drop):
        
        self.data_set = self.data_set.drop(columns_to_drop, axis=1)

    # ------------------------------------------------------------
    # input: -  list of index columns to drop
    # function: drop columns by index in a data frame
    # output: none
    def drop_columns_by_index(self, columns_to_drop):
 
         self.data_set = self.data_set.drop(self.data_set.columns[columns_to_drop], axis=1)
         
    # ------------------------------------------------------------
    # input: -  none
    # function: copy date_set
    # output: DataFrame object
    def copy(self):
        return self.data_set.copy()
    
    # ------------------------------------------------------------
    # input: int index of column
    # function: get some column with index column
    # output: date_frame with the column
    def get_column_by_index(self, index ):
        temp = self.data_set.iloc[:, index]
        temp=temp.to_frame()
        return temp
    
    # ------------------------------------------------------------
    # input: range of rows a and b
    # function: get a sub data set 
    # output: a dataFrame
    def sub_data_set(self, a, b ):
        temp = self.data_set.iloc[a:b, :]
        return temp
    
    # ------------------------------------------------------------
    # input: string with tag column
    # function: get some column with tag column
    # output: date_frame with the column
    def get_column_by_label(self, tag_column):
        index = self.data_set.columns.get_loc(tag_column)
        column = self.get_column_by_index(index)
        return column
    
    # ------------------------------------------------------------
    # input: none
    # function: drop all columns
    # output: none   
    def drop_all_columns(self):
        columns = self.data_set.columns
        self.data_set = self.data_set.drop(columns,axis = 1)
        
    # ------------------------------------------------------------
    # input: - string with column tag 
    # function: cut column
    # output: date frame with cut column  
    def cut_column(self, tag):
        column = self.get_column_by_label(tag)
        self.drop_columns_by_name([tag])
        return column
    
    # ------------------------------------------------------------
    # input: none 
    # function: get all values in data_frame
    # output: values in data_set
    def get_all_values(self):
        values  = self.data_set.iloc[:,:].values 
        return values
    
    # ------------------------------------------------------------
    # input: - number index of row
    # function: get specific row values
    # output: row values in  data
    def get_row_values(self, row):
        values = self.data_set.iloc[:,:].values
        values = values[row,:]
        return values
    
    # ------------------------------------------------------------
    # input: - number index of column
    # function: get specific colu values
    # output: row values in  data
    def get_column_values(self, column):
        values = self.data_set.iloc[:,:].values
        values = values[:,column]
        return values
    
    # ------------------------------------------------------------
    # input: none
    # function: get columns in data_set
    # output: return columns
    def get_columns_names(self):
        return self.data_set.columns
    
    # ------------------------------------------------------------
    # input: none
    # function: print head
    # output: none     
    def view_head(self):
        print(self.data_set.head())
        
    # ------------------------------------------------------------
    # input: none
    # function: print head
    # output: none 
    def view(self):
        print(self.data_set)

    # ------------------------------------------------------------
    # input: none
    # function: create csv file
    # output: none  
    def to_csv(self, name):
        self.data_set.to_csv("./src/partial_data/"+name, sep=',', encoding='utf-8')
    
    # ------------------------------------------------------------
    # input: none
    # function: create excel file
    # output: none  
    def to_excel(self, name):
        # Create a Pandas Excel writer using XlsxWriter as the engine.
        writer = pd.ExcelWriter("./src/partial_data/"+name, engine='xlsxwriter')   
        # Convert the dataframe to an XlsxWriter Excel object.
        self.data_set.to_excel(writer, sheet_name='Sheet1')
        # Close the Pandas Excel writer and output the Excel file.
        writer.save()
    
    # ------------------------------------------------------------
    # input: none
    # function: get size from data_set
    # output: int with data_set size     
    def size(self):
        # this get the count rows
        return self.data_set.shape[0]
        
