
class Network:
    def __init__(self):
        self.layers = []
        self.loss = None
        self.loss_prime = None

    def add(self, layer):
        self.layers.append(layer)

    def setup_loss(self, loss, loss_prime):
        self.loss = loss
        self.loss_prime = loss_prime

    def predict(self, input):
        """

        :param input: [[1, 3]] = > 1 , [[1, 3], [3, 5], [3, 4]]
        :return: kết quả dự đoán
        """
        result = []
        n = len(input)
        for i in range(n):
            output = input[i]

            for layer in self.layers:
                output = layer.forward_propagation(output)
            result.append(output)

        return result

    def fit(self, x_train, y_train, learning_rate, epochs):

        n = len(x_train)
        for i in range(epochs):
            err = 0
            for j in range(n):
                #lan truyen tiến
                output = x_train[j]
                for layer in self.layers:
                    output = layer.forward_propagation(output)

                #tính lỗi của từng
                err += self.loss(y_train[j], output)

                #lan truyền ngược
                error = self.loss_prime(y_train[j], output)
                for layer in reversed(self.layers):
                    error = layer.backward_propagation(error, learning_rate)

            err = err / n

            print('epoch : %d/%d  err = %f' %(i, epochs, err))

