from DataSet.DataFrame import DataFrame
import math
import copy as c

# this class help the cross_validation
# basicaly contain the folds for the k-fold cross-validation
class Folds():

    # ------------------------------------------------------------------------------------------------------------------
    def __init__(self):
        # this attribute is a list o my DataFrames then it can to be a list of pandas dataframe
        self.folds = []
        self.fold_size = 0
        # containt the unique values(classes) in the output column
        self.chekers = []


    # ------------------------------------------------------------------------------------------------------------------
    # input: DataFrame object
    # function: calculate the folds's range
    # output: none
    def calulate_fold_size(self, data_frame, k):
        self.fold_size = data_frame.size() / k
        self.fold_size = math.floor(self.fold_size)

    # ------------------------------------------------------------------------------------------------------------------
    # input: k value
    # function: balance last fold if its size is smaller than other
    # output: none
    def balance_last_fold(self, k):
        last_fold = self.folds[k:]
        if last_fold != []:
            fold = c.deepcopy(last_fold[0])
            self.folds[k-1].concat_data(fold.data_set)
            #print("este es el penultimo tiene cnt de filas: "+str(self.folds[k-1].size()))
            #self.folds[k - 1].view_head()
            #self.folds[k-1].to_csv("gg.csv")
            del(self.folds[k])


    # ------------------------------------------------------------------------------------------------------------------
    # input: DataFrame object, k value
    # function: load each fold
    # output: none
    def load_folds(self, data_frame, k):

        from_index = 0
        to_index = self.fold_size

        for i in range(k+1):
            df = data_frame.sub_data_set(from_index, to_index)
            fold = DataFrame()
            fold.data_set= df
            self.folds += [fold]
            from_index += self.fold_size
            to_index += self.fold_size
        self.balance_last_fold(k)

    # ------------------------------------------------------------------------------------------------------------------
    # input: index of fold to check, output column name
    # function: check clases in fold
    # output: boolean value

    def has_all_clases(self, index, output_column):

        df = self.folds[index];
        col = df.get_column_by_label(output_column)
        values = col.iloc[:, :].values

        for i in range(len(self.chekers)):
            if not (self.chekers[i][0] in values):
                return False

        return True

    # ------------------------------------------------------------------------------------------------------------------
    # input: index of fold to check, output_column name
    # function: check clases in all folds
    # output: none

    def check_classes(self, output_column):
        for i in range(len(self.folds)):
            if not self.has_all_clases(i, output_column):
                return False
        return True

    # ------------------------------------------------------------------------------------------------------------------
    # input: DataFrame object, k value, output column name
    # function: create the folds
    # output: none

    def created_folds(self, data_frame, k, output_column):

        self.chekers = data_frame.unique_values_in_column(output_column)
        self.calulate_fold_size(data_frame, k)
        self.load_folds(data_frame, k)

    # ------------------------------------------------------------------------------------------------------------------
    # input: index of a fold
    # function: return the fold to use as testing and other of training
    # output: a list DataFrame object of my DataFrame class, and a DataFrame object

    def get_sets(self, index):
        training = c.deepcopy(self.folds[:])
        test = training[index]
        del (training[index])
        return training, test

    # ------------------------------------------------------------------------------------------------------------------
    # input: index of a fold
    # function: return the length of my folds list
    # output: size of folds
    def size(self):
        return len(self.folds)

    # ------------------------------------------------------------------------------------------------------------------
    # input: none
    # function: print a fold
    # output: none

    def print_fold(self, index):
        print(self.folds[index])

    # ------------------------------------------------------------------------------------------------------------------
    # input: none
    # function: print all folds
    # output: none

    def print_folds(self):
        for i in range(len(self.folds)):
            self.print_fold(i)
