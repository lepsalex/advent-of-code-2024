from lib.input import get_input, clean_input

PLAYER = '@'
WALL = '#'
GROUND = '.'
BOX = 'O'


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
    return 2


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

    next_tile = state[ny][nx]

    if next_tile == WALL:
        nx = px
        ny = py

    if next_tile == GROUND:
        state[py][px] = GROUND
        state[ny][nx] = PLAYER

    if next_tile == BOX:
        boxes = [(nx, ny)]
        while True:
            cx, cy = boxes[-1]
            x, y = (cx + dx, cy + dy)

            tile = state[y][x]

            if tile == WALL:
                nx = px
                ny = py
                break

            if tile == GROUND:
                state[y][x] = BOX
                state[py][px] = GROUND
                state[ny][nx] = PLAYER
                break

            boxes.append((x, y))

    return state, (nx, ny)


def evaluate_box_gps(state: list[list[str]]):
    gps_sum = 0

    for y in range(len(state)):
        for x in range(len(state[0])):
            if state[y][x] == BOX:
                gps_sum += x + y * 100

    return gps_sum


if __name__ == '__main__':
    result = main()
    print(result)
