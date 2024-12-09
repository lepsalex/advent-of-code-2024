from lib.input import get_input


def main():
    input_str = get_input(__file__)

    return solve_part_one(input_str)


def solve_part_one(input_str: str):
    current_id = 0
    file_map = []

    # construct the file map
    for idx, char in enumerate(input_str):
        num_repeats = int(char)

        # use the index for file blocks, and the '.' char for free space
        # note: we alternate between file blocks and free space (blocks are even)
        write_char = current_id if idx % 2 == 0 else '.'

        for _ in range(num_repeats):
            file_map.append(write_char)

        if idx % 2:
            current_id += 1

    # rearrange the file map
    lc, rc = 0, len(file_map) - 1
    sum_total = 0

    # use left and right cursors to process the map
    while lc <= rc:
        # update right until it's on a block character
        while file_map[rc] == '.':
            rc -= 1

        # swap the free space char (left) with the block char (right)
        if file_map[lc] == '.':
            file_map[lc] = file_map[rc]
            file_map[rc] = '.'

        # update the running total
        sum_total = sum_total + (lc * int(file_map[lc]))

        # increment the left cursor for the next pass
        lc += 1

    return sum_total


if __name__ == '__main__':
    result = main()
    print(result)
