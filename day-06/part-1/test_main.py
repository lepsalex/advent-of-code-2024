from unittest import TestCase

from lib.input import clean_input
from main import solve

class Test(TestCase):
    def test_solve(self):
        input_lines: list[str] = clean_input('''
                ....#.....
                .........#
                ..........
                ..#.......
                .......#..
                ..........
                .#..^.....
                ........#.
                #.........
                ......#...
                ''')

        expected = 41
        actual = solve(input_lines)

        self.assertEqual(expected, actual)
