from Statistics.variance import variance
from Calculator.sqaureroot import squareroot


def standard_deviation(data):
    try:
        variance_result = variance(data)
        return round(squareroot(variance_result), 5)
    except ZeroDivisionError:
        print("ERROR: Can't divide by zero")
    except ValueError:
        print("ERROR: Check your input value")
    except IndexError:
        print("List is empty")