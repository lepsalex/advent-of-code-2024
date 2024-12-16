from unittest import TestCase

from lib.input import clean_input
from main import solve_part_one, solve_part_two

class Test(TestCase):
    def test_solve_part_one(self):
        lines = clean_input('''
                Button A: X+94, Y+34
                Button B: X+22, Y+67
                Prize: X=8400, Y=5400
                
                Button A: X+26, Y+66
                Button B: X+67, Y+21
                Prize: X=12748, Y=12176
                
                Button A: X+17, Y+86
                Button B: X+84, Y+37
                Prize: X=7870, Y=6450
                
                Button A: X+69, Y+23
                Button B: X+27, Y+71
                Prize: X=18641, Y=10279
                ''')

        expected = 480
        actual = solve_part_one(lines)

        self.assertEqual(expected, actual)

    def test_solve_part_two(self):
        lines = clean_input('''
                Button A: X+94, Y+34
                Button B: X+22, Y+67
                Prize: X=8400, Y=5400

                Button A: X+26, Y+66
                Button B: X+67, Y+21
                Prize: X=12748, Y=12176

                Button A: X+17, Y+86
                Button B: X+84, Y+37
                Prize: X=7870, Y=6450

                Button A: X+69, Y+23
                Button B: X+27, Y+71
                Prize: X=18641, Y=10279
                ''')

        expected = 875318608908
        actual = solve_part_two(lines)

        self.assertEqual(expected, actual)
