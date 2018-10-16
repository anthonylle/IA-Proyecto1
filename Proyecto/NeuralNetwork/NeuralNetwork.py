import tensorflow as tf
from tensorflow import keras
from Proyecto.DataSet.DataFrame import DataFrame
import pandas as pd
from Proyecto.Normalizer.Normalizer import Normalizer
from Proyecto.Model.Model import Model

class NeuralNetwork(Model):
    input_vars = None#DataFrame()
    output_var = None#DataFrame()
    normalizer = None#Normalizer()

    def __init__(self):
        pass

    def load_data(self, file_path):
        #self.data_frame = pd.read_csv("../src/data/" + file_path)
        #self.data_frame.drop(index=0)
        self.input_vars = DataFrame()
        self.input_vars.load_data_set("breast-cancer-wisconsin-data.csv")
        self.input_vars.drop_columns_by_name(['id', 'Unnamed: 32'])
        self.output_var = DataFrame()
        self.output_var.data_set = self.input_vars.cut_column('diagnosis')
        #data_frame = DataFrame()
        #data_frame.load_data_set(file_path)


    def normalize_data(self):
        normalizer = Normalizer()
        data = self.input_vars.data_set
        print(data)
        self.input_vars.data_set = normalizer.normalizer_data(data)
        print(self.input_vars.data_set)
        data = self.output_var.data_set
        self.output_var.data_set = normalizer.normalizer_data(data)

        print(self.output_var)
        print(self.input_vars)

instance = NeuralNetwork()
instance.load_data("breast-cancer-wisconsin-data.csv")
instance.normalize_data()
