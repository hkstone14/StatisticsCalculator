import unittest
from pprint import pprint

from Statistics.Statistics import Statistics
from CSVReader.CSVReader import CsvReader


class MyTestCase(unittest.TestCase):
    test_result = CsvReader("Test/Data/result.csv").data

    def setUp(self) -> None:
        self.statistics = Statistics()

    def test_instantiate_calculator(self):
        self.assertIsInstance(self.statistics, Statistics)

    def test_mean(self):
        sample_data = CsvReader("Test/Data/mean.csv").data
        mean_data = [int(row['Value']) for row in sample_data]
        for row in self.test_result:
            result = float(row["mean"])
        self.assertEqual(self.statistics.stat_mean(mean_data), result)
        self.assertEqual(self.statistics.result, result)

    def test_variance(self):
        sample_data = CsvReader("Test/Data/variance.csv").data
        variance_data = [float(row['Value']) for row in sample_data]
        for row in self.test_result:
            result = float(row["variance"])
        self.assertEqual(self.statistics.stat_variance(variance_data), result)
        self.assertEqual(self.statistics.result, result)

    def test_standard_deviation(self):
        sample_data = CsvReader("Test/Data/std-dev.csv").data
        std_dev_data = [float(row['Value']) for row in sample_data]
        for row in self.test_result:
            result = float(row["std-dev"])
        self.assertEqual(self.statistics.stat_standard_deviation(std_dev_data), result)
        self.assertEqual(self.statistics.result, result)

    def test_confidence_interval(self):
        sample_data = CsvReader("Test/Data/confidence_Interval.csv").data
        con_int = [float(row['Value']) for row in sample_data]
        for row in self.test_result:
            CI_bottom_result = float(row["CI-bottom"])
            CI_top_result = float(row["CI-top"])
        self.assertEqual(self.statistics.stat_confidence_interval_top(con_int), CI_top_result)
        self.assertEqual(self.statistics.stat_confidence_interval_bottom(con_int), CI_bottom_result)


if __name__ == '__main__':
    unittest.main()
