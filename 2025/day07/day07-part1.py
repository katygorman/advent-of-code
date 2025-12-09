INPUT_FILE_PATH = 'input.txt'
START = 'S'
BEAM = '|'
SPLITTER = '^'


def main():
    matrix = parse_input_file()
    count = count_splits(matrix)
    print(count)


def count_splits(matrix):
    splits = 0
    for row in range(1, len(matrix)):
        for col in range(len(matrix[row]) - 1):
            if check_for_split(matrix, row, col):
                splits += 1
    return splits


def check_for_split(matrix, row, col):
    current = matrix[row][col]
    previous = matrix[row - 1][col]
    beam = previous == BEAM or previous == START
    splitter = current == SPLITTER

    if beam and splitter:
        matrix[row + 1][col - 1] = BEAM
        matrix[row + 1][col + 1] = BEAM
        return True
    if beam:
        matrix[row][col] = BEAM
    return False


def parse_input_file():
    with open(INPUT_FILE_PATH, "r") as file:
        matrix = [list(line.strip()) for line in file]
    return matrix


if __name__ == "__main__":
    main()
