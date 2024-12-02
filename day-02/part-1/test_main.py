from unittest import TestCase
from main import evaluate_report

class Test(TestCase):
    def test_case_1(self):
        report = "7 6 4 2 1"

        result = evaluate_report(report)
        self.assertEqual(True, result)

    def test_case_2(self):
        report = "1 2 7 8 9"

        result = evaluate_report(report)
        self.assertEqual(False, result)

    def test_case_3(self):
        report = "9 7 6 2 1"

        result = evaluate_report(report)
        self.assertEqual(False, result)

    def test_case_4(self):
        report = "1 3 2 4 5"

        result = evaluate_report(report)
        self.assertEqual(False, result)

    def test_case_5(self):
        report = "8 6 4 4 1"

        result = evaluate_report(report)
        self.assertEqual(False, result)

    def test_case_6(self):
        report = "1 3 6 7 9"

        result = evaluate_report(report)
        self.assertEqual(True, result)

    def test_min_increasing(self):
        report = "74 76 78 79 80"

        result = evaluate_report(report)
        self.assertEqual(True, result)

    def test_max_increasing(self):
        report = "80 83 86 89 92"

        result = evaluate_report(report)
        self.assertEqual(True, result)

    def test_min_decreasing(self):
        report = "80 79 78 77 76"

        result = evaluate_report(report)
        self.assertEqual(True, result)

    def test_max_decreasing(self):
        report = "90 87 84 81 78"

        result = evaluate_report(report)
        self.assertEqual(True, result)

    def test_increasing_decreasing(self):
        report = "74 76 78 79 76"

        result = evaluate_report(report)
        self.assertEqual(False, result)

    def test_same(self):
        report = "80 80 80 80 80"

        result = evaluate_report(report)
        self.assertEqual(False, result)