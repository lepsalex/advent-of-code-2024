from unittest import TestCase

from lib.input import clean_input
from main import search, get_search_vectors


class Test(TestCase):
    def test_search_simple(self):
        input_str = clean_input('''
                XMAS
                XMAS
                XMAS
                XMAS
                ''')

        actual = search(input_str)
        expected = 6

        self.assertEqual(expected, actual)

    def test_search_provided_example(self):
        input_str = clean_input('''
        MMMSXXMASM
        MSAMXMSMSA
        AMXSXMAAMM
        MSAMASMSMX
        XMASAMXAMM
        XXAMMXXAMA
        SMSMSASXSS
        SAXAMASAAA
        MAMMMXMMMM
        MXMXAXMASX
        ''')

        actual = search(input_str)
        expected = 18

        self.assertEqual(expected, actual)

    def test_get_search_vectors(self):
        start_pos = (0, 0)
        length = 4
        grid_size = 4

        actual = get_search_vectors(start_pos, length, grid_size)
        expected = [
            (1, 0),  # right
            (1, 1),  # down-right
            (0, 1),  # down
        ]

        self.assertSetEqual(set(expected), set(actual))
