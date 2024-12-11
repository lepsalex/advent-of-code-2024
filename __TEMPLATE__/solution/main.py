from lib.input import get_input_lines


def main():
    lines = get_input_lines(__file__)

    return solve_part_one(lines), solve_part_two(lines)


def solve_part_one(lines: list[str]):
    return 1


def solve_part_two(lines: list[str]):
    return 2


if __name__ == '__main__':
    result = main()
    print(result)
