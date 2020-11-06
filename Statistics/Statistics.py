from Statistics.mean import mean
from Calculator.Calculator import Calculator
from CSVReader.CSVReader import CsvReader


class Statistics(Calculator):
    data = []

    def __init__(self):
        super().__init__()

    def stat_mean(self, data):
        self.result = mean(data)
        return self.result
