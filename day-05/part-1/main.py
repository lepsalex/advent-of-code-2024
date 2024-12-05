from lib.input import get_input


def main():
    input_str = get_input(__file__)

    return solve(input_str)

def solve(input_str: str):
    rules, updates = process_input_str(input_str)

    rule_map: dict[int, set[int]] = build_rule_map(rules)

    verify_func = verify_update_func(rule_map)

    valid_updates = filter(verify_func, updates)

    mid_pages = map(extract_middle, valid_updates)

    return sum(mid_pages)

def extract_middle(update: str) -> int:
    update_list = update.split(',')
    mid = int(len(update_list) / 2)

    return int(update_list[mid])

def verify_update_func(rule_map: dict[int, set[int]]):
    def verify_update(update: str, ):
        update_list = update.split(',')

        for idx, page in enumerate(update_list):
            # check that no pages after this page have
            # this page in their must be before rule
            for page_after_idx in range(idx + 1, len(update_list)):
                page_after = int(update_list[page_after_idx])

                # ignore pages that do not have rules
                if page_after not in rule_map:
                    continue

                if int(page) in rule_map[page_after]:
                    return False

        return True

    return verify_update

def build_rule_map(rules: list[str]):
    rule_map = {}

    for left, right in [map(int ,rule.split('|')) for rule in rules]:
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
