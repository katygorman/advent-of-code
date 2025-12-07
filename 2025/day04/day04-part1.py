INPUT_FILE_PATH = 'input.txt'
PAPER_ACCESS_LIMIT = 4
PAPER = '@'
DISTANCE = 1


def main():
    matrix = parse_input_file()
    count = count_paper_access(matrix)
    print(count)


def count_paper_access(matrix):
    total = 0
    num_rows_and_cols = len(matrix)
    for row in range(num_rows_and_cols):
        for col in range(num_rows_and_cols):
            if matrix[row][col] == PAPER:
                if sub_total_each_direction(matrix, row, col) < PAPER_ACCESS_LIMIT:
                    total += 1
    return total


def sub_total_each_direction(matrix, row, col):
    sub_total = 0
    if paper_right(matrix, row, col):
        sub_total += 1
    if paper_left(matrix, row, col):
        sub_total += 1
    if paper_down(matrix, row, col):
        sub_total += 1
    if paper_up(matrix, row, col):
        sub_total += 1
    if paper_right_down(matrix, row, col):
        sub_total += 1
    if paper_right_up(matrix, row, col):
        sub_total += 1
    if paper_left_down(matrix, row, col):
        sub_total += 1
    if paper_left_up(matrix, row, col):
        sub_total += 1
    return sub_total


def paper_right(matrix, row, col):
    return col + DISTANCE < len(matrix) and matrix[row][col + DISTANCE] == PAPER


def paper_left(matrix, row, col):
    return col - DISTANCE >= 0 and matrix[row][col - DISTANCE] == PAPER


def paper_down(matrix, row, col):
    return row + DISTANCE < len(matrix) and matrix[row + DISTANCE][col] == PAPER


def paper_up(matrix, row, col):
    return row - DISTANCE >= 0 and matrix[row - DISTANCE][col] == PAPER


def paper_right_down(matrix, row, col):
    return row + DISTANCE < len(matrix) and col + DISTANCE < len(matrix) and matrix[row + DISTANCE][
        col + DISTANCE] == PAPER


def paper_right_up(matrix, row, col):
    return row - DISTANCE >= 0 and col + DISTANCE < len(matrix) and matrix[row - DISTANCE][col + DISTANCE] == PAPER


def paper_left_down(matrix, row, col):
    return row + DISTANCE < len(matrix) and col - DISTANCE >= 0 and matrix[row + DISTANCE][col - DISTANCE] == PAPER


def paper_left_up(matrix, row, col):
    return row - DISTANCE >= 0 and col - DISTANCE >= 0 and matrix[row - DISTANCE][col - DISTANCE] == PAPER


def parse_input_file():
    with open(INPUT_FILE_PATH, "r") as file:
        matrix = [list(line.strip()) for line in file]
    return matrix


if __name__ == "__main__":
    main()
