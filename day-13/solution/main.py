import re

from lib.input import get_input_lines


def main():
    lines = get_input_lines(__file__)

    return solve_part_one(lines), solve_part_two(lines)


def solve_part_one(lines: list[str]):
    results = [solve_block(block) for block in get_blocks(lines)]

    return sum([x for x in results if x is not None])


def solve_part_two(lines: list[str]):
    results = [solve_block(block, 10000000000000) for block in get_blocks(lines)]

    return sum([x for x in results if x is not None])


def solve_block(block: list[int], p: int = 0):
    ax, ay, bx, by, px, py = block
    px = px + p
    py = py + p
    ca = (px * by - py * bx) / (ax * by - ay * bx)
    cb = (px - ax * ca) / bx

    if ca % 1 == cb % 1 == 0:
        return int(ca * 3 + cb)
    else:
        return None


def get_blocks(lines: list[str]):
    return [parse_block(lines[x:x + 3]) for x in range(0, len(lines), 4)]


def parse_block(lines: list[str]):
    num_regex = re.compile("\\d+")
    return [int(x) for x in num_regex.findall(" ".join(lines))]


if __name__ == '__main__':
    result = main()
    print(result)
