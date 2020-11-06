import unittest
from pprint import pprint

from Statistics.Statistics import Statistics
from CSVReader.CSVReader import CsvReader


class MyTestCase(unittest.TestCase):
    test_result = CsvReader("./Data/result.csv").data

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


if __name__ == '__main__':
    unittest.main()
