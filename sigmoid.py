from math import exp
from random import uniform


def sigmoid(x): return 1.0 / (1.0 + exp(-x))


class Neuron:
    def __init__(self, neuron_input):
        self.input = neuron_input
        self.alpha = 0.1
        self.input_weight = [uniform(-1, 1) for _ in range(len(self.input) + 1)]
        self.weight_error = list()

    def __repr__(self):
        return "<Neuron>"

    def work(self):
        # return sigmoid(sum([self.input[i] * self.input_weight[i] for i in range(len(self.input))]))

        sum = 0

        for i in range(len(self.input)):
            sum += self.input_weight[i] * self.input[i]

        sum += self.input_weight[-1]

        return sigmoid(sum)


if __name__ == '__main__':
    all_input = [
        [0, 0],
        [0, 1],
        [1, 0],
        [1, 1]
    ]

    correct_input = [0, 0, 0, 1]

    for data, correct_data in zip(all_input, correct_input):
        neuron = Neuron(data)
        print(neuron.work())
