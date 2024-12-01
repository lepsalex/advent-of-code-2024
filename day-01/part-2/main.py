import os
from itertools import groupby, count

from lib.input import get_input_lines


def main():
    lines = get_input_lines(__file__)

    list_a = []
    list_b = []

    for line in lines:
        (a, b) = line.split('   ')
        list_a.append(int(a))
        list_b.append(int(b))

    list_b_agg: dict[int, int] = {}

    for k, v in groupby(sorted(list_b)):
        list_b_agg[k] = len(list(v))

    sim_sum = 0

    for num in list_a:
        multiplier = list_b_agg.get(num, 0)
        sim_sum += num * multiplier

    return sim_sum


if __name__ == '__main__':
    result = main()
    print(result)