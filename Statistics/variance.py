from Calculator.square import square
from Calculator.division import division


def variance(data):
    try:
        num_values = len(data)
        total = 0
        for i in data:
            total = total + square(i)
        return division(num_values - 1, total)
    except ZeroDivisionError:
        print("ERROR: Can't divide by zero")
    except ValueError:
        print("ERROR: Check your input value")
    except IndexError:
        print("List is empty")
