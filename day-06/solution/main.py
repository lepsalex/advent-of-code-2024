from copy import deepcopy
from enum import StrEnum

from lib.input import get_input_lines


class TILE(StrEnum):
    NORMAL = '.'
    OBSTACLE = '#'
    GUARD_UP = '^'
    GUARD_DOWN = 'v'
    GUARD_LEFT = '<'
    GUARD_RIGHT = '>'


GUARD_TILES = {TILE.GUARD_UP, TILE.GUARD_DOWN, TILE.GUARD_LEFT, TILE.GUARD_RIGHT}

GUARD_OFF_GRID = (-1, -1)


def main():
    lines = get_input_lines(__file__)

    return solve_part_1(lines), solve_part_2(lines)


def solve_part_1(lines: list[str]):
    room_map, guard_location, room_size = create_room_map(lines)

    # init with the guard's starting location
    visited_set = {guard_location}

    # move around the map until we would go off grid
    while guard_location != GUARD_OFF_GRID:
        room_map, guard_location = guard_move(room_map, guard_location, room_size)

        # do not record the off grid location to the visited set
        if guard_location != GUARD_OFF_GRID:
            visited_set.add(guard_location)

    return len(visited_set)


def solve_part_2(lines: list[str]):
    # base room
    base_room_map, base_guard_location, room_size = create_room_map(lines)
    room_size_x, room_size_y = room_size

    # loop counter
    loop_count = 0

    for y in range(room_size_y):
        for x in range(room_size_x):
            x_y_location = (x, y)
            room_variant = create_room_map_variant(base_room_map, base_guard_location, x_y_location)

            if room_variant is None:
                continue

            room_map, guard_location = room_variant

            # for part two we store location and direction in
            # a set so that we can detect a loop vs just crossing
            # over a tile the guard had crossed before

            guard = get_tile(room_map, guard_location)
            visited_set = {(guard_location, guard)}

            # move around the map until we would go off grid
            while guard_location != GUARD_OFF_GRID:
                room_map, guard_location = guard_move(room_map, guard_location, room_size)
                guard = get_tile(room_map, guard_location)

                if (guard_location, guard) in visited_set:
                    loop_count += 1
                    break

                visited_set.add((guard_location, guard))

    return loop_count


def guard_move(room_map: list[list[TILE]], guard_location: tuple[int, int], room_size: tuple[int, int]) -> (
        list[list[TILE]], tuple[int, int]):
    guard_tile = get_tile(room_map, guard_location)
    forward_tile = get_forward_tile(room_map, guard_location)

    # exit if the next tile is off grid
    if is_tile_off_grid(room_size, forward_tile):
        return room_map, GUARD_OFF_GRID

    # rotate the guard before moving
    if is_tile_obstacle(room_map, forward_tile):
        guard_tile = rotate_guard(guard_tile)
        update_tile_at_location(room_map, guard_location, guard_tile)
        forward_tile = get_forward_tile(room_map, guard_location)

        # check if the next tile is off grid after rotating
        if is_tile_off_grid(room_size, forward_tile):
            return room_map, GUARD_OFF_GRID

        # if the next tile after is still an obstacle, return without moving
        if is_tile_obstacle(room_map, forward_tile):
            return room_map, guard_location

    # move the guard
    update_tile_at_location(room_map, guard_location, TILE.NORMAL)
    update_tile_at_location(room_map, forward_tile, guard_tile)

    # return the update room with the forward tile as the guard's next location
    return room_map, forward_tile


def rotate_guard(guard: TILE) -> TILE:
    match guard:
        case TILE.GUARD_UP:
            return TILE.GUARD_RIGHT
        case TILE.GUARD_DOWN:
            return TILE.GUARD_LEFT
        case TILE.GUARD_LEFT:
            return TILE.GUARD_UP
        case TILE.GUARD_RIGHT:
            return TILE.GUARD_DOWN
        case _:
            raise Exception("invalid guard tile")


def is_tile_off_grid(room_size: tuple[int, int], tile_location: tuple[int, int]) -> bool:
    size_x, size_y = room_size
    x, y = tile_location

    if (0 <= x <= size_x - 1
            and 0 <= y <= size_y - 1):
        return False

    return True


def is_tile_obstacle(room_map: list[list[TILE]], tile_location: tuple[int, int]) -> bool:
    return get_tile(room_map, tile_location) == TILE.OBSTACLE


def get_forward_tile(room_map: list[list[TILE]], guard_location: tuple[int, int]) -> tuple[int, int]:
    look_direction = get_tile(room_map, guard_location)
    guard_x, guard_y = guard_location

    match look_direction:
        case TILE.GUARD_UP:
            return guard_x, guard_y - 1
        case TILE.GUARD_DOWN:
            return guard_x, guard_y + 1
        case TILE.GUARD_LEFT:
            return guard_x - 1, guard_y
        case TILE.GUARD_RIGHT:
            return guard_x + 1, guard_y
        case _:
            raise Exception("invalid guard tile")


def get_tile(room_map: list[list[TILE]], x_y_location: tuple[int, int]) -> TILE:
    x, y = x_y_location
    return room_map[y][x]


def update_tile_at_location(room_map: list[list[TILE]], x_y_location: tuple[int, int], new_tile: TILE):
    x, y = x_y_location
    room_map[y][x] = new_tile


def create_room_map_variant(room_map: list[list[TILE]], guard_location: tuple[int, int], x_y_location: tuple[int, int]):
    # the tile we want to potentially swap into an obstacle
    tile_at_location = get_tile(room_map, x_y_location)

    # only swap normal tiles
    if tile_at_location != TILE.NORMAL:
        return None

    # swap from normal to obstacle
    room_map_instance = deepcopy(room_map)
    update_tile_at_location(room_map_instance, x_y_location, TILE.OBSTACLE)

    return (
        room_map_instance,
        guard_location,
    )


def create_room_map(lines: list[str]) -> (list[list[TILE]], tuple[int, int], tuple[int, int]):
    room_size_x = len(lines[0])
    room_size_y = len(lines)
    room_size = (room_size_x, room_size_y)
    guard_location = (0, 0)
    room_map: list[list[str]] = []

    for y in range(room_size_y):
        for x in range(room_size_x):
            if x == 0:
                room_map.append([])

            tile = parse_tile(lines[y][x])

            if tile in GUARD_TILES:
                guard_location = (x, y)

            room_map[y].append(tile)

    return (
        room_map,
        guard_location,
        room_size
    )


def parse_tile(tile: str) -> TILE:
    return TILE(tile)


if __name__ == '__main__':
    # Caution, running part 2 takes quite some time ...
    result_1, result_2 = main()
    print("Part 1: ", result_1)
    print("Part 2: ", result_2)
