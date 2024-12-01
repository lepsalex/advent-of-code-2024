import os


def get_input_lines(file: str):
    with open(os.path.dirname(file) + '/../data/input') as file:
        lines = [line.rstrip() for line in file]

    return lines