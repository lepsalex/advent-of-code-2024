from functools import cache

from lib.input import get_input


def main():
    input_str = get_input(__file__)
    stones = input_str.split(" ")

    return solve_part_one(stones), solve_part_two(stones)


def solve_part_one(stones: list[str]):
    return blink_at_stones(stones, 25)


def solve_part_two(stones: list[str]):
    return blink_at_stones(stones, 75)


def blink_at_stones(stones: list[str], num_blinks: int):
    return sum([blink(stone, num_blinks) for stone in stones])


@cache
def blink(stone: str, num_blinks: int):
    if num_blinks == 0:
        return 1

    if stone == '0':
        return blink('1', num_blinks - 1)
    elif len(stone) % 2 == 0:
        left_stone, right = stone[:len(stone) // 2], stone[len(stone) // 2:]
        zero_stripped_right = right.lstrip('0')
        right_stone = zero_stripped_right if len(zero_stripped_right) >= 1 else '0'

        return blink(left_stone, num_blinks - 1) + blink(right_stone, num_blinks - 1)
    else:
        num = int(stone) * 2024
        return blink(str(num), num_blinks - 1)


if __name__ == '__main__':
    result = main()
    print(result)
