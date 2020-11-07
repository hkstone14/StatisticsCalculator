from Statistics.standard_deviation import standard_deviation
from Statistics.mean import mean
from Calculator.division import division
from pprint import pprint


def z_score(data):
    z_mean = mean(data)
    std_dev_result = standard_deviation(data)
    z_list = []
    for i in data:
        z = round(division(std_dev_result, (i-z_mean)), 5)
        z_list.append(z)
    return z_list


