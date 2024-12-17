from lib.input import get_input, clean_input

# Part 1
PLAYER = '@'
WALL = '#'
GROUND = '.'
BOX = 'O'

# Part 2
WIDE_BOX_L = '['
WIDE_BOX_R = ']'


def main():
    file_str = get_input(__file__)
    state_str, commands_str = file_str.split("\n\n")
    state = [list(row) for row in clean_input(state_str)]

    return solve_part_one(state, commands_str), solve_part_two(state, commands_str)


def solve_part_one(state: list[list[str]], commands: str):
    player_pos = get_player_pos(state)

    while len(commands) > 0:
        command, commands = pop_command(commands)
        state, player_pos = run_command(state, player_pos, command)

    return evaluate_box_gps(state)


def solve_part_two(state: list[list[str]], commands: str):
    wide_state = widen_state(state)
    player_pos = get_player_pos(wide_state)

    while len(commands) > 0:
        command, commands = pop_command(commands)
        wide_state, player_pos = run_command(wide_state, player_pos, command)

    return evaluate_wide_box_gps(wide_state)


def widen_state(state: list[list[str]]):
    updated_state = []
    updated_row = []

    for row in state:
        for tile in row:
            if tile == PLAYER:
                updated_row.append(PLAYER)
                updated_row.append(GROUND)
            if tile == WALL:
                updated_row.append(WALL)
                updated_row.append(WALL)
            if tile == GROUND:
                updated_row.append(GROUND)
                updated_row.append(GROUND)
            if tile == BOX:
                updated_row.append(WIDE_BOX_L)
                updated_row.append(WIDE_BOX_R)
        updated_state.append(updated_row)
        updated_row = []

    return updated_state


def get_player_pos(state: list[list[str]]):
    for y in range(len(state)):
        for x in range(len(state[0])):
            if state[y][x] == PLAYER:
                return x, y


def pop_command(commands: str) -> (str, str):
    return commands[:1], commands[1:]


def run_command(state: list[list[str]], player_pos: (int, int), command: str):
    px, py = player_pos

    dx = {'<': -1, '>': 1}.get(command, 0)
    dy = {'^': -1, 'v': 1}.get(command, 0)

    nx = px + dx
    ny = py + dy

    next_state = [row[:] for row in state]
    next_tile = next_state[ny][nx]

    if next_tile == WALL:
        nx = px
        ny = py
        next_state = state

    if next_tile == GROUND:
        next_state[py][px] = GROUND
        next_state[ny][nx] = PLAYER

    if next_tile == BOX:
        boxes = [(nx, ny)]
        while True:
            cx, cy = boxes[-1]
            x, y = (cx + dx, cy + dy)

            tile = next_state[y][x]

            if tile == WALL:
                next_state = state
                nx = px
                ny = py
                break

            if tile == GROUND:
                next_state[y][x] = BOX
                next_state[py][px] = GROUND
                next_state[ny][nx] = PLAYER
                break

            boxes.append((x, y))

    if next_tile == WIDE_BOX_L or next_tile == WIDE_BOX_R:
        bpx, bpy = (nx + 1, ny) if next_tile == WIDE_BOX_L else (nx - 1, ny)
        boxes = [((nx, ny), (bpx, bpy))] if next_tile == WIDE_BOX_L else [((bpx, bpy), (nx, ny))]
        added_boxes = set(boxes)
        wall_contact = False

        for box in boxes:
            bl, br = box
            blx, bly = bl
            brx, bry = br

            blx_n, bly_n = blx + dx, bly + dy
            brx_n, bry_n = brx + dx, bry + dy

            # wall tile in contact with box set
            if next_state[bly_n][blx_n] == WALL or next_state[bry_n][brx_n] == WALL:
                wall_contact = True
                break

            # box directly above or below
            if next_state[bly_n][blx_n] == WIDE_BOX_L and next_state[bry_n][brx_n] == WIDE_BOX_R:
                found_box = ((blx_n, bly_n), (brx_n, bry_n))

                if found_box not in added_boxes:
                    boxes.append(found_box)
                    added_boxes.add(found_box)

            # box left
            if next_state[bly_n][blx_n] == WIDE_BOX_R:
                found_box = ((blx_n - 1, bly_n), (blx_n, bly_n))

                if found_box not in added_boxes:
                    boxes.append(found_box)
                    added_boxes.add(found_box)

            # box right
            if next_state[bry_n][brx_n] == WIDE_BOX_L:
                found_box = ((brx_n, bry_n), (brx_n + 1, bry_n))

                if found_box not in added_boxes:
                    boxes.append(found_box)
                    added_boxes.add(found_box)

        if wall_contact:
            next_state = state
            nx = px
            ny = py
        else:
            # fill current box positions with GROUND
            for box in added_boxes:
                bl, br = box
                blx, bly = bl
                brx, bry = br

                next_state[bly][blx] = GROUND
                next_state[bry][brx] = GROUND

            # shift all boxes and draw them
            for box in added_boxes:
                bl, br = box
                blx, bly = bl
                brx, bry = br

                next_state[bly + dy][blx + dx] = WIDE_BOX_L
                next_state[bry + dy][brx + dx] = WIDE_BOX_R

            next_state[py][px] = GROUND
            next_state[ny][nx] = PLAYER

    return next_state, (nx, ny)


def evaluate_box_gps(state: list[list[str]]):
    gps_sum = 0

    for y in range(len(state)):
        for x in range(len(state[0])):
            if state[y][x] == BOX:
                gps_sum += x + y * 100

    return gps_sum

def evaluate_wide_box_gps(state: list[list[str]]):
    gps_sum = 0

    for y in range(len(state)):
        for x in range(len(state[0])):
            if state[y][x] == WIDE_BOX_L:
                gps_sum += x + y * 100

    return gps_sum

if __name__ == '__main__':
    result = main()
    print(result)
