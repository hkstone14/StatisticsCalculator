from Calculator.addition import addition
from Calculator.subtraction import subtraction
from Calculator.sqaureroot import squareroot


class Calculator:
    result = 0

    def __init__(self):
        pass

    def add(self, a, b):
        a = int(a)
        b = int(b)
        self.result = addition(a, b)
        return self.result

    def sub(self, a, b):
        a = int(a)
        b = int(b)
        self.result = subtraction(a, b)
        return self.result

    def squareroot(self, a):
        a = float(a)
        temp = 0
        temp = squareroot(a)
        self.result = float('%.10g' % temp)
        return self.result
