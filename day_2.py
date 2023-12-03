from pathlib import Path
import re
from enum import Enum


class Color(Enum):
    RED = "red"
    GREEN = "green"
    BLUE = "blue"


def get_number_for_color(line: str, color: Color) -> int:
    pattern = r"(\d+)\s+" + str(color.value)
    match = re.search(pattern, line)
    return int(match.group(1)) if match else 0


def part_1() -> int:
    color_to_max = {
        Color.RED: 12,
        Color.GREEN: 13,
        Color.BLUE: 14,
    }

    def is_line_possible(line: str) -> bool:
        for turn in line.split(":")[-1].split(";"):
            for color in Color:
                if get_number_for_color(turn, color) > color_to_max[color]:
                    return False
        return True

    lines = Path("day_2.txt").read_text().splitlines()
    return sum([game_number + 1 for game_number, line in enumerate(lines) if is_line_possible(line)])


def part_2() -> int:
    lines = Path("day_2.txt").read_text().splitlines()
    powers = []
    for line in lines:
        color_to_max: dict[Color, int] = {color: 0 for color in Color}
        for turn in line.split(":")[-1].split(";"):
            for color in Color:
                color_to_max[color] = max(get_number_for_color(turn, color), color_to_max[color])
        powers.append(color_to_max[Color.BLUE] * color_to_max[Color.RED] * color_to_max[Color.GREEN])

    return sum(powers)


def main() -> None:
    print(part_2())


if __name__ == "__main__":
    main()
