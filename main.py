class Neuron:
    def __init__(self):

        # Inner Var
        self._next = None
        self._previous = None
        self._weight = dict()

        # Public Var
        self.data = None


class InputNeuron(Neuron):
    def __repr__(self):
        return "<InputNeuron %s>" % self.data


class OutputNeuron(Neuron):
    def __repr__(self):
        return "<OutputNeuron %s>" % self.data
