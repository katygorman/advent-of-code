import numpy as numpy
from collections import Counter

INPUT_FILE_PATH = './day01-input.txt'

def main():
    first_locations, second_locations = parse_input_file()
    similarity_score = find_similarity_score(first_locations, second_locations)
    print(similarity_score)

def find_similarity_score(first_locations, second_locations):
    second_location_counts = Counter(second_locations)

    similarity_score = 0
    for item in first_locations:
        count = second_location_counts.get(item)
        if count != None:
            similarity_score = similarity_score + (item * count)
    return similarity_score

def parse_input_file():
    file_data = numpy.loadtxt(INPUT_FILE_PATH, usecols=(0, 1))
    first_locations = file_data[:, 0]
    second_locations = file_data[:, 1]
    return first_locations, second_locations

if __name__ == "__main__":
    main()
