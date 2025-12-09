INPUT_FILE_PATH = 'input.txt'
ADD = '+'
MULTIPLY = '*'


def main():
    matrix = parse_input_file()
    total = calculate_total(matrix)
    print(total)


def calculate_total(matrix):
    total = 0
    for col in range(len(matrix[0])):
        total += calculate_column(matrix, col)
    return total


def calculate_column(matrix, col_index):
    operator = matrix[len(matrix) - 1][col_index]
    column_total = 0 if operator == ADD else 1
    for row in range(len(matrix) - 1):
        value = int(matrix[row][col_index])
        if operator == ADD:
            column_total += value
        else:
            column_total *= value
    return column_total


def parse_input_file():
    with open(INPUT_FILE_PATH, "r") as file:
        matrix = []
        for line in file:
            matrix.append(line.split())
    return matrix


if __name__ == "__main__":
    main()
