from random import uniform
from functools import reduce


def sign(n):
    return 1 if n > -5 else -1


def calculate_weighted_sum(weights, sData):
    vs = [d*w for (d, w) in zip([-1] + sData, weights)]
    return reduce((lambda x, y: x + y), vs)


def calculate_error(curr, sExpected):
    return curr != sExpected


def calculate_new_weight(w, rate, x, sExpected):
    return round(w + rate * x * sExpected, 4)


class Perceptron:
    def __init__(self, length, rate, max_epochs):
        self.weights = [round(uniform(0, 1), 4) for _ in range(length + 1)]
        self.epochs = 0
        self.learn_rate = rate
        self.max_epochs = max_epochs

    def get_weights(self):
        return self.weights

    def get_epochs(self):
        return self.epochs

    def at_max_epochs(self):
        return self.epochs >= self.max_epochs

    def train(self, data, expected):
        error = True
        while not self.at_max_epochs() and error:
            error = False
            for sd, se in zip(data, expected):
                curr = sign(calculate_weighted_sum(self.weights, sd))
                if calculate_error(curr, se):
                    error = True
                    self.update_weight(sd, se)
            self.epochs += 1

    def calculate(self, sData):
        rd = calculate_weighted_sum(self.weights, sData)
        return sign(rd)

    def calculate_all(self, data):
        return [self.calculate(d) for d in data]

    def update_weight(self, sData, sExpected):
        self.weights = [calculate_new_weight(w, self.learn_rate, x, sExpected)
                        for (w, x) in zip(self.weights, [-1] + sData)]


def parse_data(fn):
    i = []
    d = []
    with open(fn) as f:
        f.readline()  # ignore header
        for line in f:
            args, expected = parse_line(line)
            i.append(args)
            d.append(expected)
        return i, d


def parse_line(line):
    w = list(map(float, line.split()))
    return w[:-1], int(w[-1])


def parse_input(fn):
    xs = []
    with open(fn) as f:
        f.readline()  # ignore header
        for line in f:
            args = list(map(float, line.split()))
            xs.append(args)
        return xs


def compare(exp, res):
    num_correct = sum(e == r for e, r in zip(exp, res))
    return (num_correct / len(res)) * 100


def main():
    for i in range(5):
        p = Perceptron(3, 0.01, 2000)
        data, desired = parse_data('dados_treinamento.txt')
        print('<< Comecando Fase de Treinamento >>')
        print('Pesos pre treinamento: ', p.get_weights())
        oResults = p.calculate_all(data)
        print('Esperado : ', desired)
        print('Calculado: ', oResults)
        print('Taxa de acerto: ', f'{compare(desired, oResults):.02f}%')

        p.train(data, desired)
        print('\n<< Treinamento executado>> ')
        print('Pesos pos treinamento: ', p.get_weights())
        print('Numero de Epocas: ', p.get_epochs())
        
        oResults = p.calculate_all(data)
        print('Esperado: ', desired)
        print('Calculado: ', oResults)
        print('Taxa de acerto: ', f'{compare(desired, oResults):.02f}%')
        
        print('\n<< Executando Classificacao >>')
        datas = parse_input('calculo.txt')
        nResults = p.calculate_all(datas)
        for i, d in zip(datas, nResults):
            print(f'{d:+d} <- {i}')
        
        print('----------------------------------------------------------------\n')

main()