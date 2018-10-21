from unittest.mock import Mock
from ..neural_network import NeuralNetwork


class NeuralNetworkTests(Mock):
    model = NeuralNetwork()

    def test_0(self):
        thing = Mock()
        self.model.create_model(kwargs={"units": 2, "layers": 5, "activation": "relu"})
        self.assert_called_with()

    def test_1(self):
        None
