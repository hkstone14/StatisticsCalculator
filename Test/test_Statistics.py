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

    def test_zscore(self):
        sample_data = CsvReader("Test/Data/zscore.csv").data
        sample_z_score = [int(row['zscore']) for row in sample_data]
        zscore_answer = CsvReader("Test/Data/zscore_answer.csv").data
        zscore_result = [float(row['result']) for row in zscore_answer]
        self.assertEqual(self.statistics.stat_zscore(sample_z_score), zscore_result)
        self.assertEqual(self.statistics.result, zscore_result)

    def test_errorOfmargin(self):
        sample_data = CsvReader("Test/Data/errorOfMargin.csv").data
        for row in self.test_result:
            ErrorOfMargin_result = float(row["ErrorOfMargin"])
        self.assertEqual(self.statistics.stat_ErrorofMargin(sample_data), ErrorOfMargin_result)
        self.assertEqual(self.statistics.result, ErrorOfMargin_result)

    def test_mode(self):
        sample_data = CsvReader("Test/Data/mode.csv").data
        column1 = [float(raw['Value1']) for raw in sample_data]
        for row in self.test_result:
            Mode_result = float(row["mode"])
        self.assertEqual(self.statistics.stat_mode(column1), Mode_result)
        self.assertEqual(self.statistics.result, Mode_result)

    def test_median(self):
        sample_data = CsvReader("Test/Data/median.csv").data
        for row in self.test_result:
            Median_result = float(row["median"])
        self.assertEqual(self.statistics.stat_median(sample_data), Median_result)
        self.assertEqual(self.statistics.result, Median_result)

    def test_simpleRandomSampling(self):
        sample_data = CsvReader("Test/Data/SimpleRandomSampling.csv").data
        column1 = [int(raw['Value1']) for raw in sample_data]
        for row in self.test_result:
            SRS_result = int(row["SRS"])
        self.assertEqual(self.statistics.stat_Simplerandomsampling(column1), SRS_result)
        self.assertEqual(self.statistics.result, SRS_result)

    def test_cochrans(self):
        sample_data = CsvReader("Test/Data/cochrans.csv").data
        column1 = [float(raw['Value']) for raw in sample_data]
        for row in self.test_result:
            cochran_result = float(row["cochrans"])
        self.assertEqual(self.statistics.stat_cochrans(column1), cochran_result)
        self.assertEqual(self.statistics.result, cochran_result)

    def test_unknown_pop_std_dev(self):
        sample_data = CsvReader("Test/Data/unknow_pop_std_dev.csv").data
        column1 = [float(raw['Value']) for raw in sample_data]
        for row in self.test_result:
            Un_std_dev_result = float(row["Un_std_dev"])
        self.assertEqual(self.statistics.stat_unknown_population_std_dev(column1), Un_std_dev_result)
        self.assertEqual(self.statistics.result, Un_std_dev_result)


if __name__ == '__main__':
    unittest.main()
