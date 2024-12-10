from unittest import TestCase
from main import solve_part_one, solve_part_two

class Test(TestCase):
    def test_solve_part_one(self):
        input_str = "2333133121414131402"

        expected = 1928
        actual = solve_part_one(input_str)

        self.assertEqual(expected, actual)

    def test_solve_part_two(self):
        input_str = "2333133121414131402"

        expected = 2858
        actual = solve_part_two(input_str)

        self.assertEqual(expected, actual)
