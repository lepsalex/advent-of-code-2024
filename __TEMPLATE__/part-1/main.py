from lib.input import get_input_lines


def main():
    lines = get_input_lines(__file__)

    for line in lines:
        print(line)

    return solve()

def solve():
    return 1

if __name__ == '__main__':
    result = main()
    print(result)
