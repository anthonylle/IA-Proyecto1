from abc import ABCMeta


class Model(metaclass=ABCMeta):
    def load_data(self):
        pass

    def normalize_data(self):
        pass

    def create_model(self, *kwargs):
        '''
        :param args:
        :return:
        '''
        pass

    def train_model(self):
        pass

    def evaluate_model(self):
        pass
