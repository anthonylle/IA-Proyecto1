from abc import ABCMeta

class Model(metaclass=ABCMeta):
    def load_data(self, file_path):
        pass
    def normalize_data(self, dataset):
        pass
