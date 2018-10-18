from tensorflow.nn import relu, sigmoid, softmax
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense
from tensorflow.keras.losses import MSE, binary_crossentropy
from tensorflow.keras.optimizers import Adamax, Adam, SGD
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
        self.input_vars.data_set = normalizer.normalize_data(data)
        data = self.output_var.data_set
        self.output_var.data_set = normalizer.normalize_data(data)
        '''
        print(self.output_var.data_set)
        print(self.input_vars.data_set)
        '''

    def assign_data(self):
        self.x_train_data = self.input_vars.sub_data_set(0,400).values
        # print("X_train_data: ", self.x_train_data)
        self.y_train_data = self.output_var.sub_data_set(0,400).values
        self.x_test_data = self.input_vars.sub_data_set(400,569).values
        self.y_test_data = self.output_var.sub_data_set(400, 569).values

    def create_model(self):
        self.model = Sequential()
        self.model.compile(optimizer=Adamax(), loss=binary_crossentropy)
        no_units = 2 # number of units (neurons) in a layer
        # number of columns in the input data to train ToDo x_train_data
        # ToDo create loop for adding new layers to the model
        self.model.add(Dense(no_units, activation=relu))

    def train_model(self):
        self.model.fit(self.x_train_data,self.y_train_data, validation_data=(self.x_test_data, self.y_test_data), batch_size=57)

    def evaluate_model(self):
        pass


instance = NeuralNetwork()
instance.load_data()
instance.normalize_data()
instance.assign_data()
instance.create_model()
instance.train_model()
accuracy = instance.model.evaluate(instance.x_test_data, instance.y_test_data)
print("Accuracy: ", accuracy)
