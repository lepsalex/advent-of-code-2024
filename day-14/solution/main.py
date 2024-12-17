import re
from functools import reduce
from operator import mul

from lib.input import get_input_lines
from itertools import groupby, product


def main():
    lines = get_input_lines(__file__)

    return solve_part_one(lines, 101, 103), solve_part_two(lines)


def solve_part_one(lines: list[str], w: int, h: int, steps=100):
    quad_func = to_quad_func(w, h)
    pos_vel = map(parse_line, lines)
    updated_positions = [compute_pos(pv, w, h, steps) for pv in pos_vel]
    quads = map(quad_func, updated_positions)
    quads_agg = {k: len(list(v)) for (k, v) in groupby(sorted(quads)) if k != 0}

    return reduce(mul, quads_agg.values(), 1)


def parse_line(line: str) -> [int, int, int, int]:
    num_regex = re.compile("-?\\d+")
    return [int(x) for x in num_regex.findall(line)]


def compute_pos(pv: [int, int, int, int], w: int, h: int, steps=100):
    px, py, vx, vy = pv

    x = (px + vx * steps) % w
    y = (py + vy * steps) % h

    return x, y


def to_quad_func(w: int, h: int):
    hm = (w - 1) // 2
    vm = (h - 1) // 2

    def to_quad(pos: (int, int)):
        x, y = pos

        if x < hm and y < vm:
            return 1
        if x > hm and y < vm:
            return 2
        if x < hm and y > vm:
            return 3
        if x > hm and y > vm:
            return 4

        return 0

    return to_quad


def solve_part_two(lines: list[str]):
    return 2


if __name__ == '__main__':
    result = main()
    print(result)
