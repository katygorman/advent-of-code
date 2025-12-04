INPUT_FILE_PATH = 'input.txt'
NUM_BATTERIES = 12


def main():
    data = load_data()
    joltage = find_joltage(data)
    print(joltage)


def find_joltage(data):
    total_joltage = 0
    for line in data:
        start_index = 0
        for i in range(NUM_BATTERIES, 0, -1):
            # End index leaves off the last (i - 1) characters so we'll still have enough characters to form the joltage
            end_index = len(line) - (i - 1)
            sub_line = line[start_index:end_index]

            num, sub_str_index = find_largest_num_and_index_recursive(sub_line, 0, -1, -1)
            # Update start_index to search in the remaining substring
            start_index += sub_str_index + 1

            # Calculate the magnitude of the found number
            num_magnitude = num * (10 ** (i - 1))
            total_joltage += num_magnitude
    return total_joltage


def find_largest_num_and_index_recursive(str, index, max_num, max_index):
    # Base case: if the end of the string is reached
    if index == len(str):
        return max_num, max_index

    char = str[index]
    num = int(char)

    # If this digit is larger than the max, update
    if num > max_num:
        max_num = num
        max_index = index

    # Recursive call for the next character
    return find_largest_num_and_index_recursive(str, index + 1, max_num, max_index)


def load_data():
    with open(INPUT_FILE_PATH, 'r') as file:
        # Read all lines and strip the newline character from each
        lines = [line.strip() for line in file.readlines()]
    return lines


if __name__ == "__main__":
    main()
