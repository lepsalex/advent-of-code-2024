import os


def main():
    with open(os.path.dirname(__file__) + '/../data/input') as file:
        lines = [line.rstrip() for line in file]

    list_a = []
    list_b = []

    for line in lines:
        (a, b) = line.split('   ')
        list_a.append(int(a))
        list_b.append(int(b))

    list_a.sort()
    list_b.sort()

    zipped = zip(list_a, list_b)

    diff_sum: int = 0

    for a, b in zipped:
        diff = abs(a - b)
        diff_sum += diff

    return diff_sum


if __name__ == '__main__':
    result = main()
    print(result)