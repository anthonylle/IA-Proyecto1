from tensorflow.nn import relu
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense
from tensorflow.keras.losses import MSE
from tensorflow.keras.optimizers import SGD
from Proyecto.DataSet.DataFrame import DataFrame
from Proyecto.Normalizer.Normalizer import Normalizer
from Proyecto.Model.Model import Model


class NeuralNetwork(Model):
    input_vars = None
    output_var = None
    normalizer = None
    x_train_data = None
    y_train_data = None
    x_test_data = None
    y_test_data = None
    model = None

    def __init__(self):
        pass

    def load_data(self):
        self.input_vars = DataFrame()
        self.input_vars.load_data_set("breast-cancer-wisconsin-data.csv")
        self.input_vars.drop_columns_by_name(['id', 'Unnamed: 32'])
        self.output_var = DataFrame()
        self.output_var.data_set = self.input_vars.cut_column('diagnosis')

    def normalize_data(self):
        normalizer = Normalizer()
        data = self.input_vars.data_set
        self.input_vars.data_set = normalizer.normalizer_data(data)
        data = self.output_var.data_set
        self.output_var.data_set = normalizer.normalizer_data(data)

        print(self.output_var.data_set)
        print(self.input_vars.data_set)


    def assign_data(self):
        None#self.x_train_data = self.input_vars.

    def create_model(self):
        self.model = Sequential()
        self.model.compile(optimizer=SGD, loss=MSE)
        no_units = 1 # number of units (neurons) in a layer
        no_columns = self.input_vars.data_set.columns # number of columns in the input data to train ToDo x_train_data
        # ToDo create loop for adding new layers to the model
        self.model.add(Dense(no_units, input_shape=no_columns, activation=relu))

    def train_model(self):
        self.model.fit(self.x_train_data,self.y_train_data, validation_data=(self.x_test_data, self.y_test_data))

    def evaluate_model(self):
        pass


instance = NeuralNetwork()
instance.load_data()
instance.normalize_data()
#instance.create_model()
#instance.train_model()
