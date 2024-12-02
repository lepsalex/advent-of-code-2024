from lib.input import get_input_lines


def main():
    lines = get_input_lines(__file__)

    results = map(evaluate, lines)

    return sum(results)


def evaluate(report: str) -> bool:
    report_nums = [int(n) for n in report.split(' ')]
    return evaluate_report(report_nums)


def evaluate_report(report_nums: list[int], depth = 0) -> bool:
    """
    Evaluates the report with "dampening", meaning we can retry the calculation
    removing one number from the report to see if we get a positive result
    :param report_nums: the report list to evaluate
    :param depth: the recursion depth
    :return:
    """

    # one of -1 negative, 0 neutral, 1 positive
    direction = 0

    # default to success
    report_result = True

    for idx, num in enumerate(report_nums):
        if idx == 0:
            continue

        # evaluate absolute difference
        abs_diff = abs(num - report_nums[idx - 1])
        if abs_diff == 0 or abs_diff < 1 or abs_diff > 3:
            report_result = False

        # get the diff direction
        diff = num - report_nums[idx - 1]
        diff_direction = get_diff_direction(diff)

        # the first time it's neutral, update with the direction
        if direction == 0:
            direction = diff_direction
            continue

        # check that the direction as not changed
        if diff_direction != direction:
            report_result = False

    # retry false reports by removing at most one number (controlled by depth)
    if not report_result and depth == 0:
        for index in range(0, len(report_nums)):
            num_removed_report = report_nums[:index] + report_nums[index + 1:]
            num_removed_result = evaluate_report(num_removed_report, 1)
            if num_removed_result:
                return True

    return report_result

def get_diff_direction(diff) -> int:
    return -1 if diff > 0 else 1


if __name__ == '__main__':
    result = main()
    print(result)
