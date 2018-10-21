from abc import ABCMeta

class Model(metaclass=ABCMeta):
    def load_data(self):
        pass

    def normalize_data(self):
        pass

    def create_model(self, *kwargs):
        """
        :param kwargs: specific configuration options to create the model
        :return:
        """
        pass

    def train_model(self, x_train_data, y_train_data):
        """
        :param x_train_data: x values to train the model
        :param y_train_data: the objective or goal for the training process
        :return:
        """

        pass

    def evaluate_model(self, x_test_data, y_test_data):
        pass
