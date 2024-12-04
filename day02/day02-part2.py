INPUT_FILE_PATH = 'input.txt'


def main():
    matrix = parse_input_file()
    safe_reports = calculate_safe_reports(matrix)
    print(safe_reports)


def calculate_safe_reports(matrix):
    safe_reports = 0
    for row in matrix:
        if safe_report(row):
            safe_reports += 1
        else:
            for i in range(len(row)):
                if safe_report(row[:i] + row[i + 1:]):
                    safe_reports += 1
                    break
    return safe_reports


def safe_report(row):
    increasing = row[0] < row[1]
    for i in range(len(row) - 1):
        if (invalid_level_pair(increasing, row[i], row[i + 1])):
            return False
    return True


def invalid_level_pair(increasing, first_level, second_level):
    return ((increasing and first_level > second_level)
            or (not increasing and first_level < second_level)
            or not (0 < abs(first_level - second_level) <= 3))


def parse_input_file():
    matrix = []
    with open(INPUT_FILE_PATH, "r") as file:
        for line in file:
            row = [int(x) for x in line.split()]
            matrix.append(row)
    return matrix


if __name__ == "__main__":
    main()
