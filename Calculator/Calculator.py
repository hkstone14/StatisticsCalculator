from addition import addition
from subtraction import subtraction


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
