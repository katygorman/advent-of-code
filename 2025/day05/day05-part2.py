import numpy as numpy

INPUT_FILE_PATH = 'input.txt'


def main():
    fresh_ingredients_ranges = parse_input_file()
    unique_ranges = unique_fresh_ingredients_ranges(fresh_ingredients_ranges)
    count = count_fresh_ingredients(unique_ranges)
    print(count)


def count_fresh_ingredients(unique_ranges):
    count = 0
    for unique_range in unique_ranges:
        count += (unique_range[1] - unique_range[0] + 1)
    return count


def unique_fresh_ingredients_ranges(fresh_ingredients_ranges):
    previous_ranges = fresh_ingredients_ranges
    new_ranges = narrow_fresh_ingredients_ranges(fresh_ingredients_ranges)
    while len(previous_ranges) != len(new_ranges):
        previous_ranges = new_ranges
        new_ranges = narrow_fresh_ingredients_ranges(previous_ranges)
    return new_ranges


def narrow_fresh_ingredients_ranges(fresh_ingredients_ranges):
    unique_ranges = []
    for fresh_ingredients_range in fresh_ingredients_ranges:
        added_to_range = False
        for unique_range in unique_ranges:
            newly_expanded = expand_range(unique_range, fresh_ingredients_range)
            if newly_expanded:
                added_to_range = True
        if not added_to_range:
            unique_ranges.append(fresh_ingredients_range)
    return unique_ranges


def expand_range(existing_range, new_range):
    expanded = False
    if new_range[0] <= existing_range[0] <= new_range[1] or existing_range[0] <= new_range[0] <= existing_range[1]:
        existing_range[0] = min(existing_range[0], new_range[0])
        expanded = True
    if new_range[0] <= existing_range[1] <= new_range[1] or existing_range[0] <= new_range[1] <= existing_range[1]:
        existing_range[1] = max(existing_range[1], new_range[1])
        expanded = True
    return expanded


def parse_input_file():
    fresh_ingredients_ranges = []
    with open(INPUT_FILE_PATH, "r") as file:
        for line in file:
            if "-" in line:
                fresh_ingredients_ranges.append([int(x) for x in line.split("-")])
    fresh_ingredients_ranges = numpy.array(fresh_ingredients_ranges)
    return fresh_ingredients_ranges


if __name__ == "__main__":
    main()
