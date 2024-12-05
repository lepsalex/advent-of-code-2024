from lib.input import get_input_lines


def main():
    lines = get_input_lines(__file__)

    return search(lines)


def search(lines: list[str]) -> int:
    counter = 0

    search_str = "MAS"
    search_len = len(search_str)
    grid, size = create_grid(lines)

    down_left = (-1, 1)
    down_right = (1, 1)

    for y in range(size):
        for x in range(size):
            # do not search if we are not on the first or last char
            if grid[y][x] != search_str[0] and grid[y][x] != search_str[search_len - 1]:
                continue

            # do not start a search from a position cannot be completed
            if x > (size - search_len) or y > (size - search_len):
                continue

            start_pos_1 = (x, y)
            start_pos_2 = (x + search_len - 1, y)

            # only search from the top left and right corners of the x
            if not is_valid_pos(start_pos_1, size) or not is_valid_pos(start_pos_2, size):
                continue

            # search from top-left
            top_left_word = ""
            for idx in range(search_len):
                cursor_x = start_pos_1[0] + (down_right[0] * idx)
                cursor_y = start_pos_1[1] + (down_right[1] * idx)
                top_left_word += grid[cursor_y][cursor_x]

            if top_left_word != search_str and top_left_word != search_str[::-1]:
                continue

            # search from top-right
            top_right_word = ""
            for idx in range(search_len):
                cursor_x = start_pos_2[0] + (down_left[0] * idx)
                cursor_y = start_pos_2[1] + (down_left[1] * idx)
                top_right_word += grid[cursor_y][cursor_x]

            if top_right_word != search_str and top_right_word != search_str[::-1]:
                continue

            counter += 1

    return counter


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
