import re

INPUT_FILE_PATH = './input.txt'


def main():
    lines = parse_input_file()
    total = calculate(lines)
    print(total)


def calculate(lines):
    total = 0
    do = True
    for line in lines:
        matches = re.findall("mul\\((\\d{1,3}),(\\d{1,3})\\)|(do\\(\\))|(don't\\(\\))", line)
        for match in matches:
            if "do()" in match:
                do = True
            elif "don't()" in match:
                do = False
            elif do:
                total += int(match[0]) * int(match[1])
    return total


def parse_input_file():
    lines = []
    with open(INPUT_FILE_PATH, "r") as file:
        for line in file:
            lines.append(line)
    return lines


if __name__ == "__main__":
    main()
