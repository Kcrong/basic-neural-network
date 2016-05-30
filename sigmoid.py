from math import exp
from random import uniform

INPUT_CNT = 2


def sigmoid(x): return 1.0 / (1.0 + exp(-x))


class Neuron:
    def __init__(self):
        self.alpha = 0.1
        self.weight_error = [0 for _ in range(INPUT_CNT+1)]
        self.weight = [uniform(-1, 1) for _ in range(INPUT_CNT+1)]

    def __repr__(self):
        return "<Neuron>"

    def work(self, input_data):
        # return sigmoid(sum([self.input[i] * self.input_weight[i] for i in range(len(self.input))]))

        output_sum = 0

        for idx in range(len(input_data)):
            output_sum += self.weight[idx] * input_data[idx]

        output_sum += self.weight[-1]

        return sigmoid(output_sum)

    def learn(self, input_data, answer):
        output = self.work(input_data)
        output_error = output - answer

        for idx in range(len(input_data)):
            self.weight_error[idx] += output_error * input_data[idx] * output * (1 - output)

        self.weight_error[-1] += output_error * 1.0 * output * (1 - output)

    def fix(self):
        for idx in range(INPUT_CNT+1):
            self.weight[idx] -= self.alpha * self.weight_error[idx]
            self.weight_error[idx] = 0


if __name__ == '__main__':
    all_input = [
        [0, 0],
        [0, 1],
        [1, 0],
        [1, 1]
    ]

    correct_input = [0, 0, 0, 1]

    neuron = Neuron()

    for i in range(40000):
        for j in range(4):
            neuron.learn(all_input[j], correct_input[j])
        neuron.fix()

        if (i + 1) % 1000 == 0:
            print("-----------Learn %d times-----------" % (i+1))
            for j in range(4):
                print("%d %d : %f" % (all_input[j][0], all_input[j][1], neuron.work(all_input[j])))
