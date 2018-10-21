
from scipy.stats import zscore
from DataSet.DataFrame import DataFrame
import pandas as pd
import copy as c



class CategoricalValues():

    # ----------------------One hot-------------------------------------
    # ------------------------------------------------------------------
    # input: list with the clases in the column
    # function: create a dictionary with ceros values
    # output: dictionary
    # columns have de form ['value'],...,['value']]
    def get_dictionary_tasg(self, column_classes):
        dictionary = {}
        for item in column_classes:
            dictionary[item[0]] = 0
        return dictionary

    # ------------------------------------------------------------------
    # input: - data_list: a list with the column values
    #        - a dictionary with the classes keys
    # function: build a matrix with the dumies columns
    # output: a matrix
    def  biuld_dumies(self, data_list, dictionary_classes):
        dumies = []
        for item in data_list:
            classes_copy = c.deepcopy(dictionary_classes)
            classes_copy[item[0]] = 1
            dumies += [classes_copy]
        return dumies

    # ------------------------------------------------------------------
    # input:
    # function:
    # output:
    def dumies_tags(self, data_set, column_tag):
        classes = data_set.unique_values_in_column(column_tag)
        classes = classes.tolist()
        return self.get_dictionary_tasg(classes)

    # ------------------------------------------------------------------
    # input:
    # function:
    # output:
    def one_hot(self, data_set, column_tag ):
        df = DataFrame()
        df.data_set = data_set
        data_list = df.get_all_values().tolist()
        dumies = self.dumies_tags(df, column_tag)
        dumies = self.biuld_dumies(data_list, dumies)
        return pd.DataFrame(dumies)