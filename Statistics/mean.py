from Calculator.division import division
from Calculator.addition import addition


# 49.8

def mean(data):
    try:
        num_values = len(data)
        total = 0
        for num in data:
            total = addition(total, num)
       #total = sum(data)
        return round(division(num_values, total), 9)
    except ZeroDivisionError:
        print("ERROR: Can't divide by zero")
    except ValueError:
        print("ERROR: Check your input value")
