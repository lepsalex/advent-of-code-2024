from lib.input import get_input_lines


def main():
    lines = get_input_lines(__file__)

    return search(lines)


def search(lines: list[str]) -> int:
    counter = 0
    search_str = "XMAS"
    search_len = len(search_str)
    grid, size = create_grid(lines)

    for y in range(size):
        for x in range(size):
            if grid[x][y] != search_str[0]:
                continue

            start_pos = (x, y)
            valid_search_vectors = get_search_vectors(start_pos, search_len, size)

            for search_x, search_y in valid_search_vectors:
                word = ""

                for idx in range(search_len):
                    cursor_x = x + (search_x * idx)
                    cursor_y = y + (search_y * idx)
                    word += grid[cursor_x][cursor_y]

                if word == search_str:
                    counter += 1

    return counter


def get_search_vectors(start_pos: (int, int), length: int, grid_size: int) -> list[tuple[int, int]]:
    start_x, start_y = start_pos

    valid_search_vectors = []

    for dir_x, dir_y in get_directions():
        end_x = start_x + (dir_x * (length - 1))
        end_y = start_y + (dir_y * (length - 1))

        if not is_valid_pos((end_x, end_y), grid_size):
            continue

        valid_search_vectors.append((dir_x, dir_y))

    return valid_search_vectors


def get_directions():
    """
    Get all directions (x, y)
    """
    return [
        (-1, -1),  # up-left
        (0, -1),  # up
        (1, -1),  # up-right
        (-1, 0),  # left
        (1, 0),  # right
        (-1, 1),  # down-left
        (0, 1),  # down
        (1, 1),  # down-right
    ]


def is_valid_pos(pos: (int, int), size: int):
    x, y = pos

    if (0 <= x <= size - 1
            and 0 <= y <= size - 1):
        return True

    return False


def create_grid(lines: list[str]):
    size = len(lines)
    grid: list[list[str]] = []

    for x in range(size):
        for y in range(size):
            if x == 0:
                grid.append([])

            grid[x].append(lines[x][y])

    return (
        grid,
        size
    )


if __name__ == '__main__':
    result = main()
    print(result)
