import os


def get_input_lines(file: str) -> list[str]:
    with open(os.path.dirname(file) + '/../data/input') as file:
        lines = [line.strip() for line in file]

    return lines

def get_input(file: str) -> str:
    with open(os.path.dirname(file) + '/../data/input') as file:
        return file.read().strip()

def clean_input(input_str: str) -> list[str]:
    return [line.strip() for line in input_str.strip().split("\n")]