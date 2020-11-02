import unittest

from Calculator.Calculator import Calculator
from CSVReader.CSVReader import CsvReader


class MyTestCase(unittest.TestCase):
    def setUp(self) -> None:
        self.calculator = Calculator()

    def test_instantiate_calculator(self):
        self.assertIsInstance(self.calculator, Calculator)

    def test_results_property_calculator(self):
        self.assertEqual(self.calculator.result, 0)

    def test_add_method_calculator(self):
        test_data_add = CsvReader("./Data/addition.csv").data
        for row in test_data_add:
            result = int(row['Result'])
            self.assertEqual(self.calculator.add(row['Value 1'], row['Value 2']), result)
            self.assertEqual(self.calculator.result, result)

    def test_sub_method_calculator(self):
        test_data_sub = CsvReader("./Data/subtraction.csv").data
        for row in test_data_sub:
            result = int(row['Result'])
            self.assertEqual(self.calculator.sub(row['Value 1'], row['Value 2']), result)
            self.assertEqual(self.calculator.result, result)

    def test_squareRoot_method_calculator(self):
        test_data_sqrt = CsvReader("./Data/squareRoot.csv").data
        for row in test_data_sqrt:
            result = float(row['Result'])
            self.assertEqual(self.calculator.squareroot(row['Value 1']), result)
            self.assertEqual(self.calculator.result, result)

    def test_div_method_calculator(self):
        test_data_div = CsvReader("./Data/squareRoot.csv").data
        for row in test_data_div:
            result = float(row['Result'])
            self.assertEqual(self.calculator.div(row['Value 1'], row['Value 2']), float(row['Result']))
            self.assertEqual(self.calculator.result, float(row['Result']))


if __name__ == '__main__':
    unittest.main()
