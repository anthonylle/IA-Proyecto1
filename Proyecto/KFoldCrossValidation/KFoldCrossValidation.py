from Folds.Folds import Folds
from Model.Model import Model
import pandas as pd

from Proyecto.Normalizer.CategoricalValues import CategoricalValues

class KFoldCrossValidation():

    def __init__(self, k, output_column):
        self.folds = Folds()
        self.k = k
        self.output_column = output_column
        self.errors = list()
        self.mean_error = 0
        self.report = str()
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
    def k_fold_validation(self, data_frame, model=Model()):

        self.genered_folds(data_frame)

        for i in range(self.folds.size()):
            x_training, y_training, x_test, y_test = self.get_data_sets(i)
            cv = CategoricalValues()
            y_training = cv.one_hot2(y_training,self.output_column)
            # training section
            model.train_model(x_training.iloc[:,:].values, y_training.iloc[:,:].values)

            # test section
            y_test = cv.one_hot2(y_test,self.output_column)
            error = model.evaluate_model(x_test.iloc[:,:], y_test.iloc[:,:])
            #error = 3
            self.errors.append(error)

        self.mean_error = sum(self.errors) / self.k

        self.generate_report(data_frame)
        return self.mean_error



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

    # ------------------------------------------------------------------------------------------------------------------
    # input: a objects of my DataFrame class
    # function: generate a report string
    # output: none
    def generate_report(self, data_frame):
        text =str()
        text += "----------------------------- REPORT -------------------------\n"
        text += ">>> X : \n"
        columns= data_frame.get_columns_names()
        for column in columns:
            if column != self.output_column:
                text += "  > "+column+"\n"

        text += ">>> Y: \n"
        text += "  > "+self.output_column+"\n"

        text += ">>> clases in Y: \n"
        classes = data_frame.unique_values_in_column(self.output_column)
        for _class in classes:
            text += "  > " + str(_class[0]) + "\n"


        training_error = str(self.mean_error)
        text += ">>>Mean training error: "+training_error+"\n"
        text += ">>> Training error for iteration: \n"
        for i in range(len(self.errors)):
            text += "  > "+str(i)+": "+str(self.errors[i])+"\n"

        self.report = text

    # ------------------------------------------------------------------------------------------------------------------
    # input: none
    # function: print the report string
    # output: none
    def view_report(self):
        print(self.report)


    def prediction(self, dataframe, model = Model()):

        x_predict, y_predict = self.split_data(dataframe)
        Ys = model.predict(x_predict)
        predict_data = Ys.tolist()

        new_column = pd.DataFrame(predict_data, columns=["Predict_column"])
        dataframe.join_data(new_column)
        dataframe.to_csv("Predict_file.csv")
        return dataframe