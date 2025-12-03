import numpy as np
import re

INPUT_FILE_PATH = 'input.txt'


def main():
    range_starts, range_ends = load_data()
    count = find_doubles(range_starts, range_ends)
    print(count)


def find_doubles(range_starts, range_ends):
    count = 0
    for start, end in zip(range_starts, range_ends):
        current = start
        while current <= end:
            current_str = str(current)
            if is_repeating(current_str):
                count += current
            current += 1
    return count


def is_repeating(string):
    pattern = r"^(.+)\1+$"
    return bool(re.match(pattern, string))


def load_data():
    # Read the file as a single string
    with open(INPUT_FILE_PATH, 'r') as f:
        content = f.read()

    # Split the content by ',' to get individual ranges
    ranges = content.split(',')

    # Split each range into two numbers and store them in separate lists
    first_numbers = []
    second_numbers = []
    for r in ranges:
        start, end = map(int, r.split('-'))
        first_numbers.append(start)
        second_numbers.append(end)

    # Convert lists to NumPy arrays
    first_numbers = np.array(first_numbers)
    second_numbers = np.array(second_numbers)

    return first_numbers, second_numbers


if __name__ == "__main__":
    main()
