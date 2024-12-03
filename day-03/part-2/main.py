import re

from lib.input import get_input

DO = "do()"
DONT = "don't()"

def main():
    data = get_input(__file__)

    return process(data)

def process(data: str):
    # setup data to collect "active" parts of the code
    slices: list[tuple[int,int]] = []
    is_doing = True
    last_do = 0

    # search for do/don't markers to enable/disable code sections
    enable_disable_regex = re.compile("(?:don't|do)\\(\\)")
    do_dont_markers = list(enable_disable_regex.finditer(data))
    last_marker_idx = len(do_dont_markers) - 1

    for idx, match in enumerate(do_dont_markers):
        location = match.start()

        # mark an active slice if we are doing and encounter a "don't"
        if is_doing and match.group() == DONT:
            slices.append((last_do, location))
            is_doing = False
            continue

        # start doing if we are not and encounter a "do"
        if not is_doing and match.group() == DO:
            is_doing = True
            last_do = location

        # on end, check if we were doing and record that last slice
        if is_doing and idx == last_marker_idx:
            slices.append((last_do, len(data)))

    # join all the active regions of the code together
    active_code = "".join([data[slice[0]:slice[1]] for slice in slices])

    # regex find all instances of mul(XXX,XXX) and put into capture groups
    regex = re.compile("mul\\((\\d{1,3}),(\\d{1,3})\\)")
    calls: list[tuple[str, str]] = regex.findall(active_code)

    # multiply result tuples
    products = map(multiply, calls)

    return sum(products)

def multiply(data: tuple[str, str]):
    return int(data[0]) * int(data[1])

if __name__ == '__main__':
    result = main()
    print(result)
