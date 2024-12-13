from unittest import TestCase

from lib.input import clean_input
from main import solve_part_one, solve_part_two

class Test(TestCase):
    def test_solve_part_one_simple(self):
        lines = clean_input('''
                AAAA
                BBCD
                BBCC
                EEEC
                ''')

        expected = 140
        actual = solve_part_one(lines)

        self.assertEqual(expected, actual)

    def test_solve_part_one_example(self):
        lines = clean_input('''
                RRRRIICCFF
                RRRRIICCCF
                VVRRRCCFFF
                VVRCCCJFFF
                VVVVCJJCFE
                VVIVCCJJEE
                VVIIICJJEE
                MIIIIIJJEE
                MIIISIJEEE
                MMMISSJEEE
                ''')

        expected = 1930
        actual = solve_part_one(lines)

        self.assertEqual(expected, actual)


    def test_solve_part_two(self):
        lines = clean_input('''
                0000
                0000
                0000
                0000
                ''')

        expected = 2
        actual = solve_part_two(lines)

        self.assertEqual(expected, actual)
