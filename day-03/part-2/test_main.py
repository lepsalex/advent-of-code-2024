from unittest import TestCase
from main import process

class Test(TestCase):
    def test_process(self):
        data = "xmul(2,4)&mul[3,7]!^don't()_mul(5,5)+mul(32,64](mul(11,8)undo()?mul(8,5))"
        actual = process(data)
        self.assertEqual(48, actual)
