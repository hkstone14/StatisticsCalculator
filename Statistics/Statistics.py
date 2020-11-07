from mean import mean
from Calculator import Calculator
from CSVReader.CSVReader import CsvReader
from variance import variance
from standard_deviation import standard_deviation
from confidence_interval_bottom import confidence_interval_bottom
from confidence_interval_top import confidence_interval_top
from z_score import z_score
from errorOfMargin import errorOfMargin
from mode import mode1
from median import  median1

class Statistics(Calculator):
    data = []

    def __init__(self):
        super().__init__()

    def stat_mean(self, data):
        self.result = mean(data)
        return self.result

    def stat_variance(self, data):
        self.result = variance(data)
        return self.result

    def stat_standard_deviation(self, data):
        self.result = standard_deviation(data)
        return self.result

    def stat_confidence_interval_top(self, data):
        self.result = confidence_interval_top(data)
        return self.result

    def stat_confidence_interval_bottom(self, data):
        self.result = confidence_interval_bottom(data)
        return self.result

    def stat_zscore(self, data):
        self.result = z_score(data)
        return self.result

    def stat_ErrorofMargin(self,data):
        self.result=errorOfMargin(data)
        return self.result

    def stat_mod(self,data):
        self.result=mode1(data)
        return self.result

    def stat_medin(self,data):
        self.result=median1(data)
        return self.result
