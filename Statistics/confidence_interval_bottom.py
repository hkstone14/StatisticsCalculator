from Calculator.sqaureroot import squareroot
from Statistics.standard_deviation import standard_deviation
from Statistics.mean import mean


def confidence_interval_bottom(data):
    try:
        num_values = len(data)
        z = 1.96
        std_dev = standard_deviation(data)
        mean_result = mean(data)
        return round(mean_result - (z * std_dev / squareroot(num_values)), 5)
    except ZeroDivisionError:
        print("ERROR: Can't divide by zero")
    except ValueError:
        print("ERROR: Check your input value")
    except IndexError:
        print("List is empty")
