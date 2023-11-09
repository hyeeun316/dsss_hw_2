import unittest
from math_quiz import pickRandomInteger, choiceOperator, calculateFormula


class TestMathGame(unittest.TestCase):

    def TestPickRandomInteger(self):
        # Test if random numbers generated are within the specified range
        min_val = 1
        max_val = 10
        for _ in range(1000):  # Test a large number of random values
            rand_num = pickRandomInteger(min_val, max_val)
            self.assertTrue(min_val <= rand_num <= max_val)

    def TestChoiceOperator(self):
        # Test if ramdom operator generated is in the operator list (+, -, *)
        operator_list = ['+', '-', '*']
        for _ in range(1000):
             operator = choiceOperator()
             self.assertTrue(operator in operator_list)

    def TestCalculateFormula(self):
            # Test if the calculation of the test cases is correct
            test_cases = [
                (5, 2, '+', '5 + 2', 7),
                (4, 2, '*', '4 * 2', 8),
                (9, 5, '-', '9 - 5', 4),
                (6, 4, '*', '6 * 4', 24),
                (9, 1, '*', '9 * 1', 9),
                (4, 4, '-', '4 - 2', 0),
                (5, 1, '+', '4 * 2', 6),
                (7, 3, '*', '7 * 3', 21),
                (7, 2, '-', '7 * 2', 5),
                (8, 2, '+', '8 + 2', 10)
            ]

            for num1, num2, operator, expected_problem, expected_answer in test_cases:
                 self.assertTrue(expected_problem, expected_answer == calculateFormula(num1, num2, operator))

if __name__ == "__main__":
    unittest.main()