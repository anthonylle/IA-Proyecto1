from tensorflow.nn import relu, sigmoid, softmax, softplus
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense
from tensorflow.keras.losses import MSE
from tensorflow.keras.optimizers import Adamax, Adam, SGD

from Proyecto.KFoldCrossValidation.KFoldCrossValidation import KFoldCrossValidation
from Proyecto.Model.Model import Model
from Proyecto.DataSet.DataFrame import DataFrame
from Proyecto.Normalizer.Normalizer import Normalizer
import os

os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'


class NeuralNetwork(Model):
    model = None

    def __init__(self):
        self.model = Sequential()

    def create_model(self, kwargs):
        self.model.compile(optimizer=SGD(), loss=MSE)

        no_units = kwargs["units"]  # number of units (neurons) in a layer
        available_activation_functions = {"relu": relu, "sigmoid": sigmoid, "softmax": softmax, "softplus": softplus}
        activation_function = available_activation_functions[kwargs["activation"]]

        for i in range(0, kwargs["layers"]):
            self.model.add(Dense(no_units, activation=activation_function))

    def train_model(self, x_train_data, y_train_data):
        """
        x_val_data = DataFrame()
        x_val_data.data_set = x_train_data
        x_train_data = x_val_data.sub_data_set(0, x_val_data.size()-25)
        x_val_data.data_set = x_val_data.sub_data_set(x_val_data.size()-25 , x_val_data.size()-1)

        y_val_data = DataFrame()
        y_val_data.data_set = y_train_data
        y_train_data = y_val_data.sub_data_set(0, y_val_data.size()-25)
        y_val_data.data_set = y_val_data.sub_data_set(y_val_data.size()-25, y_val_data.size()-1)
        """
        self.model.fit(x_train_data, y_train_data)#, validation_data=(x_train_data, y_train_data), batch_size=57)

    def evaluate_model(self, x_test_data, y_test_data):
        return self.model.evaluate_model(x_test_data, y_test_data)

    def predict(self, x_data):
        return self.model.predict(x_data)


model = NeuralNetwork()
# create data_frame to input
input = DataFrame()
# create data_frame to output
output = DataFrame()
# create normalizer
normalizer = Normalizer()

input.load_data_set("breast-cancer-wisconsin-data.csv")
# drop innecesary columns in the input
#input.view()
input.drop_columns_by_name(["id"])
#input.view()
output.data_set = input.cut_column('diagnosis')
#input.view()
# normalizer data
data = input.data_set
input.data_set = normalizer.normalize_data(data)
#input.join_data(output.data_set)
#validation = KFoldCrossValidation(10, 'diagnosis')
model.create_model(kwargs={"units": 2, "layers": 5, "activation": "sigmoid"})
print("Input: ", input.data_set)

#model.train_model(input.data_set, o utput.data_set)
#validation.k_fold_validation(input, model=model)

