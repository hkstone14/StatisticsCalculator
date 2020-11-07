from Statistics.mean import mean
from Calculator.Calculator import Calculator
from CSVReader.CSVReader import CsvReader
from Statistics.variance import variance
from Statistics.standard_deviation import standard_deviation
from Statistics.confidence_interval_bottom import confidence_interval_bottom
from Statistics.confidence_interval_top import confidence_interval_top
from Statistics.z_score import z_score
from Statistics.errorOfMargin import errorOfMargin
from Statistics.median import median1
from Statistics.mode import mode1


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

    def stat_median(self,data):
        self.result=median1(data)
        return self.result
