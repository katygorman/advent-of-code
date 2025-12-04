INPUT_FILE_PATH = 'input.txt'


def main():
    data = load_data()
    joltage = find_joltage(data)
    print(joltage)


def find_joltage(data):
    total_joltage = 0
    for line in data:
        first_num, first_index = find_largest_num_and_index_recursive(line[:-1], 0, -1, -1)
        second_num, second_index = find_largest_num_and_index_recursive(line[first_index + 1:], 0, -1, -1)
        joltage = first_num * 10 + second_num
        total_joltage += joltage
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
