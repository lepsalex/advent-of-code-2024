from unittest import TestCase
from main import solve

class Test(TestCase):
    def test_solve(self):
        expected = 1
        actual = solve()

        self.assertEqual(expected, actual)
