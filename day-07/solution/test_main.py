from unittest import TestCase

from lib.input import clean_input
from main import solve_part_one

class Test(TestCase):
    def test_solve(self):
        input_str = clean_input('''
        190: 10 19
        3267: 81 40 27
        83: 17 5
        156: 15 6
        7290: 6 8 6 15
        161011: 16 10 13
        192: 17 8 14
        21037: 9 7 18 13
        292: 11 6 16 20
        ''')

        expected = 3749
        actual = solve_part_one(input_str)

        self.assertEqual(expected, actual)
