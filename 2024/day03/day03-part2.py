import re

INPUT_FILE_PATH = 'input.txt'


def main():
    text = parse_input_file()
    total = calculate(text)
    print(total)


def calculate(text):
    total = 0
    do = True
    matches = re.findall("mul\\((\\d{1,3}),(\\d{1,3})\\)|(do\\(\\))|(don't\\(\\))", text)
    for match in matches:
        if "do()" in match:
            do = True
        elif "don't()" in match:
            do = False
        elif do:
            total += int(match[0]) * int(match[1])
    return total


def parse_input_file():
    text = ""
    with open(INPUT_FILE_PATH, "r") as file:
        for line in file:
            text += line
    return text


if __name__ == "__main__":
    main()
