from unittest import TestCase
from main import solve_part_one

class Test(TestCase):
    def test_solve_part_one(self):
        input_str = "2333133121414131402"

        expected = 1928
        actual = solve_part_one(input_str)

        self.assertEqual(expected, actual)
