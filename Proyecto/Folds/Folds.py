from Proyecto.DataSet.DataFrame import DataFrame
import math


# this class help the cross_validation
# basicaly contain the folds for the k-fold cross-validation
class Folds():

    # ------------------------------------------------------------------------------------------------------------------
    def __init__(self, k, ojective_tag):
        # this attribute is a list o my DataFrames
        self.folds = []
        self.k = k
        self.fold_size = 0
        # containt the unique values(classes) in the output column
        self.chekers = []
        self.ojective_tag = ojective_tag

    # ------------------------------------------------------------------------------------------------------------------
    # input: DataFrame object
    # function: calculate the folds's range
    # output: none
    def calulate_fold_size(self, data_frame):
        self.fold_size = data_frame.size() / self.k
        self.fold_size = math.floor(self.fold_size)

    # ------------------------------------------------------------------------------------------------------------------
    # input: none
    # function: balance last fold if its size is smaller than other
    # output: none
    def balance_last_fold(self):
        last_fold = self.folds[self.k:]
        if last_fold != []:
            fold = last_fold[0]
            self.folds[self.k-1].concat_data(fold.data_set)
            self.folds.pop(self.k)


    # ------------------------------------------------------------------------------------------------------------------
    # input: DataFrame object
    # function: load each fold
    # output: none
    def load_folds(self, data_frame):

        from_index = 0
        to_index = self.fold_size

        for i in range(self.k+1):
            df = data_frame.sub_data_set(from_index, to_index)
            fold = DataFrame()
            fold.data_set= df
            self.folds += [fold]
            from_index += self.fold_size
            to_index += self.fold_size

        self.balance_last_fold()

    # ------------------------------------------------------------------------------------------------------------------
    # input: index of fold to check
    # function: check clases in fold
    # output: boolean value

    def has_all_clases(self, index):

        df = self.folds[index];
        col = df.get_column_by_label(self.ojective_tag)
        values = col.iloc[:, :].values

        for i in range(len(self.chekers)):
            if not (self.chekers[i][0] in values):
                return False

        return True

    # ------------------------------------------------------------------------------------------------------------------
    # input: index of fold to check
    # function: check clases in all folds
    # output: none

    def check_classes(self):
        for i in range(len(self.folds)):
            if not self.has_all_clases(i):
                return False
        return True

    # ------------------------------------------------------------------------------------------------------------------
    # input: DataFrame object
    # function: create the folds
    # output: none

    def created_folds(self, data_frame):

        self.chekers = data_frame.unique_values_in_column(self.ojective_tag)
        self.calulate_fold_size(data_frame)
        self.load_folds(data_frame)

    # ------------------------------------------------------------------------------------------------------------------
    # input: index of a fold
    # function: return the fold to use as testing
    # output: n fold

    def get_test(self, index):
        temp = self.folds[index]
        return temp

    # ------------------------------------------------------------------------------------------------------------------
    # input: index of a fold
    # function: return the train folds without test fold
    # output: a list

    def get_train(self, index):
        temp = self.folds[:]
        del (temp[index])
        return temp

    # ------------------------------------------------------------------------------------------------------------------
    # input: index of a fold
    # function: return the train folds without test fold
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
