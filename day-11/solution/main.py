from lib.input import get_input


def main():
    input_str = get_input(__file__)
    stones = input_str.split(" ")

    return solve_part_one(stones), solve_part_two(stones)


def solve_part_one(stones: list[str]):
    blink = 0
    result_stones = stones[:]

    while blink < 25:
        blink_stones = []

        for stone in result_stones:
            if stone == '0':
                blink_stones.append('1')
            elif len(stone) % 2 == 0:
                left, right = stone[:len(stone) // 2], stone[len(stone) // 2:]
                blink_stones.append(left)

                zero_stripped_right = right.lstrip('0')
                blink_stones.append(zero_stripped_right if len(zero_stripped_right) >= 1 else '0')
            else:
                num = int(stone) * 2024
                blink_stones.append(str(num))

        result_stones = blink_stones[:]
        blink += 1

    return len(result_stones)


def solve_part_two(stones: list[str]):
    return 2


if __name__ == '__main__':
    result = main()
    print(result)
