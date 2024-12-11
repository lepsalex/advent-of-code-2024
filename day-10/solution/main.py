from enum import nonmember

from lib.input import get_input_lines


def main():
    lines = get_input_lines(__file__)

    return solve_part_one(lines), solve_part_two(lines)


moves = [
    (0, -1),  # up
    (1, 0),  # right
    (0, 1),  # down
    (-1, 0)  # left
]


def solve_part_one(lines: list[str]):
    trail_map = [list(map(int, line)) for line in lines]
    sum_total = 0

    for y in range(len(trail_map)):
        for x in range(len(trail_map)):
            if trail_map[y][x] != 0:
                continue

            pos = (x, y)
            reached = set()
            walk_trail_distinct_peak(trail_map, pos, 0, reached)
            sum_total += len(reached)

    return sum_total

def solve_part_two(lines: list[str]):
    trail_map = [list(map(int, line)) for line in lines]
    sum_total = 0

    for y in range(len(trail_map)):
        for x in range(len(trail_map)):
            if trail_map[y][x] != 0:
                continue

            pos = (x, y)
            travelled_paths = set()
            walk_trail_distinct_trail(trail_map, pos, 0, travelled_paths)
            sum_total += len(travelled_paths)

    return sum_total


def walk_trail_distinct_peak(trail_map: list[list[int]], pos: tuple[int, int], value: int,
               reached: set[tuple[int, int]], visited: set[tuple[int, int]] = None):
    # do not repeat trail
    if visited is not None and pos in visited:
        return

    x, y = pos

    # out-of-bounds check
    if x < 0 or x >= len(trail_map) or y < 0 or y >= len(trail_map):
        return

    last_value = value
    value = trail_map[y][x]

    # if we are on a trail, only progress when there is a smooth gradient
    if visited is not None and value - last_value != 1:
        return

    # at this point we can initialize visited if it does not exist
    if visited is None:
        visited = set()

    # add the current position to our visited list
    visited.add(pos)

    # check if we are on a peak and record it to our reach set
    if value == 9:
        reached.add(pos)
        return

    # move in every direction from the current one if we are not at a peak
    for move_x, move_y in moves:
        next_pos: tuple[int, int] = (x + move_x, y + move_y)
        walk_trail_distinct_peak(trail_map, next_pos, value, reached, visited)

def walk_trail_distinct_trail(trail_map: list[list[int]], pos: tuple[int, int], value: int,
                              travelled_paths: set[str], visited: set[tuple[int, int]] = None):
    # do not repeat trail
    if visited is not None and pos in visited:
        return

    x, y = pos

    # out-of-bounds check
    if x < 0 or x >= len(trail_map) or y < 0 or y >= len(trail_map):
        return

    last_value = value
    value = trail_map[y][x]

    # if we are on a trail, only progress when there is a smooth gradient
    if visited is not None and value - last_value != 1:
        return

    # at this point we can initialize visited if it does not exist
    if visited is None:
        visited = set()

    # add the current position to our visited list
    visited.add(pos)

    # check if we are on a peak and record it to our reach set
    if value == 9:
        path_str = "".join(map(str, visited))
        travelled_paths.add(path_str)
        return

    # move in every direction from the current one if we are not at a peak
    for move_x, move_y in moves:
        next_pos: tuple[int, int] = (x + move_x, y + move_y)

        # in order to explore every path we need to copy the visited set with every move
        next_visited = visited.copy()

        walk_trail_distinct_trail(trail_map, next_pos, value, travelled_paths, next_visited)


if __name__ == '__main__':
    result = main()
    print(result)
