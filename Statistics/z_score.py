from Statistics.standard_deviation import standard_deviation
from Statistics.mean import mean
from Calculator.division import division
from pprint import pprint


def z_score(data):
    try:
        z_mean = mean(data)
        std_dev_result = standard_deviation(data)
        z_list = []
        for i in data:
            z = round(division(std_dev_result, (i-z_mean)), 5)
            z_list.append(z)
        return z_list
    except IndexError:
        print("List is empty")
    except ZeroDivisionError:
        print("ERROR: Can't divide by zero")
    except ValueError:
        print("ERROR: Check your input value")


