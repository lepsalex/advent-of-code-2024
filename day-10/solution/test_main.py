from unittest import TestCase

from lib.input import clean_input
from main import solve_part_one


class Test(TestCase):
    def test_solve_part_one(self):
        lines = clean_input('''
                89010123
                78121874
                87430965
                96549874
                45678903
                32019012
                01329801
                10456732
                ''')

        expected = 36
        actual = solve_part_one(lines)

        self.assertEqual(expected, actual)

    def test_solve_part_one_small_example(self):
        lines = clean_input('''
                0123
                1234
                8765
                9876
                ''')

        expected = 1
        actual = solve_part_one(lines)

        self.assertEqual(expected, actual)

    def test_solve_part_one_medium_example(self):
        lines = clean_input('''
                9990999
                9991999
                9992999
                6543456
                7111117
                8111118
                9111119
                ''')

        expected = 2
        actual = solve_part_one(lines)

        self.assertEqual(expected, actual)