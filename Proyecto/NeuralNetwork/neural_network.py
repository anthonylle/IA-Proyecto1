from tensorflow.nn import relu, sigmoid, softmax, softplus
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense
from tensorflow.keras.losses import MSE  # , binary_crossentropy
from tensorflow.keras.optimizers import SGD  # , Adamax, Adam
from Model.Model import Model
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
        self.model.fit(x_train_data,y_train_data) # , validation_data=(self.x_val_data, self.y_val_data), batch_size=57)

    def evaluate_model(self, x_test_data, y_test_data):
        return self.model.evaluate_model(x_test_data, y_test_data)

    def predict(self, x_data):
        return self.model.predict(x_data)
