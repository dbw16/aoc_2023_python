from pathlib import Path


#    0123456789
# 0: 467..114..
# 1: ...*......
# 2: ..35..633.
# 3: ......#...
# 4: 617*......
# 5: .....+.58.
# 6: ..592.....
# 7: ......755.
# 8: ...$.*....
# 9: .664.598..


def expand_number(grid: list[list[str]], x: int, y: int, all_ready_searched: list[list[bool]]) -> int:
    if y < 0:
        return 0
    if y > len(grid):
        return 0
    if not grid[y][x].isdigit():
        return 0

    number = []
    current_x = x

    # move left
    while grid[y][current_x].isdigit():
        if all_ready_searched[y][current_x]:
            return 0
        number.insert(0, grid[y][current_x])
        all_ready_searched[y][current_x] = True
        current_x = current_x - 1
        if current_x < 0:
            break

    # move right
    current_x = x + 1
    if current_x >= len(grid[y]):
        return int("".join(number) if number else 0)
    while grid[y][current_x].isdigit():
        if all_ready_searched[y][current_x]:
            return 0
        number.append(grid[y][current_x])
        all_ready_searched[y][current_x] = True
        current_x = current_x + 1
        if current_x >= len(grid[y]):
            break
    return int("".join(number) if number else 0)


def get_neigbor_numbers(grid: list[list[str]], x: int, y: int, all_ready_searched: list[list[bool]]) -> list[int]:
    if str(grid[y][x]).isdigit() or str(grid[y][x]) == ".":
        raise ValueError(f"{grid[y][x]} is not a sybol")

    numbers = []
    # up left
    numbers.append(expand_number(grid, x - 1, y - 1, all_ready_searched))
    # up
    numbers.append(expand_number(grid, x, y - 1, all_ready_searched))
    # up right
    numbers.append(expand_number(grid, x + 1, y - 1, all_ready_searched))
    # left
    numbers.append(expand_number(grid, x - 1, y, all_ready_searched))
    # right
    numbers.append(expand_number(grid, x + 1, y, all_ready_searched))
    # down left
    numbers.append(expand_number(grid, x - 1, y + 1, all_ready_searched))
    # down
    numbers.append(expand_number(grid, x, y + 1, all_ready_searched))
    # down right
    numbers.append(expand_number(grid, x + 1, y + 1, all_ready_searched))

    return numbers


def part_1():
    text = Path("day_3.txt").read_text()
    grid = [[str(x) for x in line] for line in text.splitlines()]
    all_ready_searched = [[False for _ in line] for line in text.splitlines()]

    total = 0
    for y, row in enumerate(grid):
        for x, char in enumerate(row):
            if str(char).isdigit() or str(char) == ".":
                continue
            total += sum(get_neigbor_numbers(grid, x, y, all_ready_searched))

    print(total)


def part_2():
    text = Path("day_3.txt").read_text()
    grid = [[str(x) for x in line] for line in text.splitlines()]
    all_ready_searched = [[False for _ in line] for line in text.splitlines()]

    total = 0
    for y, row in enumerate(grid):
        for x, char in enumerate(row):
            if str(char).isdigit() or str(char) == ".":
                continue

            numbers = [number for number in get_neigbor_numbers(grid, x, y, all_ready_searched) if number]
            if len(numbers) == 2:
                total += numbers[0] * numbers[1]

    print(total)


def main() -> None:
    part_1()
    part_2()


if __name__ == "__main__":
    main()
