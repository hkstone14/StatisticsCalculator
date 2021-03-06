from Calculator.addition import addition
from Calculator.subtraction import subtraction
from Calculator.sqaureroot import squareroot
from Calculator.division import division
from Calculator.multiplication import multiplication
from Calculator.square import square


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

    def div(self, a, b):
        a = float(a)
        b = float(b)
        self.result = division(a, b)
        return self.result

    def mul(self, a, b):
        a = int(a)
        b = int(b)
        self.result = multiplication(a, b)
        return self.result

    def square(self, a):
        self.result = square(a)
        return self.result
