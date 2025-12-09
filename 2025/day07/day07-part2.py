INPUT_FILE_PATH = 'small-input.txt'
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

                new_matrix_left = [r.copy() for r in matrix]
                new_matrix_left[row + 1][col - 1] = BEAM
                new_matrix_left = new_matrix_left[row + 1:]
                splits += count_splits(new_matrix_left)

                new_matrix_right = [r.copy() for r in matrix]
                new_matrix_right[row + 1][col + 1] = BEAM
                new_matrix_right = new_matrix_right[row + 1:]
                splits += count_splits(new_matrix_right)
    return splits


def check_for_split(matrix, row, col):
    current = matrix[row][col]
    previous = matrix[row - 1][col]
    beam = previous == BEAM or previous == START
    splitter = current == SPLITTER

    if beam and splitter:
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
