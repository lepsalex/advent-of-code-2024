from lib.input import get_input_lines

def main():
    lines = get_input_lines(__file__)

    results = map(evaluate_report, lines)

    return sum(results)

def evaluate_report(report: str) -> bool:
    report_nums = [int(n) for n in report.split(' ')]

    # one of -1 negative, 0 neutral, 1 positive
    direction = 0

    for idx, num in enumerate(report_nums):
        if idx == 0:
            continue

        # evaluate absolute difference
        abs_diff = abs(num - report_nums[idx - 1])
        if abs_diff == 0 or abs_diff < 1 or abs_diff > 3:
            return False

        # get the diff direction
        diff = num - report_nums[idx - 1]
        diff_direction = get_diff_direction(diff)

        # the first time it's neutral, update with the direction
        if direction == 0:
            direction = diff_direction
            continue

        # check that the direction as not changed
        if diff_direction != direction:
            return False

    return True

def get_diff_direction(diff) -> int:
    return -1 if diff > 0 else 1

if __name__ == '__main__':
    result = main()
    print(result)
