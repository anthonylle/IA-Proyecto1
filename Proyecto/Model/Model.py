from abc import ABCMeta


class Model(metaclass=ABCMeta):
    def create_model(self, *kwargs):
        """
        :param kwargs: dictionary containing the needed params for the specific model to implement
        :return: nothing
        """
        pass

    def train_model(self, x_train_data, y_train_data):
        """
        :param x_train_data: inputs to train the model
        :param y_train_data: objective data or goal to achieve after training
        :return:
        """
        pass

    def evaluate_model(self, x_test_data, y_test_data):
        pass

    def predict(self, x_data):
        pass
