from unittest import TestCase

from lib.input import clean_input
from main import solve_part_one, solve_part_two

class Test(TestCase):
    def test_solve_part_one(self):
        lines = clean_input('''
                p=0,4 v=3,-3
                p=6,3 v=-1,-3
                p=10,3 v=-1,2
                p=2,0 v=2,-1
                p=0,0 v=1,3
                p=3,0 v=-2,-2
                p=7,6 v=-1,-3
                p=3,0 v=-1,-2
                p=9,3 v=2,3
                p=7,3 v=-1,2
                p=2,4 v=2,-3
                p=9,5 v=-3,-3
                ''')

        expected = 12
        actual = solve_part_one(lines, 11, 7)

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
