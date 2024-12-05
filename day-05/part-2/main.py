from typing import Callable

from lib.input import get_input


def main():
    input_str = get_input(__file__)

    return solve(input_str)


def solve(input_str: str):
    rules, updates = process_input_str(input_str)
    rule_map: dict[int, set[int]] = build_rule_map(rules)

    is_update_invalid = is_update_invalid_func(rule_map)

    update_lists = [update.split(',') for update in updates]

    invalid_updates = filter(is_update_invalid, update_lists)

    sort = sort_by_rules_func(rule_map, is_update_invalid)
    sorted_updates = map(sort, invalid_updates)

    mid_pages = map(extract_middle, sorted_updates)

    return sum(mid_pages)


def sort_by_rules_func(rule_map: dict[int, set[int]], is_update_invalid: Callable[[list[str]], bool]):
    def sort_by_rules(update_list: list[str]):
        # clone the list so we are not mutating things
        new_update_list = update_list[:]
        is_invalid = is_update_invalid(new_update_list)

        # basically bubble sort ...
        while is_invalid:
            for idx, page in enumerate(new_update_list):
                did_sort = False

                for page_after_idx in range(idx + 1, len(new_update_list)):
                    page_after = new_update_list[page_after_idx]

                    # ignore pages that do not have rules
                    if int(page_after) not in rule_map:
                        continue

                    # swap positions when we find a rule break
                    if int(page) in rule_map[int(page_after)]:
                        new_update_list[idx] = page_after
                        new_update_list[page_after_idx] = page
                        did_sort = True
                        break

                if did_sort:
                    break

            is_invalid = is_update_invalid(new_update_list)

        return new_update_list

    return sort_by_rules


def extract_middle(update_list: list[str]) -> int:
    mid = int(len(update_list) / 2)

    return int(update_list[mid])


def is_update_invalid_func(rule_map: dict[int, set[int]]):
    def is_update_invalid(update_list: list[str], ):
        for idx, page in enumerate(update_list):
            # check that no pages after this page have
            # this page in their must be before rule
            for page_after_idx in range(idx + 1, len(update_list)):
                page_after = int(update_list[page_after_idx])

                # ignore pages that do not have rules
                if page_after not in rule_map:
                    continue

                if int(page) in rule_map[page_after]:
                    return True

        return False

    return is_update_invalid


def build_rule_map(rules: list[str]):
    rule_map = {}

    for left, right in [map(int, rule.split('|')) for rule in rules]:
        if left not in rule_map:
            rule_map[int(left)] = {int(right)}
            continue

        rule_map[left].add(right)

    return rule_map


def process_input_str(input_str: str):
    rules, updates = [part.strip() for part in input_str.split("\n\n")]
    rules = rules.split("\n")
    updates = updates.split("\n")

    return rules, updates


if __name__ == '__main__':
    result = main()
    print(result)
