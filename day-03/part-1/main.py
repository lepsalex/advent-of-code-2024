import re

from lib.input import get_input


def main():
    data = get_input(__file__)

    # regex find all instances of mul(XXX,XXX) and put into capture groups
    regex = re.compile("mul\\((\\d{1,3}),(\\d{1,3})\\)")
    calls: list[tuple[str, str]] = regex.findall(data)

    # multiply result tuples
    products = map(multiply, calls)

    return sum(products)

def multiply(data: tuple[str, str]):
    return int(data[0]) * int(data[1])

if __name__ == '__main__':
    result = main()
    print(result)
