from .layer import Layer
import numpy as np

# FC = Full Connected
# layer = FClayer * active_function

class FCLayer(Layer):
    def __init__(self, input_shape, output_shape):
        """
        :param input_shape:  (1, 3)       output của layer này là input của layer kia
        :param output_shape: (1, 4)
        (1X3) (3x4) => (1, 4)
        (3, 1) (1, 4) => (3x4)
        """
        self.input_shape = input_shape
        self.output_shape = output_shape
        self.weights = np.random.rand(input_shape[1], output_shape[1]) - 0.5
        self.bias = np.random.rand(1, output_shape[1]) - 0.5

    def forward_propagation(self, input):
        self.input = input
        self.output = np.dot(self.input, self.weights) + self.bias
        return  self.output

    def backward_propagation(self, output_error, learning_rate):
        curent_layer_err =  np.dot(output_error, self.weights.T)
        dweight = np.dot(self.input.T, output_error)   # d là đạo hàm

        self.weights -= dweight*learning_rate
        self.bias -= learning_rate*output_error

        return curent_layer_err





