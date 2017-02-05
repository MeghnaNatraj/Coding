class NeuralNetwork:
    def __init__(self):
        randon.seed(1)

        self.synaptic_weights = 2 * randon.random((3,1)) - 1




if __name__ == "__main__"

    neural_network = NeuralNetwork()

    print "Starting random synaptic weights"
    print neural_network.synaptic_weights

    X_train = array([0,0,1],[1,1,1],[1,0,1],[0,1,1])
    y_train = array([0,1,1,0]).T

    neural_network.train(X_train, y_train, 10000)

    print "New synaptic weights"
    print neural_network.synaptic_weights

    print "Predict [1,0,0]"
    print neural_network.predict([1,0,0])
