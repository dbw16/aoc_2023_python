from itertools import zip_longest
from pathlib import Path


def first_digit(line: str) -> int:
    for char in line:
        if char.isnumeric():
            return int(char)
    raise ValueError("No digit found in line")


def first_and_last_digit(line: str) -> tuple[int, int]:
    return first_digit(line), first_digit(line[::-1])


def first_number(line: str, _reversed: bool = False) -> int:
    numbers = {
        "one": 1,
        "two": 2,
        "three": 3,
        "four": 4,
        "five": 5,
        "six": 6,
        "seven": 7,
        "eight": 8,
        "nine": 9,
    }

    if _reversed:
        numbers = {key[::-1]: vaule for key, vaule in numbers.items()}

    sliding_window_lenght = 5  # max len of any number eg seven is 5 digits long
    for window in zip_longest(*(line[n:] for n in range(sliding_window_lenght)), fillvalue=""):
        if window[0].isnumeric():
            return int(window[0])

        for number, value in numbers.items():
            try:
                index = "".join(window).index(number)

                # if window does contain the spelling of a number we have to make sure a digit does not appear before it
                for i in range(0, index):
                    if window[i].isnumeric():
                        return int(window[i])
                else:
                    return int(value)

            except ValueError:
                continue

    raise ValueError("No number found in line")


def first_and_last_number(line: str) -> tuple[int, int]:
    return first_number(line), first_number(line[::-1], _reversed=True)


def part_1() -> None:
    lines = Path("day_1.txt").read_text().splitlines()
    pairs = [first_and_last_digit(line) for line in lines]

    answer = sum([int(f"{a}{b}") for a, b in pairs])
    print(answer)


def part_2() -> None:
    lines = Path("day_1.txt").read_text().splitlines()
    pairs = [first_and_last_number(line) for line in lines]

    answer = sum([int(f"{a}{b}") for a, b in pairs])
    print(answer)


def main() -> None:
    part_1()
    part_2()


if __name__ == "__main__":
    main()
