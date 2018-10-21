from Proyecto.Folds.Folds import Folds
from Proyecto.Model.Model import Model
from Proyecto.DataSet.DataFrame import DataFrame

class KFoldCrossValidation():

    def __init__(self, k, output_column):
        self.folds = Folds()
        self.k = k
        self.output_column = output_column
        self.errors = list()
        self.mean_error = 0

    # input: object of DataFrame class
    # function: genered the folds
    # output: none
    def genered_folds(self, data_frame):
        self.folds.created_folds(data_frame, self.k, self.output_column)

    """ 
    aqui verifica que las varas esten bien  
    """

    def validated_folds(self):
        self.folds.check_classes(self.output_column)

    # input: a object of DataFrame class
    # function: cross validation function
    # output: none
    def k_fold_validation(self,data_frame,model = Model()):

        self.genered_folds(data_frame)


        for i in range(self.folds.size()):
            x_training, y_training, x_test, y_test = self.get_data_sets(i)

            # training section
            model.train_model(x_training, y_training)

            # test section
            #error = model.evaluate_model(x_test, y_test)
            error = 3
            self.errors.append(error)

        self.mean_error = sum(self.errors) / self.k




    # input: number of iteration
    # function: get all data set for i iteration
    # output: 4 pandas dataframes
    def get_data_sets(self, iteration):
        training_set, test_set = self.folds.get_sets(iteration)
        training_set = self.concat_training_set(training_set)
        x_training, y_training = self.split_data(training_set)
        x_test, y_test = self.split_data(test_set)

        return x_training, y_training, x_test, x_test

    # ------------------------------------------------------------------------------------------------------------------
    # input: a dataframes objects of my DataFrame class
    # function: split data in input (x) and output (y) data
    # output: two pandas dataframes
    def split_data(self, data_frame):
        y = data_frame.cut_column(self.output_column)
        x = data_frame.data_set
        return x, y

    # ------------------------------------------------------------------------------------------------------------------
    # input: a list with dataframes objects of my DataFrame class
    # function: concat all dataframes in the training list
    # output: a dataframe object of my DataFrame class
    def concat_training_set(self, training_list):
        training_set = training_list[0]

        for i in range(1, len(training_list)):
            # call the function concat_data and get a data_set
            training_set.concat_data(training_list[i].data_set)
        return training_set
