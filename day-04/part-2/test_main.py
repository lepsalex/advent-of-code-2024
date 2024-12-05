from unittest import TestCase
from main import search


class Test(TestCase):
    def test_search_simple(self):
        input_str = self.clean_input('''
                M.S
                .A.
                M.S
                ''')

        actual = search(input_str)
        expected = 1

        self.assertEqual(expected, actual)

    def test_search_provided_example(self):
        input_str = self.clean_input('''
        .M.S......
        ..A..MSMS.
        .M.S.MAA..
        ..A.ASMSM.
        .M.S.M....
        ..........
        S.S.S.S.S.
        .A.A.A.A..
        M.M.M.M.M.
        ..........
        ''')

        actual = search(input_str)
        expected = 9

        self.assertEqual(expected, actual)

    @staticmethod
    def clean_input(input_str: str) -> list[str]:
        return [line.strip() for line in input_str.strip().split()]
