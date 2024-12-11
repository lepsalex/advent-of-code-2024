from unittest import TestCase

from lib.input import clean_input
from main import solve_part_one, solve_part_two


class Test(TestCase):
    def test_solve_part_one(self):
        stones = ["125", "17"]

        expected = 55312
        actual = solve_part_one(stones)

        self.assertEqual(expected, actual)

    def test_solve_part_two(self):
        stones = ["125", "17"]

        expected = 55312
        actual = solve_part_two(stones)

        self.assertEqual(expected, actual)
