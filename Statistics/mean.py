from Calculator.division import division
from Calculator.addition import addition


def mean(data):
    try:
        num_values = len(data)
        total = 0
        for num in data:
            total = addition(total, num)
        return round(division(num_values, total), 9)
    except ZeroDivisionError:
        print("ERROR: Can't divide by zero")
    except ValueError:
        print("ERROR: Check your input value")
    except IndexError:
        print("List is empty")
