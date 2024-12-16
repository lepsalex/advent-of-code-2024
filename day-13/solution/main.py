import re

from lib.input import get_input_lines


def main():
    lines = get_input_lines(__file__)

    return solve_part_one(lines), solve_part_two(lines)


def solve_part_one(lines: list[str]):
    results = [solve_block(block) for block in get_blocks(lines)]

    return sum([x for x in results if x != float('inf')])


def solve_part_two(lines: list[str]):
    return 2


def solve_block(block: list[int]):
    ax, ay, bx, by, px, py = block

    min_score = float("inf")

    for a in range(101):
        for b in range(101):
            if a * ax + b * bx == px and a * ay + b * by == py:
                min_score = min(min_score, a * 3 + b * 1)

    return min_score


def get_blocks(lines: list[str]):
    return [parse_block(lines[x:x + 3]) for x in range(0, len(lines), 4)]


def parse_block(lines: list[str]):
    num_regex = re.compile("\d+")
    return [int(x) for x in num_regex.findall(" ".join(lines))]


if __name__ == '__main__':
    result = main()
    print(result)
