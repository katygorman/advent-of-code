INPUT_FILE_PATH = 'input.txt'

START_NUM = 50
DIAL_SIZE = 100


def main():
    file_data = parse_input_file()
    zero_count = count_zero(file_data)
    print(zero_count)


def count_zero(dial_turns):
    current_position = START_NUM
    zero_count = 0

    for dial_turn in dial_turns:
        old_position = current_position
        full_rotations, new_position = divmod(current_position + dial_turn, DIAL_SIZE)

        # Add all full rotations
        zero_count += abs(full_rotations)
        # Adjust to not double count negative rotation starting at zero
        if old_position == 0 and full_rotations < 0:
            zero_count -= 1
        # Adjust to count a positive turn ending exactly at zero
        if new_position == 0 and dial_turn < 0:
            zero_count += 1

        current_position = new_position

    return zero_count


def parse_input_file():
    with open(INPUT_FILE_PATH, 'r') as file:
        lines = file.readlines()

    lines = [line.strip() for line in lines]
    lines = [line.replace("L", "-") for line in lines]
    lines = [line.replace("R", "") for line in lines]
    lines = [int(line) for line in lines]

    return lines


if __name__ == "__main__":
    main()
