INPUT_FILE_PATH = 'input.txt'


def main():
    matrix = parse_input_file()
    total = count_xmas(matrix)
    print(total)


def count_xmas(matrix):
    total = 0
    num_rows_and_cols = len(matrix)
    for row in range(1, num_rows_and_cols - 1):
        for col in range(1, num_rows_and_cols - 1):
            if matrix[row][col] == 'A' and xmas_around_a(matrix, row, col):
                total += 1
    return total


def xmas_around_a(matrix, row, col):
    if space_around_a(matrix, row, col):
        if ((mas_diagonal_right_down(matrix, row, col) or mas_diagonal_left_up(matrix, row, col)) and
                (mas_diagonal_right_up(matrix, row, col) or mas_diagonal_left_down(matrix, row, col))):
            return True
    return False


def mas_diagonal_right_down(matrix, row, col):
    return matrix[row - 1][col - 1] == 'M' and matrix[row + 1][col + 1] == 'S'


def mas_diagonal_right_up(matrix, row, col):
    return matrix[row + 1][col - 1] == 'M' and matrix[row - 1][col + 1] == 'S'


def mas_diagonal_left_down(matrix, row, col):
    return matrix[row - 1][col + 1] == 'M' and matrix[row + 1][col - 1] == 'S'


def mas_diagonal_left_up(matrix, row, col):
    return matrix[row + 1][col + 1] == 'M' and matrix[row - 1][col - 1] == 'S'


def space_around_a(matrix, row, col):
    return row - 1 >= 0 and col - 1 >= 0 and row + 1 < len(matrix) and col + 1 < len(matrix)


def parse_input_file():
    with open(INPUT_FILE_PATH, "r") as file:
        matrix = [list(line.strip()) for line in file]
    return matrix


if __name__ == "__main__":
    main()
