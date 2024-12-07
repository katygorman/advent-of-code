import numpy as numpy

INPUT_FILE_PATH = './input.txt'


def main():
    ordering_rules, updates = parse_input_file()
    total = calculate_middle_page_number_of_allowed_updates(ordering_rules, updates)
    print(total)


def calculate_middle_page_number_of_allowed_updates(ordering_rules, updates):
    middle_page_numbers = 0
    for update in updates:
        if allowed_update(ordering_rules, update):
            middle_page_numbers += update[(len(update)) // 2]
    return middle_page_numbers


def allowed_update(ordering_rules, update):
    for i in range(len(update)):
        num = update[i]
        before_nums = update[:i]
        after_nums = update[i + 1:]

        nums_before_rules, nums_after_rules = nums_rules(ordering_rules, num, update)
        before_logic = (len(nums_before_rules) > 0 and not all(x in before_nums for x in nums_before_rules))
        after_logic = (len(nums_after_rules) > 0 and not all(x in after_nums for x in nums_after_rules))

        if before_logic or after_logic:
            return False
    return True


def nums_rules(ordering_rules, num, update):
    rules_for_update = ordering_rules[numpy.isin(ordering_rules, update).all(axis=1)]
    rules_before_num = rules_for_update[rules_for_update[:, 1] == num]
    rules_after_num = rules_for_update[rules_for_update[:, 0] == num]

    nums_before = rules_before_num[:, 0]
    nums_after = rules_after_num[:, 1]

    return nums_before, nums_after


def parse_input_file():
    ordering_rules = []
    updates = []
    with open(INPUT_FILE_PATH, "r") as file:
        for line in file:
            if "|" in line:
                ordering_rules.append([int(x) for x in line.split("|")])
            elif "," in line:
                updates.append([int(x) for x in line.split(",")])
    numpy_ordering_rules = numpy.array(ordering_rules)
    return numpy_ordering_rules, updates


if __name__ == "__main__":
    main()
