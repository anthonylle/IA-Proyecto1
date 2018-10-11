import csv
from normalizer.Normalizer import Normalizer
import tensorflow as tf
from tensorflow import keras

class NeuralNetwork(Model):
    def load_data(self, file_path):
        with open(file_path, 'rb') as csvfile:
            spamreader = csv.reader(csvfile, delimiter=' ', quotechar='|')
        for row in spamreader:
            print(', '.join(row))

    def normalize_data(self, dataset=None):
        None

