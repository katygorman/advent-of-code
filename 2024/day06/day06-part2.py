import numpy as np

INPUT_FILE_PATH = 'small-input.txt'


def main():
    matrix = parse_input_file()
    distinct_positions = calculate_distinct_positions(matrix)
    print(distinct_positions)


def calculate_distinct_positions(matrix):
    current_position = find_starting_arrow(matrix)
    direction = (-1, 0)
    next_position = tuple(np.add(current_position, direction))
    total = 0

    while is_in_mapped_area(next_position, len(matrix)):
    # for i in range(2):
    #     if is_in_mapped_area(next_position, len(matrix)):
        if traverse_mapped_area_with_obstruction(matrix, current_position, direction):
            print("total", total)
            total += 1
        current_position, next_position, direction = next_move(matrix, current_position, next_position, direction)
        print("next_position_outer_loop", next_position)
    return total


def traverse_mapped_area_with_obstruction(original_matrix, current_position, direction):
    matrix = np.array(original_matrix)
    # current_position = original_current_position
    # direction = original_direction
    total = 0
    next_position = tuple(np.add(current_position, direction))
    print("next_position", next_position)
    matrix[next_position[0], next_position[1]] = "#"
    print("new obstruction", matrix[next_position[0], next_position[1]])
    loop_positions_and_directions = np.array([current_position, direction])
    print("loop_positions_and_directions", loop_positions_and_directions)
    # loop_directions = np.array(direction)
    # print("loop_directions", loop_directions)
    direction = turn_right(direction)
    print("direction",direction)
    next_position = tuple(np.add(current_position, direction))
    print("next_position", next_position)
    while is_in_mapped_area(next_position, len(matrix)):
    # for i in range(10):
    #     if is_in_mapped_area(next_position, len(matrix)):
        if [current_position, direction] in loop_positions_and_directions:
            print("loop detected", current_position, direction)
            return True
        current_position, next_position, direction = next_move(matrix, current_position, next_position, direction)
    return False


def next_move(matrix, current_position, next_position, direction):
    if matrix[next_position[0], next_position[1]] != "#":
        current_position = next_position
    else:
        direction = turn_right(direction)
    next_position = tuple(np.add(current_position, direction))
    # print("next_move_next_position", next_position)
    return current_position, next_position, direction


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
