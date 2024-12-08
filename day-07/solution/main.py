from itertools import product, zip_longest

from lib.input import get_input_lines


def main():
    lines = get_input_lines(__file__)

    return solve_part_one(lines), solve_part_two(lines)


def solve_part_one(lines: list[str]):
    operators = ["*", "+"]
    sum_total = 0

    for line in lines:
        test_case, numbers_str = line.split(": ")
        numbers = numbers_str.split(" ")

        operator_combinations = product(operators, repeat=len(numbers) - 1)

        for operator_combo in operator_combinations:
            num_idx = 0
            total = int(numbers[num_idx])

            for operator in operator_combo:
                num = int(numbers[num_idx + 1])

                if operator == '*':
                    total = total * num
                elif operator == '+':
                    total = total + num

                num_idx += 1

            if total == int(test_case):
                sum_total += total
                break

    return sum_total


def solve_part_two(lines: list[str]):
    operators = ["*", "+", "||"]
    sum_total = 0

    for line in lines:
        test_case, numbers_str = line.split(": ")
        numbers = numbers_str.split(" ")

        operator_combinations = product(operators, repeat=len(numbers) - 1)

        for operator_combo in operator_combinations:
            num_idx = 0
            total = int(numbers[num_idx])

            for operator in operator_combo:
                num = numbers[num_idx + 1]

                if operator == '*':
                    total = total * int(num)
                elif operator == '+':
                    total = total + int(num)
                elif operator == '||':
                    total = int(f"{total}{num}")

                num_idx += 1

            if total == int(test_case):
                sum_total += total
                break

    return sum_total


if __name__ == '__main__':
    result = main()
    print(result)
