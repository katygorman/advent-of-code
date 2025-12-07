import numpy as numpy

INPUT_FILE_PATH = 'input.txt'


def main():
    fresh_ingredients_ranges, ingredient_ids = parse_input_file()
    count = count_fresh_ingredients(fresh_ingredients_ranges, ingredient_ids)
    print(count)


def count_fresh_ingredients(fresh_ingredients_ranges, ingredient_ids):
    count = 0
    for ingredient_id in ingredient_ids:
        for fresh_ingredients_range in fresh_ingredients_ranges:
            if fresh_ingredients_range[0] <= ingredient_id <= fresh_ingredients_range[1]:
                count += 1
                break
    return count


def parse_input_file():
    fresh_ingredients_ranges = []
    ingredient_ids = []
    with open(INPUT_FILE_PATH, "r") as file:
        for line in file:
            if "-" in line:
                fresh_ingredients_ranges.append([int(x) for x in line.split("-")])
            elif line.strip().isdigit():
                ingredient_ids.append(int(line))
    fresh_ingredients_ranges = numpy.array(fresh_ingredients_ranges)
    return fresh_ingredients_ranges, ingredient_ids


if __name__ == "__main__":
    main()
