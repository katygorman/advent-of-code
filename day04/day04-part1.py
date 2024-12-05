INPUT_FILE_PATH = './input.txt'


def main():
    matrix = parse_input_file()
    total = count_xmas(matrix)
    print(total)


def count_xmas(matrix):
    total = 0
    num_rows_and_cols = len(matrix)
    for row in range(num_rows_and_cols):
        for col in range(num_rows_and_cols):
            if matrix[row][col] == 'X':
                total += sub_total_each_direction(matrix, row, col)
    return total


def sub_total_each_direction(matrix, row, col):
    sub_total = 0
    if xmas_left_to_right(matrix, row, col):
        sub_total += 1
    if xmas_right_to_left(matrix, row, col):
        sub_total += 1
    if xmas_up_to_down(matrix, row, col):
        sub_total += 1
    if xmas_down_to_up(matrix, row, col):
        sub_total += 1
    if xmas_diagonal_right_down(matrix, row, col):
        sub_total += 1
    if xmas_diagonal_right_up(matrix, row, col):
        sub_total += 1
    if xmas_diagonal_left_down(matrix, row, col):
        sub_total += 1
    if xmas_diagonal_left_up(matrix, row, col):
        sub_total += 1
    return sub_total


def xmas_left_to_right(matrix, row, col):
    return (col + 3 < len(matrix) and matrix[row][col + 1] == 'M'
            and matrix[row][col + 2] == 'A' and matrix[row][col + 3] == 'S')


def xmas_right_to_left(matrix, row, col):
    return (col - 3 >= 0 and matrix[row][col - 1] == 'M'
            and matrix[row][col - 2] == 'A' and matrix[row][col - 3] == 'S')


def xmas_up_to_down(matrix, row, col):
    return (row + 3 < len(matrix) and matrix[row + 1][col] == 'M'
            and matrix[row + 2][col] == 'A' and matrix[row + 3][col] == 'S')


def xmas_down_to_up(matrix, row, col):
    return (row - 3 >= 0 and matrix[row - 1][col] == 'M'
            and matrix[row - 2][col] == 'A' and matrix[row - 3][col] == 'S')


def xmas_diagonal_right_down(matrix, row, col):
    return (row + 3 < len(matrix) and col + 3 < len(matrix) and matrix[row + 1][col + 1] == 'M'
            and matrix[row + 2][col + 2] == 'A' and matrix[row + 3][col + 3] == 'S')


def xmas_diagonal_right_up(matrix, row, col):
    return (row - 3 >= 0 and col + 3 < len(matrix) and matrix[row - 1][col + 1] == 'M'
            and matrix[row - 2][col + 2] == 'A' and matrix[row - 3][col + 3] == 'S')


def xmas_diagonal_left_down(matrix, row, col):
    return (row + 3 < len(matrix) and col - 3 >= 0 and matrix[row + 1][col - 1] == 'M'
            and matrix[row + 2][col - 2] == 'A' and matrix[row + 3][col - 3] == 'S')


def xmas_diagonal_left_up(matrix, row, col):
    return (row - 3 >= 0 and col - 3 >= 0 and matrix[row - 1][col - 1] == 'M'
            and matrix[row - 2][col - 2] == 'A' and matrix[row - 3][col - 3] == 'S')


def parse_input_file():
    with open(INPUT_FILE_PATH, "r") as file:
        matrix = [list(line.strip()) for line in file]
    return matrix


if __name__ == "__main__":
    main()
