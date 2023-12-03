import day_3

grid_str = """\
467..114..
...*......
..35..633.
......#...
617*......
.....+.58.
..592.....
......755.
...$.*...1
.664....*."""

grid = [[str(x) for x in line] for line in grid_str.splitlines()]


def test_expand_number():
    # all_ready_searched = [[False for x in line] for line in grid_str.splitlines()]
    # assert day_3.expand_number(grid, x=1, y=0, all_ready_searched=all_ready_searched) == 467
    # all_ready_searched = [[False for x in line] for line in grid_str.splitlines()]
    # assert day_3.expand_number(grid, x=2, y=0, all_ready_searched=all_ready_searched) == 467
    # all_ready_searched = [[False for x in line] for line in grid_str.splitlines()]
    # assert day_3.expand_number(grid, x=3, y=0, all_ready_searched=all_ready_searched) == 0
    # all_ready_searched = [[False for x in line] for line in grid_str.splitlines()]
    # assert day_3.expand_number(grid, x=6, y=5, all_ready_searched=all_ready_searched) == 0
    all_ready_searched = [[False for x in line] for line in grid_str.splitlines()]
    assert day_3.expand_number(grid, x=9, y=8, all_ready_searched=all_ready_searched)


def test_get_neigbor_numbers():
    all_ready_searched = [[False for x in line] for line in grid_str.splitlines()]
    assert sum(day_3.get_neigbor_numbers(grid, 3, 1, all_ready_searched=all_ready_searched)) == sum([467, 35])
    all_ready_searched = [[False for x in line] for line in grid_str.splitlines()]
    assert sum(day_3.get_neigbor_numbers(grid, 5, 5, all_ready_searched=all_ready_searched)) == sum([592])
