from unittest import TestCase
from main import evaluate

class Test(TestCase):
    def test_case_1(self):
        report = "7 6 4 2 1"

        result = evaluate(report)
        self.assertEqual(result, True)

    def test_case_2(self):
        report = "1 2 7 8 9"

        result = evaluate(report)
        self.assertEqual(result, False)

    def test_case_3(self):
        report = "9 7 6 2 1"

        result = evaluate(report)
        self.assertEqual(result, False)

    def test_case_4(self):
        report = "1 3 2 4 5"

        result = evaluate(report)
        self.assertEqual(result, True)

    def test_case_5(self):
        report = "8 6 4 4 1"

        result = evaluate(report)
        self.assertEqual(result, True)

    def test_case_6(self):
        report = "1 3 6 7 9"

        result = evaluate(report)
        self.assertEqual(result, True)