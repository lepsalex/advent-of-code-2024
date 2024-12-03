from lib.input import get_input_lines


def main():
    lines = get_input_lines(__file__)

    for line in lines:
        print(line)

    return True


if __name__ == '__main__':
    result = main()
    print(result)
