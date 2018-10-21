from tensorflow.nn import relu, sigmoid, softmax, softplus
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense
from tensorflow.keras.losses import MSE, binary_crossentropy
from tensorflow.keras.optimizers import Adamax, Adam, SGD
from Proyecto.DataSet.DataFrame import DataFrame
from Proyecto.Normalizer.Normalizer import Normalizer
from Proyecto.Model.Model import Model
import os

os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'


class NeuralNetwork(Model):
    input_vars = None
    output_var = None
    normalizer = None
    x_train_data = None
    y_train_data = None
    x_test_data = None
    y_test_data = None
    x_val_data = None
    y_val_data = None
    model = None

    def __init__(self):
        self.model = Sequential()

    def load_data(self):
        self.input_vars = DataFrame()
        self.input_vars.load_data_set("breast-cancer-wisconsin-data.csv")
        self.input_vars.drop_columns_by_name(['id', 'Unnamed: 32'])
        self.output_var = DataFrame()
        self.output_var.data_set = self.input_vars.cut_column('diagnosis')

    def normalize_data(self):
        normalizer = Normalizer()
        data = self.input_vars.data_set
        self.input_vars.data_set = normalizer.normalize_data(data)
        data = self.output_var.data_set
        self.output_var.data_set = normalizer.normalize_data(data)
        '''
        print("---- Output vars ---- \n", self.output_var.data_set)
        print("---- Input vars ---- \n", self.input_vars.data_set)
        '''

    def assign_data(self):
        self.x_train_data = self.input_vars.sub_data_set(0,200).values
        self.y_train_data = self.output_var.sub_data_set(0,200).values

        self.x_val_data = self.input_vars.sub_data_set(201,400).values
        self.y_val_data = self.output_var.sub_data_set(201,400).values

        self.x_test_data = self.input_vars.sub_data_set(401,569).values
        self.y_test_data = self.output_var.sub_data_set(401, 569).values

    def create_model(self, kwargs):
        self.model.compile(optimizer=SGD(), loss=MSE)

        no_units = kwargs["units"]  # number of units (neurons) in a layer
        available_activation_functions = {"relu": relu, "sigmoid": sigmoid, "softmax": softmax, "softplus": softplus}
        activation_function = available_activation_functions[kwargs["activation"]]

        for i in range(0, kwargs["layers"]):
            self.model.add(Dense(no_units, activation=activation_function))
        self.load_data()
        self.normalize_data()
        self.assign_data()

    def train_model(self):
        self.model.fit(self.x_train_data,self.y_train_data, validation_data=(self.x_val_data, self.y_val_data), batch_size=57)

    def evaluate_model(self):
        return self.model.evaluate_model(self.x_test_data, self.y_test_data)



instance = NeuralNetwork()
instance.load_data()
instance.normalize_data()
instance.assign_data()
instance.create_model(kwargs={"layers": 5, "units": 2, "activation":"softmax"})
instance.train_model()
accuracy = instance.model.evaluate(instance.x_test_data, instance.y_test_data)
print("Accuracy: ", accuracy)
