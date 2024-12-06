from unittest import TestCase

from lib.input import clean_input
from main import solve_part_1, solve_part_2


class Test(TestCase):
    def test_solve_part_1_example(self):
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
        actual = solve_part_1(input_lines)

        self.assertEqual(expected, actual)

    def test_solve_part_2_example(self):
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

        expected = 6
        actual = solve_part_2(input_lines)

        self.assertEqual(expected, actual)

    def test_solve_part_2_no_loops_possible(self):
        input_lines: list[str] = clean_input('''
                #...
                ...#
                ....
                ^.#.
                
                ''')

        expected = 0
        actual = solve_part_2(input_lines)

        self.assertEqual(expected, actual)

    def test_solve_part_2_exactly_one_loop(self):
        input_lines: list[str] = clean_input('''
                ###..
                ....#
                .....
                .....
                ^..#.

                ''')

        expected = 1
        actual = solve_part_2(input_lines)

        self.assertEqual(expected, actual)

    def test_solve_part_2_exactly_one_loop_top_corner(self):
        input_lines: list[str] = clean_input('''
                .##..
                ....#
                .....
                .#...
                ^..#.

                ''')

        expected = 1
        actual = solve_part_2(input_lines)

        self.assertEqual(expected, actual)

    def test_solve_part_2_exactly_one_loop_right_edge(self):
        input_lines: list[str] = clean_input('''
                #####
                .....
                .....
                #.<..
                ...##
                ''')

        expected = 1
        actual = solve_part_2(input_lines)

        self.assertEqual(expected, actual)

    def test_solve_part_2_tiny(self):
        input_lines: list[str] = clean_input('''
                ###
                #<.
                ###
                ''')

        expected = 1
        actual = solve_part_2(input_lines)

        self.assertEqual(expected, actual)