from lib.input import get_input


def main():
    input_str = get_input(__file__)

    return solve_part_one(input_str), solve_part_two(input_str)


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


def solve_part_two(input_str: str):
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
        # sum up moved blocks (update left cursor)
        while file_map[lc] != '.':
            lc += 1

        # move right cursor to end of next block
        while file_map[rc] == '.':
            rc -= 1

        # get the block we are trying to move
        block_end = rc
        block_start = block_end
        block_char = file_map[block_end]
        while file_map[block_start] == block_char:
            block_start -= 1

        block_size = block_end - block_start

        # go through all possible free slots until one fits
        free_block_start = lc
        while free_block_start < block_start:
            free_block_end = free_block_start
            while file_map[free_block_end] == '.':
                free_block_end += 1

            free_block_size = free_block_end - free_block_start

            if free_block_size >= block_size:
                # copy the block to the free space
                for copy_offset in range(block_size):
                    file_map[free_block_start + copy_offset] = file_map[block_start + copy_offset + 1]
                    file_map[block_start + copy_offset + 1] = '.'
                # exit after copy
                break
            else:
                # get the next free space block
                free_block_start = free_block_end + 1
                while file_map[free_block_start] != '.':
                    free_block_start += 1

        rc = block_start

    # count up the final state of the file map
    for idx, char in enumerate(file_map):
        if char != '.':
            sum_total = sum_total + (idx * int(char))

    return sum_total


if __name__ == '__main__':
    result = main()
    print(result)
