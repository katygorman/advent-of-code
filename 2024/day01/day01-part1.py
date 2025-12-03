import numpy as numpy

INPUT_FILE_PATH = 'input.txt'


def main():
    first_locations, second_locations = parse_input_file()
    location_diff_sum = find_location_diff_sum(first_locations, second_locations)
    print(location_diff_sum)


def find_location_diff_sum(first_locations, second_locations):
    first_locations.sort()
    second_locations.sort()

    location_diff = numpy.absolute(first_locations - second_locations)
    return numpy.sum(location_diff)


def parse_input_file():
    file_data = numpy.loadtxt(INPUT_FILE_PATH, usecols=(0, 1))
    first_locations = file_data[:, 0]
    second_locations = file_data[:, 1]
    return first_locations, second_locations


if __name__ == "__main__":
    main()
