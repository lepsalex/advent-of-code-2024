from functools import reduce

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
    added_to_region = set()
    regions = {}
    grid_size = len(lines)

    for y, line in enumerate(lines):
        for x in range(len(line)):
            if (x, y) in added_to_region:
                continue

            region = line[x]
            key = f"{region}-{x}-{y}"

            if key in regions:
                continue

            regions[key] = {}
            regions[key][y] = [x]
            regions[key]['area'] = 1
            regions[key]['perimeter'] = calculate_perimeter(lines, (x, y), grid_size, region)
            added_to_region.add((x, y))

            next_moves = get_valid_moves((x, y), grid_size)

            while len(next_moves) > 0:
                next_move = next_moves.pop()
                n_x, n_y = next_move

                if lines[n_y][n_x] != region:
                    continue

                if next_move in added_to_region:
                    continue

                added_to_region.add(next_move)

                if n_y not in regions[key]:
                    regions[key][n_y] = []

                regions[key][n_y].append(n_x)

                regions[key]['area'] += 1
                regions[key]['perimeter'] += calculate_perimeter(lines, next_move, grid_size, region)

                next_moves.extend(get_valid_moves(next_move, grid_size))

    return sum(map(lambda region_value: region_value['area'] * region_value['perimeter'], regions.values()))


def solve_part_two(lines: list[str]):
    return 2


def calculate_perimeter(lines: list[str], pos: (int, int), grid_size: int, region: str):
    perimeter = 4
    coords_around_pos = get_valid_moves(pos, grid_size)
    for (cx, cy) in coords_around_pos:
        if lines[cy][cx] == region:
            perimeter -= 1

    return perimeter


def get_valid_moves(pos: (int, int), grid_size: int):
    return [apply_move(pos, move) for move in moves if is_valid_pos(apply_move(pos, move), grid_size)]


def apply_move(pos: (int, int), move: (int, int)):
    return pos[0] + move[0], pos[1] + move[1]


def is_valid_pos(pos: (int, int), grid_size: int):
    x, y = pos

    if (0 <= x <= grid_size - 1
            and 0 <= y <= grid_size - 1):
        return True

    return False


if __name__ == '__main__':
    result = main()
    print(result)
