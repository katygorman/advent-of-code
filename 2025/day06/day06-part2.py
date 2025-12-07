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
    for index in range(len(matrix[0][col_index])):
        value = ''
        for row in range(len(matrix) - 1):
            value += matrix[row][col_index][index]
        value = int(value)
        if operator == ADD:
            column_total += value
        else:
            column_total *= value
    return column_total


def parse_input_file():
    with open(INPUT_FILE_PATH, "r") as file:
        matrix = [list(line) for line in file]
    matrix = transform_matrix(matrix)
    return matrix


def transform_matrix(matrix):
    transformed = []
    new_col = 0

    col = 0
    while col < len(matrix[0]):
        col_start, col_end = calculate_col_range(matrix, col)
        while col < col_end - 1:
            for row in range(len(matrix) - 1):
                if len(transformed) <= row:
                    transformed.append([])
                if len(transformed[row]) <= new_col:
                    transformed[row].append('')

                value = matrix[row][col]
                transformed[row][new_col] += value
            col += 1
        if len(transformed) < len(matrix):
            transformed.append([])
        operator = matrix[len(matrix) - 1][col_start]
        transformed[len(matrix) - 1].append(operator)

        new_col += 1
        col += 1
    return transformed


def calculate_col_range(matrix, col_start):
    col_end = col_start + 1
    col_end_char = matrix[len(matrix) - 1][col_end]
    while col_end_char == ' ':
        col_end += 1
        if col_end == len(matrix[0]) - 1:
            col_end += 1
            break
        col_end_char = matrix[len(matrix) - 1][col_end]
    return col_start, col_end


if __name__ == "__main__":
    main()
