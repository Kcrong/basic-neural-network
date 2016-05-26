from string import ascii_lowercase
from random import random, choice
from math import exp


def sigmoid(x):
    return 1.0 / (1.0 + exp(-x))


def randomkey(length):
    return ''.join(choice(ascii_lowercase) for _ in range(length))


class Neuron:
    def __init__(self, name):
        # Private Var
        self._next = list()  # 연결된 다음 뉴런을 저장할 list 변수
        self._weight = dict()  # 가중치 dict 변수
        self.data = None  # 이 뉴런의 데이터 합을 저장할 변수
        self.threshold = 0  # 역치값 (여기선 0으로 설정)
        if name is None:
            name = randomkey(5)
        self.name = name  # 식별을 위한 이름 설정

    def link_neuron(self, next_neuron, weight=None):
        """
        :param next_neuron: 연결할 뉴런
        :param weight: 연결할 뉴런과의 가중치
        """
        self._next.append(next_neuron)
        if not weight:
            weight = random()
        self._weight[next_neuron] = weight

    def __repr__(self):
        return "<Neuron %s>" % self.data

    def go_next(self):
        if self.data >= self.threshold:  # 역치값 비교 (역치값보다 데이터합이 작으면 다음 뉴런으로 전달하지 않음)
            for next_neuron in self._next:  # 자신과 연결된 모든 뉴런에서
                next_data = self.data * self._weight[next_neuron]  # 전달할 데이터 연산 (가중치 * 자신의 데이터)

                if next_neuron.data:  # 전달할 뉴런의 데이터가 None 이 아니면
                    next_neuron.data += next_data
                else:  # None 일 경우, 전달 데이터로 초기화
                    next_neuron.data = next_data
        else:
            pass


class InputNeuron(Neuron):
    all_neuron = list()  # 모든 InputNeuron 객체를 저장할 리스트

    def __init__(self, name=None):
        super().__init__(name)  # 부모 클래스의 생성자 호출 (인자로 받은 name 전달)
        InputNeuron.all_neuron.append(self)  # 객체 생성 시 InputNeuron 클래스의 all_neuron 리스트에 객체 추가

    def __repr__(self):
        return "<InputNeuron %s>" % self.name

    @classmethod
    def set_init_data(cls, data_list):  # 처음 입력 데이터 설정
        if len(cls.all_neuron) != len(data_list):  # 데이터 길이와 입력 뉴런 길이가 다를 경우 에러
            print("Input Error Diff length")
            return False

        OutputNeuron.reset()  # 출력뉴런의 데이터 초기화

        for neuron, data in zip(cls.all_neuron, data_list):
            neuron.data = data  # 입력뉴런 데이터 초기화

    @classmethod
    def work(cls):  # 모든 입력 뉴런 데이터 전달
        for neuron in cls.all_neuron:
            neuron.go_next()


class OutputNeuron(Neuron):
    all_neuron = list()

    def __init__(self, name=None):
        super().__init__(name)
        OutputNeuron.all_neuron.append(self)

    @classmethod
    def reset(cls):  # OutputNeuron 의 데이터 초기화
        for neuron in cls.all_neuron:
            neuron.data = None

    @classmethod
    def get_result(cls):  # OutputNeuron 중에 가장 데이터가 큰 Neuron 을 반환
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

    inputdata = [  # 입력할 데이터 생성
        [0, 0],
        [0, 1],
        [1, 0],
        [1, 1]
    ]

    for data in inputdata:
        InputNeuron.set_init_data(data)  # 입력뉴런에 데이터 설정
        InputNeuron.work()  # 다음 뉴런으로 데이터 전달
        result = OutputNeuron.get_result()  # 출력 뉴런 중에 가장 큰 뉴런 결과로 가져옴
        print(data, result)  # 결과 출력
