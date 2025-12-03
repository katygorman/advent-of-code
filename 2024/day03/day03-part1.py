import re
import numpy as numpy

INPUT_FILE_PATH = 'input.txt'


def main():
    text = parse_input_file()
    total = calculate(text)
    print(total)


def calculate(text):
    total = 0
    mul_instr_tuples = re.findall("mul\\((\\d{1,3}),(\\d{1,3})\\)", text)
    mul_instr_int_array = (numpy.array(mul_instr_tuples)).astype(int)
    total += numpy.sum(numpy.prod(mul_instr_int_array, axis=1))
    return total


def parse_input_file():
    text = ""
    with open(INPUT_FILE_PATH, "r") as file:
        for line in file:
            text += line
    return text


if __name__ == "__main__":
    main()
