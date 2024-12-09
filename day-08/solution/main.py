from itertools import combinations

from lib.input import get_input_lines


def main():
    lines = get_input_lines(__file__)

    return solve_part_one(lines), solve_part_two(lines)


def solve_part_one(lines: list[str]):
    size = len(lines)
    antennas = {}
    antinodes = set()

    # read in the map, grouping coords of the same antennas
    for y in range(size):
        for x, char in enumerate(lines[y]):
            if char == '.':
                continue

            if char not in antennas:
                antennas[char] = []

            antennas[char].append((x, y))

    # for every antenna type ...
    for grouped_antennas in antennas.values():
        # get all possible pairs of antenna coordinates
        pairs = combinations(grouped_antennas, 2)

        for a, b in pairs:
            # x/y for each antenna in pair
            ax, ay = a
            bx, by = b

            # delta between pairs
            dx = bx - ax
            dy = by - ay

            # compute antinode positions by extending each point
            # with the distance between the points
            an_1_x = ax - dx
            an_1_y = ay - dy
            an_2_x = bx + dx
            an_2_y = by + dy

            # for both new points, if they are valid positions
            # (ie on the grid), add the position to the set

            if is_valid_pos((an_1_x, an_1_y), size):
                antinodes.add((an_1_x, an_1_y))

            if is_valid_pos((an_2_x, an_2_y), size):
                antinodes.add((an_2_x, an_2_y))

    return len(antinodes)


def solve_part_two(lines: list[str]):
    size = len(lines)
    antennas = {}
    antinodes = set()

    # read in the map, grouping coords of the same antennas
    for y in range(size):
        for x, char in enumerate(lines[y]):
            if char == '.':
                continue

            if char not in antennas:
                antennas[char] = []

            antennas[char].append((x, y))

    # for every antenna type ...
    for grouped_antennas in antennas.values():
        # get all possible pairs of antenna coordinates
        pairs = combinations(grouped_antennas, 2)

        for a, b in pairs:
            # x/y for each antenna in pair
            ax, ay = a
            bx, by = b

            # every node in a pair is also an antinode in part 2
            antinodes.add((ax, ay))
            antinodes.add((bx, by))

            # delta between pairs
            dx = bx - ax
            dy = by - ay

            # for each pair, repeat creation of an antinode
            # until the position is not valid, recording each
            # antinode coordinate pair to the set as we go

            an_1_x = ax - dx
            an_1_y = ay - dy

            while is_valid_pos((an_1_x, an_1_y), size):
                antinodes.add((an_1_x, an_1_y))
                an_1_x = an_1_x - dx
                an_1_y = an_1_y - dy

            an_2_x = bx + dx
            an_2_y = by + dy

            while is_valid_pos((an_2_x, an_2_y), size):
                antinodes.add((an_2_x, an_2_y))
                an_2_x = an_2_x + dx
                an_2_y = an_2_y + dy

    return len(antinodes)


def is_valid_pos(pos: (int, int), size: int):
    x, y = pos

    if (0 <= x <= size - 1
            and 0 <= y <= size - 1):
        return True

    return False


if __name__ == '__main__':
    result = main()
    print(result)
