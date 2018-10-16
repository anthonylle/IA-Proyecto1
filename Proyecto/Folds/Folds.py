from DataSet.DataFrame import DataFrame
import math
# this class help the cross_validation
# basicaly contain the folds for the k-fold cross-validation
class Folds():
    def __init__(self):
        # this attribute is a list o DataFrames
        self.folds = []
        self.k = 10
        self.fold_size = 0
    
    #--------------------------------------------------------------------------    
    #input: DataFrame object
    #function: calculate the folds's range
    #output: none
    def calulate_fold_size(self, data_frame):
        self.fold_size = data_frame.size() /self.k     
        self.fold_size = math.floor(self.fold_size)

    #--------------------------------------------------------------------------    
    #input: DataFrame object
    #function: load each fold
    #output: none        
    def load_folds(self,data_frame):

        a = 0
        b = self.fold_size
        for i in range(self.k):
            fold = data_frame.sub_data_set(a,b)
            self.folds += [fold]
            a += self.fold_size
            b += self.fold_size
            
    #--------------------------------------------------------------------------    
    #input: DataFrame object
    #function: create the folds
    #output: none
    def created_folds(self, data_frame):
        self.calulate_fold_size(data_frame)
        self.load_folds(data_frame)           
            
    #--------------------------------------------------------------------------    
    #input: none
    #function: print a fold
    #output: none
    def print_fold(self,index):
        print(self.folds[index])
        

    #--------------------------------------------------------------------------    
    #input: none
    #function: print all folds
    #output: none
    def print_folds(self):
        for i in range(len(self.folds)):
            self.print_fold(i)
            
        
    
            