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
        test_data_add = CsvReader("Test/Data/addition.csv").data
        for row in test_data_add:
            result = int(row['Result'])
            self.assertEqual(self.calculator.add(row['Value 1'], row['Value 2']), result)
            self.assertEqual(self.calculator.result, result)

    def test_sub_method_calculator(self):
        test_data_sub = CsvReader("Test/Data/subtraction.csv").data
        for row in test_data_sub:
            result = int(row['Result'])
            self.assertEqual(self.calculator.sub(row['Value 1'], row['Value 2']), result)
            self.assertEqual(self.calculator.result, result)

    def test_squareRoot_method_calculator(self):
        test_data_sqrt = CsvReader("Test/Data/sqroot.csv").data
        for row in test_data_sqrt:
            result = float(row['Result'])
            self.assertEqual(self.calculator.squareroot(row['Value 1']), result)
            self.assertEqual(self.calculator.result, result)

    def test_div_method_calculator(self):
        test_data_div = CsvReader("Test/Data/division.csv").data
        for row in test_data_div:
            result = float(row['Result'])
            self.assertEqual(self.calculator.div(row['Value 1'], row['Value 2']), float(row['Result']))
            self.assertEqual(self.calculator.result, float(row['Result']))

    def test_mul_method_calculator(self):
        test_data_mul = CsvReader("Test/Data/multiplication.csv").data
        for row in test_data_mul:
            result = int(row['Result'])
            self.assertEqual(self.calculator.mul(row['Value 1'], row['Value 2']), int(row['Result']))
            self.assertEqual(self.calculator.result, int(row['Result']))

    def test_square_method_calculator(self):
        test_data_sqr = CsvReader("Test/Data/square.csv").data
        for row in test_data_sqr:
            result = float(row['Result'])
            self.assertEqual(self.calculator.square(row['Value 1']), result)
            self.assertEqual(self.calculator.result, result)


if __name__ == '__main__':
    unittest.main()
