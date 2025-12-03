import numpy as np

INPUT_FILE_PATH = 'input.txt'


def main():
    matrix = parse_input_file()
    distinct_positions = calculate_distinct_positions(matrix)
    print(distinct_positions)


def calculate_distinct_positions(matrix):
    current_position = find_starting_arrow(matrix)
    set_of_positions = {current_position}
    direction = (-1, 0)
    next_position = tuple(np.add(current_position, direction))
    while is_in_mapped_area(next_position, len(matrix)):
        if matrix[next_position[0], next_position[1]] != "#":
            set_of_positions.add(next_position)
            current_position = next_position
        else:
            direction = turn_right(direction)
        next_position = tuple(np.add(current_position, direction))
    return len(set_of_positions)


def turn_right(direction):
    if direction[0] == 0:
        direction = (direction[1], 0)
    else:
        direction = (0, -direction[0])
    return direction


def is_in_mapped_area(next_position, max_dimension):
    if 0 <= next_position[0] < max_dimension and 0 <= next_position[1] < max_dimension:
        return True
    return False


def find_starting_arrow(matrix):
    indices = np.where(matrix == "^")
    return indices[0][0], indices[1][0]


def parse_input_file():
    with open(INPUT_FILE_PATH, "r") as file:
        matrix = [list(line.strip()) for line in file]
    return np.array(matrix)


if __name__ == "__main__":
    main()
