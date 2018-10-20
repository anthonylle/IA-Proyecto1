from abc import ABCMeta


class Model(metaclass=ABCMeta):
    def load_data(self):
        pass

    def normalize_data(self):
        pass

    def create_model(self):
        pass

    def train_model(self, x, y):
        pass

    def evaluate_model(self, x, y):
        pass
