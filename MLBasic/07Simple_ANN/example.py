from network.network import Network
from layers.FCLayer import FCLayer
from layers.activation_layer import ActivationLayer
import numpy as np

def relu(z):
    """
    :param z:  numpy array
    :return: 0 nếu z <= 0
         z nếu z > 0
         [1, -3, 9, -7] => [1, 0, 9, 0]
    """
    return np.maximum(0, z)

def relu_prime(z):
    """
    :param z: numpy array
    :return: array 1, 0 z> 0 => 1, z < 0 => 0
    """
    z[z<0] = 0
    z[z>0] = 1
    return z


def loss(y_true, y_pred):
    return 0.5*(y_pred-y_true)**2

def loss_prime(y_true, y_pred):
    return y_pred-y_true

x_train = np.array([[[0, 0]], [[0, 1]], [[1, 0]], [[1, 1]]])
y_train = np.array([[[0]], [[1]], [[1]], [[0]]])

net = Network()
net.add(FCLayer((1, 2), (1, 3)))
net.add(ActivationLayer((1, 3), (1, 3), relu, relu_prime))
net.add(FCLayer((1, 3), (1, 1)))
net.add(ActivationLayer((1, 1), (1, 1), relu, relu_prime))

net.setup_loss(loss, loss_prime)

net.fit(x_train, y_train, epochs=1000, learning_rate=0.01)

out = net.predict([[0, 1]])

print(out)

