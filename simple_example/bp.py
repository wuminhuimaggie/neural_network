#-*-coding:utf-8-*-

import numpy as np

class FullyConnect:
    #l_x: input length l_y: output length
    def __init__(self, l_x, l_y) :
        self.weights = np.random.randn(l_y, l_x) # random init
        self.bias = np.random.randn(2, 1)

    def forward(self, x):
        self.x = x
        self.y = np.dot(self.weights, x) + self.bias #W * A + b
        return self.y

    def backward(self, d):
        self.dw = d * self.x
        self.db = d
        self.dx = d * self.weights

        return self.dw, self.db

class Sigmoid:
    def __init__(self):
        pass

    def sigmoid(self, x):
        return 1 / ( 1 + np.exp(-x))

    def forward(self, x):
        self.x = x
        self.y = self.sigmoid(x)
        return self.y

    def backward(self):
        sig = self.sigmoid(self.x)
        self.dx = sig * (1 - sig)
        return self.dx

def main():
    fc = FullyConnect(2, 2)
    sigmoid = Sigmoid()
    x = np.array([[1], [2]])

    print 'weights: ' ,fc.weights, ' bias: ', fc.bias, ' input: ', x

    #forward
    y1 = fc.forward(x)
    y2 = sigmoid.forward(y1)

    print 'forward result: ', y2

    #backward
    d1 = sigmoid.backward()
    dx = fc.backward(d1)

    print 'backward result: ', dx

if __name__ == '__main__':
    main()