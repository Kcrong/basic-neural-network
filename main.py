from string import ascii_lowercase
from random import random, choice


def randomkey(length):
    return ''.join(choice(ascii_lowercase) for _ in range(length))


class Neuron:
    def __init__(self, name):
        # Private Var
        self._next = list()
        self._weight = dict()
        self.data = None
        if name is None:
            name = randomkey(5)
        self.name = name

    def link_neuron(self, next_neuron, weight=None):
        self._next.append(next_neuron)
        if not weight:
            weight = random()
        self._weight[next_neuron] = weight

    def __repr__(self):
        return "<Neuron %s>" % self.data

    def go_next(self):
        for next_neuron in self._next:
            next_data = self.data * self._weight[next_neuron]

            if next_neuron.data:
                next_neuron.data += next_data
            else:
                next_neuron.data = next_data


class InputNeuron(Neuron):
    all_neuron = list()

    def __init__(self, name=None):
        super().__init__(name)
        InputNeuron.all_neuron.append(self)

    def __repr__(self):
        return "<InputNeuron %s>" % self.name

    @classmethod
    def set_init_data(cls, data_list):
        if len(cls.all_neuron) != len(data_list):
            print("Input Error Diff length")
            return False

        OutputNeuron.reset()

        for neuron, data in zip(cls.all_neuron, data_list):
            neuron.data = data

    @classmethod
    def work(cls):
        for neuron in cls.all_neuron:
            neuron.go_next()


class OutputNeuron(Neuron):
    all_neuron = list()

    def __init__(self, name=None):
        super().__init__(name)
        OutputNeuron.all_neuron.append(self)

    @classmethod
    def reset(cls):
        for neuron in cls.all_neuron:
            neuron.data = None

    @classmethod
    def get_result(cls):
        return max(cls.all_neuron, key=lambda x: x.data)

    def __repr__(self):
        return "<OutputNeuron %s>" % self.name


if __name__ == '__main__':

    # Make Neuron Object list
    # Two Input Neuron (0, 1)
    # Two Output Neuron (0, 1)
    input_neuron_list = [InputNeuron() for i in range(2)]
    output_neuron_list = [OutputNeuron(i) for i in [0, 1]]

    # Link All Neuron
    for input_neuron in input_neuron_list:
        for output_neuron in output_neuron_list:
            # Set Random weight of links
            input_neuron.link_neuron(output_neuron)

    inputdata = [
        [0, 0],
        [0, 1],
        [1, 0],
        [1, 1]
    ]

    for data in inputdata:
        InputNeuron.set_init_data(data)
        InputNeuron.work()
        result = OutputNeuron.get_result()
        print(data, result)
